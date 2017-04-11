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
       
          workbook = xlsxwriter.Workbook("C:\\Users\\%s\\Desktop\\%sprduct.xlsx" % (self.us,self.today_dt))
          
          worksheet = workbook.add_worksheet()


          worksheet.set_column('A:D', 15)
          xa = Sql3()
          xa_all = xa.s_sql("select * from det_time as d inner join users as u on u.id=user_id order by  user_id")
          xf = FDate()

          
          row_u_name = 0
          row_time = 1
         
          for row in xa_all:
             if (row[2]!=None and row[3]!=None):
               worksheet.write(row_u_name,0,row[7])
               worksheet.write(row_u_name,row_time,row[1])
               worksheet.write(row_u_name,row_time+1,row[2])
               worksheet.write(row_u_name,row_time+2,row[3])
               worksheet.write(row_u_name,row_time+3,round(xf.date_less(row[2],row[3])/60))
               row_u_name += 1
               #print(round(xf.date_less(row[2],row[3])/60))
             else:
               print("nocheck")
          #xu_all = xa.s_sql("select * from det_time")
          workbook.close()
          xa.del_con()
   def total_excel(self):
      
      user_list=[]
      t_list=[]
      user_name=[]
      det_user={}
      
      xf = FDate()
      xa = Sql3()
      xu_all = xa.s_sql("select * from users")
      
      num_user = 0
      for row_u in xu_all:
         user_list.append(row_u[0])
         user_name.append(row_u[1])
         
      for row_sql in user_list:
         t_time_all = 0
         xut_all=xa.s_sql("select * from det_time where (w_time between '2017-04-01' and '2017-04-30') and user_id=%s" %(row_sql))
         
         for t_total in xut_all:
            if (t_total[2]!=None and t_total[3]!=None):
               t_time_all += round(xf.date_less(t_total[2],t_total[3])/60)
         t_list.append(t_time_all)
         det_user[user_name[num_user]] = t_time_all
         num_user += 1
      print(t_list)
      print(det_user)

      
   def per_excel(self):
      pass

xb=EXport_excel()      
xb.total_excel()     

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
