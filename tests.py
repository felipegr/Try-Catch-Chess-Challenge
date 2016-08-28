import unittest
from chess_board_lib import find_configurations, valid_combination, threats


class TestMethods(unittest.TestCase):
    def test_validations(self):
        try:
            find_configurations(0, 0, 1, 1, 1, 1, 1, False)
        except Exception as e:
            self.assertEquals(type(e), ValueError)

        try:
            find_configurations(1, 1, 0, 0, 0, 0, 0, False)
        except Exception as e:
            self.assertEquals(type(e), ValueError)

        try:
            find_configurations(3, 3, 9, 1, 0, 0, 0, False)
        except Exception as e:
            self.assertEquals(type(e), ValueError)

    def test_threats(self):
        self.assertTrue(threats(('R', 3, 3), ('Q', 3, 3)))
        self.assertTrue(threats(('Q', 3, 3), ('Q', 0, 0)))
        self.assertTrue(threats(('Q', 3, 3), ('Q', 0, 3)))
        self.assertFalse(threats(('Q', 0, 0), ('Q', 5, 4)))
        self.assertTrue(threats(('B', 1, 2), ('Q', 3, 0)))
        self.assertFalse(threats(('B', 1, 2), ('Q', 2, 2)))
        self.assertTrue(threats(('R', 5, 3), ('Q', 5, 5)))
        self.assertFalse(threats(('R', 5, 3), ('Q', 4, 2)))
        self.assertTrue(threats(('K', 4, 3), ('Q', 3, 4)))
        self.assertFalse(threats(('K', 4, 3), ('Q', 2, 5)))
        self.assertTrue(threats(('N', 0, 1), ('Q', 2, 2)))
        self.assertFalse(threats(('N', 0, 1), ('Q', 1, 2)))

    def test_valid_combinations(self):
        self.assertTrue(valid_combination((('R', 0, 0), ('R', 1, 1)))[0])
        self.assertEqual(valid_combination((('R', 0, 0), ('R', 1, 1)))[1],
                         (('R', 1, 1), ('R', 0, 0)))
        self.assertEqual(
            valid_combination((('R', 0, 0), (('R', 1, 1), ('R', 2, 2))))[1],
            (('R', 1, 1), ('R', 2, 2), ('R', 0, 0)))
        self.assertNotEqual(
            valid_combination((('R', 0, 0), (('R', 1, 1), ('R', 2, 2))))[1],
            (('R', 0, 0), ('R', 1, 1), ('R', 2, 2)))
        self.assertFalse(valid_combination((('R', 0, 0), ('Q', 0, 0)))[0])
        self.assertTrue(
            valid_combination((('R', 0, 0), (('R', 1, 1), ('R', 2, 2))))[0])
        self.assertFalse(valid_combination(
            (('R', 0, 0), (('R', 1, 1), ('R', 2, 2), ('B', 3, 3))))[0])

    def test_one_piece_only(self):
        self.assertEqual(find_configurations(3, 3, 1, 0, 0, 0, 0, False), 9)
        self.assertEqual(find_configurations(4, 4, 0, 0, 0, 1, 0, False), 16)

    def test_know_combinations(self):
        self.assertEqual(find_configurations(3, 3, 2, 0, 0, 1, 0, False), 4)
        self.assertEqual(find_configurations(4, 4, 0, 0, 0, 2, 4, True), 8)
        # add more code coverage to the tests.
        self.assertEqual(find_configurations(4, 4, 1, 1, 1, 1, 1, False), 16)


if __name__ == '__main__':
    unittest.main()
