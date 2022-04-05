#전시간 복습
x = float(input('x좌표값을 입력해 주세요: '))
y = float(input('y좌표값을 입력해 주세요: '))
s = ((x*x)+(y*y))**0.5
if s <= 5.0:
    print(s,'원의 내부에 있습니다.')
else:
    print(s,'원의 외부에 있습니다.')
#while문 사용해 보기
repeat = True
while repeat:
    flag = input('맘에 드는 옷을 골랐니? (예/아니오)')
    if flag == "예":
        print('축하합니다!:)')
        repeat = False
    else:
        print('그렇구나.. 다른메장을 더 돌아보자:)')
# 브레이크 문장 예시 커피자판기
coffee= 5
while True:
    
    money = int(input('돈을 투입해 주세요 >'))
    if money == 300:
        print('커피 한 잔 받으세요.')
        coffee = coffee-1
    if money > 300:
        print('커피 한 잔 받으세요.')
        coffee = coffee-1
        print('잔돈 {}원 받으세요'.format(money-300))
    if money < 300:
        print('커피는 300원 입니다.')
        print('투입한돈 {}원 받으세요'.format(money))

sum = 0
i = 0
while 1<= 10:
    i = i +1
    sum = sum +1
print('sum = {} i = {}'.format(sum,i))

#정수 위치 바꾸기

min = int(input('정수1 입력: '))
max = int(input('정수2 입력: '))
if min > max:
    min,max = max,min
print('min+ {} max= {}'.format(min,max))
sum = 0
while max>=min:
    sum=sum+min
    min=min+1
print('sum= ',sum)

#학생 성적 예제
n = 0 
sum= 0
while n<5:
    n = n+1
    score = int(input(str(n)+'번째 학생 성적 입력'))
    sum=sum+score
avg= sum/n
print('총점 : ',sum)
print('평균 : ',round(avg,1))
#---------------------------------------------------------------
sum= 0
n = 0
while ( sum <= 1000 ):
    n=n+1
    sum=sum+n
print('sum= ',sum)
print('n= ',n)

# while 문 예제 - 최대공약수 구하기 break 와 end 문장도 활용          end='' == 줄바꾸기 하지 않기

num1=int(input('첫번째 정수를 입력해주세요. >'))
num2=int(input('두번째 정수를 입력해주세요. >'))
print('{},{} 의'.format(num1,num2),end = '')
if num1 < num2:
    num1,num2=num2,num1

while True:
    remainder = num1 % num2
    if remainder == 0:
        break
    else:
        num1 = num2
        num2 = remainder
    
print("GCD: {}".format(num2))


#리스트
cards = [10,20,30,40,50]
type(cards)
cards[1]
cards[0]
cards[-1]
cards[-2]
cards[2]=100

fruit = ["apple","banana","kiwi","tomato","pech"]
fruit [2:5]

#리스트 원소 추가하기
#리스트명.append(원소값) 리스트 뒤에 하나의 원소를 추가
#리스트명.insert(삽입 위치,원소값) 리스트 중간에 원하는 위치에 원소 추가 ex)
fruit.insert(2,"melon")
#리스트명.extend(원소값) 한번에 여러개의 리스트를 추가한다 (마지막 리스트 뒤에 추가됨)
#del 리스트명[인덱스] 리스트 특정 인덱스에 있는 원소를 삭제함
#리스트명.pop(인덱스)  리스트 중간의 원소를 제거한다. (인덱스 생략시 마지막 원소 삭제) 




    