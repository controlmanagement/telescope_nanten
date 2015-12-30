#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    

------------------------------------------------
[History]

2015/12/16 maruyama

------------------------------------------------
"""

import telescope_nanten.abs
import telescope_nanten.m4
import telescope_nanten.ac240
import telescope_nanten.antenna_nanten_controller
#import pymeasure.weather

# ---------- #

class antenna(object):
    
    def __init__(self):
        host = '172.20.0.11'
        port = 8003
        self.antenna = telescope_nanten.antenna_nanten_controller.antenna_client(host, port)
        pass
    """
    def drive_on(self):
    """


class hot_load(object):
    
    def __init__(self):
        host = '172.20.0.12'
        port = 6001
        self.l = telescope_nanten.abs.abs_client(host, port)
        pass
    
    def move_r(self):
        self.l.move_r()
        return
    
    def move_sky(self):
        self.l.move_sky()
        return

    def stop(self):
        self.l.stop()
        return

    def get_status(self):
        ret = self.l.get_pos()
        return ret

    # def insert_status(self):
        # fm = file_manager.file_manager()
        # fm.db_insert()

class m4(object):
    
    def __init__(self):
        host = '172.20.0.12'
        port = 6003
        self.m4 = telescope_nanten.m4.m4_client(host, port)
        pass
    
    def m4_in(self):
        self.m4.m4_in()
        return

    def m4_out(self):
        self.m4.m4_out()
        return

    def stop(self):
        self.m4.stop()
        return

    def get_status(self):
        ret = self.m4.get_pos()
        return ret

    # def insert_status(self):
        # fm = file_manager.file_manager()
        # fm.db_insert()


class dfs(object):
    
    def __init__(self):
        host_dfs01 = '172.20.0.41'
        port_dfs01 = 52700
        host_dfs02 = '172.20.0.43'
        port_dfs02 = 52701
        self.dfs01 = telescope_nanten.ac240.ac240(host_dfs01, port_dfs01)
        self.dfs02 = telescope_nanten.ac240.ac240(host_dfs02, port_dfs02)
        self.dfs01.open()
        self.dfs02.open()
        pass
    
    def oneshot_dfs01(self, repeat=1, integsec=1.0, starttime=0.0):
        self.dfs01.getspectrum(repeat, integsec, starttime)
        data = self.dfs01.getdata()
        return data
    
    def oneshot_dfs02(self, repeat=1, integsec=1.0, starttime=0.0):
        self.dfs02.getspectrum(repeat, integsec, starttime)
        data = self.dfs02.getdata()
        return data


class read_status(object):
    
    def __init__(self):
        """
        opt_host = '172.20.0.12'
        l_m_port = 6002
        m4_m_port = 6004
        self.l_m = telescope_nanten.abs.abs_monitor_client(opt_host, l_m_port)
        self.m4_m = telescope_nanten.m4.m4_monitor_client(opt_host, m4_m_port)        
        self.weather = pymeasure.weather.weather_controller()
        """
        ctrl_host = '172.20.0.11'
        enc_port = 8002
        antenna_port = 8004
        self.enc = telescope_nanten.antenna_enc.enc_monitor_client(ctrl_host, enc_port)
        self.antenna = telescope_nanten.antenna_nanten_controller.antenna_monitor_client(ctrl_host, antenna_port)
        pass
    """
    def get_beam(self):
        load_status = self.l_m.read_pos()
        m4_status = self.m4_m.read_pos()
        return [load_status, m4_status]
    
    def get_weather(self):
        ret = self.weather.get_weather()
        return ret
    """
    
    def get_antenna(self):
        enc = self.enc.read_azel()
        target = self.antenna.read_targetazel()
        #track = self.antenna.read_track()
        #error = self.antenna.read_error()
        #velocity = self.antenna.read_v()
        #return [enc[0], enc[1], target[0], target[1], track[0], track[1], error[0], error[1], error[2], error[3], velocity[0], velocity[1]]
        return [enc[0], enc[1], target[0], target[1]]
    


