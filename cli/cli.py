"""
G_Kingdom CLI

Usage:
    $ python cli.py

Examples:
    TODO

"""

import argparse


def main(args):
    """Main entry point of CLI app"""
    print("The following arguments passed: ")
    print(args)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    args = parser.parse_args()

    main(args)

