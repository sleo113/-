'''

0. 가변인자를 이용한 함수 호출에 대해 배워보자.

++

end""를 쓰면 옆에 이어서 쓸수 있다.
'''

# def information(name, age, team1, team2, team3, team4, team5) :
#     print("이름 : {0}\t 나이 : {1}\t " \
#         .format(name, age), end =" ")
#     print(team1, team2, team3, team4, team5)

# information("박떙떙", 19, "레드", "나이트", "고고프로", "사하라", "싱싱")
# information("궁떙떙", 39, "나이트", "레드", "코브라", "고릴라", "레디")
# information("지떙떙", 26, "레드", "고릴라", "고고프로", "아미르", "인티니티")

'''

이렇게 하게 되면 한 문장에만 함수를 추가하고 싶을때 한 문장에만 추가하지 못하고
각각의 문장에 함수를 하나씩 더 적어줘야 한다.

이렇게 하기 싫을떄 가변인자를 활용한다.

어떻게 활용하냐면
=> team함수들에 앞에 *를 붙여주고
ex)
for te in team :
        print( te, end=" ")
    print()
를 적어주면 된다.

'''
def information(name, age, *team) :
    print("이름 : {0}\t 나이 : {1}\t " \
        .format(name, age), end =" ")
    for te in team :
        print( te, end=" ")
    print()

information("박떙떙", 19, "레드", "나이트", "고고프로", "사하라")
information("궁떙떙", 39, "나이트", "레드", "코브라",)
information("지떙떙", 26, "레드", "고릴라", "고고프로", "아미르", "인티니티", "싱싱")