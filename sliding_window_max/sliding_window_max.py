'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    max_numbers = []
    k_index = 0
    while k_index + k != len(nums) + 1:
        window = []
        for i in range(k):
            window.append(nums[k_index + i])
        

        max_numbers.append(max(window))
        k_index += 1

    return max_numbers 




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
