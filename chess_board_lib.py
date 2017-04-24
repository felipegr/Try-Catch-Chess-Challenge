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
    """
    Find and print all configurations for a chess board where no piece
    threats another.
    Args:
        x_dim: Number of squares of the X dimension of the board
        y_dim: Number of squares of the Y dimension of the board
        kings: Number of Kings to be placed on the board
        queens: Number of Queens to be placed on the board
        bishops: Number of Bishops to be placed on the board
        rooks: Number of Rooks to be placed on the board
        knights: Number of Knights to be placed on the board
        verbose: Stdout configurations.

    Returns: comb_num Returns the number of configurations found.

    """

    # Some arguments checking
    # Check if dimensions are greater than zero
    if x_dim <= 0 or y_dim <= 0:
        raise ValueError(
            "Dimensions X={0} Y={1}, "
            "they must be both greater than zero.".format(x_dim, y_dim)
        )

    # Check if there are pieces to be placed
    total_pieces = kings + queens + bishops + rooks + knights
    if total_pieces == 0:
        raise ValueError("There aren't pieces to be placed, "
                         "add some of those chess pieces: "
                         "kings, queens, bishops, rooks, knights")

    # Check if number of pieces is correct
    board_dims = x_dim * y_dim
    if total_pieces > board_dims:
        raise ValueError(
            "The dimension of the board is {0} and the pieces quantity are {1}"
            " Please add a bigger board or use less pieces :)".format(
                board_dims, total_pieces
            )
        )

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
                    if not is_duplicate(valid_comb, valid_combs_list):
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
    print 'Total elapsed time: {0} seconds'.format(elapsed_time)

    return comb_num


def valid_combination(combination):
    """
    Check if a combination is one where no piece is threatened.
    Args:
        combination: Tuple with positions of pieces

    Returns: Returns a boolean that tells if the combination
    is one where no piece is threatened and the combination itself as a Tuple.

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
    """
    Check if there's a threat between two pieces.
    Args:
        first_piece: Tuple with a piece type, x position and y position
        second_piece: Tuple with a piece type, x position and y position

    Returns: Returns a boolean if one of the pieces threats the other.

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


def is_duplicate(combination, list_of_combinations):
    """
    Check if a combination exists in a list of combinations.
    Args:
        combination: Tuple with positions of pieces
        list_of_combinations:  List of Tuples with positions of pieces

    Returns: Returns True if the combination is contained in the list,
    False otherwise.

    """
    is_contained = False
    # Create permutations of the combination
    check_combs = itertools.permutations(combination, len(combination))
    # Check if any permutation is contained in the list
    for check_comb in check_combs:
        if check_comb in list_of_combinations:
            is_contained = True
            break

    return is_contained
