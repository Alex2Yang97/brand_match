import os


__proj_dir = os.path.dirname(os.path.dirname(__file__))
SCPT_DIR = os.path.join(__proj_dir, 'script')
DATA_DIR = os.path.join(__proj_dir, 'data')


if __name__ == '__main__':
    print(f"__proj_dir: {__proj_dir}")
    print(f"SCPT_DIR: {SCPT_DIR}")