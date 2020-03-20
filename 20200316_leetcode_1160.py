# 1160. 拼写单词 Find Words That Can Be Formed by Characters
import collections


class Solution:
    @staticmethod
    def countCharacters(words: list, chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        print(ans)
        return ans


test = Solution()
test.countCharacters(["cat", "bt", "hat", "tree"], "atach")

# 直接统计字母表 chars 中每个字母出现的次数，然后检查词汇表 words 中的每个单词，如果该单词中
# 每个字母出现的次数都小于等于词汇表中对应字母出现的次数，就将该单词长度加入答案中。

