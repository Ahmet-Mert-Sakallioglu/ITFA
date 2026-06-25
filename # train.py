# train.py
"""
Forest Fire Reinforcement Learning System (ITFA)

Deep Reinforcement Learning training pipeline using PPO.

Author: Ahmet Mert Sakallıoğlu
"""

import os
import time
import numpy as np

from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold

from environment import FireEnv


def make_env():

    env = FireEnv()
    env = Monitor(env)
    return env


TOTAL_TIMESTEPS = 150000
EVAL_FREQ = 5000
SAVE_PATH = "models/"
LOG_PATH = "logs/"


def main():

    print("=" * 60)
    print("Forest Fire DRL Training System Starting...")
    print("=" * 60)

    start_time = time.time()

    os.makedirs(SAVE_PATH, exist_ok=True)
    os.makedirs(LOG_PATH, exist_ok=True)

    env = make_env()

    reward_threshold = StopTrainingOnRewardThreshold(
        reward_threshold=200,
        verbose=1
    )

    eval_callback = EvalCallback(
        env,
        best_model_save_path=SAVE_PATH,
        log_path=LOG_PATH,
        eval_freq=EVAL_FREQ,
        deterministic=True,
        render=False,
        callback_on_new_best=reward_threshold
    )

    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        learning_rate=3e-4,
        n_steps=1024,
        batch_size=64,
        gamma=0.99,
        gae_lambda=0.95,
        clip_range=0.2,
        ent_coef=0.01,
        tensorboard_log=LOG_PATH
    )

    print("\nModel initialized successfully.")
    print("Starting training process...\n")

    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        callback=eval_callback
    )

    final_path = os.path.join(SAVE_PATH, "fire_drl_model_final")
    model.save(final_path)

    end_time = time.time()

    print("\n" + "=" * 60)
    print("Training completed successfully.")
    print(f"Total training time: {round(end_time - start_time, 2)} seconds")
    print(f"Model saved at: {final_path}")
    print("=" * 60)

    print("\nTraining Summary:")
    print(f"- Total timesteps: {TOTAL_TIMESTEPS}")
    print(f"- Evaluation frequency: {EVAL_FREQ}")
    print(f"- Algorithm: PPO (Proximal Policy Optimization)")
    print(f"- Environment: Grid-based wildfire simulation")


if __name__ == "__main__":
    main()
