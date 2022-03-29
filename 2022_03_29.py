#복습

a=10
b=4
a+=1     #a=a+1
a*=2     #a=a*2
print ('a=',a)
print(type(a))

#수업
#예제 1

kor=91
eng=80
mat=89
tot=kor+eng+mat
avg=round(tot/3,1)
print("총점:",tot)
print("평균:",avg)

#예제 2

ralo=float(input("가로의 길이는?"))
selo=float(input("세로의 길이는?"))
area=ralo*selo
print("가로의 길이:",ralo)
print("세로의 길이:",selo)
print("면적의 넓이:",area)
print("{}X{}={}".format(ralo,selo,area))

#예제3

height=int(input('당신의 신장(cm)은?'))       #신장
weight=int(input('당신의 체중(kg)은?'))       #체중
stdweight=(height-100)*0.9
bmi=((weight-stdweight)/stdweight)*100
print('신장 : {}cm'.format(height))
print('체중 : {}kg'.format(weight))
print('비만도(BMI) : {}%'.format(round(bmi,2)))

#참과 거짓

a=20
b=100
print(a!=b)

100>200 or 400>300

100>200 and 400>300

not 100>200

#제어문 

#예제1

num=int(input('정수를 입력하세요 : '))
if num<0:
    print('{}은 음수'.format(num))
else:
    print('{}은 0또는 양수'.format(num))


#예제2

num1=int(input('양수를 입력하세요 : '))
if num1 %2 == 0:
    print('{}은 짝수'.format(num1))
else:
    print('{}은 홀수'.format(num1))
    
# 조건 분기문 활용하기
#if-else 문 활용

flag = input('마음에 드는 옷을 찾았니? (Y/N)')
if (flag=="Y")or (flag=="y")or(flag=="Yes")or(flag=="yes"):
    print('그럼 그거 사자!')
elif (flag=="N")or (flag=="n")or(flag=="No")or(flag=="no"):
    print('다른 옷들도 봐보자!')
else:
    print('Yes또는 No로 답해주세요!')

#예제3

score=float(input('점수를 입력하세요 :'))
if   score>=90:
    grade="A"
elif score>= 80:
    grade="B"
elif score>= 70:
    grade="C"
elif score>= 60:
    grade="D"
else:
    grade="F"
print("{}점:{}등급 입니다".format(score,grade))

#예제4

code = int(input('직급코드(1:과장/2:차장3:부장) :'))
income = int(input('총 소득(원) 입력 : '))

if code==1:
    tax= income*0.08
    position="과장"
elif code==2:
    tax= income*0.12
    position="차장"
elif code==3:
    tax= income*0.18
    position="부장"
pay= income-tax
print('직급 : {}'.format(position))
print('총 소득 : {}원'.format(income))
print('세금 : {}원'.format(tax))
print('실수령액 : {}원'.format(pay))

#내포된 if문

gender=input('당신의 성별은? (남/여): ')
if (gender =="남")or(gender =="남자")or(gender.upper()=="m")or(gender.upper()=="male"):
    military= input('병역을 필했는가?(Y/N)')
    if (military.upper=="Y") or (military.upper=='yes') or (military=='예'):
        gubun="예비역"
    else:
        gubun="병역준비역"
else:
    gubun="비대상자(여성)"
print('구분 : ',gubun)

#정리하기 문제1

height=float(input('키와 몸무게 제한이 있는 놀이기구 입니다 키(cm)가 어떻게 되나요?'))
weight=float(input('몸무게 도 적어주세요.'))
if (height>=100) or (weight>=35):
    print('탑승이 가능합니다!!')
else:
    print('다른 놀이기구를 이용해주세요!')    

#정리하기 문제2

sub1= int(input('과목1 점수 : '))
sub2= int(input('과목2 점수 : '))
sub3= int(input('과목3 점수 : '))
avr=(sub1+sub2+sub3)/3
print('평균 :',round(avr,1))
if ((sub1>=40) and(sub2>=40)and(sub3>=40)and(avr>=60)):
    print('축하합니다, 합격입니다!')
else:
    print('아쉽습니다, 다음에 다시 도전하세요!')

#정리하기 문제3

num=int(input('정수를 입력 : '))
if num >=10 :
    if num&2==0:
        print('{}:10 이상의 짝수'.format(num))
    else:
        print('{}:10이상의 홀수'.format(num))
else:
    if num%2==0:
        print('{}:10보다 작은 짝수')
    else:
        print('{}:10보다 작은 홀수')

#정리하기 문제 4

lv= int(input('물개반:1,돌고래반:2,상어반:3 > '))
jm= input('지역 주민 인가요?(Y/N)')
fee= 50000
if lv ==1:
    dc= fee*0.2           #물개반 인하율 20%  / 돌고래반 인하율 15% / 상어반 인하율 10% 
    print("레벨 : 물개반")
elif lv ==2:
    dc= fee*0.15
    print("레벨 : 돌고래반")
elif lv ==3:
    dc= fee*0.1
    print("레벨: 상어반")
    
if (jm.upper()=="Y")or(jm=="네")or(jm=="예"):    #지역주민 할인
    dc=dc+10000

pay= fee - dc

print("수강료: {}원".format(int(pay))) 
