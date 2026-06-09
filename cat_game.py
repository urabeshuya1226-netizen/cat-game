meter = 30
max_lv = 12
lv_n = 1
lv = 1
exp = 0 # 猫との親密度
month = 0
food = 3 # 猫にご飯をあげなくてもいい日数
cat = 1

def lv_up():
    global meter, lv_n, lv, exp
    if lv == lv_n and round(exp) >= meter:
        while lv == lv_n and round(exp) >= meter:
            print("レベルが上がった!")
            lv_n += 1
            print(f"Lv: {lv} → ", end="")
            lv += 1
            print(f"Lv: {lv}\n")
            
            print(f"経験値: {round(exp)} → ", end="")
            exp -= meter
            print(f"経験値: {round(exp)}")
            meter = meter * 1.2
            print()

print("生まれたばかりの子猫を友達からもらったんだけど名前どうしようかな？")
print("名前を決めよう！")
name = input("> ")

print("=================")
print(f"{name}育成ゲーム")
print("=================")
input()
while cat <= 0:
    month += 1
    if food <= 0:
        print(f"{name}は死んでしまった...")
        cat = 0
    print(f"{month}ヶ月目")
    print(f"{name}と何をする？")
    print("(エサをあげる/ミニゲームで遊ぶ/お買い物に行く)")
    move = input("> ")
    if move == "エサをあげる":
        print(f"{name}にエサをあげた！")
        food = 3
        exp += 3