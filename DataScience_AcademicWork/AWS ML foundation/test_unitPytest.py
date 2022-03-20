#run on current working directory pytest

from nearst_square import nearst_square

def test_nearst_square_5():
    assert(nearst_square(5) == 4)

def test_nearst_square_n12():
    assert(nearst_square(-12) == 0)

def test_nearst_square_23():
    assert(nearst_square(23) == 16)

def test_nearst_square_9():
    assert(nearst_square(9) == 9)

'''
Error
def test_nearst_square_25():
    assert(nearst_square(25) == 23)
'''