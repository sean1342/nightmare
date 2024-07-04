import itertools

def find_parent_dots(d, g):
    group = []
    for i, face_dots in enumerate(g.faces_dotss):
        if d in face_dots:
            group = (g.faces[i])
    if group == []:
        return None
    return group

def find_child_dots(d, g):
    child_dots = []
    for i, face in enumerate(g.faces):
        if d in itertools.chain.from_iterable(face) and g.faces_dotss[i] != []:
            child_dots.extend(g.faces_dotss[i])
    if child_dots == []:
        return None
    return child_dots

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

def find_group(d, g):
    dots_in_group = [d]
    for dot in range(0, g.num_dots):
        if d != dot:
            if find_paths(d, dot, g.lines, []):
                dots_in_group.append(dot)
    return dots_in_group

def find_isolated_groups(g):
    groups = []
    return groups

def gen_child_states(g):
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:

                # this is if both dots are inside of faces
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotss):
                    print("both inside", i, j)

                # if one is in and one isnt
                elif i in itertools.chain.from_iterable(g.faces_dotss) and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    print("one and one", i, j)

                # if both are on outside
                elif (i in itertools.chain.from_iterable(g.faces_dotss)) == False and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    print("both on border", i, j)
