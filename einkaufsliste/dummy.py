#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Einkaufsliste import Einkauf

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
