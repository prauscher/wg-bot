#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Einkauf(object):
	def __init__(self, label, author):
		self.label = label
		self.author = author
	
	def __str__(self):
		return self.label + " (" + self.author + ")"

class DummyEinkaufsliste(object):
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)
	
	def delete(self, id):
		del(self.items[id])
	
	def get(self, id):
		return self.items[id]
	
	def ids(self):
		return range(0, self.length())
	
	def length(self):
		return len(self.items)
	
	def clear(self):
		self.items = []
	
class IRCEinkaufsliste(object):
	def __init__(self, el):
		self.el = el;
	
	def ircAdd(self, context, command, text):
		try:
			id = self.el.add(Einkauf(text, context.sender))
		except:
			context.reply('Failure!')
		else:
			context.reply('Success!')
	
	def ircDel(self, context, command, text):
		try:
			id = int(text)
			self.el.delete(id)
		except:
			context.reply('Failure!')
		else:
			context.reply('Deleted #' + str(id))
	
	def ircShow(self, context, command, text):
		for id in self.el.ids():
			context.reply(str(id) + ": " + str(self.el.get(id)))
		else:
			context.reply('End Of List')
	
	def ircClear(self, context, command, text):
		try:
			self.el.clear()
		except:
			context.reply('Failure!')
		else:
			context.reply('Done!')
