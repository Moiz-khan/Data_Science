from nearst_square import nearst_square

nearst_5 = nearst_square(5)
print("Result of 5 is {}, Correct Answer is 4".format(nearst_5))
assert(nearst_5 == 4)

nearst_n12 = nearst_square(-12)
print("Result of -12 is {}, Correct Answer is 0".format(nearst_n12))
assert(nearst_n12 == 0)

nearst_23 = nearst_square(23)
print("Result of 23 is{}, Correct Answer is 16".format(nearst_23))
assert(nearst_23 == 16)

nearst_9 = nearst_square(9)
print("Result of 9 is {}, Correct Answer is 0".format(nearst_9))
assert(nearst_9 == 9)

'''
Error
nearst_9 = nearst_square(9)
print("Result of 9 is {}, Correct Answer is 0".format(nearst_9))
assert(nearst_9 == 0)
'''


