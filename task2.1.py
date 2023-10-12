def bank(a, years, interest_rate):
    total_amount = a
    try:
        for _ in range(years):
            total_amount += total_amount * interest_rate
        return total_amount
    except (TypeError, ValueError):
        print("Ошибка вводи числа.")
        return None
try:
    initial_deposit = float(input("Введите начальную сумму вклада: "))
    investment_years = int(input("Введите количество лет: "))
    annual_interest_rate = float(input("Введите годовую процентную ставку (в долях, например, 0.10 для 10%): "))
    
    final_amount = bank(initial_deposit, investment_years, annual_interest_rate)
    if final_amount is not None:
        print("Итоговая сумма на счету пользователя после", investment_years, "лет:", final_amount)
except ValueError:
    print("Ошибка вводи числа")
