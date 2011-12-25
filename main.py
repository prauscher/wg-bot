#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IRCSession import IRCSession
from Einkaufsliste import IRCEinkaufsliste
from einkaufsliste.dummy import DummyEinkaufsliste
from Rezeptdatenbank import IRCRezeptdatenbank
from rezeptdatenbank.dummy import DummyRezeptdatenbank

#irc = IRCSession('172.22.24.1', 6667, 'Marvin', 'wgbot', 'Haushälter im Alfred-Messel-Wg 8a (WG 61)', None)
irc = IRCSession('irc.eu.hackint.org', 6667, 'Marvin', 'wgbot', 'Haushälter im Alfred-Messel-Wg 8a (WG 61)', None)

einkaufsliste = IRCEinkaufsliste(DummyEinkaufsliste())
rezeptdatenbank = IRCRezeptdatenbank(DummyRezeptdatenbank())

irc.registerCommand('!ping', lambda context, command, text:
	context.reply(text))

irc.registerCommand('!einkauf add ', einkaufsliste.ircAdd)
irc.registerCommand('!einkauf del ', einkaufsliste.ircDel)
irc.registerCommand('!einkauf list', einkaufsliste.ircList)
irc.registerCommand('!einkauf clear', einkaufsliste.ircClear)

irc.registerCommand('!rezept random', rezeptdatenbank.ircRandom)
irc.registerCommand('!rezept add ', rezeptdatenbank.ircAdd)
irc.registerCommand('!rezept del ', rezeptdatenbank.ircDel)
irc.registerCommand('!rezept list', rezeptdatenbank.ircList)
irc.registerCommand('!rezept show', rezeptdatenbank.ircShow)

irc.join('#8a-61')
