from gamestate import GameState
from gen_child_states import *
from are_games_iso import *

g1 = GameState(6, [(1,2), (1,3), (3,0), (0,1), (1,4)], [[(1,0), (0,3), (3,1)]], [[4, 5]])
g2 = GameState(5, [(1,4), (4,3), (3,2), (2,4), (4,0)], [[(4,3), (3,2), (2,4)]], [[0]])

g = GameState(5, [(0,4), (1,3), (1,2), (3,2)], [[(1,2), (1,3), (3,2)]], [[]])

bad_game = GameState(7, [(1,0), (6,2), (3,5)], [[(1,0)], [(6,2)], [(3,5)]], [[6,2], [3,5], [4]])

worse_game = GameState(5, [(4,4), (1,0), (2,3)], [[(4,4)], [(1,0)], [(2,3)]], [[1, 2, 3, 0], [], []])

#gen_child_states(g1)

print(is_on_outside(5, g1))