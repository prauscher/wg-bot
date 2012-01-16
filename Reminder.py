#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import time
import re

scaling = {'w' : 7*24*60*60, 'd' : 24*60*60, 'h' : 60*60, 'm' : 60, 's' : 1}

class IRCReminder:
	def ircAdd(self, context, command, text):
		destTime,event = (text+" ").split(" ",1)
		
		unixtime = time.time()
		tempTime = 0
		for char in destTime:
			if char.isdigit():
				tempTime = tempTime*10 + int(char)
			elif char in scaling:
				unixtime = unixtime + tempTime * scaling[char]
				tempTime = 0
			else:
				context.reply("Unbekanntes Zeitelement " + char)
				return
		unixtime = unixtime + tempTime
		
		def reminderThread():
			time.sleep(unixtime - time.time())
			context.reply(event)
		Thread(target=reminderThread).start()
		context.reply("Zeitmarker gesetzt auf " + time.strftime("%H:%M:%S", time.localtime(unixtime)) )
