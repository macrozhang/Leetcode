# 面试题 01.06. 字符串压缩


class Solution:
    @staticmethod
    def compressString(S: str) -> str:
        S += '-'
        cnt, n, encoded = 1, len(S),  ""

        for i in range(1, n):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                encoded += S[i - 1] + str(cnt)
                cnt = 1

        return S[:-1] if len(encoded) >= n - 1 else encoded
