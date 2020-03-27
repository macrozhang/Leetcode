# 820. 单词的压缩编码


class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        N = len(words)
        # 反转每个单词
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        # 字典序排序
        reversed_words.sort()

        res = 0
        for i in range(N):
            if i + 1 < N and reversed_words[i + 1].startswith(reversed_words[i]):
                # 当前单词是下一个单词的前缀，丢弃
                pass
            else:
                res += len(reversed_words[i]) + 1  # 单词加上一个 '#' 的长度
        print(res)
        return res


test = Solution()
test.minimumLengthEncoding(["time", "me", "bell"])
