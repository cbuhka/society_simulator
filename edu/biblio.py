# biblioteka.py

print("\n=== БИБЛИОТЕКА ===")

print("1 - Читать книгу")
print("2 - Уйти")

choice = input("> ")

if choice == "1":
    stats["INT"] += 1
    print("Вы получили +1 INT")