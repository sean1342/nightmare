import itertools

def find_paths(d1, d2, lines, path):
    _lines = lines.copy()
    if d1 == d2:
        return path
    else:
        for line in _lines:
            if line[0] == d1:
                _lines.remove(line)
                path.append(line[1])
                return find_paths(line[1], d2, _lines, path)
            if line[1] == d1:
                _lines.remove(line)
                path.append(line[0])
                return find_paths(line[0], d2, _lines, path)

def find_group(d, dots, lines):
    dots_in_group = [d]
    for dot in dots:
        if d != dot:
            path = find_paths(d, dot, lines, [])
            if path != None:
                dots_in_group.append(dot)
    return dots_in_group

def find_isolated_groups(g):
    groups = []
    for i in range(0, g.num_dots):
        for j in range(0, g.num_dots):
            if i != j:
                path = find_paths(i, j, g.lines, [])

                if path == None:
                    print(i, j)
                    print(g.lines)
                    groups.append(find_group(i, range(0, g.num_dots), g.lines))
                    break
    for group_a in groups:
        for group_b in groups:
            if group_a != group_b and set(group_a) == set(group_b):
                groups.remove(group_b)
    return groups

def generate_moves(g):
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:

                # this is if both dots are inside of faces
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotts):
                    pass

                # if one is in and one isnt
                elif i in itertoolsitertools.chain.from_iterable(g.faces_dotss) and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    pass

                # if both are on outside
                elif (i in itertools.chain.from_iterable(g.faces_dotss)) == False and (j in itertools.chain.from_iterable(g.faces_dotts)) == False:
                    pass