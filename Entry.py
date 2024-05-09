from typing import List, Tuple, Dict, Optional, Union


class Entry:
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self) -> Dict[str, Union[str, float]]:
        return {
            'Date': self.date,
            'Category': self.category,
            'Summ': self.amount,
            'Description': self.description
        }
