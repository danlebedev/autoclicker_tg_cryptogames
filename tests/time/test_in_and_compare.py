from tests.tools import check_time


c_min = (0, 0, 0)
c_max = (255, 255, 255)
test = (100, 100, 100)
def test_in(c_min, c_max, test):
    if test[0] in range(c_min[0], c_max[0]) and \
    test[1] in range(c_min[1], c_max[1]) and \
    test[2] in range(c_min[2], c_max[2]):
        return True
    

def test_compare(c_min, c_max, test):
    if (test[0] >= c_min[0] and test[0] <= c_max[0]) and \
    (test[1] >= c_min[1] and test[1] <= c_max[1]) and \
    (test[2] >= c_min[2] and test[2] <= c_max[2]):
        return True


check_time(test_in, c_min, c_max, test, iterations=1000000)
check_time(test_compare, c_min, c_max, test, iterations=1000000)