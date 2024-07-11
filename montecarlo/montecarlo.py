import numpy as np
import pandas as pd

class Die():
    '''
    Purpose: The purpose of the Die class is to create dice to be used in the Game class. Every created die can can be customized to contain any number of string/number faces, with each face having any desired weight. Dice default as fair, meaning that face weights default to 1.0
    '''
    def __init__(self, face_symbols):
        '''
        Purpose: 
        Creates the die and ensures that the passed face_symbols argument an array with valid face symbols. Sets the weight of each face of the die to the default 1.0.
        
        Parameters: 
        face_symbols - numpy array of desired face symbols. Symbols must be of data type string, integer, or float. All face symbols in array must be of same data type.
        
        Returns: 
        None
        '''
        
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
        '''
        Purpose: 
        Change the weight of a specific side of the created die.
        
        Parameters:
        face - Face that user would like to change the weight of. Can be of type integer, float, or string. Must already exist on the created die
        new_weight - New weight to be assigned to the passed face. Can be integer or float.
        
        Returns:
        None
        '''
        if face not in self._faces_weights.index:
            raise IndexError('That face does not exist on this die')
        if type(new_weight) not in [int, float]:
            raise ValueError('Weight is not a valid type')
        
        self._faces_weights.loc[face] = new_weight
        
    def roll(self, n = 1):
        '''
        Purpose:
        Roll your created die 'n' number of times and output results
        
        Parameters:
        n - Integer number of desired rolls. Defaults to 1
        
        Returns:
        List of results from rolls
        '''
        results = []
        self.probs = [i/sum(self._faces_weights.weight) for i in self._faces_weights.weight]
        
        for i in range(n):
            result = self._faces_weights.sample(weights = self.probs).index.values[0]
            results.append(result)
            
        return results
        
    def current_state(self):
        '''
        Purpose:
        Show user the current faces and weights of the die
        
        Parameters:
        None
        
        Returns:
        Dataframe of faces on the die with the related weight for each face
        '''
        return self._faces_weights
        
class Game():
    '''
    The purpose of the Game class is to take a list of die objects and roll each of them a specified number of times. The user can then access the results of the most recent play.
    '''
    
    def __init__(self, die_list):
        '''
        Purpose:
        Initialize the game by taking a list of die objects
        
        Parameters:
        die_list - list of die objects. All dice must have the same number of faces
        
        Returns:
        None
        '''
        self.die_list = die_list
    
    def play(self, n):
        '''
        Purpose:
        Roll all dice a specified n number of times to simulate "play." Records all rolls and values.
        
        Parameters:
        n - integer number of times you would like all dice to be rolled. Applies to all dice together, cannot be specific to each
        
        Returns:
        None
        '''
        self.df_index = []
        for i in range(n):
            self.df_index.append('Roll ' + str(i + 1))
        
        self._play_results = pd.DataFrame([], self.df_index)
        
        for i, die in enumerate(self.die_list):
            self._play_results.insert(i, i + 1, die.roll(n))
    
    def last_round(self, form = 'wide'):
        '''
        Purpose: Print dataframe of all rolls and values from most recent play. Table can be either wide or narrow format, depending on passed preference
        
        Parameters:
        form - Input must be strings 'wide' or 'narrow' to request the respective table. Can be left empty to default to wide table.
        
        Returns:
        Dataframe of results from the most recent play. Format will be either wide or narrow.
        '''
        if form == 'narrow':
            return self._play_results.stack().to_frame('Value')
        elif form == 'wide':
            return self._play_results
        else:
            raise ValueError('Must request for a "narrow" or "wide" table')
        
class Analyzer():
    '''
    The purpose of the Analyzer class is to take the results of a single game object and compute various descriptive statistical properties about it. These statistical properties include: number of jackpots (number of times all faces of the dice were the same for a single roll), the face count for each roll, and the number of combinations and permutations from a game.
    '''
    def __init__(self, game_object):
        '''
        Purpose: Check that passed object is of Game type.
        
        Parameters:
        game_object - Game object that has been played
        
        Returns: None
        '''
        if not isinstance(game_object, Game):
            raise ValueError('Passed value is not a Game object')
        
        self.game = game_object
        
        self.outcome = game_object._play_results
    
    def jackpot(self):
        '''
        Purpose: Counts the frequency of jackpots from a game, or the number of results in which all faces were the same
        
        Parameters:
        None
        
        Returns:
        Prints the number of times a jackpot occured in a game
        '''
        count = 0
        for i in self.outcome.nunique(axis=1) == 1:
            if i == True:
                count += 1
        
        return count
    
    def face_count(self):
        '''
        Purpose:
        Computes how many times a given face was rolled in each roll event
        
        Parameters:
        None
        
        Returns:
        Dataframe where each value corresponds to a roll and face. Value depicts number of times corresponding face appeared in the related roll
        '''
        return pd.DataFrame(self.outcome).apply(pd.Series.value_counts, axis = 1).fillna(0)
    
    def combo_count(self, sort = True):
        '''
        Purpose:
        Computes the distinct combinations of faces rolled and their counts.
        
        Parameters:
        sort - Bool. True to output dataframe sorted by frequency. False to output dataframe sorted by index. Defaults to True.
        
        Returns:
        Dataframe with multiindex of distinct combinations and the associated frequencies.
        '''
        sorted_outcome = self.outcome.apply(sorted, axis = 1, result_type = 'broadcast')
        return sorted_outcome.value_counts(sort = sort).to_frame('Combination Count')
    
    def permutation_count(self, sort = True):
        '''
        Purpose:
        Computes the distinct permutations of faces rolled and their counts.
        
        Parameters:
        sort - Bool. True to output dataframe sorted by frequency. False to output dataframe sorted by index. Defaults to True.
        
        Returns:
        Dataframe with multiindex of distinct permutations and the associated frequencies.
        '''
        return self.outcome.value_counts(sort = sort).to_frame('Permutation Count')