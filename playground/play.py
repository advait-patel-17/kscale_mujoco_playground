from runner import ZBotRunner
import logging
import argparse

def main():
    parser = argparse.ArgumentParser(description='ZBot Runner Script')
    parser.add_argument('--env', type=str, default="ZbotJoystickFlatTerrain", help='Environment to run')
    parser.add_argument('--task', type=str, default="flat_terrain", help='Task to run')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode with minimal parameters')
    parser.add_argument('--save-model', action='store_true', help='Save model after training')
    parser.add_argument('--load-model', action='store_true', help='Load existing model instead of training')
    parser.add_argument('--seed', type=int, default=1, help='Random seed')
    parser.add_argument('--num-episodes', type=int, default=2, help='Number of evaluation episodes')
    parser.add_argument('--episode-length', type=int, default=3000, help='Length of each episode')
    parser.add_argument('--x-vel', type=float, default=1.0, help='X velocity command')
    parser.add_argument('--y-vel', type=float, default=0.0, help='Y velocity command')
    parser.add_argument('--yaw-vel', type=float, default=0.0, help='Yaw velocity command')
    args = parser.parse_args()
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    runner = ZBotRunner(args, logger)
    
    runner.load_model()
    
    runner.evaluate()


if __name__ == "__main__":
    main()
