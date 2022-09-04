
def binary_search(l, num, low=None, high=None):
    if low is None:
        low= 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1


    midpoint= (low + high) // 2

    if l[midpoint] == num:
        return num , " is at index ",  midpoint
    elif num < l[midpoint]:
        return binary_search(l, num, low, midpoint-1)

    else:
        return binary_search(l, num, midpoint+1, high)


if __name__ =='__main__':
    l=[1,3,5,10,12,15,9,6,19,54,29]
    num = 5
    print(binary_search(l, num))

    