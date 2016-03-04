import itertools
import argparse
import sys
import time


def main():
    """Main function."""
    # Find configurations and print them to the screen
    configs = find_configurations(args.x, args.y, args.kings, args.queens,
                                  args.bishops, args.rooks, args.knights)

    # Print total number of configurations
    print ''
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

    # Get combinations of first piece
    piece_iter = iterators.pop(0)

    # Loop to check all combinations of all pieces
    while len(iterators) > 0:
        sec_piece = iterators.pop(0)
        combs = itertools.product(sec_piece, piece_iter)
        valid_combs_list = set()

        # Loop for these two pieces
        for c in combs:
            v, vc = valid_combination(c)
            if (v):
                valid_combs_list.add(vc)

        piece_iter = itertools.chain(valid_combs_list)

    # Set final combinations
    final_combinations = piece_iter
    
    print ''
    print 'Combinations: '

    # Print combinations
    comb_num = 0
    for elem in final_combinations:
        print elem
        comb_num = comb_num + 1

    # Set end time and print elapsed time
    elapsed_time = time.time() - start_time
    print ''
    print 'Total elapsed time: %f seconds' % (elapsed_time)

    return comb_num


def valid_combination(combination):
    """Check if a combination is one where no piece is threatened.

    Keyword arguments:
    combination -- Tuple with positions of pieces

    Returns a boolean that tells if the combination is one where no piece is
    threatened and the combination itself as a Tuple.
    """
    first_piece = combination[0]
    pieces = list(combination[1])

    # Loop comparissons
    while len(pieces) > 0:
        for piece in pieces:
            if threats(first_piece, piece)


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
    args = parser.parse_args()

    # Some arguments checking
    total_pieces = args.kings + args.queens + args.bishops + args.rooks + \
                   args.knights

    # Check if dimensions are greater than zero
    if args.x <= 0 or args.y <= 0:
        print "Dimensions must be both greater than zero."
        sys.exit()
    
    # Check if there are pieces to be placed
    if total_pieces == 0:
        print "There aren't pieces to be placed."
        sys.exit()

    # Check if number of pieces is correct
    if total_pieces > (args.x * args.y):
        print "There are more pieces than places to put them."
        sys.exit()

    # Call main function
    main()
