import itertools

def find_parent_dots(d, g):
    group = []
    for i, face_dots in enumerate(g.faces_dotss):
        if d in face_dots:
            group.extend(g.faces[i][0])
    if group == []:
        return None
    return group

def find_child_dots(d, g):
    child_dots = []
    for i, face in enumerate(g.faces):
        if d in itertools.chain.from_iterable(face) and g.faces_dotss[i] != []:# and d not in g.faces_dotss[i]:
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

# i split the function into two fight me
def find_parent_group(d, g):
    dots_in_group = [d]
    for d2 in range(0, g.num_dots):
        if find_paths(d, d2, g.lines, []):
            dots_in_group.append(d2)
    if find_parent_dots(d, g) != None:
        print("her")
        dots_in_group.extend(find_parent_group(find_parent_dots(d, g)[0], g))
    return set(dots_in_group)

def find_child_group(d, g):
    dots_in_group = []
    for d2 in range(0, g.num_dots):
        if find_paths(d, d2, g.lines, []):
            dots_in_group.append(d2)
    for d2 in dots_in_group:
        if find_child_dots(d2, g) != None:
            print(d2, find_child_dots(d2, g))
            for i, child_dot in enumerate(find_child_dots(d2, g)):
                if not find_paths(d2, find_child_dots(d2,g)[i], g.lines, []):
                    dots_in_group.extend(find_child_group(find_child_dots(d2, g)[i], g))
    return set(dots_in_group)

def find_group(d, g):
    return(list(set(list(find_child_group(d, g)) + (list(find_parent_group(d, g))))))

def find_isolated_groups(g):
    groups = []
    groups.append(find_group(0, g))

    for d in range(0, g.num_dots):
        if d not in itertools.chain.from_iterable(groups):
            groups.append(find_group(d, g))

    #for d1 in range(0, g.num_dots):
    #    for d2 in range(0, g.num_dots):
    #        if d1 != d2:
    #            if d2 not in find_group(d1, g) or d1 not in find_group(d2, g):
    #                print(d1 in find_group(d2, g), d2 in find_group(d1, g))
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
            if i == j:
                pass