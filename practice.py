from string import printable


print(5)
print('풍선')
print('n'*10)

# 참/거짓 boolean 학습
print(5>10)
print(5<10)
print(False)
print(True)
print(not True)

# 변수 학습
animal = '강아지'
name = '뚜이'
age = 9
hobby = '산책'
is_adult = age >= 3


print('우리집' + animal + '이름은' + name )
print('우리집' + name +'는' + str(age) +'살 이에요 산책을 좋아하며 까만색 개임')
print('우리집',name,'는',age,'살 이에요 산책을 좋아하며 까만색 개임')
#컴마는 스트링을 안씌워도 숫자를 바로 쓸 수 있지만 컴마 앞에 띄어쓰기 한칸이 들어간다는 특징이 있음.
print( name +'는 어른인가요?'+ str(is_adult))

#여러문장에 대해서
#주석 처리를 하고 싶으면 
#따옴표 작은거 세개를 이용해라. 
'''이렇게 해도 한번에 주석처리 됨.
다음줄 까지 쓰고 싶을 때. '''
#전체 문장을 주석 처리 하고 싶으면 선택 영역 드래그 후
#컨트롤 누르고 슬래시 . 다시 해제하고 싶으면 똑같이 컨트롤 슬래시

#quiz 변수를 이용하여 다음문장을 출력하시오. 
#변수명: station
#변수값: 사당,신도림,인천공항 순으로 입력
#출력문장: @@행 열차가 들어오고 있습니다.

station = '사당'
print(station,'행 열차가 들어오고 있습니다')
station = '신도림'
print(station,'행 열차가 들어오고 있습니다')
station = '인천공항'
print(station,'행 열차가 들어오고 있습니다')

#연산자에 대해서 배워보자.
print(1+1)
print(3*190)
print(3**2)#제곱수구하기
print(7%3)#나머지구하기
print(7//3)#몫구하기는 슬러쉬를 이용한다.
print(10>22)#참인지 거짓인지 알려줄것임
print(3==3)#같다는 뜻. 이건 트루나옴.
print(1!=3)#앞뒤가 같지 않다는 뜻. 느낌표로 처리함. 트루로 나올것
print(not(1!=3))# 트루의 낫은 False 가 나올것.



