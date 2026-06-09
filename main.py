import os
import random

# --- ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ---
stats = {"STR": 1, "AGI": 1, "INT": 1, "VIT": 1, "DEX": 1, "LCK": 1, "SOC": 1}

age_months = 0
age_years = 0

development = 0

max_ap = 10
ap = 10

ticks = 0
TICKS_PER_YEAR = 36

school_class = 1
library_level = 0
exam_time = 5

counters = {"smotret": 0, "krik": 0, "sluh": 0, "uchit": 0, "polzat": 0, "zvuki": 0, "rech_try": 0}

skills = {"sluh": False, "vzglyad": False, "polzat": False, "agukat": False, "rech": False, "hodit": False}

school_actions = {
    "study": 0,
    "sport": 0,
    "social": 0
}

school_skills = {
    "alphabet": False,
    "social": False,
    "reading": False,
    "writing": False
}
#детский сад
phases = [
    "Учеба",
    "Еда",
    "Свободное время",
    "Сон",
    "Учеба",
    "Свободное время",
    "Дом"
]
#школа
school_phases = [
    "Урок",
    "Перемена",
    "Урок",
    "Перемена",
    "Урок",
    "Дом"
]
# --- ПРЕДМЕТЫ ПО КЛАССАМ ---
school_subjects = {
    1: ["Математика", "Языки", "Спорт"],
    2: ["Математика", "Языки", "Спорт"],
    3: ["Математика", "Языки", "Спорт"],

    4: ["Математика", "Языки", "Общество", "Творчество", "Наука", "Спорт", "Технологии"],
    5: ["Математика", "Языки", "Общество", "Творчество", "Наука", "Спорт", "Технологии"],
    6: ["Математика", "Языки", "Общество", "Творчество", "Наука", "Спорт", "Технологии"],

    7: ["Математика", "Языки", "Общество", "Биология", "История", "География", "Спорт", "Технологии"],
    8: ["Математика", "Языки", "Общество", "Биология", "История", "География", "Физика", "Химия", "Спорт", "Технологии"],
    9: ["Математика", "Языки", "Общество", "Биология", "История", "География", "Физика", "Химия", "Инженерия", "Спорт", "Технологии"],

    10: ["Математика", "Языки", "История", "География", "Физика", "Химия", "Биология", "Программирование", "Спорт"],
    11: ["Математика", "Языки", "История", "География", "Физика", "Химия", "Биология", "Программирование", "Спорт"],
    12: ["Проект", "Углублённый предмет 1", "Углублённый предмет 2", "Углублённый предмет 3"]
}

current_phase_index = 0
day_count = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ИНИЦИАЛИЗАЦИЯ ---
clear_screen()

#НЕПОСРЕДСТВЕННО ИГРА
exec(open("mir.py", encoding="utf-8").read())

print("Вы видите свет. Вы только что родились.")
print("1 - Обычная игра | 2 - Пропустить младенчество | 3 - ДЕБАГ: В ШКОЛУ")
vybor_rezhima = input("> ")

if vybor_rezhima == "2":
    ticks = TICKS_PER_YEAR; development = 50 
    for key in counters: counters[key] = 5
    for key in skills: skills[key] = True
elif vybor_rezhima == "3":
    ticks = TICKS_PER_YEAR
    for key in skills:
        skills[key] = True
    stats = {"STR": 5, "AGI": 5, "INT": 5, "VIT": 5, "DEX": 5, "LCK": 5, "SOC": 5}

# --- МЛАДЕНЧЕСТВО ---
exec(open("mlad.py", encoding="utf-8").read())

# --- ДЕТСКИЙ САД ---
exec(open("sad.py", encoding="utf-8").read())

# --- БОНУСЫ ИЗ ДЕТСТВА ---

stats["INT"] += counters["smotret"] // 2
stats["INT"] += counters["sluh"] // 2
stats["INT"] += counters["krik"] // 4

stats["AGI"] += counters["smotret"] // 3
stats["AGI"] += counters["uchit"] // 2
stats["AGI"] += counters["polzat"] // 2

stats["STR"] += counters["polzat"] // 2
stats["VIT"] += counters["polzat"] // 2

stats["SOC"] += counters["rech_try"] // 2
stats["SOC"] += counters["zvuki"] // 2
stats["SOC"] += counters["sluh"] // 4

age_years = 6
school_class = 1

# --- ТЕСТОВАЯ ЛЕКЦИЯ ---
lesson_text = "1+2=3"

# --- ТЕСТОВЫЙ ЭКЗАМЕН ---
exam_question = "1+2=?"

exam_answers = [
    "2",
    "3",
    "4"
]

exam_correct = 2

# --- ШКОЛА ---
exec(open("shkol.py", encoding="utf-8").read())
#ВУЗ
exec(open("vuz.py", encoding="utf-8").read())
#работа
exec(open("rabota.py", encoding="utf-8").read())
#развлечения
exec(open("razvlek.py", encoding="utf-8").read())
#курсы
exec(open("kursi.py", encoding="utf-8").read())
#семья
exec(open("semja.py", encoding="utf-8").read())
#возраст
exec(open("vozrast.py", encoding="utf-8").read())