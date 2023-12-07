import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import Icome
from module import Expenses_fixed
from module import Expenses_variable

class Setter:
    def __init__(self):
        self.check = 99
        self.sql = 'A'
        self.set_sql()

    def set_sql(self):
         print('何修正するの')
         
         self.check = int(input('1.icome 2.variable 3.fixed 4.cancel '))
         if self.check == 1:
            self.setter_icome()
            return(self.sql)
         
         elif self.check == 2:
            self.setter_expenses_variable()
            return(self.sql)

         elif self.check == 3:
              self.setter_expenses_fixed()   
              return(self.sql)
              
         else:
             print('byebye！')
             return('A')

    def setter_icome(self):
        income = Icome.Icome
        income.set_icome()
        income_ary = income.get_icome()
        self.sql = "insert into icome values(lpad(no,7,'0'),"+income_ary[0]+","+income_ary[1]+");"

    def setter_expenses_variable(self):
        variable = Expenses_variable.Expenses_variable
        variable.set_expenses_variable()
        variable_ary = variable.get_expenses_variable()
        self.sql = "insert into expenses_variable values(lpad(no,7,'0'),"+variable_ary[0]+","+variable_ary[1]+","+variable_ary[2]+","+variable_ary[3]+","+variable_ary[4]+");"

    def setter_expenses_fixed(self):
        fixed = Expenses_fixed.Expenses_fixed
        fixed.set_expenses_fixed()
        fixed_ary = fixed.get_expenses_fixed()
        self.sql = "insert into expenses_fixed values (lpad(no,7,'0'),"+fixed_ary[0]+","+fixed_ary[1]+");"
        print(self.sql)