# -*- coding: cp1252 -*-
"""Try Catch's Chess Challenge - Functions Library
Here are the helper functions used by the main process (chess_board_config.py)
to check if a chess board configuration is one where no piece threats another.

List of functions names:
find_configurations
valid_combination
threats
"""

import itertools
import time


def find_configurations(x_dim, y_dim, kings, queens, bishops, rooks,
                        knights, verbose):
    """Find and print all configurations for a chess board where no piece
    threats another.

    Keyword arguments:
    x_dim -- Number of squares of the X dimension of the board
    y_dim -- Number of squares of the Y dimension of the board
    kings -- Number of Kings to be placed on the board
    queens -- Number of Queens to be placed on the board
    bishops -- Number of Bishops to be placed on the board
    rooks -- Number of Rooks to be placed on the board
    knights -- Number of Knights to be placed on the board

    Returns the number of configurations found.
    """
    # Set start time (for total elapsed time)
    start_time = time.time()

    # Create possible positions for every piece
    iterators = []
    for _ in range(queens):
        iterators.append(itertools.product('Q', range(x_dim), range(y_dim)))
    for _ in range(bishops):
        iterators.append(itertools.product('B', range(x_dim), range(y_dim)))
    for _ in range(rooks):
        iterators.append(itertools.product('R', range(x_dim), range(y_dim)))
    for _ in range(kings):
        iterators.append(itertools.product('K', range(x_dim), range(y_dim)))
    for _ in range(knights):
        iterators.append(itertools.product('N', range(x_dim), range(y_dim)))

    # Get combinations of first piece
    piece_iter = iterators.pop(0)

    # Loop to check all combinations of all pieces
    comb_num = -1
    while len(iterators) > 0:
        sec_piece = iterators.pop(0)
        combs = itertools.product(sec_piece, piece_iter)
        valid_combs_list = set()

        # Loop for these two pieces
        for comb in combs:
            is_valid, valid_comb = valid_combination(comb)

            # If it's a valid combination
            if is_valid:
                if len(valid_combs_list) == 0:
                    valid_combs_list.add(valid_comb)
                else:
                    # Don't include duplicates
                    inc = True
                    check_combs = itertools.permutations(valid_comb,
                                                         len(valid_comb))
                    for check_comb in check_combs:
                        if check_comb in valid_combs_list:
                            inc = False
                            break

                    if inc:
                        valid_combs_list.add(valid_comb)

        comb_num = len(valid_combs_list)
        piece_iter = itertools.chain(valid_combs_list)

    # Gets number of combinations if not set
    if comb_num < 0:
        comb_num = sum(1 for x in piece_iter)

    if verbose:
        # Set final combinations to print
        final_combinations = piece_iter

        print ''
        print 'Combinations: '

        # Print combinations
        for elem in final_combinations:
            print elem

    # Set end time and print elapsed time
    elapsed_time = time.time() - start_time
    print ''
    print('Total elapsed time: {0} seconds'.format(elapsed_time))

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
    if not isinstance(combination[1][0], tuple):
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
    if first_piece[0] in ('Q', 'R'):
        if (first_piece[1] == second_piece[1] or
                first_piece[2] == second_piece[2]):
            return True

    # Diagonal: Queens and Bishops
    if first_piece[0] in ('Q', 'B'):
        if (abs(second_piece[1] - first_piece[1]) ==
                abs(second_piece[2] - first_piece[2])):
            return True

    # King
    if first_piece[0] == 'K':
        if (abs(second_piece[1] - first_piece[1]) in (0, 1) and
                abs(second_piece[2] - first_piece[2]) in (0, 1)):
            return True

    # Knight
    if first_piece[0] == 'N':
        if ((abs(second_piece[1] - first_piece[1]) == 2 and
             abs(second_piece[2] - first_piece[2]) == 1) or
                (abs(second_piece[1] - first_piece[1]) == 1 and
                 abs(second_piece[2] - first_piece[2]) == 2)):
            return True
