# coding=UTF-8
import os
import xlsxwriter
from datetime import datetime
from con_sql import Sql3
class EXport_excel:
    
   def __init__(self):
       self.today_dt = datetime.now().strftime('%Y-%m')
       self.us = os.getlogin()
          
   def w_excel(self):       
       #pattern = re.compile(r"%s" %(self.today_dt))
       #if os.path.exists("C:\\Users\\%s\\Desktop\\%s.xlsx"):
          workbook = xlsxwriter.Workbook("C:\\Users\\%s\\Desktop\\%sprduct.xlsx" % (self.us,self.today_dt))
          
          worksheet = workbook.add_worksheet()


          worksheet.set_column('A:D', 10)
   
xa=Sql3()
xa_all=xa.s_sql("select ")
       
      

'''
from datetime import datetime
import os
import re
# 編譯成 Pattern 對象
pattern = re.compile(r'hello\(\d\)')
 
# 取得匹配結果，無法匹配返回 None
match = pattern.match('hello(5)')
 
if match:
    # 得到匹配結果
    print(match.group())
print(match)
if os.path.exists("C:\\PRy.ico"):
    print("True")
else:
    print("False")
'''
