import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.monitor import Monitor
import os

ENV_ID = "Humanoid-v4"
LOG_DIR = "./humanoid_logs"
MODEL_DIR = "./humanoid_models"

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

def make_env(rank):
    def _init():
        env = gym.make(ENV_ID)
        env = Monitor(env, filename=os.path.join(LOG_DIR, f"monitor_{rank}.csv"))
        return env
    return _init

if __name__ == "__main__":
    # Parallel environments for faster training
    num_envs = 8
    env = SubprocVecEnv([make_env(i) for i in range(num_envs)])

    checkpoint_callback = CheckpointCallback(
        save_freq=500_000 // num_envs,  # in steps (per env)
        save_path=MODEL_DIR,
        name_prefix="ppo_humanoid"
    )

    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        n_steps=2048,
        batch_size=64,
        gae_lambda=0.95,
        gamma=0.99,
        n_epochs=10,
        ent_coef=0.0,
        learning_rate=3e-4,
        clip_range=0.2,
        tensorboard_log=LOG_DIR,
    )

    total_timesteps = 5_000_000  # Start with 1e6 while testing
    model.learn(
        total_timesteps=total_timesteps,
        callback=checkpoint_callback
    )

    model.save(os.path.join(MODEL_DIR, "ppo_humanoid_final"))
    env.close()
