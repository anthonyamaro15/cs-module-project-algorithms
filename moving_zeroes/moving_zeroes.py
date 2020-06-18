'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
   #  create a list to store postitive nums and one for negative numbers
    low = []
    high = []

   # iterate through the list and append numbers to created list
   # depending if there negative or positive
    for i in arr:
        if i <= 0:
            low.append(i)
            low.sort()
        elif i > 0:
            high.append(i)
         # check if lists are empty, if they are empty
         # it means no negative number were found in the list
        elif len(low) and len(high) == 0:
         #   return the original list
            return arr
   #  otherwise return high and low list

    return high + low


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
