from Wallet import *


def run():
    filename = "financial_records.txt"
    tracker = Wallet(filename)
    tracker.load_entries()
    tracker.update_balance()

    while True:
        print("Меню:")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Поиск по записям")
        print("4. Выход")
        choice = input("Выберите действие: ")

        match choice:
            case "1":
                print(f"\nТекущий баланс: {tracker.balance}")
                income, expenses = tracker.get_income_and_expenses()
                print(f"Доход: {income}\n"
                      f"Расход: {expenses}")
                print("\n")

            case "2":
                category = input("Введите категорию (Доход/Расход) или оставьте пустым: ")
                while True:
                    amount = input("Введите сумму или оставьте пустым: ")
                    if amount == "":
                        amount = 0
                        break
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print("Некорректное значение. Введите число или оставьте поле пустым.")

                description = input("Введите описание: ")
                tracker.add_entry(category, amount, description)
                tracker.change_balance(category, amount)
                print("Запись добавлена.")

            case "3":
                category = input("Введите категорию (Доход/Расход) или оставьте пустым: ")
                date = input("Введите дату (гггг-мм-дд) или оставьте пустым: ")
                while True:
                    amount = input("Введите сумму или оставьте пустым: ")
                    if amount == "":
                        break  # Оставить сумму пустой, если ввод пустой
                    try:
                        amount = float(amount)
                        break  # Прервать цикл, если введено корректное числовое значение
                    except ValueError:
                        print("Некорректное значение. Введите число или оставьте поле пустым.")
                results = tracker.search_entries(category, date, amount)
                if results:
                    print("\nРезультаты поиска:")
                    for entry in results:
                        for key, value in entry.items():
                            print(f"{key}: {value}")
                        print()
                else:
                    print("Ничего не найдено.")

            case "4":
                print("До свидания!")
                break

            case _:
                print("Некорректный ввод. Пожалуйста, выберите действие из меню.")
