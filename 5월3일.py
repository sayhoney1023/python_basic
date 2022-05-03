name= ["s",'d','x','n','q','a']
for c in name:
    print(c, end='')
print ()
print(name[2])

name[2]= 'A'
print(name)
#튜플 타입 선언
ff=("신한대학교","신한대") # *튜플타입 선언할 때 괄호안에 ("000")만 있으면 숫자면 int 문자면 str 함수 가 된다
for a in ff:              #  이것을 방지 할려면 ("000",) ","를 사용해서 튜플로 선언
    print(a,end='')
print()
# ff[0]="신한"              # 튜플타입 데이터는 값을 바꿀수 없다.
# print(ff)
# for a in ff:             
    # print(a,end='')       #튜플에는 리스트에서 제공하는 메소드는 사용이 불가능 하다.
    
#튜플 -> 리스트 / 리스트->튜플   tuple () 함수 사용
fruit = ('apple','orange','peach','mango')

fruit_list= list(fruit)      #튜플->리스트 과정 list()

print(type(fruit_list))

fruit= tuple(fruit_list)    #리스트-> 튜플 과정 tuple()

print(type(fruit))

#세트 타입 선언
languages={'c++','python','c','c++','python'}    #세트 생성
print(languages)                                 # <- 세트값 확인
# 세트는 중복값을 허용하지 않음.
"python" in languages # 항목 존재 유무 확인
"R"in languages
                 #빈세트 타입 선언은 {} 만으로는 생성 불가  set() 함수를 사용해야 한다.
                 
                 #세트타입은 튜플타입과 달리 삭제나 변경이 가능하다.
languages.add("java")                          #'java'를 추가하지만 중복 불허로 추가 안됨
print(languages)
languages.remove('java')                       #"java" 원소를 삭제
print(languages)
languages.update(['C++','PHP','JavaScript'])   #리스트 항목을 세트 원소로 추가
print(languages)
languages.discard("JavaScript")                #"JavaScript"  원소를 삭제
print(languages)
languages.clear()                              #모든 원소 삭제
print(languages)

# 세트타입 집합 연산자 사용

a=set('abracabadara')
b=set('alafresfgtrs')
a - b                                  # a에만 존재하는 문자 (차집합)
b - a                                  # b에만  ""
a | b                                  # a와 b의 합집합
a & b                                  # a와 b의 교집합
a ^ b                                  # a와 b의 대칭차집합  (합집합 - 교집합

# 딕셔너리 타입

a_dict = {"python":5,"C":2,"C++":3,'Java':4}     # <-딕셔너리 선언
print(type(a_dict))                              # 타입 확인
print(len(a_dict))                               # 항목 개수 확인
print(a_dict["python"])                          # 'python 의 값 확인

a_dict['python'] = 7                             # 특정 항목 값 변경
print( a_dict )                                  # 딕셔너리 값 재확인
# keys( ) 메소드
print(a_dict.keys())                             # 전체 키 변환
print(list(a_dict.keys()))                       # 전체 키 리스트 변환
# values ( ) 메소드
print(a_dict.values())                           #딕셔너리의 값만 출력
print(list(a_dict.values()))                     #리스트에 값만 넣기
# 딕셔너리 실습
stationery={"pencil":200,
            "pen"   :800,
            "eraser":500,
            "ruler" :300}
stationery_list = list(stationery.values())           # 딕셔너리 값들을 리스트에 추가
print(stationery_list)


stationery={"pencil":200,
            "pen"   :800,
            "eraser":500,
            "ruler" :300}
print(stationery.get("eraser"))
stationery["phone"]=500000                       # 항목 추가
print(stationery)
del stationery["phone"]                          # 항목 삭제
stationery.clear()                               # 전체 항목 삭제
print(stationery)

#튜플을 딕셔너리로 바꾸기
a_list = [("python",7),("Java",2)]              #튜플에 저장되어 있는 값
a_dict = dict(a_list)                           # dict()를 사용하여 딕셔너리로 변환

print(a_dict.get("python")) 
#실습
                                                # .get() 메소드 사용 예제
honey_dict = {
    'name'      :  '허니버터 아몬드',
    'type'      :  '견과류',
    'ingredient': ['아몬드','물엿','설탕','아스파탐'],
    'company'   : '길림양행',
    'price'     : 8000}
name_value=honey_dict.get('name')
print("품명 : ",name_value)
ingredient_value=honey_dict.get('ingredient')
print('원재료 명 : ',ingredient_value)
weight_value = honey_dict.get('weight')
print('가격 : {} 원'.format(weight_value))
if weight_value == None:
    print('키가 존재하지 않습니다.')
# 실습 프로젝트

count=int(input('총 몇명 인가요?'))
print('학생의 이름과 시험성적을 차례대로 입력하세요!')
scores =list()
for i in range(count):           #이름및 점수 입력
    num =i+1
    print(num,'번쨰 학생 =====')
    name = input('* 이름: ')
    score= int(input(' * 점수 : '))
    pair = (name,score)
    scores.append(pair)
    
#리스트를 딕셔너리 타입으로 변환 
scores_dict=dict(scores)

#학생 이름을 입력 받아 점수를 출력
flag = True
while flag:
    wanted = input ('어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요.: ')
    
    if wanted in scores_dict:
        print(wanted,'하생의 점수: ',scores_dict.get(wanted))
        flag= False
        print('프로그램을 종료합니다.')
    else:
        print('찾는학생(',wanted,') 의 점수가 존재하지 않습니다.')
            
# 실습 2

menu = {'Americano'      :2000,
        'Cafe latte'     :2500,
        'Green Tea latte':3000,
        'Mocha latte'    :3500}
print('Americano'in menu.keys())
print('Vanila latte'in menu.keys())
if 'Vanila latte'in menu.keys():
    print('Vanila latte가 있습니다.')
else:
    print('죄송합니다, Vanila latte가 준비되지 않았습니다.')

#실습3
menus = {'돈가스'  :5000,
         '생선가스':5500,
         '우동'    :2500,
         '초밥세트':9000}
for menu, price in menus.items():
    print(menu,':',price,'원')
    