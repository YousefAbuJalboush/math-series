from math_series.series import fibonacci , list_fibonacci , lucas , list_lucas , sum_series , list_sum_series

"""
Fibonacci test cases:
    [ 0 ]  -> 0
    [ 1 ]  -> 1
    [ 7 ]  -> 13
"""
# def test_fibonacci_one():
#     expected = 0
#     actual = fibonacci(0)
#     assert  expected == actual

# def test_fibonacci_tow():
#     expected = 1
#     actual = fibonacci(1)
#     assert  expected == actual

# def test_fibonacci_seven():
#     expected = 13
#     actual = fibonacci(7)
#     assert  expected == actual

def test_list_fibonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    actual = list_fibonacci([0 , 1, 2, 3, 4, 5, 6, 7])
    assert  expected == actual

##########################################################

"""
lucas test cases:
    [ 0 ]  -> 0
    [ 1 ]  -> 1
    [ 7 ]  -> 29
"""
# def test_lucas_one():
#     expected = 2
#     actual = lucas(0)
#     assert  expected == actual

# def test_lucas_tow():
#     expected = 1
#     actual = lucas(1)
#     assert  expected == actual

# def test_lucas_three():
#     expected = 4
#     actual = lucas(3)
#     assert  expected == actual

# def test_lucas_seven():
#     expected = 29
#     actual = lucas(7)
#     assert  expected == actual

def test_list_lucas():
    expected = [2, 1, 3, 4, 7, 11, 18, 29]
    actual = list_lucas([0 , 1, 2, 3, 4, 5, 6, 7])
    assert  expected == actual

##########################################################

"""
sum_series test cases:
    [ 7 , 0 , 1 ]  -> 13
    [ 7 , 2 , 1 ]  -> 29
    [ 7 , 3 , 2 ]  -> 50
"""

def test_sum_series_fibonacci_seven():
    expected = 13
    actual = sum_series(7 ,0 ,1)
    assert  expected == actual

def test_sum_series_lucas_seven():
    expected = 29
    actual = sum_series(7 ,2 ,1)
    assert  expected == actual

def test_sum_series_seven_tow_one():
    expected = 50
    actual = sum_series(7 ,3 ,2)
    assert  expected == actual

def test_list_sum_series_fibonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 0 , 1)
    assert  expected == actual

def test_list_sum_series_lucas():
    expected = [2, 1, 3, 4, 7, 11, 18, 29]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 2 , 1)
    assert  expected == actual

def test_list_sum_series_n_three_two():
    expected = [3, 2, 5, 7, 12, 19, 31, 50]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 3 , 2)
    assert  expected == actual

def test_list_sum_series_n_five_five():
    expected = [5, 5, 10, 15, 25, 40, 65, 105]
    actual = list_sum_series([0 , 1, 2, 3, 4, 5, 6, 7] , 5 , 5)
    assert  expected == actual