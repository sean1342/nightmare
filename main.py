import itertools
import numpy

class GameState:
    def __init__(self, num_dots, line_end_dot_pairs, face_border_line_dot_pairs, faces_dots) -> None:
        self.num_dots = num_dots
        self.lines = line_end_dot_pairs
        self.faces = face_border_line_dot_pairs
        self.faces_dots = faces_dots

def are_lines_iso(g1, g2):
    association_exists = False

    unshaped_associations = numpy.array(list(itertools.product(list(range(1,g1.num_dots+1)), list(range(1,g1.num_dots+1)))))
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
                if (g2_line[0] == start_dot_g2 and g2_line[1] == end_dot_g2):# or (g2_line[1] == start_dot_g2 and g2_line[0] == end_dot_g2):
                    g1_line_exists_in_g2 = True

            if not g1_line_exists_in_g2:
                works = False

        if works:
            print(association)
            return True

    return True

def are_games_iso(g1, g2):
    if (    (g1.num_dots != g2.num_dots) or
            (len(g1.lines) != len(g2.lines)) or
            (len(g1.faces) != len(g2.faces)) or
            (len(g1.faces_dots) != len(g2.faces_dots))):
        return False

    if not are_lines_iso(g1, g2):
        return False
    
    return True

g1 = GameState(5, [[1,2], [2,3], [2,4], [4,5]], [], [])

g2 = GameState(5, [[3,4], [4,1], [4,2], [2,5]], [], [])

print(are_games_iso(g1, g2))