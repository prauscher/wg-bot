#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Einkauf(object):
	def __init__(self, label, author):
		self.label = label
		self.author = author
	
	def __str__(self):
		return self.label + " (" + self.author[0] + " " + self.author[1:] + ")"
	
class IRCEinkaufsliste(object):
	def __init__(self, el):
		self.el = el;
	
	def ircAdd(self, context, command, text):
		try:
			id = self.el.add(Einkauf(text, context.sender))
		except Exception as ex:
			context.reply('Failure: ' + str(ex))
		else:
			context.reply('Success!')
	
	def ircDel(self, context, command, text):
		try:
			id = int(text)
			self.el.delete(id)
		except Exception as ex:
			context.reply('Failure: ' + str(ex))
		else:
			context.reply('Deleted #' + str(id))
	
	def ircList(self, context, command, text):
		for id in self.el.ids():
			context.reply(str(id) + ": " + str(self.el.get(id)))
		else:
			context.reply('End Of List')
	
	def ircClear(self, context, command, text):
		try:
			self.el.clear()
		except Exception as ex:
			context.reply('Failure: ' + str(ex))
		else:
			context.reply('Done!')
