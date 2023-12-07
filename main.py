import sys
from DAO import expensesDAO
from DBcon import Setter

class main:

    def set_DB():
        print('DBの内容を変えるの？')
        check1 = 0
        sql = 'A'
        while check1 != 2:
            check1 = int(input('1.yes 2.no '))

            if check1 == 1:
                st = Setter.Setter()
                print(st)
                sql = st.set_sql()

                if sql != 'A':
                    check2 = 0
                    print('これimportするの？')
                    print(sql)
                    check2 = int(input('1.yes 2.no '))

                    if check2 == 1 :
                        ex = expensesDAO.expensesDAO()
                        ex.insert_sql(sql)

                    else: 
                        print('byebye!')
                print('他にも修正するものあるの？')
            
            else:
                check1 = 2
                print('byebye!')

    set_DB()








        