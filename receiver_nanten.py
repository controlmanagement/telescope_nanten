#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    receiver_nanten(core.controller.receiver): 

------------------------------------------------
[History]

2015/11/10 maruyama

------------------------------------------------
"""

import numpy
import threading
import equipment_nanten
#import cont
import core.controller

class receiver_nanten(core.controller.receiver):
    
    def __init__(self):
        #self.opt_cam = equipment_nanten.opt_cam()
        self.dfs = equipment_nanten.dfs()
        #self.cont = self._cont_open()
        #self.init()
        pass
    
    def oneshot_dfs01(self, repeat=1, integsec=1.0, starttime=0.0):
        """dfs01のoneshotを取得"""
        data = self.dfs.oneshot_dfs01(repeat, integsec, starttime)
        return data
    
    def oneshot_dfs02(self, repeat=1, integsec=1.0, starttime=0.0):
        """dfs02のoneshotを取得"""
        data = self.dfs.oneshot_dfs02(repeat, integsec, starttime)
        return data
    
