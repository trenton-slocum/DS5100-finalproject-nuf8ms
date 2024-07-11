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