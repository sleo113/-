'''

break문과 continue문.

반복문에서 주로 사용된다.

'''
nonplayer = {5,6}

for player in range(1,12):
    if(player in nonplayer) :
           print("{0}, 잠깐 멈춰 당신 누구야?".format(player))
           continue
    elif (player == nonplayer) :
        break
    print("{0},얼른 준비해".format(player))