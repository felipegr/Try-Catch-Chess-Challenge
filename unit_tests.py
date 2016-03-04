import unittest
from chess_board_config import find_configurations

class TestMethods(unittest.TestCase):

  def test_one_piece_only(self):
      self.assertEqual(find_configurations(3, 3, 1, 0, 0, 0, 0), 9)
      self.assertEqual(find_configurations(4, 4, 0, 0, 0, 1, 0), 16)

if __name__ == '__main__':
    unittest.main()
