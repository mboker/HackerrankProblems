import sys

#try splitting string in half, then thirds, then 4ths, etc.


file = open('sep_nums.txt')
q = int(file.readline().strip())
for a0 in range(q):
    s = file.readline().strip()
    orig = s
    curr_first_len = 1
    passing = False
    while curr_first_len <= len(orig)//2 and not passing:
        s = orig
        int1_string = s[:curr_first_len]
        s = s[curr_first_len:]
        first = None
        while len(int1_string) <= len(s) :
            int1 = int(int1_string)
            int2 = int1+1
            int2_string = str(int2)
            if int2_string in s and s.index(int2_string) == 0:
                passing = True
                if first is None:
                    first = int1
                int1_string = int2_string
                s = s[len(int2_string):]
            else:
                passing = False
                while not passing and len(int1_string) <= len(s):
                    int1_string += s[0]
                    s = s[1:]
                    int1 = int(int1_string)
                    int2 = int1+1
                    int2_string = str(int2)
                    if int2_string in s and s.index(int2_string) == 0:
                        if first is None:
                            first = int1
                        int1_string = int2_string
                        s = s[len(int2_string):]
                        passing = True
                if not passing:
                    break
        if len(s) > 0:
            passing = False
        curr_first_len += 1
    print('YES '+str(first) if passing else 'NO')


