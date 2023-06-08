import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("root_dir", nargs='?', default=None, type=str)
    args = parser.parse_args()
    if args.root_dir is None:
        print("Directory is not specified")
    else:
        os.chdir(str(args.root_dir))
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                print(os.path.join(root, file))
