import itertools
from gamestate import GameState

def find_parent_dots(d, g):
    group = []
    for i, face_dots in enumerate(g.faces_dotss):
        if d in face_dots:
            group.extend(g.faces[i][0])
    if group == []:
        return None
    return group

# this works, is chatgpt
def find_all_paths(d1, d2, lines, path):
    if d1 == d2:
        return [path]

    paths = []
    for i, line in enumerate(lines):
        new_lines = lines[:i] + lines[i+1:]  # Create a new list excluding the current line
        if line[0] == d1:
            new_path = find_all_paths(line[1], d2, new_lines, path + [line[1]])
            paths.extend(new_path)
        elif line[1] == d1:
            new_path = find_all_paths(line[0], d2, new_lines, path + [line[0]])
            paths.extend(new_path)

    return paths

def is_on_outside(d, g):
    if d not in itertools.chain.from_iterable(g.faces_dotss):
        return True
    else:
        return False

def find_all_paths_outside(d1, d2, g):
    paths = find_all_paths(d1, d2, g.lines, [])
    good_paths = []
    for path in paths:
        is_good = True
        for d in path:
            if not is_on_outside(d, g):
                is_good = False
        if is_good:
            good_paths.append([d1] + path)
    return good_paths


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

def is_path(d1, d2, lines, path):
    if d1 == d2:
        return True

    for i, line in enumerate(lines):
        new_lines = lines[:i] + lines[i+1:]  # Create a new list excluding the current line
        if line[0] == d1:
            path.append(line[1])
            if is_path(line[1], d2, new_lines, path):
                return True
            path.pop()  # Backtrack if not successful
        elif line[1] == d1:
            path.append(line[0])
            if is_path(line[0], d2, new_lines, path):
                return True
            path.pop()  # Backtrack if not successful

    return False

# i split the function into two fight me
def find_parent_group(d, g):
    dots_in_group = [d]
    for d2 in range(0, g.num_dots):
        if is_path(d, d2, g.lines, []):
            dots_in_group.append(d2)
    if find_parent_dots(d, g) != None:
        dots_in_group.extend(find_parent_group(find_parent_dots(d, g)[0], g))
    return set(dots_in_group)

def find_child_group(d, g):
    dots_in_group = []
    for d2 in range(0, g.num_dots):
        if is_path(d, d2, g.lines, []):
            dots_in_group.append(d2)
    for d2 in dots_in_group:
        if find_child_dots(d2, g) != None:
            for i, child_dot in enumerate(find_child_dots(d2, g)):
                if not is_path(d2, find_child_dots(d2,g)[i], g.lines, []):
                    dots_in_group.extend(find_child_group(find_child_dots(d2, g)[i], g))
    return set(dots_in_group)

def find_sibling_groups(d, g):
    groups = []
    # this top loop might be unnessesary
    if find_parent_dots(d, g) != None:
        for parent_dot in find_parent_dots(d, g):
            for sibling_dot in find_child_dots(parent_dot, g):
                if not is_path(d, sibling_dot, g.lines, []):
                    sibling_group = []
                    for i in range(0, g.num_dots):
                        if is_path(sibling_dot, i, g.lines, []):
                            sibling_group.append(i)
                    groups.extend(set(sibling_group))
    if groups == []:
        return None
    else:
        return groups

def find_group(d, g):
    group = []
    if find_child_group(d, g) != None:
        group.extend(list(find_child_group(d, g)))
    if find_parent_group(d, g) != None:
        group.extend(list(find_parent_group(d, g)))
    if find_sibling_groups(d, g) != None:
        group.extend(list(find_sibling_groups(d, g)))
    
    return list(set(group))

def find_isolated_groups(g):
    groups = []
    groups.append(find_group(0, g))

    for d in range(0, g.num_dots):
        if d not in itertools.chain.from_iterable(groups):
            groups.append(find_group(d, g))
    return groups

def gen_child_states(g):
    both_inside = []
    both_outside = []
    one_and_one = []
    for i in range (0,g.num_dots):
        for j in range (0,g.num_dots):
            if i != j:
                if i in itertools.chain.from_iterable(g.faces_dotss) and j in itertools.chain.from_iterable(g.faces_dotss):
                    both_inside.append(tuple(sorted((i, j))))

                elif i in itertools.chain.from_iterable(g.faces_dotss) and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    one_and_one.append(tuple(sorted((i, j))))

                elif (i in itertools.chain.from_iterable(g.faces_dotss)) == False and (j in itertools.chain.from_iterable(g.faces_dotss)) == False:
                    both_outside.append(tuple(sorted((i, j))))
            if i == j:
                pass
    both_inside = list(set(both_inside))
    both_outside = list(set(both_outside))
    one_and_one = list(set(one_and_one))

    for inside_pair in both_inside:
        pass
    
    for one_and_one_pair in one_and_one:
        pass
    
    for outside_pair in both_outside:
        new_gs_with_line = []
        groups = find_isolated_groups(g)

        for group in groups:
            if outside_pair[0] in group and outside_pair[1] in group:
                # these are the two gs where the new route doesnt contain any other isolated groups
                one_way =   GameState(g.num_dots + 1, new_lines, g.lines.copy().append(new_face_line_one), g.faces_dotss.copy().append([]))
                other_way = GameState(g.num_dots + 1, new_lines, g.lines.copy().append(new_face_line_two), g.faces_dotss.copy().append([]))