# 01. 파이썬 시작하기

# 001. print 기초
# 화면에 <Hello World> 문자열을 출력하시오
print("Hello World")
print('Hello World')

# 002.
# 화면에 <Mary's cosmetics> 를 출력하시오
print("Mary's cosmetics")

# 003.
# <신씨가 소리질렀다, "도둑이야".> 를 출력하시오
print('신씨가 소리질렀다, "도둑이야".')

# 004. 
# <C:\Windows> 를 출력하시오
print("C:\Windows")

# 005. print 탭과 줄바꿈
# 코드를 실행하고 \t 와 \n의 역할을 설명하시오
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n : 줄바꿈을 한다.
# \t : tab과 같은 역할을 한다.

# 006. print 여러 데이터 출력
# 코드의 출력 결과를 예상하시오
print ("오늘은", "일요일")
# <오늘은 월요일> 이 출력된다. , 로 출력할 시 사이 공백이 있다.

# 007. print 기초
# print() 함수를 사용하여 <naver;kakao;sk;samsung>를 출력하시오
print("naver", "kakao", "samsung", sep=";") # (O)
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.

# 008. 
# print() 함수를 사용하여 <naver/kakao/sk/samsung>를 출력하시오
print("naver", "kakao", "samsung", sep="/")

# 009. print 줄바꿈
# 다음의 코드를 줄바꿈 없이 출력하시오. 
# print 함수는 두 번 사용합니다. 세미콜론(;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first", end="");print("second")

# 010. 연산 결과 출력
# 5/3의 결과를 화면에 출력하시오.
print(5/3)

