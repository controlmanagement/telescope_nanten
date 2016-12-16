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
2016/12/16 kohno
------------------------------------------------
"""

import core.controller

class beam_nanten(core.controller.beam):
    """hot,m4\u306e\u5236\u5fa1\u3092\u884c\u3046"""
    
    def __init__(self):
        import telescope_nanten.equipment_nanten
        
        self.load = telescope_nanten.equipment_nanten.hot_load()
        self.m4 = telescope_nanten.equipment_nanten.m4()
        self.m2 = telescope_nanten.equipment_nanten.m2()
	self.m2_status = self.m2.get_status()
        pass
    
    def hot_in(self):
        """hotload\u3092r\u306e\u4f4d\u7f6e\u306b\u52d5\u304b\u3059"""
        self.load.move_r()
        return
    
    def hot_out(self):
        """hotload\u3092sky\u306e\u4f4d\u7f6e\u306b\u52d5\u304b\u3059"""
        self.load.move_sky()
        return
    
    def stop_hot(self):
        """hotload\u306e\u52d5\u4f5c\u505c\u6b62"""
        self.load.stop()
        return

    def m4_in(self):
        """m4\u3092IN\u306e\u4f4d\u7f6e\u306b\u52d5\u304b\u3059"""
        self.m4.m4_in()
        return
    
    def m4_out(self):
        """m4\u3092OUT\u306e\u4f4d\u7f6e\u306b\u52d5\u304b\u3059"""
        self.m4.m4_out()
        return
    
    def stop_m4(self):
        """m4\u306e\u52d5\u4f5c\u505c\u6b62"""
        self.m4.stop()
        return

    def m2_move(self, dist):
        """m2?????"""
        self.m2.m2_move(dist)
        return

    def get_status(self):
        """\u73fe\u5728\u306ehotload, m4\u306e\u72b6\u614b\u3092\u53d6\u5f97\u3059\u308b"""
        l_status = self.load.get_status()
        m4_status = self.m4.get_status()
	m2_status = self.m2.get_status()
        return [l_status, m4_status, m2_status]
