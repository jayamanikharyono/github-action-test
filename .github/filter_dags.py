import os
import logging
import argparse


def main(args):
    logging.info("added and modified : {}".format(args.addmodified))
    addmodified = args.addmodified
    excluded_files = addmodified.split(",")
    for file in excluded_files:
        print(file)
    """
    for subdir, dirs, files in os.walk('airflow/dags/'):
        for file in files:
            if subdir + file not in excluded_files:
                print(subdir + file)
                os.remove(subdir + file)
    """


if __name__=="__main__":
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--addmodified', action = 'store', type = str, required = True)
    args = parser.parse_args()
    main(args)
