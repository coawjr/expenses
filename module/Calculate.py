import sys
sys.path.insert(1,'/Users/yashiroyuushi/Desktop/expenses/module')
from Icome import Icome
from Expenses_fixed import Expenses_fixed
from Expenses_variable import Expenses_variable

class Calculate():

    ary_icome = Icome.get_icome()
    ary_expenses_fixed = Expenses_fixed.get_expenses_fixed()
    ary_expenses_variable = Expenses_variable.get_expenses_variable()
    
    saving = sum(ary_icome) - (sum(ary_expenses_fixed) + sum(ary_expenses_variable))

    print(saving)
