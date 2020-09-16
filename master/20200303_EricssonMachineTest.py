# 爱立信面试题：
# 给两个字符串，对这两个字符串进行比较
# 输入：s:nice t:nicer  输出(ADD:r)
# 输入：s:meet t:met    输出(JOIN:e)
# 输入：s:rate t:tare   输出(SWAP:t,r)
# 输入：s:o    t:ood    输出(IMPOSSIBLE)
# 如果两个字符串相同，则输出NOTHING


def solution_add(s, t):
    if (len(s) - len(t)) != 1:
        return None
    for i in range(len(t)):
        if s[i] != t[i]:
            return None
    return "ADD:{}".format(s[len(t)])


def solution_join(s, t):
    if (len(s) - len(t)) != 1:
        return None
    join_index = None
    for i in range(len(t)):
        if join_index is None:  # 此处如果将is换为==会报PEP8警告
            if s[i] != t[i]:
                join_index = i
        else:
            if s[i+1] != t[i]:
                return None
    return "JOIN:{}".format(s[i])


def solution_swap(s, t):
    if len(s) != len(t):
        return None
    swap_index_1 = None
    swap_index_2 = None
    swap_char_1 = None
    swap_char_2 = None
    for i in range(len(t)):
        if swap_index_1 is None:
            if s[i] != t[i]:
                swap_index_1 = i
                swap_char_1 = s[i]
                swap_char_2 = t[i]
        elif swap_index_2 is None:
            if s[i] != t[i]:
                swap_index_2 = i
                if (swap_char_1 != t[i]) or (swap_char_2 != s[i]):
                    return None
        else:
            if s[i] != t[i]:
                return None
    return "SWAP:{},{}".format(swap_char_1, swap_char_2)


def solution(s, t):
    if len(t) > len(s):
        tmp = s
        s = t
        t = tmp
    return\
        solution_add(s, t) or\
        solution_join(s, t) or\
        solution_swap(s, t) or\
        "IMPOSSIBLE"


def main():
    while True:
        s = input("请输入第一个字符串:")
        t = input("请输入第二个字符串:")
        if len(s) == 0 and len(t) == 0:
            exit_str = input("退出请输入y:")
            if exit_str == "y":
                exit(0)
        result = solution(s, t)
        print("结果为:{}".format(result))


if __name__ == "__main__":
    main()
