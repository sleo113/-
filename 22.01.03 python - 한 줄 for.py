'''

한 줄 for문

[어떤 함수나 기타 등등 for 어떤 변수 in 위에서 언급한 변수 이름]

'''

player = ["나땡떙", "박떙떙", "기땡땡"]
print(player)
player = [len(i) for i in player]
print("선수 이름 길이 :", player)