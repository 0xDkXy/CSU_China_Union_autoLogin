import sys

file=open('./log.txt','w')
file.close()
while True:
    str=input()
    print(str)
    file=open('./log.txt','a')
    file.write(str+'\n')
    file.close()
    sys.stdin.flush()
