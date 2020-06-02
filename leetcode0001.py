import random

# 两数之和

# 1.简单题

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        result = []

        for i,num in enumerate(nums):

            if hashmap.get(target - num) is not None:
                # hashmap[num] = i
                result.append([hashmap.get(num),num])
                result.append([hashmap.get(target - num),target - num])
                return result

            hashmap[num] = i
            #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况,,,感觉并没有解决
            #但是前面那个数字将不会有数值





test = Solution()
nums = list(range(1,1000))

nums2 = [2,2,5,5,6,6]

# random.shuffle 在原来的列表上修改，随机打乱数组顺序
random.shuffle(nums)
print(nums)
target = 520

target2 = 10

print(test.twoSum(nums2,target2))


