file = open('Cipher.txt')
n, k = map(int, file.readline().strip().split())
s = file.readline().strip()
digits = []
idx = 0
k-=1
last_k = [0] * k
running = 0
while idx < n:
    s_digit = int(s[idx])
    s_digit ^= running
    digits.append(s_digit)
    last_k.append(s_digit)
    running ^= last_k[idx] ^ s_digit
    idx += 1

print(''.join(list(map(str,digits))))