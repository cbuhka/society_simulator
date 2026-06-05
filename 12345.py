import os

# --- ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ---
stats = {"STR": 1, "AGI": 1, "INT": 1, "VIT": 1, "DEX": 1, "LCK": 1}
age_months = 0  
development = 0
max_ap = 10  
ap = 10     
ticks = 0             
TICKS_PER_YEAR = 36       

counters = {"smotret": 0, "krik": 0, "sluh": 0, "uchit": 0, "polzat": 0, "zvuki": 0, "rech_try": 0}
skills = {"sluh": False, "vzglyad": False, "polzat": False, "agukat": False, "rech": False, "hodit": False}

# Наше расписание: 7 фаз
phases = ["Учеба", "Еда", "Свободное время", "Сон", "Учеба", "Свободное время", "Дом"]
current_phase_index = 0
day_count = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Вы видите свет. Вы только что родились.")
print("1 - Обычная игра | 2 - Пропустить младенчество")
vybor_rezhima = input("> ")

if vybor_rezhima == "2":
    ticks = TICKS_PER_YEAR 
    development = 50 
    for key in counters: counters[key] = 5
    for key in skills: skills[key] = True

# --- МЛАДЕНЧЕСТВО ---
while ticks < TICKS_PER_YEAR:
    print(f"\nВОЗРАСТ: {age_months} мес. | РАЗВИТИЕ: {development} | ОД: {ap}/{max_ap}")
    print("1-Смотреть, 2-Кричать, 3-Спать")
    if skills["sluh"]: print("4-Слушать")
    if skills["vzglyad"]: print("5-Изучать")
    if skills["polzat"]: print("6-Ползти")
    if skills["agukat"]: print("7-Агукать")
    if skills["rech"]: print("9-Речь")
    if skills["hodit"]: print("8-ШАГИ")

    action = input("> ")
    action_made = False

    if action == "1" and ap >= 1: counters["smotret"] += 1; development += 1; ap -= 1; action_made = True
    elif action == "2" and ap >= 1: counters["krik"] += 1; development += 1; ap -= 1; action_made = True
    elif action == "3": development += 1; ap = max_ap; action_made = True
    elif action == "4" and skills["sluh"] and ap >= 1: counters["sluh"] += 1; ap -= 1; action_made = True
    elif action == "5" and skills["vzglyad"] and ap >= 2: counters["uchit"] += 1; development += 2; ap -= 2; action_made = True
    elif action == "6" and skills["polzat"] and ap >= 3: counters["polzat"] += 1; development += 3; ap -= 3; action_made = True
    elif action == "7" and skills["agukat"] and ap >= 2: counters["zvuki"] += 1; development += 3; ap -= 2; action_made = True
    elif action == "8" and skills["hodit"] and ap >= 4: development += 5; ap -= 4; action_made = True
    elif action == "9" and skills["rech"] and ap >= 2: counters["rech_try"] += 1; development += 4; ap -= 2; action_made = True

    if action_made: ticks += 1; age_months = ticks // 3 
    
    if counters["krik"] >= 4 and not skills["sluh"]: skills["sluh"] = True; print("!!! Вы научились СЛУШАТЬ!")
    if counters["smotret"] >= 4 and not skills["vzglyad"]: skills["vzglyad"] = True; print("!!! Вы научились ИЗУЧАТЬ!")
    if counters["sluh"] >= 4 and development >= 15 and not skills["agukat"]: skills["agukat"] = True; print("!!! Вы научились АГУКАТЬ!")
    if counters["smotret"] >= 4 and counters["uchit"] >= 4 and development >= 25 and not skills["polzat"]: skills["polzat"] = True; print("!!! Вы научились ПОЛЗТИ!")
    if counters["krik"] >= 4 and counters["sluh"] >= 4 and counters["zvuki"] >= 4 and development >= 35 and not skills["rech"]: skills["rech"] = True; print("!!! Вы научились ГОВОРИТЬ!")
    if counters["polzat"] >= 4 and counters["rech_try"] >= 4 and development >= 45 and not skills["hodit"]: skills["hodit"] = True; print("!!! Вы научились ХОДИТЬ!")

# --- ДЕТСКИЙ САД И ДОМ ---
if skills["hodit"]:
    print("\n=== ВЫ ПОШЛИ В ДЕТСКИЙ САД ===")
    max_ap = 20
    ap = 20
    
    while True:
        phase = phases[current_phase_index]
        print(f"\n--- ДЕНЬ {day_count} | ФАЗА: {phase} ---")
        print(f"[СТАТЫ: {stats} | ОД: {ap}/{max_ap}]")
        
        # ЛОГИКА ФАЗ
        if phase == "Учеба":
            print("1-Учиться(1), 2-Алфавит(3), 3-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1: stats["INT"] += 1; ap -= 1
            elif choice == "2" and ap >= 3: 
                if stats["INT"] >= 2: stats["INT"] += 2; ap -= 3
                else: print("!!! Нужно INT >= 2!")
            elif choice == "3" and ap >= 1: print("Вы ленитесь."); ap -= 1
            else: print("!!! Ошибка или нет ОД!")
        
        elif phase == "Еда":
            print("1-Кушать(цена 1, восстановит +1), 2-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1:
                ap = min(ap + 1, max_ap)
                stats["VIT"] += 1
                print("Вы поели и взбодрились.")
            elif choice == "2" and ap >= 1: print("Вы сидите."); ap -= 1
            else: print("!!! Ошибка или нет ОД!")

        elif phase == "Свободное время":
            print("1-Бег(2), 2-Турники(2), 3-Палка(2), 4-Безделье(1)")
            choice = input("> ")
            if choice in ["1", "2", "3"] and ap >= 2:
                if choice == "1": stats["AGI"] += 1; stats["VIT"] += 1; ap -= 2
                elif choice == "2": stats["STR"] += 1; stats["VIT"] += 1; ap -= 2
                elif choice == "3": 
                    if stats["STR"] >= 3 and stats["AGI"] >= 3: stats["STR"] += 1; stats["AGI"] += 1; ap -= 2
                    else: print("!!! Нужно STR и AGI >= 3!")
            elif choice == "4" and ap >= 1: print("Вы смотрите в окно."); ap -= 1
            else: print("!!! Ошибка или нет ОД!")

        elif phase == "Сон":
            print("1-Дремать(цена 2, восстановит +2), 2-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 2:
                ap = min(ap + 2, max_ap)
                print("Вы выспались.")
            elif choice == "2" and ap >= 1: print("Вы ворочаетесь."); ap -= 1
            else: print("!!! Ошибка или нет ОД!")

        elif phase == "Дом":
            print("1-Читать(1), 2-Игрушки(1), 3-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1: stats["INT"] += 1; ap -= 1
            elif choice == "2" and ap >= 1: stats["DEX"] += 1; ap -= 1
            elif choice == "3" and ap >= 1: print("Вы отдыхаете."); ap -= 1
            else: print("!!! Ошибка или нет ОД!")

        # ПЕРЕКЛЮЧЕНИЕ ФАЗ (СТРОГО ПО ОЧЕРЕДИ)
        current_phase_index += 1
        if current_phase_index >= len(phases):
            current_phase_index = 0
            day_count += 1
            print(f"\n--- ДЕНЬ {day_count - 1} ЗАКОНЧЕН. ---")
else:
    print("Вы еще не готовы к садику.")