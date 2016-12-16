#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    

------------------------------------------------
[History]


------------------------------------------------
"""

import telescope_nanten.abs
import telescope_nanten.m4
import telescope_nanten.m2
import telescope_nanten.ac240
import telescope_nanten.antenna_nanten_controller
import telescope_nanten.antenna_enc
import telescope_nanten.dome
import pymeasure.weather

import threading
# ---------- #

class thread(threading.Thread):
    ret = None
    
    def __init__(self, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        pass
    
    def run(self):
        self.ret = self._Thread__target(self._Thread__args)
        return
    
    def get(self):
        return self.ret

def tmap(funcs, args):
    th = [thread(target=_f, args=_a) for _f, _a in zip(funcs, args)]
    [t.start() for t in th]
    [t.join() for t in th]
    ret = [t.ret for t in th]
    return ret

# ---------- #


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

class m2(object):
    
    def __init__(self):
        host = '172.20.0.12'
        port = 9999
        self.m2 = telescope_nanten.m2.m2_client(host, port)
        pass
    
    def m2_move(self, dist):
        self.m2.move(dist)
        return


    def get_status(self):
        ret = self.m2.get_pos()
        return ret

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
        if type(repeat) == tuple:
            starttime = repeat[2]
            integsec = repeat[1]
            repeat = repeat[0]
            pass
        
        self.dfs01.getspectrum(repeat, integsec, starttime)
        data = self.dfs01.getdata()
        return data
    
    def oneshot_dfs02(self, repeat=1, integsec=1.0, starttime=0.0):
        if type(repeat) == tuple:
            starttime = repeat[2]
            integsec = repeat[1]
            repeat = repeat[0]
            pass
        
        self.dfs02.getspectrum(repeat, integsec, starttime)
        data = self.dfs02.getdata()
        return data
    
    def oneshot(self, repeat=1, integsec=1.0, starttime=0.0):
        arg = (repeat, integsec, starttime)
        args = (arg, arg)
        funcs = (self.oneshot_dfs01, self.oneshot_dfs02)
        data = tmap(funcs, args)
        return data

class read_status(object):
    
    def __init__(self):
        
        opt_host = '172.20.0.12'
        l_m_port = 6002
        m4_m_port = 6004
        m2_m_port = 9998
        self.l_m = telescope_nanten.abs.abs_monitor_client(opt_host, l_m_port)
        self.m4_m = telescope_nanten.m4.m4_monitor_client(opt_host, m4_m_port)
        self.m2_m = telescope_nanten.m2.m2_monitor_client(opt_host, m2_m_port)
        
        ctrl_host = '172.20.0.11'
        enc_port = 8002
        antenna_port = 8004
        domepos_port = 8006
        dome_port = 8008
        weather_port = 3002
        self.enc = telescope_nanten.antenna_enc.enc_monitor_client(ctrl_host, enc_port)
        self.tel = telescope_nanten.antenna_nanten_controller.antenna_monitor_client(ctrl_host, antenna_port)
        self.dome = telescope_nanten.dome.dome_monitor_client(ctrl_host, dome_port)
        self.weather = pymeasure.weather.weather_monitor_client(ctrl_host, weather_port)
        pass
    
    def read_beam(self):
        load_status = self.l_m.read_pos()
        m4_status = self.m4_m.read_pos()
        m2_status = self.m2_m.read_pos()
        return [load_status, m4_status, m2_status]
    
    def read_weather(self):
        ret = self.weather.read_weather()
        return ret
    
    
    def read_antenna(self):
        telstatus = self.tel.read_error()
        telstatus2 = self.tel.read_status()
        telstatus3 = self.tel.read_azel()
        encstatus = self.enc.read_azel()
        domestatus = self.dome.read_status()
        domeposstatus = self.dome.read_domepos()
        limit = ''

        # limit check
        if telstatus[4] == 0:
            limit += 'soft limit cw-'
        if telstatus[5] == 0:
            limit += 'soft limit ccw-'
        if telstatus[6] == 0:
            limit += 'soft limit up-'
        if telstatus[7] == 0:
            limit += 'soft limit down-'
        if telstatus[8] == 0:
            limit += '1st limit cw-'
        if telstatus[9] == 0:
            limit += '1st limit ccw-'
        if telstatus[10] == 0:
            limit += '1st limit up-'
        if telstatus[11] == 0:
            limit += '1st limit down-'
        if telstatus[12] == 0:
            limit += '2nd limit cw-'
        if telstatus[13] == 0:
            limit += '2nd limit ccw-'
        if telstatus[14] == 0:
            limit += '2nd limit up-'
        if telstatus[15] == 0:
            limit += '2nd limit down-'
        #if telstatus[18] == 1:
            #limit += 'deviation error az-'
        #if telstatus[19] == 1:
            #limit += 'deviation error el-'
        if telstatus[20] == 1:
            limit += 'controller error az-'
        if telstatus[21] == 1:
            limit += 'controller error el-'
        #if telstatus[22] == 1:
            #print 'servo pack error az\n'
        #if telstatus[23] == 1:
            #print 'servo pack error el\n'
        #if telstatus[24] == 0:
            #limit += 'emergency switch'
        if limit == '':
            limit += 'OFF'
        
        #track = self.antenna.read_track()
        #error = self.antenna.read_error()
        #velocity = self.antenna.read_v()
        #return [enc[0], enc[1], target[0], target[1], track[0], track[1], error[0], error[1], error[2], error[3], velocity[0], velocity[1]]
        return [limit, telstatus, telstatus2, telstatus3, encstatus, domestatus, domeposstatus]
    


