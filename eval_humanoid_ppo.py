import gymnasium as gym
from stable_baselines3 import PPO

ENV_ID = "Humanoid-v4"
MODEL_PATH = "./humanoid_models/ppo_humanoid_final.zip"


if __name__ == "__main__":
    env = gym.make(ENV_ID, render_mode="human")
    model = PPO.load(MODEL_PATH)

    obs, info = env.reset()
    for _ in range(2000):
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            obs, info = env.reset()

    env.close()
