from util import Stack, Queue

cache = {}


def earliest_ancestor(ancestors, starting_node):

    # Loop over ancestors
    for i in ancestors:

        # If the first index of i is not in the cache
        if i[0] not in cache:

            # Make cache equal set and add the second index
            cache[i[0]] = set()
            cache[i[0]].add(i[1])

        else:
            cache[i[0]].add(i[1])

    s = Stack()

    visited = set()
    array_list = list()

    s.push([starting_node])

    # While the size of s
    while s.size():
        path = s.pop()
        array_list.append(path)

        v = path[-1]

        # If the last path index isnt in visited
        if v not in visited:

            # Add it to visited
            visited.add(v)

            # Loop over get_ancestors
            for next_vert in get_ancestors(v):
                # Create a new path and append it from next_vert
                new_path = list(path)
                new_path.append(next_vert)

                # Push to new_path
                s.push(new_path)

    biggest_index = (0, 0)

    # Loop over and enumerate array_list
    for index, item in enumerate(array_list):

        # If the length of item is larger then the biggest index
        if len(item) > biggest_index[1]:

            # Set biggest_index to the new index and item
            biggest_index = (index, len(item))

        # If the length of item is equal to biggest_index
        elif len(item) == biggest_index[1]:
            # And if the last item is less then the biggest index of array list
            if item[-1] < array_list[biggest_index[0]][-1]:

                # Set biggest_index to the new index and item
                biggest_index = (index, len(item))

    # If the length of array_list is less then 1
    if len(array_list) > 1:

        # Return the biggest index of array list
        return array_list[biggest_index[0]][-1]
    else:
        return -1


def get_ancestors(v):
    parents = list()

    for key, value in cache.items():
        for second_value in value:
            if v == second_value:
                parents.append(key)

    return parents
