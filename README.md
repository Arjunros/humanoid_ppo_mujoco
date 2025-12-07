# Humanoid Locomotion Using PPO in MuJoCo
Reinforcement Learning for Bipedal Control

This repository contains a complete training pipeline for teaching a humanoid agent to walk using the Proximal Policy Optimization (PPO) algorithm in the MuJoCo physics simulator.  
The implementation demonstrates an end-to-end reinforcement learning workflow on the `Humanoid-v4` benchmark environment and serves as a foundation for future experiments with custom humanoid models.

---

## Project Overview

Humanoid locomotion is a complex control problem due to its high dimensionality, unstable dynamics, and continuous action space.  
Using PPO, the agent learns balance, stepping behavior, and coordinated motion purely from interaction, without manually designed gait trajectories.

This repository provides:
- A PPO training script for the Humanoid-v4 environment  
- An evaluation script for rendering learned policies  
- A clean structure for model saving and logging  
- Modular code suitable for extension to custom robots

---

## Repository Structure

humanoid_ppo_mujoco/
│
├── train_humanoid_ppo.py # PPO training pipeline
├── eval_humanoid_ppo.py # Evaluation and rendering script
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
│
├── models/ # Saved model checkpoints (ignored)
└── logs/ # TensorBoard and training logs (ignored)



---

## Installation

### 1. Create and activate a virtual environment

**Windows**
python -m venv venv
venv\Scripts\activate



**Linux / macOS**
python3 -m venv venv
source venv/bin/activate



### 2. Install dependencies
pip install -r requirements.txt



Ensure that MuJoCo is installed through Gymnasium or that the MuJoCo runtime is available on your system.

---

## Training

To train the humanoid using PPO:

python train_humanoid_ppo.py



The script will:
- Initialize the Humanoid-v4 MuJoCo environment  
- Train a PPO policy  
- Save model checkpoints in the `models/` directory  
- Log metrics into the `logs/` directory  

---

## Evaluation

To load and render a trained model:

python eval_humanoid_ppo.py



Edit the script to specify the desired model checkpoint path.

---

## TensorBoard Visualization

If logging is enabled, launch TensorBoard with:

tensorboard --logdir logs/



This provides visualizations of:
- Episode returns  
- Value and policy loss  
- KL divergence  
- Training stability over time  

---

## Customization Roadmap

The repository is structured to support advanced extensions:
- Integration of custom humanoid models (URDF → MJCF)  
- Domain randomization for sim-to-real transfer  
- Curriculum-based locomotion training  
- Integration with hardware IMU sensors  
- Deployment of learned policies on real robotic legs  

---

## Dependencies (Summary)

Key packages used:
gymnasium[mujoco]
stable-baselines3
torch
numpy
tensorboard
mujoco==3.2.0



Refer to `requirements.txt` for exact versions.

---

## Future Work

Planned enhancements include:
- Training RL policies on the Nexomation Humanoid V1 design  
- Improved reward shaping for stable gait generation  
- Comparison with alternative RL algorithms  
- Experimentation with perception-driven locomotion  
- Real-world deployment on hardware prototypes  

---

## Contributing

Contributions are welcome for:
- Additional training features  
- Improved reward functions  
- Visualization improvements  
- Environment wrappers and utilities  

---

## License

Specify license information here (MIT recommended).
