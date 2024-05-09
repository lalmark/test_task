import datetime
import os
import json
from Entry import *


class Wallet:
    filename: str
    initial_balance: float
    initial_entries: List[Entry]

    def __init__(self, filename: str, initial_balance: float = 0,
                 initial_entries: List[Entry] = []) -> None:
        """ initialization of variables
            Args:
                - filename: file name
                -initial_balance: initial wallet balance
                - Entry: records like date: str, category: str, amount: float, description: str
        """

        self.filename = filename
        self.__balance = initial_balance
        self.entries = initial_entries

    @property
    def balance(self) -> float:
        """ Get balance
                return: balance: float
        """
        return self.__balance

    def load_entries(self) -> None:
        """ loads data from a file into an Entry object
                execept: if the file is missing
        """
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    entries_data = json.load(file)
                    self.entries = [Entry(entry['Date'], entry['Category'], entry['Summ'], entry['Description']) for
                                    entry in entries_data]
            else:
                print(f"Файл {self.filename} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при открытии файла: {self.filename}")

    def update_balance(self) -> None:
        """ reads the existing balance in the file
        """
        for entry in self.entries:
            category = entry.category
            amount = entry.amount
            self.__change(category, amount)

    def save_entries(self) -> None:
        """ saves descriptions to file
        """
        entries_as_dicts = [entry.to_dict() for entry in self.entries]
        with open(self.filename, 'w') as file:
            json.dump(entries_as_dicts, file, indent=4, ensure_ascii=False)

    def __change(self, category: str, amount: float) -> None:
        """ changes balance after adding entries
            Args:
                - category: income or expense
                - amount: amount of income or expense
        """
        if category == "Расход":
            self.__balance -= float(amount)
        elif category == "Доход":
            self.__balance += float(amount)

    def add_entry(self, category: str, amount: float, description: str) -> None:
        """ adds entry to entriese
               """
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        entry = Entry(date, category, amount, description)
        self.entries.append(entry)
        self.save_entries()

    def get_income_and_expenses(self) -> Tuple[float, float]:
        """ calculation of income and losses
                       """

        total_income = 0
        total_expenses = 0

        for entry in self.entries:
            if entry.category == "Доход":
                total_income += entry.amount
            elif entry.category == "Расход":
                total_expenses += entry.amount

        return total_income, total_expenses

    def change_balance(self, category: str, amount: float | str) -> None:
        self.__change(category, amount)

    def search_entries(self, category: Optional[str] = None, date: Optional[str] = None,
                       amount: Optional[float] = None) -> List[Entry]:
        results: List[Entry] = []
        """ searching for events from a file
         Args:
                - category: income or expense
                - date: record creation date
                - amount: amount of replenishment or expense
        return:
                - dList[Entry]: found records by criteria
                       """
        for entry in self.entries:
            if (not category or entry.category == category) and \
                    (not date or entry.date == date) and \
                    (not amount or entry.amount == float(amount)):
                results.append(entry.to_dict())
        return results
