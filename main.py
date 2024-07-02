import itertools
import numpy
from genmoves import generate_moves, find_paths, find_group, find_isolated_groups

class GameState:
    def __init__(self, num_dots, line_end_dot_pairs, face_border_line_dot_pairs, faces_dots) -> None:
        self.num_dots = num_dots
        self.lines = line_end_dot_pairs
        self.faces = face_border_line_dot_pairs
        self.faces_dotss = faces_dots

def are_lines_iso(g1, g2):
    good = False
    good_associations = []

    unshaped_associations = numpy.array(list(itertools.product(list(range(0,g1.num_dots)), list(range(0,g1.num_dots)))))
    unshaped_associations = list(unshaped_associations.reshape(g1.num_dots,g1.num_dots,2))

    routes = list(itertools.permutations(list(range(0, len(unshaped_associations[0])))))

    associations = []
    for route in routes:
        association = []
        for j in route:
            association.append(unshaped_associations[j][route[j]])
        association= sorted(association, key=lambda x: x[0])
        associations.append(association)

    for association in associations:
        works = True
        for g1_line in g1.lines:
            g1_line_exists_in_g2 = False

            start_dot_g1 = g1_line[0]
            end_dot_g1 = g1_line[1]

            start_dot_g2 = association[start_dot_g1-1][1]
            end_dot_g2 = association[end_dot_g1-1][1]

            for g2_line in g2.lines:
                if (g2_line[0] == start_dot_g2 and g2_line[1] == end_dot_g2) or (g2_line[1] == start_dot_g2 and g2_line[0] == end_dot_g2):
                    g1_line_exists_in_g2 = True

            if not g1_line_exists_in_g2:
                works = False

        if works:
            good_associations.append(association)

            good = True

    if good:
        return good_associations, True
    else:
        return None, False

def are_faces_iso(g1, g2, good_associations):
    better_associations = []
    works = False
    for association in good_associations:
        good = False
        for i, face_dots in enumerate(g1.faces_dotss):
            for j, dot in enumerate(face_dots):
                if association[dot-1][1] == g2.faces_dotss[i][j]:
                    good = True
        if good:
            better_associations.append(association)
            works = True
    
    return better_associations, works

def are_games_iso(g1, g2):
    if (    (g1.num_dots != g2.num_dots) or
            (len(g1.lines) != len(g2.lines)) or
            (len(g1.faces) != len(g2.faces)) or
            (len(g1.faces_dotss) != len(g2.faces_dotss))):
        return False

    good_associations, lines_iso = are_lines_iso(g1, g2)
    if not lines_iso:
        return False

    better_associations, faces_iso = are_faces_iso(g1, g2, good_associations)
    if not faces_iso:
        return False
    
    print(better_associations)
    
    return True

g1 = GameState(5, [(1,2), (1,3), (3,0), (0,1), (1,4)], [[(1,0), (0,3), (3,1)]], [[4]])
g2 = GameState(5, [(1,4), (4,3), (3,2), (2,4), (4,0)], [[(4,3), (3,2), (2,4)]], [[0]])
#print(are_games_iso(g1, g2))

g = GameState(5, [(0,4), (1,3), (1,2), (3,2)], [[((1,2), (1,3), (3,2))]], [[]])

#print(find_paths(0, 4, g.lines, []))
print(find_isolated_groups(g1))