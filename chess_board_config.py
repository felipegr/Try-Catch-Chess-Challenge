import itertools
import argparse
import sys
import time

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
args = parser.parse_args()


def main():
    """Main function."""
    # Check if there are pieces to be placed
    total = args.kings + args.queens + args.bishops + args.rooks + args.knights
    if total == 0:
        print "There aren't pieces to be placed."
        sys.exit()

    # Find configurations and print them to the screen
    configs = find_configurations(args.x, args.y, args.kings, args.queens,
                                  args.bishops, args.rooks, args.knights)

    # Print total number of configurations
    print 'Total number of configurations: %d' % (configs)

    sys.exit()


def find_configurations(x, y, k, q, b, r, n):
    """Find and print all configurations for a chess board where no piece
    threats another.

    Keyword arguments:
    x -- Number of squares of the X dimension of the board
    y -- Number of squares of the Y dimension of the board
    k -- Number of Kings to be placed on the board
    q -- Number of Queens to be placed on the board
    b -- Number of Bishops to be placed on the board
    r -- Number of Rooks to be placed on the board
    n -- Number of Knights to be placed on the board

    Returns the number of configurations found.
    """
    # Set start time (for total elapsed time)
    start_time = time.time()

    # Create possible positions for every piece
    iterators = []
    for i in range(q):
        iterators.append(itertools.product('Q', range(x), range(y)))
    for i in range(b):
        iterators.append(itertools.product('B', range(x), range(y)))
    for i in range(r):
        iterators.append(itertools.product('R', range(x), range(y)))
    for i in range(k):
        iterators.append(itertools.product('K', range(x), range(y)))
    for i in range(n):
        iterators.append(itertools.product('N', range(x), range(y)))

    # Create all board combinations using cartesian product
    combinations = itertools.product(*iterators)

    for el in combinations:
        print el

    # Set end time and print elapsed time
    elapsed_time = time.time() - start_time
    print 'Total elapsed time: %f seconds' % (elapsed_time)

    return 2


if __name__ == "__main__":
    main()
