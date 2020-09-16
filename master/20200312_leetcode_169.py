# 169. 多数元素
import collections


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        print(max(counts.keys(), key=counts.get))


test = Solution()
test.majorityElement([3, 2, 3])


# 我们知道出现次数最多的元素大于(n/2)次，所以可以用哈希表来快速统计每个元素出现的次数。
# 算法如下：
# 我们使用哈希映射（HashMap）来存储每个元素以及出现的次数。
# 对于哈希映射中的每个键值对，键表示一个元素，值表示该元素出现的次数。
# 我们用一个循环遍历数组 nums 并将数组中的每个元素加入哈希映射中。
# 在这之后，我们遍历哈希映射中的所有键值对，返回值最大的键。
# 我们同样也可以在遍历数组 nums 时候使用打擂台的方法，维护最大的值，这样省去了最后对哈希映射的遍历。
