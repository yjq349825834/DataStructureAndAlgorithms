

def bubble_sort (nums:list) ->int:
    count = 0
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                count += 3
    return count


if __name__ == "__main__":
    nums = [1,3,4,5,7,3,6]
    print(bubble_sort(nums))
    print(nums)
    print(range(5)) 