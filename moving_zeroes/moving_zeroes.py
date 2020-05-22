'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zero_count = 0
    while 0 in arr:
        zero_count += 1
        arr.remove(0)
    for zero in range(zero_count):
        arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")