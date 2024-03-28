import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = 'game'

def find_all_game_paths(source):
    gamePaths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                gamePaths.append(path)


        break
    return gamePaths


def main(source):#, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    print(game_paths)


if __name__ == '__main__':
    args = sys.argv
    # print(args)
    if len(args) != 2:
        print("Invalid number of arguments, you must pass a source and target directory ONLY ")
        sys.exit(1)
        # raise Exception("Invalid number of arguments, you must pass a source and target directory ONLY ")
    
    source, target = args[1:]
    main(source, target)


