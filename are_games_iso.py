import itertools
import numpy

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