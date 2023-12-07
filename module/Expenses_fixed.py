class Expenses_fixed:
    cost_lent = int(0)
    cost_utility = int(0)

    def set_expenses_fixed():
        Expenses_fixed.cost_lent = int(input('cost_lent'))
        Expenses_fixed.cost_utility = int(input('cost_utility'))

    def get_expenses_fixed():

        return (str(Expenses_fixed.cost_lent), str(Expenses_fixed.cost_utility))