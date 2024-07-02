import itertools

def find_paths(d1, d2, lines, path):
    if d1 == d2:
        return path
    else:
        for line in lines:
            if line[0] == d1:
                lines.remove(line)
                path.append(line[1])
                return find_paths(line[1], d2, lines, path)
            if line[1] == d1:
                lines.remove(line)
                path.append(line[0])
                return find_paths(line[0], d2, lines, path)

def find_group(d, dots, lines):
    dots_in_group = [d]
    for dot in dots:
        path_exists = find_paths(d, dot, lines, [])
        if path_exists:
            dots_in_group.append(dot)
    return dots_in_group

def find_isolated_groups(g):
    groups = []
    for i in range(0, g.num_dots):
        for j in range(0, g.num_dots):
            path = find_paths(i, j, g.lines)

            # FIX THIS
            if not is_path:
                groups.append(find_group(i))
                groups.append(find_group(j))
    return groups

def generate_moves(g):
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:

                # this is if both dots are inside of faces
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotts):
                    pass

                # if isolated groups, use 2^n thing
                else:
                    pass