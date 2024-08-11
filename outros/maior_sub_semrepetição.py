from collections import defaultdict


def maior_substring_sem_repetição(string):
    n = len(string)
    dp = defaultdict(int)
    max_len = 0
    start = 0
    end = 0
    left = 0

    for right in range(n):
        if string[right] in dp:
            left = max(left, dp[string[right]]+1)

        dp[string[right]] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
            end = right

    return string[start:end+1]


if __name__ == '__main__':
    string = input()
    print(maior_substring_sem_repetição(string))
