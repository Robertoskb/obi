from collections import defaultdict


def maior_sub_string_palindroma(string):
    n = len(string)
    dp = defaultdict(bool)
    max_len = 1
    start = 0
    end = 0

    for i in range(n):
        dp[i, i] = True

    for i in range(n-1):
        if string[i] == string[i+1]:
            dp[i, i+1] = True

    for i in range(n-3, -1, -1):
        for j in range(i+2, n):
            if string[i] == string[j] and dp[i+1, j-1]:
                dp[i, j] = True
                if j-i+1 > max_len:
                    max_len = j-i+1
                    start = i
                    end = j

    return string[start:end+1]


if __name__ == '__main__':
    string = input()
    print(maior_sub_string_palindroma(string))
