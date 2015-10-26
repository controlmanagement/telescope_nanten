#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    condition_nanten(core.controller.condition): 
        
------------------------------------------------
[History]

2015/10/20 maruyama

------------------------------------------------
"""
import core.controller

class condition_nanten(core.controller.condition):
    """weatherの取得制御を行う"""
    def __init__(self):
        import telescope_nanten.equipment_nanten
        self.weather = telescope_nanten.equipment_nanten.weather()
        pass
    
    def get_status(self):
        """weather,を取得する"""
        ret = self.weather.get_weather()
        weather = {"Year" : ret[0],
                   "Month" : ret[1],
                   "Day" : ret[2],
                   "Hour" : ret[3],
                   "Min" : ret[4],
                   "Sec" : ret[5],
                   "InTemp" : ret[6],
                   "OutTemp" : ret[7],
                   "InHumi" : ret[8],
                   "OutHumi" : ret[9],
                   "WindDir" : ret[10],
                   "WindSp" : ret[11],
                   "Press" : ret[12],
                   "Rain" : ret[13],
                   "CabinTemp[1,2]" : [ret[14],ret[15]],
                   "DomeTemp[1,2]" : [ret[16],ret[17]],
                   "GenTemp[1,2]" : [ret[18],ret[19]]
                   }
        return weather


