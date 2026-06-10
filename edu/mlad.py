# --- МЛАДЕНЧЕСТВО ---

while ticks < TICKS_PER_YEAR:
print(f"\nВОЗРАСТ: {age_months} мес.")

```
action = input(
    "1-Смотреть, 2-Кричать, 4-Слушать, 5-Изучать, 6-Ползти, 7-Агукать > "
)

action_made = False

if action == "1":
    counters["smotret"] += 1
    action_made = True

elif action == "2":
    counters["krik"] += 1
    action_made = True

elif action == "4" and skills["sluh"]:
    counters["sluh"] += 1
    action_made = True

elif action == "5" and skills["vzglyad"]:
    counters["uchit"] += 1
    action_made = True

elif action == "6" and skills["polzat"]:
    counters["polzat"] += 1
    action_made = True

elif action == "7" and skills["agukat"]:
    counters["zvuki"] += 1
    action_made = True

if action_made:
    ticks += 1
    age_months = ticks // 3

# РЕЧЬ

if counters["krik"] >= 4 and not skills["sluh"]:
    skills["sluh"] = True
    print("\nВы начинаете различать звуки.")

if counters["sluh"] >= 4 and not skills["agukat"]:
    skills["agukat"] = True
    print("\nВы начинаете агукать.")

if counters["zvuki"] >= 4 and not skills["rech"]:
    skills["rech"] = True
    print("\nПоздравляем! Вы произносите первые слова!")

# ХОДЬБА

if counters["smotret"] >= 4 and not skills["vzglyad"]:
    skills["vzglyad"] = True
    print("\nВаш взгляд становится осознанным.")

if counters["uchit"] >= 4 and not skills["polzat"]:
    skills["polzat"] = True
    print("\nВы научились ползать.")

if counters["polzat"] >= 4 and not skills["hodit"]:
    skills["hodit"] = True
    print("\nПоздравляем! Вы сделали первый шаг!")
```

# --- КОНЕЦ МЛАДЕНЧЕСТВА ---

if not skills["hodit"] and not skills["rech"]:
print("GAME OVER")
print("Вы не научились ходить и говорить.")

elif not skills["hodit"]:
print("GAME OVER")
print("Вы не научились ходить.")

elif not skills["rech"]:
print("GAME OVER")
print("Вы не научились говорить.")

else:
print("Вы готовы к детскому саду.")
