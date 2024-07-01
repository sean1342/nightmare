import itertools
import numpy

class GameState:
    def __init__(self, num_dots, line_end_dot_pairs, face_border_line_dot_pairs) -> None:
        self.num_dots = num_dots
        self.line_end_dot_pairs = line_end_dot_pairs
        self.face_border_line_dot_pairs = face_border_line_dot_pairs

def paths_through_permutations():
    pass

def are_games_iso(g1, g2):
    if (    (g1.num_dots != g2.num_dots) or
            (len(g1.line_end_dot_pairs) != len(g2.line_end_dot_pairs)) or
            (len(g1.face_border_line_dot_pairs) != len(g2.face_border_line_dot_pairs))):
        return False
    
    all_associations = numpy.array(list(itertools.product(list(range(1,g1.num_dots+1)), list(range(1,g1.num_dots+1)))))

    all_associations = all_associations.reshape(5,5,2)
    print(all_associations)

    routes = list(itertools.permutations(list(range(0, len(all_associations[0])))))

are_games_iso(GameState(5, [], []), GameState(5, [], []))
