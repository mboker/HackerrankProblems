file = open('StoneGame.txt','r')
num_piles = int(file.readline().strip())
piles = [int(i.strip()) for i in file.readline().strip().split(' ')]


#take answer mod 1000000007