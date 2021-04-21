
revenue = int(input("Введите размер выручки: "))
losses = int(input("Введите размер издержек: "))

if revenue > losses:
    employees = int(input("Введите общее количество сотрудников: "))
    profit = int(revenue) - int(losses)
    margin = revenue/profit
    profit_per_employee = profit/employees

    print(f"Ваша компания прибыльна, выручка больше издержек!, Рентабельность выручки - {margin} %, прибыль фирмы в "
          f"расчёте на одного сотрудника {profit_per_employee}")
else:
    print("Ваша компания убыточна, издержки слишком велики!")