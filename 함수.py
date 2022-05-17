def hap (a,b,c):
    return a+b+c

sum= hap(10,20,30)
print(sum)

def hello():
    name= input('이름을 입력하세요! ')
    print('안녕!',name)

hello()

def halo(a):
     print('안녕!', a)

na= input('이름을 입력 :')
halo(na)

def my_student_info(name,school_ID,PhoneNumber):
    print("-----------------------")
    print(' 학생이름 :',name)
    print(' 학급번호 :',school_ID)
    print(' 전화번호 :',PhoneNumber)
name=input('학생 이름:')
school_ID= input('학급번호:')
PhoneNumber= input('전화번호:')

my_student_info(name,school_ID, PhoneNumber)
my_student_info('현아','01','01-235-6789')
my_student_info('진수','02','01-987-6543')

def sum(a,b):
    print(a+b)

sum(1,4)
sum(7,3)

def change_name(name):
    return name+'님'

name=input('이름을 입력해 주세요 : ')
print(change_name(name))
print(change_name('지희'))


def my_calc(x,y):
    z=x*y
    return z
selo=int(input('세로의 길이를 입력해주세요 : '))
galo=int(input('가로의 길이를 입력해주세요 : '))
print(my_calc(selo,galo))


def circle_area(r):
    s = 3.14* r*r
    print('반지름이 {}cm 인 원의 면적은 {}cm'.format(r,s))

r=float(input('반지름 을 입력해 주세요 :'))
circle_area(r)

def area(rr):
    s = 3.14*r*r
    return s
rr= 5.0
print('반지름이 {}cm 인 원의 면적은 {}cm'.format(r,area(rr))) 


def y(x):
    return 3 * x **2 +5*x+2

print(y(3))
print(y(5))

def print_n_times(n,*values):
    print('n= {} 입니다.'.format(n))
    for value in values:
        print(value)
        
    print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")


def print_n_times(n,*values):
    print('n= {} 입니다.'.format(n))
    for value in values:
        print(value)
        
    print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

def nn_times(value,n=5):
    for i in range(n):
        print(value)
        
nn_times("안녕하세요",3)

def my_func ():
         
    param = 100          # 로컬 변수
    print(param)

param = 500  # 전역 변수 

my_func()           # 함수 불러오기
print(param)        #전역 변수 프린트

my_func()          # 함수 불러오기 

param=300          #전역변수 300으로 바꿈
print(param)      #전역 변수 프린트

def func1():
    a=10
    print('fumc1() 에서 a = {}'.format(a))

def func2():
    print('func2()에서 a={}'.format(a))
a=20
func1()
func2()

print(a)

del param  #기존 위의 param 변수 삭제
def my_func ():
    global param         #전역변수 선언
    param = 100          
    print(param)  

my_func()         # 함수 불러오기
print(param)      # 앞의 전역변수 선언한 100 프린트
param = 500       #전역 변수 변경 
print(param)      #전역 변수 프린트

my_func()         # 함수 불러오기 

param=300         #전역변수 변경
print(param)      #전역 변수 프린트


def gugudan(n):
    for i in range(1,9+1):
        print('{}X{}={}'.format(n,i,n*i))
    
gugudan(4)

def check_pw(pw):
    if pw =='1234':
        return True
    else:
        return False
while check_pw(input('비밓번호 4자리 를 입력해주세요 : ')) == False:
    print('비밀번호가 틀렸습니다, 다시 입력해 주세요.')
print('비밀번호가 맞습니다.')


def plus_one(num):
    num+=1;
    return num

num=5
print(plus_one(num))

print(num)

def func(**student):
    for name in student.keys():
        print(name,student[name])
        
func(인석='python',치훈='java',수빈='JS')

def func5(**student):
    for index, item in student.items():
        print('{} : {}'.format(index,item))
func5(Gildong="python",Ara='Java',Yoona='Ruby')

def concat(*args,sep='/'):
    return sep.join(args)
print(concat('a','b','c'))
print(concat('a','b','c',sep='.'))
print(concat('a','b','c',sep='-'))

list(range(5,9+1))
aros=5,10
list(range(*aros))

def student_info(name,birth,major='cs',country='Kor'):
    print('이름 : {}\n생년월일 : {} \n전공 : {}\n국적 : {}'.format(name,birth,major,country))

info = {'name' : '김강우', 'birth' : 19990802}
student_info(**info)








