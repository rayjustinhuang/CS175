# CS 175: Topics in Computational Science - Probability and Stochastics

# Assignment: Program to check if a set of sets is a sigma-algebra (of some given universal set)


def is_sigma_algebra(space, sets):
    """
    This function checks if a given set of sets is a sigma-algebra of a given sample space ("universal set").

    :param space: list
        An iterable containing the universe of objects (sample space)
    :param sets: list of lists
        A set of sets to check against the sample space
    :return: boolean
        True if 'sets' is a sigma-algebra of 'space'
    """
    check = []
    test = sets
    if [] not in sets:
        return False
    if not set([element for subset in sets for element in subset]) == set(space):
        return False
    for i in test:
        i.sort()
    for i in test:
        temp = list(set(space).difference(set(i)))
        temp.sort()
        check.append(temp in sets)
        if temp in test:
            test.remove(temp)
    return all(check)


test_space1 = ['A', 'B', 'C', 'D', 'E']
test_sets1 = [['A', 'B'], ['C', 'D', 'E'],[],['A','B','C','D','E']]

test_space2 = [1, 2, 3, 4, 5, 6]
test_sets2 = [[1, 2], [4], [5, 6], [4, 3, 5],[],[3,4,5,6],[6,2,3,5,1],[1,2,3,4],[1,2,6],[1,2,3,4,5,6]]

test_space3 = ['chess', 'checkers', 'backgammon']
test_sets3 = [['chess'], ['poker', 'backgammon'], ['chess', 'checkers', 'backgammon'],[],['checkers','backgammon'],['chess','checkers']]

test_space4 = ['Clark', 'Bruce', 'Diana']
test_sets4 = [['Clark', 'Bruce', 'Diana'], []]

test_space5 = ['Superman', 'Green Lantern', 'Flash', 1, 5, 9]
test_sets5 = [['Superman', 1], ['Green Lantern'], [5, 9, 'Flash']]

test_space6 = ['Universal', 'Disney']
test_sets6 = [[]]

test_space7 = ['Green', 'Blue', 'Red', 'Yellow']
test_sets7 = [['Green', 'Blue', 'Red', 'Yellow'],[]]

test_space8 = ['a','b','c','d']
test_sets8 = [[],['a','b'],['c','d'],['a','b','c','d']]

print(is_sigma_algebra(test_space1, test_sets1), "test 1")  # True
print(is_sigma_algebra(test_space2, test_sets2), "test 2")  # True
print(is_sigma_algebra(test_space3, test_sets3), "test 3")  # False
print(is_sigma_algebra(test_space4, test_sets4), "test 4")  # True
print(is_sigma_algebra(test_space5, test_sets5), "test 5")  # False
print(is_sigma_algebra(test_space6, test_sets6), "test 6")  # False
print(is_sigma_algebra(test_space7, test_sets7), "test 7")  # True
print(is_sigma_algebra(test_space8, test_sets8), "test 8")  # True
