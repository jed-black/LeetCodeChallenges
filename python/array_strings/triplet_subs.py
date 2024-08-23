def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # This needs to be working, but taking a small break from this one
    
    isTriplet = False
    len_num = len(nums)

    for num in range(len_num):
        if num + 1 < len_num and nums[num + 1] and nums[num] < nums[num + 1]:
            if num + 2 < len_num and nums[num + 2] and nums[num + 1] < nums[num + 2]:
                print(nums[num])
                print(nums[num + 1])
                print(nums[num + 2] )
                isTriplet = True
                break

    print(isTriplet)
    return isTriplet
            
increasingTriplet([20,100,10,12,5,13])
#increasingTriplet([0,4,2,1,0,-1,-3])
#increasingTriplet([1,2,3,4,5])
#increasingTriplet([5,4,3,2,1])