#print(86400-ad.seconds)
#86400 a day total
from datetime import datetime
class FDate:
    
    def date_analyst(self,date_str):
        date_str = date_str.replace(':','-')
        date_str = date_str.replace(' ','-')
        
        y_str,m_str,d_str,h_str,mi_str,sec_str = date_str.split('-')
        date_model=datetime(int(y_str),int(m_str),int(d_str),int(h_str),int(mi_str),int(sec_str))
        
        return date_model
    
    def date_plus(self):
        pass
    
    def date_less(self,t_date,a_date):
        t_a_date = self.date_analyst(t_date)
        a_a_date = self.date_analyst(a_date)
        d_less = (a_a_date-t_a_date).seconds
        #total seconds
        #print(round(d_less/60))
        #ceil < up   down < floor 4-5++ < round
        return d_less
    
    def date_now(self,now_date):
        if(now_date=='1'):
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif(now_date=='2'):
            return datetime.now().strftime('%Y-%m-%d %H:%M')
        elif(now_date=='3'):
            return datetime.now().strftime('%Y-%m-%d')

#x=FDate()
#x.date_less('2014-10-25 09:00:00','2014-10-25 10:05:00')
