import random

min=1
max=50
count=0
target=random.randint(min,max)
print("---------猜數字遊戲--------\n")
while(True):
    try:
        guess=int(input(f"請輸入數字開始猜數字{min}~{max}:"))
    except:
        print("輸入格式錯誤")
        count+=1
        print(f"總共猜了{count}次")
    else:
        count+=1
        if(guess>=min and guess<=max):  
            if guess ==target:
                print(f"bingno,答案是{target}")
                print(f"總共猜了{count}次")
                break
            elif guess>target:
                print("再小一點")
                max=guess -1   
            elif guess<target:
                print("再大一點")
                min=guess +1
            print(f"總共猜了{count}次") 
        else:
            print("超出範圍")
            print(f"總共猜了{count}次")

print("遊戲結束")