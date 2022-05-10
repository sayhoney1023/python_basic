nums= 4,2,5,7,1,3
print(sorted (nums))                 #순서 정렬
print(sorted(nums,reverse = True))   # 반대순서 정렬
print(nums)

fruits= 'orange','apple','mango','tomto'
print(sorted(fruits))                #문자열은 알파벳 순서대로 정렬됨

num = [4,2,5,7,1,3]
print(sorted(num))


programmer_dict={'Python':5,'C':6,'C++':3,'Java':12,'Ruby':1}
print(sorted(programmer_dict.keys()))
print(sorted(programmer_dict.keys(),reverse = True))

programmer_dict.values()    #값 보여지기
list(programmer_dict.keys()) #딕셔너리 -> 리스트로 변경

# sorted(list(programmer_dict.keys())) 와 sorted(programmer_dict.keys()) 는 같다
# sorted 함수는 리스트 타입으로 나오기 때문에

for n in  range(1,10+1):
    print(n)

a=10
#a= range(0,a/2)       # 실수로 계산되어 연산 불가능.
a= range(0,int(a/2))   # 이렇게 적어야 연산이 됨.

langs ='Python','Java','C++','Ruby'
for index in range(len(langs)):
    print(index,langs[index])

langs =['Python','Java','C++','Ruby']
for i in range(len(langs)):
    print('{}:{}'.format(i,langs[i]))
    
langs =['Python','Java','C++','Ruby']
for index,item in enumerate(langs):
    print('{}:{}'.format(index, langs[index]))

a= list()
for x in range(10):
    a.append(x**2)
    
print(a)

a=[x**2 for x in range(10)]  #윗 문장을 한줄로 간단히 만든 문장
print(a)

A=['blue','yellow','red']
B=['red','green','blue']
pairs=[]
for a in A:
    for b in B:
        if a!=b:
            pairs.append((a,b))
print(pairs)

A=['blue','yellow','red']
B=['red','green','blue']
C=[]
C=[(a,b)for a in A for b in B if a!=b] #윗 문장을 한줄로 바꾸는법
print(C)

a= set()
for x in 'abracadabra':
    if x not in 'abc':
        a.add(x)
print (a)

a={x for x in 'abracadabra' if x not in 'abc'} #윗 문장을 한줄로 바꾸는법
print(a)

a= dict()
for x in (2,4,6):
    a[x]=x**2
print(a)

a= {x: x**2 for x in (2,4,6)}      # 윗문장 한줄로 바꾸는법
print (a)

books = list()
books. append({'제목':'개발자의 코드','출판연도':'2013.02.28','출판사':'A','쪽수':200,'추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'A', '쪽수':248, '추천유무':True})

print('전체 책 목록')
for book in books:
    print(book)

many_page = list()
for book in books:
    if book ['쪽수']> 250:
        many_page.append(book['제목'])
print('쪽수가 250쪽이 넘는 책의 리스트 :',many_page)


print()

#=============================================================================

recommends = list()
for book in books:
    if book['추천유무']:
            recommends.append (book['제목'])

print('내가 추천하는 책의 리스트 :',recommends)
print()
#=============================================================================
all_pages = 0
for book in books:
    all_pages = all_pages +book['쪽수']

print('내가 읽은 책의 전체 쪽수 : ',all_pages)
print()

#=============================================================================
pub_company = set()
for book in books:
    pub_company.add(book['출판사'])

print('내가 읽은 책의 출판사 목록 : ',pub_company)
print()

#=============================================================================
many_page=list()
recommends=list()
pub_company=set()
all_pages=0

for book in books:
    if book['쪽수']>250:
        many_page.append(book['제목'])
    
    if book['추천유무']:
        recommends.append(book['제목'])
   
    all_pages = all_pages +book['쪽수']

    pub_company.add(book['출판사']) 

print('\n')
print('쪽수가 250쪽 넘는 책 리스트:',many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_company)
#=============================================================================

n= int(input('양의 정수 입력 : '))
divisor =list()

for i in range (1,n+1):
    if n % i == 0:
         divisor.append(i)
print('약수 : ', divisor)
print('약수의 개수 : ',len(divisor))

a= int (input('첫번째 정수 : '))
b= int (input('두번째 정수 : '))

A= set()
B= set() 

for i in range (1,a+1):
    if a % i == 0:
        A.add(i)

for i in range (1,b+1):
    if b % i == 0:
        B.add(i)

print('{}의 약수 {} '.format(a,A))
print('{}의 약수 {} '.format(b,B))

print('{}와 {} 의 공약수 {}'.format(a,b,A.intersection(B)))
print('{}와 {} 의 최대공약수 {}'.format(a,b,max(A.intersection(B))))
#=============================================================================
menus = ['돈가스','생선가스','우동','초밥','냉모밀']

for button, food in enumerate(menus):
    print('{} : {}'.format(button,food)) 
while True:
    button_num = int(input('주문 버튼을 눌러 주세요 : '))
    if button_num == 9:
        break;
    print('{} : {} 주문 되었습니다.'.format(button_num,menus[button_num]))
print('이용해 주셔서 감사합니다.')



fruit={'사과 ':0,'딸기':0,'수박':0,'레몬':0,'포도':0}
fruit['사과'],fruit['딸기'],fruit['수박'],fruit['레몬'],fruit['포도'] =\
    map(int,input('사과,딸기,수박,레몬,포도,가격을 공백으로 구분하여 입력 :').split())

print(fruit)
print('-'*7)

for name, price in fruit.items():
    print('{} : {}원'.format(name,price))

print('-'*7)
print('------- 오늘의 과일 가격 조회 -------')
name=input('조회하고 싶은 과일의 이름은? ')
print('오늘의 {}의 가격 : {} 원'.format(name,price))
