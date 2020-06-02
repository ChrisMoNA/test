# 1431. 拥有最多糖果的孩子

# 简单题

# 给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

# 对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

#只需要判断是否能成为最大拥有者 


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def kidsWithCandiesbyMyself(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # 自己做的，用时32ms

        hashmap = {}
        pxlist = []

        result = []

        #找出最大拥有的孩子，将糖果数按顺序排好
        for i,num in enumerate(candies):
            hashmap[i] = num
            pxlist.append(num)
            
        newlist = sorted(pxlist,reverse=True)
        maxnum = newlist[0]

        for k,v in hashmap.items():
            kid = k + 1
            if v + extraCandies >= maxnum:
                result.append(True)
                print("孩子 %d 可能成为最大拥有者" % kid)
            else:
                print("孩子 %d 不可能成为最大拥有者" % kid)
                result.append(False)

        return result

    def kidsWithCandies01(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # 只需要简单返回true false 完全可以这样，参考别人用时28ms

        return [num + extraCandies >= max(candies) for num in candies]

    def kidsWithCandies02(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # 虽然比上面的多写了几行，但是执行更高效用时20ms
        # 将max提出来，不用每次遍历都要执行，更高效
        maxnum = max(candies)

        result = []

        for i in candies:
            result.append(extraCandies + i >= maxnum)

        return result

    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # 用时12ms
        # 这种第一次见
        maxnum = max(candies)
        return [True if extraCandies + num >= maxnum else False for num in candies]



candies = [2,3,5,1,3]

extraCandies = 3

test = Solution()

print(test.kidsWithCandies(candies,extraCandies))
            