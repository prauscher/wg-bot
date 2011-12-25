#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Rezeptdatenbank import Rezept

class DummyRezeptdatenbank(object):
	def __init__(self):
		pass

	def add(self, rezept):
		pass
	
	def delete(self, rezept):
		pass
	
	def get(self, id):
		return Rezept("Pfannkuchen", "http://www.chefkoch.de/magazin/artikel/1404,1/Chefkoch/Pfannkuchen-Eierkuchen.html")
	
	def ids(self):
		return range(0, self.length())
	
	def length(self):
		return 1
