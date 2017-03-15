# def isSigmaAlgebra(space, sets):
#     check = []
#     for i in sets:
#         listcheck = list(set(i))
#         for j in range(len(set(i))):
#             if listcheck[j] not in check:
#                 check.append(listcheck[j])
#     if set(check) == set(space):
#         return True
#     else: return False

# def isSigmaAlgebra(space, sets):
#     check = set()
#     for i in sets:
#         for j in i:
#             check.add(j)
#     if set(check) == set(space):
#         return True
#     else: return False

# def isSigmaAlgebra(space, sets):
#     check = [element for subset in sets for element in subset]
#     if set(check) == set(space):
#         return True
#     else:
#         return False


def isSigmaAlgebra(space, sets):
    check = [element for subset in sets for element in subset]
    return set(check) == set(space)


testspace1 = ['A', 'B', 'C', 'D', 'E']
testsets1 = [['A', 'B'], ['C', 'D', 'E']]

testspace2 = [1, 2, 3, 4, 5, 6]
testsets2 = [[1, 2], [4], [5, 6], [4, 3, 5]]

testspace3 = ['chess', 'checkers', 'backgammon']
testsets3 = [['chess'], ['poker', 'backgammon'], ['chess', 'checkers', 'backgammon']]

testspace4 = ['Clark', 'Bruce', 'Diana']
testsets4 = [['Clark', 'Bruce', 'Diana'], []]

testspace5 = ['Superman', 'Green Lantern', 'Flash', 1, 5, 9]
testsets5 = [['Superman', 1], ['Green Lantern'], [5, 9, 'Flash']]

testspace6 = ['Universal', 'Disney']
testsets6 = [[]]

testspace7 = ['Green', 'Blue', 'Red', 'Yellow']
testsets7 = [['Green', 'Blue', 'Red', 'Yellow']]

# print(isSigmaAlgebra(testspace1,testsets1))
# print(isSigmaAlgebra(testspace2,testsets2))

# Another function
# def SigmaAlgebraCheck(space, sets):
#     for i in sets:
#         if set(i).issubset(space):
#             continue
#         else:
#             return False
#     return True
#
# def isSigmaAlgebra(space, sets):
#     """
#     This function checks if a given set of sets is a sigma algebra of a given sample space.
#
#     :param space: list
#         An iterable containing the universe of objects (sample space)
#     :param sets: list of lists
#         A set of sets to check against the sample space
#     :return: boolean
#         True if 'sets' is a sigma algebra of 'space'
#     """
#     if sets == [[]]: return False
#     return all(set(i).issubset(space) for i in sets)

print(isSigmaAlgebra(testspace1, testsets1))  # True
print(isSigmaAlgebra(testspace2, testsets2))  # True
print(isSigmaAlgebra(testspace3, testsets3))  # False
print(isSigmaAlgebra(testspace4, testsets4))  # True
print(isSigmaAlgebra(testspace5, testsets5))  # True
print(isSigmaAlgebra(testspace6, testsets6))  # False
print(isSigmaAlgebra(testspace7, testsets7))  # True
