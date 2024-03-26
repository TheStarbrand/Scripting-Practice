import os
import json
import shutil
from subprocess import PIPE, run
import sys


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)


if __name__ == '__main__':
    args = sys.argv
    # print(args)
    if len(args) != 3:
        raise Exception("Invalid number of arguments, you must pass a source and target directory ONLY ")
    
    source, target = args[1]
    main(source, target)


