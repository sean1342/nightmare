import itertools

def remove_array_dupes(arr):
    seen = set()
    unique_arr = []
    for sub_arr in arr:
        sorted_tuple = tuple(sorted(sub_arr))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            unique_arr.append(sub_arr)
    return unique_arr

def find_paths(d1, d2, lines, path):
    if d1 == d2:
        return True

    for i, line in enumerate(lines):
        new_lines = lines[:i] + lines[i+1:]  # Create a new list excluding the current line
        if line[0] == d1:
            path.append(line[1])
            if find_paths(line[1], d2, new_lines, path):
                return True
            path.pop()  # Backtrack if not successful
        elif line[1] == d1:
            path.append(line[0])
            if find_paths(line[0], d2, new_lines, path):
                return True
            path.pop()  # Backtrack if not successful

    return False

def find_group(d, dots, lines):
    dots_in_group = [d]
    for dot in dots:
        if d != dot:
            if find_paths(d, dot, lines, []):
                dots_in_group.append(dot)
    return dots_in_group

def find_isolated_groups(g):
    groups = []
    for i in range(0, g.num_dots):
        groups.append(find_group(i, range(0,g.num_dots), g.lines))
        for j in range(0, g.num_dots):
            if i != j:
                if not find_paths(i, j, g.lines, []):
                    groups.append(find_group(i, range(0, g.num_dots), g.lines))
                    break
    groups = remove_array_dupes(groups)
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