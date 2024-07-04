import itertools
import numpy
from gen_child_states import *
from are_games_iso import *

class GameState:
    def __init__(self, num_dots, line_end_dot_pairs, face_border_line_dot_pairs, faces_dots) -> None:
        self.num_dots = num_dots
        self.lines = line_end_dot_pairs
        self.faces = face_border_line_dot_pairs
        self.faces_dotss = faces_dots

g1 = GameState(6, [(1,2), (1,3), (3,0), (0,1), (1,4)], [[(1,0), (0,3), (3,1)]], [[4, 5]])
g2 = GameState(5, [(1,4), (4,3), (3,2), (2,4), (4,0)], [[(4,3), (3,2), (2,4)]], [[0]])
#print(are_games_iso(g1, g2))

g = GameState(5, [(0,4), (1,3), (1,2), (3,2)], [[(1,2), (1,3), (3,2)]], [[]])

fucker = GameState(7, [(1,0), (6,2), (3,5)], [[(1,0)], [(6,2)], [(3,5)]], [[6,2], [3,5], [4]])

#print(find_isolated_groups(fucker))

#print(find_parent_dots(6, fucker))

print(find_group(5, fucker), -1)