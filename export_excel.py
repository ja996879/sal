# coding=UTF-8
import os
import xlsxwriter
from datetime import datetime
from con_sql import Sql3
from date import FDate
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
          xa = Sql3()
          xa_all=xa.s_sql("select * from det_time as d inner join users as u on   u.id=user_id")
          xf = FDate()
          
          for row in xa_all:
             if (row[2]!=None and row[3]!=None):
               print(row[2])
               print(row[3])
               print(round(xf.date_less(row[2],row[3])/60))
             else:
               print("nocheck")
#xa=Sql3()
#xa_all=xa.s_sql("select ")
xb=EXport_excel()      
xb.w_excel()     

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
計算每月最大天數
import calendar
monthRange = calendar.monthrange(2017,3)
print(monthRange)

'''
