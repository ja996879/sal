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
          
          worksheet = workbook.add_worksheet('pg1')


          worksheet.set_column('A:D', 15)
          xa = Sql3()
          xa_all = xa.s_sql("select * from det_time as d inner join users as u on u.id=user_id  where (w_time between '2017-04-01' and '2017-04-30') order by  user_id")
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
      xa.del_con()
      
   def per_excel(self):
      xa = Sql3()
      xf = FDate()
      row_x_start=0
      row_y_start=0
      workbook = xlsxwriter.Workbook("C:\\Users\\%s\\Desktop\\%sprduct.xlsx" % (self.us,'b4597'))
      worksheet = workbook.add_worksheet('b4597')
      worksheet.set_column('A:D', 15)
      xu_num = xa.s_sql("select id from users where name = 'b4597'")
      for xu_n in xu_num:
         xu_number=xu_n[0]
      xu_per_information = xa.s_sql("select w_time,off_time from det_time where user_id = %s and (w_time between '2017-04-01' and '2017-04-30')" %(xu_number))
      for xu_det in xu_per_information: 
         print(round(xf.date_less(xu_det[0],xu_det[1])/60))
         worksheet.write(row_x_start,row_y_start,xu_det[0])
         worksheet.write(row_x_start,row_y_start+1,xu_det[1])
         worksheet.write(row_x_start,row_y_start+2,round(xf.date_less(xu_det[0],xu_det[1])/60))
         row_x_start += 1
      workbook.close()
      xa.del_con()
      
   def some_excel(self):
      xa = Sql3()
      u_dict = {}
      xu_all = xa.s_sql("select * from users")
      for xu_dict in xu_all:
         u_dict[xu_dict[1]] = xu_dict[0]
      for k,v in u_dict.items():
         print("Key : %s, Value : %s" %(k, v))
         #xu_total_information = xa.s_sql("")
   
xb=EXport_excel() 
xb.some_excel()     

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
