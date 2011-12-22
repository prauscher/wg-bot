#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ircsession import IRCSession
from database import ExampleDatabase

irc = IRCSession('172.22.24.1', 6667, 'Marvin', 'wgbot', 'Haushälter im Alfred-Messel-Wg 8a (WG 61)', None)

database = ExampleDatabase()

# TODO initialize database, register commands
irc.registerCommand('!ping', lambda context, line:
	context.reply(line))

irc.registerCommand('!something', database.something)

irc.join('#8a-61')
