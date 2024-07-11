from montecarlo.montecarlo import Die, Game, Analyzer
import unittest
import pandas as pd
import numpy as np

class MontecarloTestSuite(unittest.TestCase):
    
    # Die() Class
    def test_1_isarray(self):
        
        with self.assertRaises(TypeError):
            Die([1, 2, 3])
    
    def test_2_array_type(self):
        
        with self.assertRaises(TypeError):
            Die(np.array([True, False]))
    
    def test_3_distinct_faces(self):
        
        with self.assertRaises(ValueError):
            Die(np.array([1, 1, 2]))
    
    def test_4_change_side_weight__face(self):
        die1 = Die(np.array([1, 2, 3]))
        
        with self.assertRaises(IndexError):
            die1.change_side_weight(4, 2)
    
    def test_5_change_side_weight__weight_type(self):
        die1 = Die(np.array([1, 2, 3]))
        
        with self.assertRaises(ValueError):
            die1.change_side_weight(1, 'weight')
    
    def test_6_change_side_weight__weight(self):
        die1 = Die(np.array([1, 2, 3]))
        die1.change_side_weight(1, 4)
        
        expected = 4
        
        self.assertTrue(die1._faces_weights.weight[1] == expected)
    
    def test_7_roll(self):
        die1 = Die(np.array([1, 2, 3]))
        
        expected = 3
        
        self.assertEqual(len(die1.roll(3)), expected)
    
    def test_8_current_state(self):
        die1 = Die(np.array([1, 2, 3]))
        
        expected = pd.DataFrame([1.0, 1.0, 1.0], [1, 2, 3], columns = ['weight'])
        
        self.assertTrue(die1.current_state().equals(expected))
    
    # Game() Class
    def test_9_is_die_list(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
            
        self.assertTrue(isinstance(game1.die_list, list))
        
    def test_10_play(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        expected = (3, 2)
        
        self.assertEqual(game1._play_results.shape, expected)
    
    def test_11_last_round_wide(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        expected = (3, 2)
        
        self.assertEqual(game1.last_round().shape, expected)
    
    def test_12_last_round_narrow(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        expected = (6, 1)
        
        self.assertEqual(game1.last_round('narrow').shape, expected)

    def test_13_last_round_error(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        with self.assertRaises(ValueError):
            game1.last_round('test')
    
    # Analyzer() Class
    def test_14_is_game(self):
        game = 5
        
        with self.assertRaises(ValueError):
            Analyzer(game)
    
    def test_15_jackpot(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        analyzer1 = Analyzer(game1)
        analyzer1.outcome = pd.DataFrame([[1, 1], [1, 0]], [1, 2], columns = [1, 2])
        expected = 1
        
        self.assertEqual(analyzer1.jackpot(), expected)
    
    def test_16_face_count(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        analyzer1 = Analyzer(game1)
        analyzer1.outcome = pd.DataFrame(np.array([[1, 1, 3, 3, 5], [1, 1, 2, 2, 4]]), columns = [1, 2, 3, 4, 5])
        
        expected = pd.DataFrame(np.array([[2.0, 0.0, 2.0, 0.0, 1.0], [2.0, 2.0, 0.0, 1.0, 0.0]]), columns = [1, 2, 3, 4, 5])
        
        self.assertTrue(analyzer1.face_count().equals(expected))
    
    def test_17_combo_count(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        analyzer1 = Analyzer(game1)
        analyzer1.outcome = pd.DataFrame(np.array([[1, 2, 3], [3, 2, 1]]), columns = [1, 2, 3])
        
        expected = (1, 1)
        
        self.assertTrue(analyzer1.combo_count().shape == expected)
        
    def test_18_permutation_count(self):
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        die_list = [die1, die2]
        
        game1 = Game(die_list)
        game1.play(3)
        
        analyzer1 = Analyzer(game1)
        analyzer1.outcome = pd.DataFrame(np.array([[1, 2, 3], [3, 2, 1]]), columns = [1, 2, 3])
        
        expected = (2, 1)
        
        self.assertTrue(analyzer1.permutation_count().shape == expected)
        
if __name__ == '__main__':
    unittest.main(verbosity = 3)