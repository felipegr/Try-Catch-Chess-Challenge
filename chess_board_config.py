# -*- coding: cp1252 -*-
"""Try Catch's Chess Challenge
The problem is to find all unique configurations of a set of normal chess
pieces on a chess board with dimensions M×N where none of the pieces is in
a position to take any of the others.
The colour of the piece does not matter, and there are no pawns
among the pieces.

Input arguments:
x -- Number of squares of the X dimension of the board
y -- Number of squares of the Y dimension of the board
k -- Number of Kings to be placed on the board
q -- Number of Queens to be placed on the board
b -- Number of Bishops to be placed on the board
r -- Number of Rooks to be placed on the board
n -- Number of Knights to be placed on the board
verbose -- If present, prints the comfigurations to the screen
"""

import argparse
from chess_board_lib import find_configurations


def main():
    """Main function."""
    # Find configurations and print them to the screen
    configs = find_configurations(args.x, args.y, args.kings, args.queens,
                                  args.bishops, args.rooks, args.knights,
                                  args.verbose)

    # Print total number of configurations
    print ''
    print('Total number of configurations: {0}'.format(configs))


if __name__ == "__main__":
    """Arguments checking and main function call."""
    # Arguments parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=int,
                        help='Number of squares of the X dimension of the board',
                        required=True)
    parser.add_argument('-y', type=int,
                        help='Number of squares of the Y dimension of the board',
                        required=True)
    parser.add_argument('-k', '--kings', type=int, default=0,
                        help='Number of Kings to be placed on the board')
    parser.add_argument('-q', '--queens', type=int, default=0,
                        help='Number of Queens to be placed on the board')
    parser.add_argument('-b', '--bishops', type=int, default=0,
                        help='Number of Bishops to be placed on the board')
    parser.add_argument('-r', '--rooks', type=int, default=0,
                        help='Number of Rooks to be placed on the board')
    parser.add_argument('-n', '--knights', type=int, default=0,
                        help='Number of Knights to be placed on the board')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Writes the board combinations to the screen')
    args = parser.parse_args()

    # Some arguments checking
    total_pieces = args.kings + args.queens + args.bishops + args.rooks + \
                   args.knights
    invalid = False

    # Check if dimensions are greater than zero
    if args.x <= 0 or args.y <= 0:
        print "Dimensions must be both greater than zero."
        invalid = True

    # Check if there are pieces to be placed
    if total_pieces == 0:
        print "There aren't pieces to be placed."
        invalid = True

    # Check if number of pieces is correct
    if total_pieces > (args.x * args.y):
        print "There are more pieces than places to put them."
        invalid = True

    # Call main function
    if not invalid:
        main()
