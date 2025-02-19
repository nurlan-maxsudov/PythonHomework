hisoblar = {"Ali": 100000, "Vali": 50000, "Hasan": 75000}

message = "Operatsiyalardan birisini tanlang:\n"
message += "#1 ni bossangiz - hisobdagi pulni ko'rish.\n"
message += "#2 ni bossangiz - hisobga pul qo'shish.\n"
message += "#3 ni bossangiz - hisobdan pul yechish.\n"

message += "#0 ni bossangiz - dastur to'xtaydi\n"

print(message)

user_ism = input("Iltimos ismingizni kiriting: ")
user_ism = user_ism.capitalize()

is_on = True

while (is_on):

    operation = int(input("Operatsiya kiriting: "))

    if operation == 0:
        is_on = False

    if operation == 1:
        print(f"balansigniz {hisoblar[user_ism]}")
    elif operation == 2:
        print("Summani kiriting: ", end=" ")
        summa = int(input())

        hisoblar[user_ism] += summa

    elif operation == 3:
        print("Summani kiriting: " ,end= " ")
        summa = int(input())

        if (hisoblar[user_ism] - summa):
            print("Balansingizda yetarlicha pul mavjud emas.", end=" ")
            print("Iltimos, balansingizni tekshirish uchun 1 ni tanlang!")
        else:
            hisoblar[user_ism] -= summa
        
