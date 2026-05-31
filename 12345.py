import os

# Возраст и общее развитие
age_months = 0  
development = 0

# Счётчики кликов (практика)
can_watch = 0
can_speak = 0
can_listen = 0
can_study = 0
can_crawl = 0
can_babble = 0
can_speech_try = 0  # Сколько раз пробовал говорить

# Очки Действия (Энергия)
max_ap = 10  
ap = 10      

# Система времени (Строго 36 тиков на всю игру)
ticks = 0             
TICKS_PER_YEAR = 36    

# Флаги разблокировки навыков
listen_unlocked = False
study_eye = False 
crawl_unlocked = False   
babble_unlocked = False  
speech_unlocked = False  # Флаг открытия речи
walk_unlocked = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Вы видите свет. Вы только что родились. Начинается ваш первый год жизни.")

while True:
    print("\n" + "="*40)
    print(f"ВОЗРАСТ: {age_months} мес. (Ход: {ticks}/{TICKS_PER_YEAR})")
    print(f"ОЧКИ РАЗВИТИЯ: {development} pts")
    print(f"ЭНЕРГИЯ (ОД): {ap} / {max_ap}")
    print(f"ПРАКТИКА: Смр: {can_watch}/4 | Крик: {can_speak}/4 | Слух: {can_listen}/4 | Изч: {can_study}/4 | Полз: {can_crawl}/4 | Звуки: {can_babble}/4 | Слова: {can_speech_try}/4")
    print("="*40)

    # --- МЕНЮ ДЕЙСТВИЙ ---
    if ap >= 1:
        print("1 - Смотреть (1 ОД) -> Учит фокусировать взгляд")
        print("2 - Кричать (1 ОД) -> Разрабатывает голос")
    else:
        print("[!] Нет сил на базовые действия. Вы истощены.")
        
    print("3 - Спать (Восстановит ОД)")
    
    if listen_unlocked:
        if ap >= 1: print("4 - Слушать звуки (1 ОД)")
        else: print("[!] 4 - Слушать (Нет ОД)")
        
    if study_eye:
        if ap >= 2: print("5 - Изучать увиденное (2 ОД)")
        else: print("[!] 5 - Изучать увиденное (Нужно 2 ОД)")
        
    if crawl_unlocked:
        if ap >= 3: print("6 - Ползти (3 ОД)")
        else: print("[!] 6 - Ползти (Нужно 3 ОД)")
        
    if babble_unlocked:
        if ap >= 2: print("7 - Агукать и лепетать (2 ОД)")
        else: print("[!] 7 - Агукать (Нужно 2 ОД)")

    if speech_unlocked:
        if ap >= 2: print("9 - Пробовать речь (2 ОД)")
        else: print("[!] 9 - Пробовать речь (Нужно 2 ОД)")    

    if walk_unlocked:
        if ap >= 4: print("8 - СДЕЛАТЬ ПЕРВЫЕ ШАГИ НОЖКАМИ (4 ОД)")
        else: print("[!] 8 - Сделать шаги (Нужно 4 ОД)")

    action = input("> ")
    action_made = False

    # --- ОБРАБОТКА КЛИКОВ ---

    if action == "1" and ap >= 1:
        print("\n[Вы смотрите вокруг. Глаза пытаются зацепиться за контуры.]")
        can_watch += 1       
        development += 1     
        ap -= 1
        action_made = True

    elif action == "2" and ap >= 1:
        print("\n[Вы кричите во все легкие. Мама подбегает и качает вас.]")
        can_speak += 1       
        development += 1
        ap -= 1
        action_made = True

    elif action == "3":
        print("\n[Вы спите. Мозг раскладывает по полочкам полученный за день опыт.]")
        development += 1
        ap = max_ap  
        action_made = True

    elif action == "4" and listen_unlocked and ap >= 1:
        print("\n[Вы затихаете и впитываете звуки родительского голоса.]")
        can_listen += 1      
        development += 1
        ap -= 1
        action_made = True

    elif action == "5" and study_eye and ap >= 2:
        print("\n[Вы сопоставляете форму предметов. Память улучшается.]")
        can_study += 1
        development += 2  
        ap -= 2
        action_made = True

    elif action == "6" and crawl_unlocked and ap >= 3:
        print("\n[Вы толкаетесь коленями и продвигаетесь по ковру. Мышцы растут!]")
        can_crawl += 1
        development += 3  
        ap -= 3
        action_made = True

    elif action == "7" and babble_unlocked and ap >= 2:
        print("\n[Вы складываете губы и выдаете: 'А-гу... Кхх... Ба!']")
        can_babble += 1
        development += 3
        ap -= 2
        action_made = True

    elif action == "9" and speech_unlocked and ap >= 2:
        print("\n[Вы собираетесь с силами, смотрите маме в глаза и четко говорите: 'Ма-ма!']")
        can_speech_try += 1
        development += 4  
        ap -= 2
        action_made = True     

    elif action == "8" and walk_unlocked and ap >= 4:
        print("\n[Вы отрываете руки от дивана и делаете самостоятельные шаги!]")
        development += 5
        ap -= 4
        action_made = True

    else:
        print("\n[Действие недоступно, не хватает ОД или неверный ввод.]")
        continue

    # --- ХОД ВРЕМЕНИ ---
    if action_made:
        ticks += 1
        age_months = ticks // 3 
        
        if ticks >= TICKS_PER_YEAR:
            print("\n" + "★"*60)
            if walk_unlocked:
                print(f" ПОБЕДА! Год подошел к концу. Вам 12 месяцев.\n Вы успешно научились ХОДИТЬ и готовы изучать весь дом! ")
            else:
                print(f" ГОД ПРОШЕЛ... Вам 12 месяцев. Но вы так и не научились ходить.\n Развитие распределено неравномерно. Попробуйте еще раз! ")
            print("★"*60)
            break

# --- СИСТЕМА ЕСТЕСТВЕННОЙ ЭВОЛЮЦИИ (С исправлениями логики) ---

    # 1. Слышать: нужно всего 4 крика
    if can_speak >= 4 and not listen_unlocked:
        print("\n*** ВСПЫШКА: Голос окреп, вы начали различать интонации. Вы научились СЛУШАТЬ! ***")
        listen_unlocked = True

    # 2. Изучать: нужно всего 4 осмотра
    if can_watch >= 4 and not study_eye:
        print("\n*** ВСПЫШКА: Взгляд сфокусировался, картинка стала четкой. Вы научились ИЗУЧАТЬ предметы! ***")
        study_eye = True

    # 3. Агукать: нужно 4 осознанных прослушивания + 15 общего опыта
    if can_listen >= 4 and development >= 15 and not babble_unlocked:
        print("\n*** ВСПЫШКА: Наслушавшись чужой речи, вы пытаетесь ей подражать. Вы научились АГУКАТЬ! ***")
        babble_unlocked = True
        

    # 4. Ползти: ТЕПЕРЬ ЖЕСТКО ТРЕБУЕТ видеть куда ползти!
    # Нужно: Сначала посмотреть по сторонам (4) + Изучить предметы вокруг (4) + 25 опыта
    if can_watch >= 4 and can_study >= 4 and development >= 25 and not crawl_unlocked:
        print("\n*** ВСПЫШКА: Вы видите цель перед собой и изучили комнату. Вы научились ПОЛЗТИ! ***")
        crawl_unlocked = True

    # 5. Речь: ТЕПЕРЬ ЖЕСТКО ТРЕБУЕТ и крик, и слух!
    # Нужно: Наораться (4) + Наслушаться маму (4) + Поагукать (4) + 35 опыта
    if can_speak >= 4 and can_listen >= 4 and can_babble >= 4 and development >= 35 and not speech_unlocked:
        print("\n*** ВСПЫШКА: Связки разработаны криком, слух настроен. Детский лепет перерос в РЕЧЬ! ***")
        speech_unlocked = True


    # 6. Ходьба: Финал года
    if can_crawl >= 4 and can_speech_try >= 4 and development >= 45 and not walk_unlocked:
        print("\n*** ВСПЫШКА: Мышцы ног окрепли от ползания, а мозг через речь готов держать баланс. Вы научились ХОДИТЬ! ***")
        walk_unlocked = True