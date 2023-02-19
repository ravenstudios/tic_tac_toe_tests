import unittest

import tictactoe


class TestRow(unittest.TestCase):



    def test_row_row0_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a row
        """
        data = ["X", "X", "X", "O", "_", "O", "_", "_", "_"]
        result = ttt.row_check(data)
        self.assertEqual(result, True)


    def test_row_row0_dash(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a row
        """
        data = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        result = ttt.row_check(data)
        self.assertEqual(result, False)


    def test_row_row1_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a row
        """
        data = ["X", "X", "_", "O", "O", "O", "_", "_", "_"]
        result = ttt.row_check(data)
        self.assertEqual(result, True)


    def test_row_row2_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a row
        """
        data = ["X", "_", "X", "_", "O", "O", "X", "X", "X"]
        result = ttt.row_check(data)
        self.assertEqual(result, True)

    def test_col_col0_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["X", "X", "X", "X", "_", "O", "X", "_", "_"]
        result = ttt.col_check(data)
        self.assertEqual(result, True)

    def test_col_col1_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["X", "X", "_", "O", "X", "O", "_", "X", "_"]
        result = ttt.col_check(data)
        self.assertEqual(result, True)


    def test_col_col2_won(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["X", "_", "O", "_", "O", "O", "X", "X", "O"]
        result = ttt.col_check(data)
        self.assertEqual(result, True)

    def test_row_stop_win1(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["X", "X", "_", "_", "_", "_", "_", "_", "_"]
        result = ttt.row_stop_win_check(data)
        self.assertEqual(result, 2)

    def test_row_stop_win2(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["_", "X", "_", "_", "_", "_", "_", "_", "_"]
        result = ttt.row_stop_win_check(data)
        self.assertEqual(result, -1)

    def test_row_stop_win3(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["_", "X", "_", "X", "_", "X", "_", "_", "_"]
        result = ttt.row_stop_win_check(data)
        self.assertEqual(result, 4)


    def test_row_stop_win4(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["_", "X", "_", "_", "_", "_", "_", "X", "X"]
        result = ttt.row_stop_win_check(data)
        self.assertEqual(result, 6)

    def test_row_stop_win5(self):
        ttt = tictactoe.Tic_Tac_Toe()
        """
        Test that checks if 3 in a col
        """
        data = ["_", "X", "_", "_", "_", "_", "O", "X", "X"]
        result = ttt.row_stop_win_check(data)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
