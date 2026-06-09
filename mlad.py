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