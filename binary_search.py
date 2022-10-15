def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint_value
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 12

# print(binary_search(sequence_a, item_a))


# Binary Search Optimized 
# return index, or index of where it would be.
def searchInsert(nums, target): 
    i=0
    j=len(nums)-1;
    while i < j:
        mid = (i+j) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid -1;
        else:
            i = mid +1
    if nums[i] >= target:
        return i
    else: 
        return i+1
print(searchInsert([1,3,5,6], 5))
        