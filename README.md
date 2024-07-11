# DS5100-finalproject-nuf8ms

Name: Trenton Slocum\
Project: Monte Carlo Simulator

### Using The Monte Carlo Simulator

#### Install
1. Download the package
2. Navigate to the root directory of the package using Terminal
3. Install the 'montecarlo' package with:
```bash
pip install -e .
```

#### Import
1. Open desired python file
2. Import all classes and needed packages into the file
```Python
from montecarlo.montecarlo import Die, Game, Analyzer
import pandas as pd
import numpy as np
```

#### Usage
##### Die Class
1. Create dice
```Python
faces1 = np.array([1, 2, 3])
faces2 = np.array(['Heads', 'Tails'])

die1 = Die(faces1)
die2 = Die(faces2)
```
2. Change weights of dice sides
```Python
die1.change_side_weight(1, 5)
die2.change_side_weight('Heads', 5)
```
3. Roll the dice with desired number of rolls
```Python
die1.roll(20)
die2.roll(10)
```
4. Show the current weights of each face of the die
```Python
die1.current_state()
```

##### Game Class
1. Create Game
```Python
game1 = Game([die1, die2])
```
2. Play Game with desired number of rolls for the dice
```Python
game1.play(20)
```
3. Show results of the most recent play of the game. Frame can be wide or narrow
```Python
game1.last_round('wide')
game1.last_round('narrow')
```

##### Analyzer Class
1. Create Analyzer object
```Python
game1_analyzer = Analyzer(game1)
```
2. Show the frequency with which each face appeared in each roll
```Python
game1_analyzer.face_count()
```
3. Show the number of jackpots that appeared in the most recent play
```Python
game1_analyzer.jackpot()
```
4. Show the distinct number of combinations from the most recent play
```Python
game1_analyzer.combo_count()
```
5. Show the distinct number of permutations from the most recent play
```Python
game1_analyzer.permutation_count()
```

### API Description:

NAME
    montecarlo.montecarlo

CLASSES
    builtins.object
        Analyzer
        Die
        Game
    
    class Analyzer(builtins.object)
     |  Analyzer(game_object)
     |  
     |  The purpose of the Analyzer class is to take the results of a single game object and compute various descriptive statistical properties about it. These statistical properties include: number of jackpots (number of times all faces of the dice were the same for a single roll), the face count for each roll, and the number of combinations and permutations from a game.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game_object)
     |      Purpose: Check that passed object is of Game type.
     |      
     |      Parameters:
     |      game_object - Game object that has been played
     |      
     |      Returns: None
     |  
     |  combo_count(self, sort=True)
     |      Purpose:
     |      Computes the distinct combinations of faces rolled and their counts.
     |      
     |      Parameters:
     |      sort - Bool. True to output dataframe sorted by frequency. False to output dataframe sorted by index. Defaults to True.
     |      
     |      Returns:
     |      Dataframe with multiindex of distinct combinations and the associated frequencies.
     |  
     |  face_count(self)
     |      Purpose:
     |      Computes how many times a given face was rolled in each roll event
     |      
     |      Parameters:
     |      None
     |      
     |      Returns:
     |      Dataframe where each value corresponds to a roll and face. Value depicts number of times corresponding face appeared in the related roll
     |  
     |  jackpot(self)
     |      Purpose: Counts the frequency of jackpots from a game, or the number of results in which all faces were the same
     |      
     |      Parameters:
     |      None
     |      
     |      Returns:
     |      Prints the number of times a jackpot occured in a game
     |  
     |  permutation_count(self, sort=True)
     |      Purpose:
     |      Computes the distinct permutations of faces rolled and their counts.
     |      
     |      Parameters:
     |      sort - Bool. True to output dataframe sorted by frequency. False to output dataframe sorted by index. Defaults to True.
     |      
     |      Returns:
     |      Dataframe with multiindex of distinct permutations and the associated frequencies.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(face_symbols)
     |  
     |  Purpose: The purpose of the Die class is to create dice to be used in the Game class. Every created die can can be customized to contain any number of string/number faces, with each face having any desired weight. Dice default as fair, meaning that face weights default to 1.0
     |  
     |  Methods defined here:
     |  
     |  __init__(self, face_symbols)
     |      Purpose: 
     |      Creates the die and ensures that the passed face_symbols argument an array with valid face symbols. Sets the weight of each face of the die to the default 1.0.
     |      
     |      Parameters: 
     |      face_symbols - numpy array of desired face symbols. Symbols must be of data type string, integer, or float. All face symbols in array must be of same data type.
     |      
     |      Returns: 
     |      None
     |  
     |  change_side_weight(self, face, new_weight)
     |      Purpose: 
     |      Change the weight of a specific side of the created die.
     |      
     |      Parameters:
     |      face - Face that user would like to change the weight of. Can be of type integer, float, or string. Must already exist on the created die
     |      new_weight - New weight to be assigned to the passed face. Can be integer or float.
     |      
     |      Returns:
     |      None
     |  
     |  current_state(self)
     |      Purpose:
     |      Show user the current faces and weights of the die
     |      
     |      Parameters:
     |      None
     |      
     |      Returns:
     |      Dataframe of faces on the die with the related weight for each face
     |  
     |  roll(self, n=1)
     |      Purpose:
     |      Roll your created die 'n' number of times and output results
     |      
     |      Parameters:
     |      n - Integer number of desired rolls. Defaults to 1
     |      
     |      Returns:
     |      List of results from rolls
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(die_list)
     |  
     |  The purpose of the Game class is to take a list of die objects and roll each of them a specified number of times. The user can then access the results of the most recent play.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, die_list)
     |      Purpose:
     |      Initialize the game by taking a list of die objects
     |      
     |      Parameters:
     |      die_list - list of die objects. All dice must have the same number of faces
     |      
     |      Returns:
     |      None
     |  
     |  last_round(self, form='wide')
     |      Purpose: Print dataframe of all rolls and values from most recent play. Table can be either wide or narrow format, depending on passed preference
     |      
     |      Parameters:
     |      form - Input must be strings 'wide' or 'narrow' to request the respective table. Can be left empty to default to wide table.
     |      
     |      Returns:
     |      Dataframe of results from the most recent play. Format will be either wide or narrow.
     |  
     |  play(self, n)
     |      Purpose:
     |      Roll all dice a specified n number of times to simulate "play." Records all rolls and values.
     |      
     |      Parameters:
     |      n - integer number of times you would like all dice to be rolled. Applies to all dice together, cannot be specific to each
     |      
     |      Returns:
     |      None
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)