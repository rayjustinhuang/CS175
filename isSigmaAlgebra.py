# CS 175: Topics in Computational Science - Probability and Stochastics

# Assignment: Program to check if a set of sets is a sigma-algebra (of some given universal set)


# def is_sigma_algebra(space, sets):
#     """
#     This function checks if a given set of sets is a sigma-algebra of a given sample space ("universal set").
#
#     :param space: list
#         An iterable containing the universe of objects (sample space)
#     :param sets: list of lists
#         A set of sets to check against the sample space
#     :return: boolean
#         True if 'sets' is a sigma-algebra of 'space'
#     """
#     return (set([element for subset in sets for element in subset]) == set(space)) & ([] in sets)

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
    if [] not in sets: return False
    for i in sets:
        i.sort()
        print(i)
        print(i in sets)
        print(set(space).difference(set(i)))
        print(list(set(space).difference(set(i))))
        test = list(set(space).difference(set(i)))
        test.sort()
        print(test in sets, "----")
        # check.append(i.sort in sets)
        # print(i.sort)
        # check.append(list(set(space).difference(set(i))).sort() in sets)
        # print(list(set(space).difference(i)).sort())
    # print(check)
    # print([set(i) for i in sets])
    # print([set(space).difference(set(i)) for i in set(space)])
    # print([((set(i) in set(space)) and (set(space).difference(set(i)) in set(space))) for i in sets])
    # return all([((set(i) in set(space)) and (set(space).difference(set(i)))) for i in sets])


test_space1 = ['A', 'B', 'C', 'D', 'E']
test_sets1 = [['A', 'B'], ['C', 'D', 'E']]

test_space2 = [1, 2, 3, 4, 5, 6]
test_sets2 = [[1, 2], [4], [5, 6], [4, 3, 5],[]]

test_space3 = ['chess', 'checkers', 'backgammon']
test_sets3 = [['chess'], ['poker', 'backgammon'], ['chess', 'checkers', 'backgammon']]

test_space4 = ['Clark', 'Bruce', 'Diana']
test_sets4 = [['Clark', 'Bruce', 'Diana'], []]

test_space5 = ['Superman', 'Green Lantern', 'Flash', 1, 5, 9]
test_sets5 = [['Superman', 1], ['Green Lantern'], [5, 9, 'Flash']]

test_space6 = ['Universal', 'Disney']
test_sets6 = [[]]

test_space7 = ['Green', 'Blue', 'Red', 'Yellow']
test_sets7 = [['Green', 'Blue', 'Red', 'Yellow'],[]]

test_space8 = ['a','b','c','d']
test_sets8 = []

# print(is_sigma_algebra(test_space1, test_sets1), "test 1")  # True
# print(is_sigma_algebra(test_space2, test_sets2), "test 2")  # True
# print(is_sigma_algebra(test_space3, test_sets3), "test 3")  # False
print(is_sigma_algebra(test_space4, test_sets4), "test 4")  # True
# print(is_sigma_algebra(test_space5, test_sets5), "test 5")  # True
# print(is_sigma_algebra(test_space6, test_sets6), "test 6")  # False
# print(is_sigma_algebra(test_space7, test_sets7), "test 7")  # True
