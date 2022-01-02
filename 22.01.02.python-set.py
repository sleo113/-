'''

0. set(=세트=집합)를 배워보자.

형태
1. 변수 이름 = {값 1개 ~ 여러 개}
2. 변수 이름 = set([값 1개 ~ 여러 개])

ex)my_set = {set 안에 넣고 싶은 값 1개 ~ 여러 개}

1. 세트 특징

1) 중복이 않된다. 만약 값을 중복시킬 경우 중독되는 건 하나만 출력한다. 나머지는 무시---
2) 순서가 없다. 따라서 순서는 보장되지 않는다.

2. 종류 

ex) 
Java = {"박땡떙", "이땡땡", "구땡땡"}
JS = {"박떙땡", "홍땡땡"}
일 때

1) 교집합 => Java와 JS를 모두 쓸 줄 아는 사람

print(변수 이름1 & 변수 이름2) -> and 아님! 논리곱임!

혹은

print(변수이름1.intersection(변수이름2) )


2) 합집합 => Java와 JS 둘 중 하나라도 쓸 줄 아는 사람

print( Java | JS ) -> or 아님! 논리합임!

혹은

print( Java.union(JS) )

3) 차집합 => 하나는 할 줄 아는데 다른 건 할 줄 아예 모르는 사람
print( Java - JS )

혹은

print( Java.difference(JS) )

4) 집합에 값을 넣고 싶은 경우

변수이름.add("넣고 싶은 값")

ex)
Java.add("치땡땡")
print(Java)

5) 집합에 들어 있는 값을 뺴고 싶은 경우

변수이름.remove("뺴고 싶은 값")

ex) 
Java.remove(""치땡땡)
print(Java)

'''

soccer = {"Roce", "Pozy", "Eoc"}
baseball = set(["Nago", "Noga", "Roce"])


print( soccer & baseball ) # {"Roce"}
print( baseball.intersection(soccer) ) #{"Roce"}

print( soccer | baseball ) #{"Roce", "Pozy", "Eoc", "Nago", "Noga", "Roce"}
print( soccer.union(baseball) )#{"Roce", "Pozy", "Eoc", "Nago", "Noga", "Roce"}

print( soccer - baseball ) # {"Nago", "Noga"}
print( soccer.difference(baseball) ) #{"Nago", "Noga"}

baseball.add("Potter") 
print(baseball) #{"Nago", "Noga", "Roce", "Potter"}

soccer.add("koyo")
print(soccer) #{"Roce", "Pozy", "Eoc"}

baseball.remove("Nago")
print(baseball) #{"Noga", "Roce", "Potter"}

soccer.remove("Eoc")
print(soccer) #{"Roce", "Pozy", "Koyo"}

