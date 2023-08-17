import os
from src.config import REPLAY_ROOT


def read_file(filename):
    contents = None
    with open(f"{REPLAY_ROOT}/{filename}", "rb") as f:
        contents = f.read()
    return contents

def main():
    filename = os.listdir(REPLAY_ROOT)[0]
    contents = read_file(filename)
    

if __name__ == "__main__":
    main()
