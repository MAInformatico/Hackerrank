def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if int(s[i]) ^ int(t[i]):
            res += '1';
        else:
            res += '0';

    return res

s = input()
t = input()
print(strings_xor(s, t))
