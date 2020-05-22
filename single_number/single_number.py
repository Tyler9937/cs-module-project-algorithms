'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    storage_list = []
    dup_list = []
    return_list = []

    for value in arr:
        if value not in storage_list:
            storage_list.append(value)
        else:
            dup_list.append(value)
    for value in storage_list:
        if value not in dup_list:
            return_list.append(value)

    if len(return_list) == 1:
        return return_list[0]
        
    return return_list




def single_number2(nums):
    no_dups = []

    for x in nums:
        if x not in no_dups:
            no_dups.append(x)
        else:
            no_dups.remove(x)
    return no_dups[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")