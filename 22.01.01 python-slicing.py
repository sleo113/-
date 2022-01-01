'''

슬라이싱에 대해 배우기
어떤 정보를 잘라서 가져오는 것을 슬라이싱이라 한다.
필요한 값을 가져올때 []를 사용한다.
강의를 보니 배열같은 느낌이다.

슬라이싱을 하는 부분은 0부터 해당 자리에 들어간다.
앞에서부터 불러올 수도 있고 뒤에서부터 가져올 수도 있다.

'''

jumin = '112391-1234567'
#슬라이싱

data0 = '생년 :'
data1 = '월 :'
data2 = '일 :'
data3 = '생년월일 :'
data4 = '뒤에 일곱자리 :'
data5 = '생년 월일 뒷자리부터 :'

print("주민등록번호을 알려주시겠어요?", jumin)

print( data3 + data4, jumin[0:] )

print( data0, jumin[0:2] )

print( data1, jumin[2:4] )

print( data2, jumin[4:6] )

print( data3, jumin[0:6] )

print( data4, jumin[7:14] )

print( data5, jumin[-7:] )