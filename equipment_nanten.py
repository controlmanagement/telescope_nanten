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
import telescope_nanten.antenna_nanten_controller
import telescope_nanten.dome
import telescope_nanten.membrane
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
		self.abs = telescope_nanten.abs.abs_client('192.168.100.187',5921)
		self.abs.open()
		pass
	
	def move_r(self):
		self.abs.start_thread('IN')
		return
	
	def move_sky(self):
		self.abs.start_thread('OUT')
		return
	
	def get_status(self):
		return self.abs.read_pos()
	
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
		self.m4.start_thread('NAGOYA')
		return

	def m4_out(self):
		self.m4.start_thread('SMART')
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

class antenna(object):
	
	def __init__(self):
		host = ''
		port = 
		self.antenna = telescope.antenna_nanten_controller.antenna_client('',)
		pass
	
	def move_azel(self, az, el, dcos, hosei = 'hosei_230.txt', off_az = 0, off_el = 0):
		self.antenna.move_azel(az, el, dcos, hosei, off_az, off_el)
		return
	
	def move_radec(self, gx, gy, gpx, gpy, code_mode, temp, pressure, humid, lamda, dcos, hosei = 'hosei_230.txt', off_x = 0, off_y = 0):
		
		
		self.antenna.move_radec(gx, gy, gpx, gpy, code_mode, temp, pressure, humid, lamda, dcos, hosei, off_x, off_y)
		
		
		
		
		
		
	
	def move_lb(self, gx, gy, temp, pressure, humid, lamda, dcos, hosei = 'hosei_230.txt', off_x = 0, off_y = 0):
		
		
		self.antenna.move_lb(gx, gy, temp, pressure, humid, lamda, dcos, hosei, off_x, off_y)
		
		
		
		
		
		
	
	def move_planet(self, ):
		
		
		
		
		
		
	
	def do_otf():
		
		self.antenna.calc_otf()
		
		
		
		
		

class dome(object):
	
	track_flag = 0
	
	def __init__(self):
		host = ''
		port = 
		self.dome = telescope.dome.dome_client('',)
		self.dome.open()

	def dome_track_start(self):
		self.dome.start_track()
		self.track_flag = 1
		return

	def dome_track_end(self):
		self.dome.end_track()
		self.track_flag = 0
		return

	def dome_move_org(self):
		if track_flag == 1:
			self.dome_track_end()
		self.dome.move_org()
		return

	def dome_move(self, az):
		if track_flag == 1:
			self.dome_track_end()
		self.dome.move(az)
		return

	def emergency_stop(self):
		if track_flag == 1:
			self.dome_track_end()
		self.dome.emergency_stop()
		return

class membrane(object):
	
	def __init__(self):
		host = ''
		port = 
		self.memb = telescope.mambrane.memb_client('',)
		self.memb.open()
	
	def memb_open(self):
		self.memb.start_thread('OPEN')
		return
	
	def memb_close(self): # move_org() = memb_close()
		self.memb.start_thread('CLOSE')
		return
	
	def get_status(self):
		ret = self.memb.get_status()
		return ret
	

