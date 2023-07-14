def binary_search (a_list, a_value):

    first = 0
    last = len(a_list)-1

    while first <= last:
        midpoint = (first+last) // 2
        if a_list[midpoint] == a_value:
            return True
        else:
            if a_value < a_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint + 1
    return False

if __name__ == '__main__':

    a_list = [2,4,6,7,8,9,12,7,6,8,93]

    print('Binary search:', binary_search(a_list, 97))