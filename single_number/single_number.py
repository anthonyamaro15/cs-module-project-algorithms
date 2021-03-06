'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    single = []

    for x in arr:
        single_index = None
        for i in range(len(single)):
            if single[i] == x:
                single_index = i
                next
        if single_index == None:
            single.append(x)
        else:
            single.pop(single_index)
    return single[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
