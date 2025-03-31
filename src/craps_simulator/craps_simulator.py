import argparse
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, filename='../../logs/test.log', filemode='w')

def read_args():
    parser = argparse.ArgumentParser(description='Optional app description')
    
    # Required positional argument
    parser.add_argument('turns', type=int,
                    help='A required integer positional argument')

    # Optional positional argument
    parser.add_argument('opt_pos_arg', type=int, nargs='?',
                        help='An optional integer positional argument')
    
    return parser.parse_args()


def craps_simulator():
    pass

if __name__ == '__main__':
    logging.info(f"Starting application ...")
    args = read_args()
    craps_simulator()
    logging.info(f"Execution completed")