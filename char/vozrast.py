# --- ВОЗРАСТ И ЭТАПЫ ЖИЗНИ ---

if age_years < 3:
    stage = "Младенчество"

elif age_years < 6:
    stage = "Детский сад"

elif age_years < 18:
    stage = "Школа"

elif age_years < 23:
    stage = "ВУЗ"

elif age_years < 65:
    stage = "Работа"

else:
    stage = "Старость"

print(f"Возраст: {age_years}")
print(f"Этап жизни: {stage}")