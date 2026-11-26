func removeElement(nums []int, val int) int {
    for i:=0;i<len(nums);i++{
        if i == len(nums){
            break
        }
        if nums[i] == val{
            nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
            nums = nums[:len(nums)-1]
            i--
        }
    }
    return len(nums)
}