import os
os.chdir('C:/Users/user/Desktop')
with open('Git_Command.txt') as git:
    count=0
    for i in git.read():
        if i.isupper():
            count=count+1
    print(count)