import random

def play_game():
    min = 1
    max = 99
    count = 0
    target = random.randint(min, max)
    print("=========猜數字遊戲============\n\n")
    print(target)
    while(True):
        keyin = int(input(f'猜數字範圍{min}~{max}:'))
        count += 1
        if(keyin >= min and keyin <= max):
            if(keyin == target):
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"您共猜了{count}次")
                break
            elif keyin < target:
                print("再大一點")
                min = keyin + 1
            elif keyin > target:
                print("再小一點")
                max = keyin - 1
            print(f"您已經猜了:{count}次")
        else:
            print("請輸入提示範圍內的數字")

while(True):    
    play_game()
    play_again:str = input("您還要繼續嗎(y,n)?")
    if play_again == "n":
        break
    
    

print("猜數字遊戲結束")
    