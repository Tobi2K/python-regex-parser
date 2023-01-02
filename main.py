from RegexProcessing import *

import argparse


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='Run regular expression conversion.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # general arguments
    parser.add_argument('-e', '--expression', type=str, help='The expression to be converted.')
    parser.add_argument('destination', metavar='dest', type=str, choices=['REGEX', 'SYA', 'NFA', 'DFA'], help="The destination goal, possible values are: 'REGEX', 'SYA', 'NFA', 'DFA'")
    parser.add_argument('-d', '--debug', action='store_true', help='Whether to print conversion steps.')
    parser.add_argument('-s', '--strict', action='store_true', help='Whether to throw an error instead of making an assumption when converting.')

    args = parser.parse_args()
    item = None
    no_guarantee = False
    if args.destination == 'REGEX':
        item, no_guarantee = Regexer.regex(args.expression, steps=args.debug, strict=args.strict)
    elif args.destination == 'SYA':
        item, no_guarantee = Regexer.full_shunting_yard(args.expression, steps=args.debug, strict=args.strict)
    elif args.destination == 'NFA':
        item, no_guarantee = Regexer.create_nfa(args.expression, steps=args.debug, strict=args.strict)
    elif args.destination == 'DFA':
        item, no_guarantee = Regexer.create_dfa(args.expression, steps=args.debug, strict=args.strict)

    if no_guarantee:
        print("WARNING: Some features might not have been converted correctly!")

    if type(item) == DFA:
        item.print_dfa()
    elif type(item) == NFA:
        item.print_nfa()
    else:
        print(item)
