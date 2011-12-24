#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ircsession import IRCSession
from database import ExampleDatabase
from einkaufsliste import DummyEinkaufsliste, IRCEinkaufsliste

#irc = IRCSession('172.22.24.1', 6667, 'Marvin', 'wgbot', 'Haushälter im Alfred-Messel-Wg 8a (WG 61)', None)
irc = IRCSession('irc.eu.hackint.org', 6667, 'Marvin', 'wgbot', 'Haushälter im Alfred-Messel-Wg 8a (WG 61)', None)

database = ExampleDatabase()
einkaufsliste = IRCEinkaufsliste(DummyEinkaufsliste())

# TODO initialize database, register commands
irc.registerCommand('!ping', lambda context, command, text:
	context.reply(text))

irc.registerCommand('!einkauf add ', einkaufsliste.ircAdd)
irc.registerCommand('!einkauf del ', einkaufsliste.ircDel)
irc.registerCommand('!einkauf list', einkaufsliste.ircShow)
irc.registerCommand('!einkauf clear', einkaufsliste.ircClear)

irc.registerCommand('!something', database.something)

irc.join('#8a-61')
