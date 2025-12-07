🧠 Teaching a Humanoid to Walk Using PPO in MuJoCo
Reinforcement Learning for Humanoid Locomotion

This repository contains the training pipeline used to teach a humanoid agent to walk using Proximal Policy Optimization (PPO) in the MuJoCo physics simulator.
The project validates a complete RL workflow for bipedal locomotion and prepares the foundation for training on a custom Nexomation humanoid model.

🚀 Project Overview

Humanoid locomotion is a complex control problem due to its high dimensionality, unstable dynamics, and multi-joint coordination requirements.
Using PPO, a model-free reinforcement learning algorithm, the agent learns to generate stable walking behavior entirely from experience.

This repo includes:

PPO training script for Humanoid-v4 environment

Evaluation script for rendering learned policies

Modular structure for adding custom humanoid models

Ignore rules for heavy RL models & logs

📁 Repository Structure
humanoid_ppo_mujoco/
│
├── train_humanoid_ppo.py      # Main PPO training pipeline
├── eval_humanoid_ppo.py       # Evaluation & visualization script
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore models, logs, venv, etc.
│
├── models/                    # (empty) trained models are saved here
└── logs/                      # (empty) TensorBoard logs or eval data

⚙️ Installation
1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

2. Install dependencies
pip install -r requirements.txt

3. Install MuJoCo

MuJoCo is installed automatically via Gymnasium, but ensure the runtime is available:

Download MuJoCo (if required): https://mujoco.org

Ensure environment variables are configured.

🧬 Training the Humanoid

Run the PPO training script:

python train_humanoid_ppo.py


This will:

Initialize MuJoCo Humanoid-v4

Train using PPO

Save checkpoints in models/

Log training metrics in logs/

During early training, the humanoid may fall frequently while learning balance and gait patterns.

🎞️ Evaluating a Learned Policy

To visualize the humanoid walking:

python eval_humanoid_ppo.py


You can change the model path inside the script to load a specific checkpoint.

📊 TensorBoard Support

If your training script includes TensorBoard logging:

tensorboard --logdir logs/


This displays curves for:

Episode reward

Policy loss

Value loss

KL divergence

Performance over time

🛠️ Customization Roadmap

This repository is designed to support extensions such as:

✓ Custom humanoid models (URDF → MJCF)
✓ Domain randomization for sim-to-real
✓ Curriculum learning (standing → steps → walking)
✓ Integration with hardware IMU sensors
✓ Real-world controller deployment
📌 Requirements

Typical versions used:

gymnasium[mujoco]
stable-baselines3
torch
numpy
mujoco==3.2.0
tensorboard


(Exact list in requirements.txt)

🧩 Future Work

Integrate Nexomation Humanoid V1 custom URDF

Train RL policies on custom morphology

Add perception-based locomotion (vision + RL)

Explore sim-to-real transfer for prototype hardware legs

🤝 Contributing

Pull requests are welcome for:

Improved RL training stability

Alternative reward functions

Better logging/visualization

Custom humanoid examples
