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

            # If it's a valid combination
            if v:
                if len(valid_combs_list) == 0:
                    valid_combs_list.add(vc)
                else:
                    # Don't include duplicates
                    inc = True
                    check_combs = itertools.permutations(vc, len(vc))
                    for cc in check_combs:
                        if cc in valid_combs_list:
                            inc = False
                            break

                    if inc:
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

    # If the rest is just one piece
    if type(combination[1][0]) != tuple:
        pieces = [combination[1]]
    else:
        pieces = list(combination[1])
    
    return_combination = list(pieces)
    return_combination.append(combination[0])

    # Loop comparissons
    while len(pieces) > 0:
        for piece in pieces:
            if threats(first_piece, piece):
                return False, ()
            if threats(piece, first_piece):
                return False, ()

        first_piece = pieces.pop(0)

    # If there's no threat
    return True, tuple(return_combination)


def threats(first_piece, second_piece):
    """Check if there's a threat between two pieces.

    Keyword arguments:
    first_piece -- Tuple with a piece type, x position and y position
    second_piece -- Tuple with a piece type, x position and y position

    Returns a boolean if one of the pieces threats the other.
    """
    # Same position
    if (first_piece[1] == second_piece[1] and
            first_piece[2] == second_piece[2]):
        return True

    # Same column or line: Queens and Rooks
    if (first_piece[0] in ('Q', 'R')):
        if (first_piece[1] == second_piece[1] or
                first_piece[2] == second_piece[2]):
            return True

    # Diagonal: Queens and Bishops
    if (first_piece[0] in ('Q', 'B')):
        if (abs(second_piece[1] - first_piece[1]) ==
                abs(second_piece[2] - first_piece[2])):
            return True

    # King
    if (first_piece[0] == 'K'):
        if (abs(second_piece[1] - first_piece[1]) in (0, 1) and
                abs(second_piece[2] - first_piece[2]) in (0, 1)):
            return True

    # Knight
    if (first_piece[0] == 'N'):
        if ((abs(second_piece[1] - first_piece[1]) == 2 and
            abs(second_piece[2] - first_piece[2]) == 1) or
            (abs(second_piece[1] - first_piece[1]) == 1 and
            abs(second_piece[2] - first_piece[2]) == 2)):
            return True


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
