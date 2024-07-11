import numpy as np
import pandas as pd

class Die():
    '''
    Docstring
    '''
    def __init__(self, face_symbols):
        
        # Test for numpy array
        if not isinstance(face_symbols, np.ndarray):
            raise TypeError('Face Argument must be NumPy array')
          
        # Tests that array is strings or numbers
        if face_symbols.dtype.char not in ['U', 'l', 'd']:
            raise TypeError('Faces must be strings or numbers')
        
        # Tests for unique faces
        if len(set(face_symbols)) != len(face_symbols):
            raise ValueError('Face values must be distinct')
        
        # Initialize weights as 1.0 for each face
        self.faces = face_symbols
        self.weights = [1.0 for i in face_symbols]
        
        # Save faces and weights in private data frame
        self._faces_weights = pd.DataFrame(self.weights, self.faces, columns=['weight'])
        
    def change_side_weight(self, face, new_weight):
        if face not in self._faces_weights.index:
            raise IndexError('That face does not exist on this die')
        if type(new_weight) not in [int, float]:
            raise ValueError('Weight is not a valid type')
        
        self._faces_weights.loc[face] = new_weight
        
    def roll(self, n = 1):
        results = []
        self.probs = [i/sum(self._faces_weights.weight) for i in self._faces_weights.weight]
        
        for i in range(n):
            result = self._faces_weights.sample(weights = self.probs).index.values[0]
            results.append(result)
            
        return results
        
    def current_state(self):
        return self._faces_weights
        
class Game():
    
    def __init__(self, die_list):
        self.die_list = die_list
    
    def play(self, n):
        self.df_index = []
        for i in range(n):
            self.df_index.append('Roll ' + str(i + 1))
        
        self._play_results = pd.DataFrame([], self.df_index)
        
        for die in self.die_list:
            self._play_results.insert(self.die_list.index(die), self.die_list.index(die) + 1, die.roll(n))
    
    def last_round(self, form = 'wide'):
        if form == 'narrow':
            return self._play_results.stack().to_frame('Value')
        elif form == 'wide':
            return self._play_results
        else:
            raise ValueError('Must request for a "narrow" or "wide" table')
        
class Analyzer():
    def __init__(self, game_object):
        if not isinstance(game_object, Game):
            raise ValueError('Passed value is not a Game object')
        
        self.game = game_object
        
        self.outcome = game_object._play_results
    
    def jackpot(self):
        count = 0
        for i in self.outcome.nunique(axis=1) == 1:
            if i == True:
                count += 1
        
        return count
    
    def face_count(self):
        return pd.DataFrame(self.outcome).apply(pd.Series.value_counts, axis = 1).fillna(0)
    
    def combo_count(self, sort = True):
        sorted_outcome = self.outcome.apply(sorted, axis = 1, result_type = 'broadcast')
        return sorted_outcome.value_counts(sort = sort).to_frame('Combination Count')
    
    def permutation_count(self, sort = True):
        return self.outcome.value_counts(sort = sort).to_frame('Permutation Count')