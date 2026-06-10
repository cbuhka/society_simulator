import time
#тестовый экзамен
exam_question = "1+2=?"

exam_answers = [
    "2",
    "3",
    "4"
]

exam_correct = 2
# --- ТЕСТОВАЯ ЛЕКЦИЯ ---
lesson_text = "1+2=3"

# --- ШКОЛА ---
print("\n=== ДОБРО ПОЖАЛОВАТЬ В ШКОЛУ! ===")


for school_years in range(1, 13):

    print(f"\n=== КЛАСС {school_years} ===")

    for week in range(1, 5):

        print(f"\n--- НЕДЕЛЯ {week} ---")

        for lesson in range(1, 5):

            print(f"\nУРОК {lesson}")
            print(lesson_text)

            time.sleep(2)

        # --- ОЦЕНКИ ---
        if week == 2:
            print("\n=== ОЦЕНКИ ===")
            input("Нажмите Enter...")

        # --- ЭКЗАМЕН ---
        if week == 4:

            print("\n=== ЭКЗАМЕН ===")
            print(exam_question)

            for i, answer in enumerate(exam_answers, 1):
                print(f"{i}) {answer}")

            choice = input("> ")

            if choice == str(exam_correct):
                print("Верно")
            else:
                print("Неверно")

            input("Нажмите Enter...")

print("\n!!! ШКОЛА ОКОНЧЕНА !!!")