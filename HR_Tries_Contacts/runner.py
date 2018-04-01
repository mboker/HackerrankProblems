from word_tries import WordTries
import time

f = open('test_file_1.txt', 'r')
lines = int(f.readline().strip())
tries = WordTries()
start = time.time()
for line in range(lines):
    operation, name = f.readline().strip().split(' ')
    if operation == 'add':
        tries.add(name)
    elif operation == 'find':
        print(tries.find(name))

end = time.time()
print(end-start)