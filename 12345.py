import os
import random

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

phases = ["Учеба", "Еда", "Свободное время", "Сон", "Учеба", "Свободное время", "Дом"]
current_phase_index = 0
day_count = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ИНИЦИАЛИЗАЦИЯ ---
clear_screen()
print("Вы видите свет. Вы только что родились.")
print("1 - Обычная игра | 2 - Пропустить младенчество | 3 - ДЕБАГ: В ШКОЛУ")
vybor_rezhima = input("> ")

if vybor_rezhima == "2":
    ticks = TICKS_PER_YEAR; development = 50 
    for key in counters: counters[key] = 5
    for key in skills: skills[key] = True
elif vybor_rezhima == "3":
    ticks = TICKS_PER_YEAR
    for key in skills: skills[key] = True
    stats = {"STR": 5, "AGI": 5, "INT": 5, "VIT": 5, "DEX": 5, "LCK": 5}

# --- МЛАДЕНЧЕСТВО ---
while ticks < TICKS_PER_YEAR:
    print(f"\nВОЗРАСТ: {age_months} мес. | РАЗВИТИЕ: {development} | ОД: {ap}/{max_ap}")
    print("1-Смотреть, 2-Кричать, 3-Спать, 4-Слушать, 5-Изучать, 6-Ползти, 7-Агукать, 8-ШАГИ, 9-Речь")
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
    
    if counters["krik"] >= 4: skills["sluh"] = True
    if counters["smotret"] >= 4: skills["vzglyad"] = True
    if counters["sluh"] >= 4 and development >= 15: skills["agukat"] = True
    if counters["smotret"] >= 4 and counters["uchit"] >= 4 and development >= 25: skills["polzat"] = True
    if counters["krik"] >= 4 and counters["sluh"] >= 4 and counters["zvuki"] >= 4 and development >= 35: skills["rech"] = True
    if counters["polzat"] >= 4 and counters["rech_try"] >= 4 and development >= 45: skills["hodit"] = True

# --- ДЕТСКИЙ САД (300 ДНЕЙ) ---
if skills["hodit"] and vybor_rezhima != "3":
    print("\n=== ВЫ ПОШЛИ В ДЕТСКИЙ САД ===")
    max_ap = 20
    ap = 20
    while day_count <= 300:
        phase = phases[current_phase_index]
        print(f"\n--- ДЕНЬ {day_count} | ФАЗА: {phase} | ОД: {ap}/{max_ap} | СТАТЫ: {stats} ---")
        
        if phase == "Учеба":
            print("1-Учиться(1), 2-Алфавит(3), 3-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1: stats["INT"] += 1; ap -= 1
            elif choice == "2" and ap >= 3: 
                if stats["INT"] >= 2: stats["INT"] += 2; ap -= 3
                else: print("!!! Нужно INT >= 2!")
        elif phase == "Еда":
            print("1-Кушать(1), 2-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1: ap = min(ap + 1, max_ap); stats["VIT"] += 1; ap -= 1
        elif phase == "Свободное время":
            print("1-Бег(2), 2-Турники(2), 3-Палка(2), 4-Безделье(1)")
            choice = input("> ")
            if choice in ["1", "2", "3"] and ap >= 2:
                if choice == "1": stats["AGI"] += 1; stats["VIT"] += 1; ap -= 2
                elif choice == "2": stats["STR"] += 1; stats["VIT"] += 1; ap -= 2
                elif choice == "3": stats["STR"] += 1; stats["AGI"] += 1; ap -= 2
        elif phase == "Сон":
            print("1-Дремать(2, +2 ОД), 2-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 2: ap = min(ap + 2, max_ap)
        elif phase == "Дом":
            print("1-Читать(1), 2-Игрушки(1), 3-Безделье(1)")
            choice = input("> ")
            if choice == "1" and ap >= 1: stats["INT"] += 1; ap -= 1
            elif choice == "2" and ap >= 1: stats["DEX"] += 1; ap -= 1

        current_phase_index += 1
        if current_phase_index >= len(phases):
            current_phase_index = 0
            day_count += 1
            ap = max_ap
            if day_count % 100 == 0: print(f"\n--- ВАМ ИСПОЛНИЛОСЬ {3 + (day_count // 100)} ЛЕТ! ---")

# --- ШКОЛА ---
print("\n=== ДОБРО ПОЖАЛОВАТЬ В ШКОЛУ! ===")
for school_years in range(1, 12):
    print(f"\n--- КЛАСС: {school_years} | СТАТЫ: {stats} ---")
    print("1-Усердная учеба(+5 INT), 2-Спорт(+5 STR), 3-Безделье")
    choice = input("> ")
    if choice == "1": stats["INT"] += 5
    elif choice == "2": stats["STR"] += 5
print("\n!!! ВЫ ВЗРОСЛЫЙ! ШКОЛА ОКОНЧЕНА.")