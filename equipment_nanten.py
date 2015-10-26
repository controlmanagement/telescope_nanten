#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    

------------------------------------------------
[History]

2015/10/20 maruyama

------------------------------------------------
"""

import telescope_nanten.abs
import telescope_nanten.m4
# import telescope_nanten.ac240
# import pymeasure.ondotori
# import pymeasure.lakeshore
# import pymeasure.signal_generator
import pymeasure.weather
# import pymeasure.gps
# import core.file_manager
# import telescope_nanten.ccd
# import pymeasure.power_meter

# ---------- #

#------------------

class hot_load(object):
    
    def __init__(self):
        host = '192.168.100.187'
        port = 5921
        self.l = telescope_nanten.abs.abs_client('192.168.100.187',5921)
        self.l.open()
        pass
    
    def move_r(self):
        self.l.move_r()
        return
    
    def move_sky(self):
        self.l.move_sky()
        return
    
    def move_org(self):
        self.l.move_org()
        return
    
    def get_status(self):
        return self.l.read_pos()
    
    # def insert_status(self):
        # fm = file_manager.file_manager()
        # fm.db_insert()

class m4(object):
    
    def __init__(self):
        host = '192.168.100.187'
        port = 5923
        self.m4 = telescope_nanten.m4.m4_client('192.168.100.187',5923)
        self.m4.open()
        pass
    
    def m4_in(self):
        self.m4.m4_in()
        return

    def m4_out(self):
        self.m4.m4_out()
        return
    
    def get_status(self):
        ret = self.m4.read_pos()
        return ret

    # def insert_status(self):
        # fm = file_manager.file_manager()
        # fm.db_insert()

class weather(object):
    
    def __init__(self):
        # host = '192.168.100.187'
        # port = 5925
        self.weather = pymeasure.weather.weather_controller()
        pass
    
    def get_weather(self):
        ret = self.weather.get_weather()
        return ret

