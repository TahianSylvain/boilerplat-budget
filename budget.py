class Category:
    """ Une classe qui cherche les dépenses and les cases dans une catégorie"""

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=""):
        if self.get_balance() >= amount:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.get_balance() >= amount:
            self.ledger.append({"amount": -amount,
                                "description": f"Transfer to {destination.name}"})
            destination.ledger.append({"amount": amount,
                                       "description": f"Transfer from {self.name}"})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        output = f"*************{self.name}*************\n"
        for transaction in self.ledger:
            amount = format(transaction["amount"], ".2f")
            output += f"{transaction['description']:20} {amount:10}\n"
        output += f"Total: {self.get_balance():.2f}\n"
        return output

def create_spend_chart(categories: list[Category]):
    total_expenses = 0
    for category in categories:
        total_expenses += category.get_balance()

    percentages = []
    for category in categories:
        percentage = category.get_balance() / total_expenses * 100
        percentages.append(percentage)

    chart = "Percentage spent by category\n"

    scaled_percentages = [int(p * 10) for p in percentages]

    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for j, scaled_percentage in enumerate(scaled_percentages):
            if i <= scaled_percentage:
                chart += " o "
            else:
                chart += "   "
        chart += "\n"

    chart += "   ----------\n"
    for category in categories:
        chart += f"    {category.name[0]} "
    chart += "\n    u "
    for category in categories:
        chart += f"{category.name[1]} "
    chart += "\n    s "
    for category in categories:
        chart += f"{category.name[2]} "
    chart += "\n    i "
    for category in categories:
        chart += f"{category.name[3]} "
    chart += "\n    n    r "
    for category in categories:
        if len(category.name) > 4:
            chart += f"{category.name[4]} "
        else:
            chart += " "
    chart += "\n        t "
    for category in categories:
        if len(category.name) > 5:
            chart += f"{category.name[5]} "
        else:
            chart += " "
    chart += "\n        a "
    for category in categories:
        if len(category.name) > 6:
            chart += f"{category.name[6]} "
        else:
            chart += ""
            
    return chart