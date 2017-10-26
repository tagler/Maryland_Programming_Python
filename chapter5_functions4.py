
def test_function(l1,l2):
    result = []
    for i in l1:
        for j in l2:
            if i == j:
                result.append(i)
    return result

l1 = [1,2,3]
l2 = [2,3,4]
test_function(l1,l2)
