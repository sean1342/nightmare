import itertools

def find_paths(d1, d2, lines, path):
    if d1 == d2:
        path.append(d2)
        return path, True
    else:
        for line in lines:
            if line[0] == d1:
                lines.remove(line)
                path.append(line[1])
                return path, find_paths(line[1], d2, lines, path)
            if line[1] == d1:
                lines.remove(line)
                path.append(line[0])
                return path, find_paths(line[0], d2, lines, path)

def find_isolated_groups(g):
    for i in range(0, g.num_dots):
        for j in range(0, g.num_dots):
            _, is_path = find_paths(i, j, g.lines)
            
            if not is_path:
                return True

def generate_moves(g):
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotts):
                    pass
                else:
                    # if isolated groups, use 2^n thing
                    pass