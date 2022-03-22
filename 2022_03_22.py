#숫자 진수법 복습
#num =0o157
#print('10진수 =>',(num))
#print('8진수 =>' , oct(num))
#print('2진수 =>' , bin (num))
#print('16진수>' , hex (num))

#float 함수 이해
#a = "100"
#int(a)

#float("42.195")
#a = float("42.195")
#type(a)
#a
#int(a)

#int 함수와 float 함수의 차이
#a = int(input("정수 입력1 :"))
#a= int(input("정수 입력2 :"))
#sum = a + b
#print('a + b =',sum)

#a = float(input("정수 입력1 :"))
#b = float(input("정수 입력2 :"))
#sum = a + b
#print('a + b =',sum)




# 곱하기 나누기 제곱 응용해보기 / float 함수 활용해보기
height = float(input('신장(cm)을 입력하세요 >>'))
weight = float(input('체중(kg)을 입력하세요 >>'))
BMI    = float(weight/((height/100)**2))
BMIzisu= round(BMI,2)
print("당신의 신장은 "+ str(height) + "입니다")
print("당신의 체중은" + str(weight) + "입니다")
print("당신의 BMI 지수는 "+ str(BMIzisu) +" 입니다")



#시험 점수 총점과 평균 구하기
kor=float(input('국어 점수'))
eng=float(input('영어 점수'))
mat=float(input('수학 점수'))
tot= kor + eng + mat
avg= tot/3
print('총점: ',tot)
print('평균: ',round(avg))



# 교수님 퀴즈 (사각형)
garo=float(input('가로의 길이는?'))
sero=float(input('세로의 길이는?'))
L=(garo+sero)*2
s=(garo*sero)
print("가로의 길이는",garo)
print("세로의 길이는",sero)
print('변의 길이는?',L)
print('면적은?',s)

# 교수님 퀴즈 (삼각형)
under=float(input("삼각형의 밑변의 길이는?"))
tall =float(input("삼각형의 높이는?"))
area=under*tall/2
print('삼각형의 넓이는',area)

#정리하기 문제 1
num1=float(input("첫번째 정수를 입력하세요."))
num2=float(input("두번째 정수를 입력하세요."))
plus=num1+num2
multi=num1*num2
square=num1**num2
print('a','+'+'b','=',plus)
print('a'+'x'+'b','=',multi)
print('a'+'**'+'b','=',square)

#정리하기 문제 2
num = 0b101011
print('10진수: ',num)
print('8진수: ' ,oct(num))
print('16진수: ',hex(num))
print('2진수: ' ,bin(num))

#정리하기 문제3
r=float(input("반지름은?"))
pi=3.14

length=2 * pi * r
area  =pi*r**2
print('둘레 =',length)
print('면적 =',area)

#정리하기 문제4
inch= float(input('몇 inch인가요?'))
cm= inch * 2.54
print(inch,"inch =",cm,'cm')
#나중에 배울것 
print("{}인치 = {}cm".format(inch,cm))

#정리하기 문제5
won=int(input('환전할 금액(원)을 입력해주세요.'))
usd=won//1220             #오늘의 USD환율:1220원/USD
change = won % 1220
print('환전금액(원) :',won)
print('USD :',usd)
print('잔액(원) :', change)
#나중에 배울것
print('환전금액 : {}(원)'.format(won))
print('USD : {}달러'.format(usd))
print("잔액 :{}(원)".format(change))
#문제 1
num =(input('정수를 입력 :'))
a=int(num)
b=str(a)
print(type(a))
print(type(b))
#문제2
bun= int(input('입력(minte)'))
h = bun//60
m = bun %60
print('{}분= {}시간{}분'.format(bun,h,m))