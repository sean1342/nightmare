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

def find_parent_face(d, faces, face_dots):
    for i, face_dot in enumerate(face_dots):
        if d in face_dot:
            return faces[i]
    return None

def find_child_dots(d, faces, face_dots):
    dots = []
    for i, face_line_pairs in enumerate(faces):
        if d in face_line_pairs:
            dots.append(face_dots[i])
    return dots

def find_paths(d1, d2, lines, path):
    if d1 == d2:
        return path

    for i, line in enumerate(lines):
        new_lines = lines[:i] + lines[i+1:]  # Create a new list excluding the current line
        if line[0] == d1:
            new_path = find_paths(line[1], d2, new_lines, path + [line[1]])
            if new_path:
                return new_path
        elif line[1] == d1:
            new_path = find_paths(line[0], d2, new_lines, path + [line[0]])
            if new_path:
                return new_path

    return None

def find_group(d, dots, lines, faces, face_dots):
    dots_in_group = [d]
    for dot in dots:
        if d != dot:
            if find_paths(d, dot, lines, []):
                dots_in_group.append(dot)
                for child_dot in find_child_dots(dot, faces, face_dots):
                    if find_paths(d, child_dot, lines, []) == False and child_dot not in dots_in_group:
                        dots_in_group.append(child_dot)

    return dots_in_group

def find_isolated_groups(g):
    groups = []
    for i in range(0, g.num_dots):
        # this adds the one group if there are no disconnected dots in the game.
        groups.append(find_group(i, range(0,g.num_dots), g.lines, g.faces, g.faces_dotss))
        for j in range(0, g.num_dots):
            if i != j:
                if (    find_paths(i, j, g.lines, []) == None and
                        find_parent_face(i, g.faces, g.faces_dotss) == None and
                        find_parent_face(j, g.faces, g.faces_dotss) == None):
                    print(i in itertools.chain.from_iterable(g.faces_dotss))
                    print(j in itertools.chain.from_iterable(g.faces_dotss))
                    print(i, j)
                    groups.append(find_group(i, range(0, g.num_dots), g.lines, g.faces, g.faces_dotss))
                    break
    groups = remove_array_dupes(groups)
    return groups

def gen_child_states(g):
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:

                # this is if both dots are inside of faces
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotss):
                    pass

                # if one is in and one isnt
                elif i in itertools.chain.from_iterable(g.faces_dotss) and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    pass

                # if both are on outside
                elif (i in itertools.chain.from_iterable(g.faces_dotss)) == False and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    # case that i and j are in same group
                    if sorted(find_group(i, range(0, g.num_dots), g.lines)) == sorted(find_group(j, range(0, g.num_dots), g.lines)):
                        pass
                    else:
                        pass