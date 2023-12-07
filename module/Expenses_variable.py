class Expenses_variable:
    allowance = int(0)
    expenses_food = int(0)
    expenses_comunication = int(0)
    nest_egg = int(0)
    loan = int(0)

    def set_expenses_variable():
        Expenses_variable.allowance = int(input('allowance'))
        Expenses_variable.expenses_food = int(input('expenses_food'))
        Expenses_variable.expenses_comunication = int(input('expenses_comunication'))
        Expenses_variable.nest_egg = int(input('nest_egg'))
        Expenses_variable.loan = int(input('loan'))
    
    def get_expenses_variable():
        return(str(Expenses_variable.allowance),
        str(Expenses_variable.expenses_food),
        str(Expenses_variable.expenses_comunication),
        str(Expenses_variable.nest_egg),
        str(Expenses_variable.loan))