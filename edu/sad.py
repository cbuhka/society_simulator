# --- ДЕТСКИЙ САД (300 ДНЕЙ) ---
if skills["hodit"] and vybor_rezhima != "3":
    age_years = 3

    print("\n=== ВЫ ПОШЛИ В ДЕТСКИЙ САД ===")
    print("Вы начинаете осознавать свои способности.")
    print(f"STR: {stats['STR']}")
    print(f"AGI: {stats['AGI']}")
    print(f"INT: {stats['INT']}")
    print(f"VIT: {stats['VIT']}")
    print(f"DEX: {stats['DEX']}")
    print(f"LCK: {stats['LCK']}")
    print(f"SOC: {stats['SOC']}")

    max_ap = 20
    ap = 20

    while day_count <= 300:
        phase = phases[current_phase_index]

        print(f"\n--- {age_years} ЛЕТ | ДЕНЬ {day_count} | ФАЗА: {phase} | ОД: {ap}/{max_ap} ---")

        if phase == "Учеба":
            print("1-Учиться(1), 2-Алфавит(3), 3-Безделье(1)")
            choice = input("> ")

            if choice == "1" and ap >= 1:
                stats["INT"] += 1
                ap -= 1

            elif choice == "2" and ap >= 3:
                if stats["INT"] >= 2:
                    stats["INT"] += 2
                    ap -= 3
                else:
                    print("!!! Нужно INT >= 2!")

        elif phase == "Еда":
            print("1-Кушать(1), 2-Безделье(1)")
            choice = input("> ")

            if choice == "1" and ap >= 1:
                ap = min(ap + 1, max_ap)
                stats["VIT"] += 1
                ap -= 1

        elif phase == "Свободное время":
            print("1-Бег(2), 2-Турники(2), 3-Палка(2), 4-Безделье(1)")
            choice = input("> ")

            if choice == "1" and ap >= 2:
                stats["AGI"] += 1
                stats["VIT"] += 1
                ap -= 2

            elif choice == "2" and ap >= 2:
                stats["STR"] += 1
                stats["VIT"] += 1
                stats["DEX"] += 1
                ap -= 2

            elif choice == "3" and ap >= 2:
                stats["STR"] += 1
                stats["AGI"] += 1
                stats["DEX"] += 1
                ap -= 2

        elif phase == "Сон":
            print("1-Дремать(2, +2 ОД), 2-Безделье(1)")
            choice = input("> ")

            if choice == "1" and ap >= 2:
                ap = min(ap + 2, max_ap)

        elif phase == "Дом":
            print("1-Читать(1), 2-Игрушки(1), 3-Безделье(1)")
            choice = input("> ")

            if choice == "1" and ap >= 1:
                stats["INT"] += 1
                ap -= 1

            elif choice == "2" and ap >= 1:
                stats["DEX"] += 1
                ap -= 1

        current_phase_index += 1

        if current_phase_index >= len(phases):
            current_phase_index = 0
            day_count += 1
            ap = max_ap

            if day_count % 100 == 0:
                age_years += 1
                print(f"\n--- ВАМ ИСПОЛНИЛОСЬ {age_years} ЛЕТ! ---")