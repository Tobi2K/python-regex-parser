from RegexProcessing import *

import argparse


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='Run regular expression conversion.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # general arguments
    parser.add_argument('-e', '--expression', type=str, help='The expression to be converted.')

    args = parser.parse_args()
    print(Regexer.preprocess(args.expression))
