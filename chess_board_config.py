# -*- coding: cp1252 -*-
"""Try Catch's Chess Challenge
The problem is to find all unique configurations of a set of normal chess
pieces on a chess board with dimensions M×N where none of the pieces is in
a position to take any of the others.
The colour of the piece does not matter, and there are no pawns
among the pieces.

Usage: chess_board_config.py [OPTIONS]

  Find configurations and print them to the screen

Options:
  -x INTEGER         Number of X.
  -y INTEGER         Number of Y.
  --kings INTEGER    Number of Kings.
  --queens INTEGER   Number of Queens.
  --bishops INTEGER  Number of Bishop.
  --rooks INTEGER    Number of Rooks.
  --knights INTEGER  Number of Knights.
  -v, --verbose      Writes the board combinations to the screen
  --help             Show this message and exit.

"""

import click
from chess_board_lib import find_configurations


def validate_board_dimensions(ctx, param, value):
    if value > 0:
        return value
    raise click.BadParameter('{0} should have a dimension'.format(param.name))


@click.command()
@click.option('-x', default=3,
              help='Number of X.',
              prompt='Number of X dimensions of the board?',
              callback=validate_board_dimensions,
              type=int)
@click.option('-y', default=3,
              help='Number of Y.',
              prompt='Number of Y dimensions of the board?',
              callback=validate_board_dimensions,
              type=int)
@click.option('--kings', default=0,
              help='Number of Kings.',
              prompt='Number of Kings placed on the board?',
              type=int)
@click.option('--queens', default=0,
              help='Number of Queens.',
              prompt='Number of Queens placed on the board?',
              type=int)
@click.option('--bishops', default=0,
              help='Number of Bishop.',
              prompt='Number of Bishops placed on the board?',
              type=int)
@click.option('--rooks', default=0,
              help='Number of Rooks.',
              prompt='Number of Rooks placed on the board?',
              type=int)
@click.option('--knights', default=0,
              help='Number of Knights.',
              prompt='Number of Knights placed on the board?',
              type=int)
@click.option('-v', '--verbose',
              count=True,
              help='Writes the board combinations to the screen')
def main(x, y, kings, queens, bishops, rooks, knights, verbose):
    """
    Find configurations and print them to the screen
    """

    configs = find_configurations(
        x, y, kings, queens, bishops, rooks, knights, verbose
    )

    # Print total number of configurations
    print ''
    print 'Total number of configurations: {0}'.format(configs)


if __name__ == '__main__':
    main()
