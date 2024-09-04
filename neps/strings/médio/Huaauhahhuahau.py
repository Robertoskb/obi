# https://neps.academy/br/exercise/118

vogais = ['a', 'e', 'i', 'o', 'u']

string = input()

vstr = ''
for i in range(len(string)):
    if string[i] in vogais:
        vstr += string[i]

print("S" if vstr == vstr[::-1] else "N")
