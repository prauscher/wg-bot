#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice

class Rezept(object):
	def __init__(self, label, url):
		self.label = label
		self.url = url
	
	def __str__(self):
		return self.label + " <" + self.url + ">"

class IRCRezeptdatenbank(object):
	def __init__(self, rdb):
		self.rdb = rdb

	def ircRandom(self, context, command, text):
		id = choice(self.rdb.ids())
		context.reply("#" + str(id) + ": " + str(self.rdb.get(id)))

	def ircShow(self, context, command, text):
		try:
			id = int(text)
			context.reply("#" + str(id) + ": " + str(self.rdb.get(id)))
		except Exception as e:
			context.reply("Failure: " + str(e))

	def ircList(self, context, command, text):
		try:
			for id in self.rdb.ids():
				context.reply("#" + str(id) + ": " + str(self.rdb.get(id)))
			else:
				context.reply("End Of List")
		except Exception as e:
			context.reply("Failure: " + str(e))

	def ircAdd(self, context, command, text):
		try:
			parts = text.split(' ')
			url = parts.pop()
			label = " ".join(parts)
			self.rdb.add(Rezept(label, url))
		except Exception as e:
			context.reply("Failure: " + str(e))
		else:
			context.reply("Success!")

	def ircDel(self, context, command, text):
		try:
			id = int(text)
			self.rdb.delete(id)
		except Exception as e:
			context.reply("Failure: " + str(e))
		else:
			context.reply("Success!")
