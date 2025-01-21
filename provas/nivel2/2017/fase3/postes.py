# https://neps.academy/br/exercise/41

N = int(input())
postes = tuple(map(int, input().split()))

sub = ref = 0

for i in range(N):
    if postes[i] < 50:
        sub += 1
    elif postes[i] < 85:
        ref += 1

print(sub, ref)
