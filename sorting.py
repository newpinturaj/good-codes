def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums  = [4, 5, 72, 8, 2, 7,3]
bubble_sort(nums)
print(nums)
