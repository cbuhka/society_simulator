# perem.py

print("\n=== ПЕРЕМЕНА ===")

print("1 - Общаться")
print("2 - Отдыхать")
print("3 - Сходить на дополнительная занятия")
print("4 - Бездельничать")


choice = input("> ")

if choice == "1":
    stats["SOC"] += 1
    ap -= 2
    print("Вы получили +1 SOC 2 AP")
    
if choice == "2" and ap >= 1:
    ap = min(ap + 2, max_ap)
    ap -= 1
    print("Вы отлично отдохнули и получили дополнительное AP")
    
#БИЮЛИОТЕКА
if choice == "3":
    exec(open("biblio.py", encoding="utf-8").read())
    ap -= 5
if choice == "4":
    print("Вы бездельничаете")