import datetime

class Transformer():
    
    def __init__(self):
        return None
    
    def result_interpreter(self,play):  
        plays=[('Pass',0),('Run',1),('Punt',2),('Field Goal',3)]
        result_=None
        for i in range(len(plays)):
            if play == plays[i][1]:
                result_=plays[i][0]
        return result_

    def play_interpreter(self,play):  
        plays=[('pass',0),('run',1),('punt',2),('fieldGoal',3)]
        result_=None
        for i in range(len(plays)):
            if play == plays[i][0]:
                result_=plays[i][1]
        return result_

    def quarter_interpreter(self,quarter):  
        quarters=[('q1',1),('q2',2),('q3',3),('q4',4)]
        result_=None
        for i in range(len(quarters)):
            if quarter==quarters[i][0]:
                result_=quarters[i][1]
        return result_

    def down_interpreter(self,dwn):  
        downs=[('d1',1),('d2',2),('d3',3),('d4',4)]
        result_=None
        for i in range(len(downs)):
            if downs[i][0]==dwn:
                result_=downs[i][1]
        return result_
   

    def time_converter(self,time_string,quart):
        index=[(4,0),(3,900),(2,1800),(1,2700)]
        (m,s) = time_string.split(':')
        residual = float(m)*60+float(s)
        for i in range(len(index)):
            if quart == index[i][0]:
                primary=index[i][1]
                remaining=residual+primary
        return float(remaining)
