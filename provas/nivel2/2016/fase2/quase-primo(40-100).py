N, K = (int(n) for n in input().split())
nums = [int(n) for n in input().split()]

count = 0
for i in range(1, N+1):
    for p in nums:
        if i % p == 0:
            break
    else:
        count += 1
        
print(count)
