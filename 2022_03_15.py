#b=0xCF
#(b)
#c=0o27
#print(c)
#d=0b1011
#print(d)
#print(b+d)
#print(b*c)
#f=0xBC
#print(f)
# 16진수 8진수 2진수 기본은 10진수/ 16진수는 10이후부터 A B C D E F
# 0x     0o    0b    
#  복습
#birth_year=int(input("태어난 년도는?"))
#print("당신의 나이:", 2022- birth_year)
#name = input("당신의 이름은?")
#print("안녕,",name)

안녕="니하오"
hello= 안녕
print(hello)

guide='큰 따옴표(")을 문자열의 시작과 끝에 붙인다.'
print(guide)
guide2= "작은 따옴표(') 또한 문자열의 시작과 끝에 붙일수 있다."
print(guide2)
guide3="큰 따옴표(\")을 문자열의 시작과 끝에 붙인다."
print(guide3)
guide4="역슬레쉬(\)를 사용하여 여러가지를 할 수 있다"
print(guide4)

print('이달의 추천도서는 \'모스크바의 신사\' 입니다.')
print("영어 공부하는건 어려워요\nit is difficult study English")
print("안녕하세요\n저는 홍길동 입니다.")
print("안녕하세요\t저는 홍길동 입니다.")
#\n은 줄 바꿈 \t는 tab 처럼 뛰어쓰기

book="모스크바의 신사\n에니미 토울스\n현대문학\n2018.06"
print(book)

print("이름 \t나이\t 지역")
print("홍길동\t25\t강서구")
print("이성계\t26\t강남구")

text='''실패하는 것보다
도전하지 않는것을
두려워라하...'''
print(text)

#name2 = input('이름을 입력하세요. ')
#wellcome= name2+ '님, 반갑습니다~'
#print(wellcome)

cheer='파이팅!! ' * 3
print(cheer)
#연속으로 반복 할때 * 뒤에 반복할 수 적기

text="신한대학교"
len(text)
print(len(text))
#len 함수 : 글자 수를 세준다
name="ShinHan"
name.upper()
print(name.upper())
name.lower()
print(name.lower())
name.swapcase()
print(name.swapcase())
name.title()
print(name.title())
#.upper() 메소드: 변수.uppe()r는 전부다 대문자로 바꿔준다
#.lower() 메소드: 변수.lower()는 전부다 소문자로 바꿔준다
#.swapcase() 메소드:변수.swapcase()는 소문자는 대문자로 대문자는 소문자로 바꿔준다
#.title() 메소드: 변수.title()는 각 단어의 앞글자만 대문자로 변환 나머진 다 소문자로 변환해준다
word='python'
'-'.join(word)
print('-'.join(word))
#'-'.join() 문자열 메소드: 각 문자 사이에 하이픈(-)을 삽입한다


 #교제 p.92 6번 문제
print('안나가 "아빠!"라고 말했다.')
print("안나가 \"아빠!\"라고 말했다.")
print("삶은 복잡하지만, 행복은'단순'하다")
print("큰따옴표(\")와 작은따옴표(')의사용법")
print('큰따옴표(")와 작은따옴표(\')의사용법')
 #교제p.92 7번 문제
print("그가 말했다.\"이제'WHAT'은 결정 되었으니,'HOW'에 대해서 이야기 해보자.\"")
 #교제p.92 8번 문제
print("Dont'tbe afraid to fall.\n실패하는 것을 두려워하지 말아라.\nBeafraid not to try.\n시도조차 하지 않는 것을 두려워하라.")
text='''Don'tbe afraid to fall
실패하는것을 두려워하지 말아라.
Be dafraid not to try
시도조차 하지 않는 것을 두려워하라.'''
print(text)

#a=input('첫번째 문자를 입력:')
#b=int(input('두번째 정수를 입력:'))
#print(a*b)


#txt= input('입력문자 -> ') 
#result = '"'+ txt + '"'
#print(result)
#print('문자의 갯수:',len(result))



 
