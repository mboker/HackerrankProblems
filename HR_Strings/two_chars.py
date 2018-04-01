from collections import Counter

file = open('two_chars.txt', 'r')
n = file.readline()
string = file.readline()
char_counter = Counter(string)
char_counter = char_counter.most_common()
left, right = 0, 1
while left < right < len(char_counter):
