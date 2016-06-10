#! /usr/bin/env python
# coding:utf-8

"""
------------------------------------------------
[Detail Description]

    beam_nanten(core.controller.beam): 
        hot_in
        hot_out
        stop_hot
        m4_in
        m4_out
        stop_m4
        get_status

------------------------------------------------
[History]

2015/12/17 maruyama

------------------------------------------------
"""

import core.controller

class beam_nanten(core.controller.beam):
    """hot,m4の制御を行う"""
    
    def __init__(self):
        import telescope_nanten.equipment_nanten
        
        self.load = telescope_nanten.equipment_nanten.hot_load()
        self.m4 = telescope_nanten.equipment_nanten.m4()
        pass
    
    def hot_in(self):
        """hotloadをrの位置に動かす"""
        self.load.move_r()
        return
    
    def hot_out(self):
        """hotloadをskyの位置に動かす"""
        self.load.move_sky()
        return
    
    def stop_hot(self):
        """hotloadの動作停止"""
        self.load.stop()
        return

    def m4_in(self):
        """m4をINの位置に動かす"""
        self.m4.m4_in()
        return
    
    def m4_out(self):
        """m4をOUTの位置に動かす"""
        self.m4.m4_out()
        return
    
    def stop_m4(self):
        """m4の動作停止"""
        self.m4.stop()
        return

    def get_status(self):
        """現在のhotload, m4の状態を取得する"""
        l_status = self.load.get_status()
        m4_status = self.m4.get_status()
        return [l_status, m4_status]
