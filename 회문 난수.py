for c in 'Shinhan':
    print(c,end="")
    
########################################
a='  i love python programming   '
a.lower()
##########################################
a= "10 20 30 40 50 60 70 70 80 90 "
a.split()

a= "10,20,30,40,50,60,70,80,90"
a.split(",")
print(a)
####################################################
text = input('문자열 입력 : ')
print('뤙본 문자열 : ',text)
print(text.upper())
print(text.lower())
print(text.swapcase())
###################################################
result = str ()
for c in text:
    if c.islower():
        result = result + c.upper()
    else:
        result = result + c.lower()
print(result)
#################################################

text= input('문자열을 입력하세요 > ')

origin = text.replace(' ','')
print('origin :', origin)
reverse = str()

last_index = len(origin)-1

for index in range(last_index,-1,-1):
    reverse = reverse + origin[index]

if origin == reverse:
    print('회문')
else:
    print('회문이 아님')
#############################################

##################################################

import random
all = ['가위','바위','보']
while True:
    theend = input ('계속 할래? (Y/S)')
    if theend.upper()=='N':
        break;
    n= random.randrange(0,3)
    print(all(n))
print('게임 종료!')
