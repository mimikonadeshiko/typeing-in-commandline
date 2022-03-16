import random
def dedenn(mondai):
    syutudai = (random.choice(mondai))
    print(syutudai)
    inputdata = input()
    if inputdata == syutudai:
        print("あってると思うよ!")
    else:
        print("はぁ?間違えてんじゃねーよばーかばーか")