# 365. 水壶问题 Water and Jug Problem

"""
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
"""
"""
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""


class Solution:
    @staticmethod
    def canMeasureWater(x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        queue = [(0, 0)]
        seen = set((0, 0))

        while len(queue) > 0:
            a, b = queue.pop(0)
            if a == z or b == z or a + b == z:
                return True
            states = set()

            states.add((x, b))
            states.add((a, y))
            states.add((0, b))
            states.add((a, 0))
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a)))
            states.add((0 if a + b < y else a - (y - b), min(b + a, y)))
            for state in states:
                if state in seen:
                    continue
                queue.append(state)
                seen.add(state)
        return False


test = Solution()
print(test.canMeasureWater(3, 5, 4))
print(test.canMeasureWater(2, 6, 5))
