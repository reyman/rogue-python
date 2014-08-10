# -*- coding: utf-8 -*-

from objects import *

mapOfWorld = ['~~~~~~~~~~~~~~~~~~~~~~~~~~~YYYYYYYYYYYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~~...YYYYYYYYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~.......YYYYYYYYY',
             '~~~~~~~~~~~~~~~~~..~~~~~~~~....Y..YYYYYYYY',
             '~~~~~~~~~~~~~~~~......~~~~....YYY.YYYYYYYY',
             '~~~~~~~~~~~~~~~......||||.....YY...YYYYYYY',
             '~~~~~~~~~~~~~~~~....~~~~..........YYYYYYYY',
             '~~~~~~~~~~~~~~~~~..~~~~~~......YY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~.....YYYYYY..YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~...YYYY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~....YYYYYY..YYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~....YYYYYY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~.....YYYYYY....YYYYYYY',
             '~~~~~~~~~~~~~~~~~~.......YYYYYY..YYYYYYYYY',
             '~~~~~~~~~~~~~~~~~..YYY...YYYYY....YYYYYYYY',
             '~~~~~~~.~~~~~~~~~.YYYYYY.........YYYYYYYYY',
             '~~~~~~...~~~~~~~~..YYYY....YYYYYYYYYYYYYYY',
             '~~~~~......~~~~~~~...Y.....YYYYYYYYYYYYYYY',
             '~~~~~~........YYY....YY........YYYYYYYYYYY',
             '~~~~~........YYYY..YYYY...........YYYYYYYY',
             '~~~~~~~....YYYYY...YY.....YYYY....YYYYYYYY',
             '~~~~~~~~~..YYYY..YYYYYY...YYYYY.....YYYYYY',
             '~~~~~~~~~~..YYY...YYYYY...YYYYYY...YYYYYYY',
             '~~~~~~~~~~...Y..YYYYYYY...YYYYY......YYYYY',
             '~~~~~~~~~~..YY...YYYYY......YYY..Y...YYYYY',
             '~~~~~~~~~YY.....YYYYY............YY...YYYY',
             '~~~~~~~YYYYYYYYYYYYY.........YYYYYY..YYYYY',
             '~~~~YYYYYYYYYYYYYYYYYY......YYYYY.....YYYY',
             '~~YYYYYYYYYYYYYYYYYY....YYYYYYYYYY......YY',
             'YYYYYYYYYYYYYYYYYYY.....YYYYYYYY......YYYY',
             'YYYYYYYYYYYYYYYY.......YYYYYYYYYYY...YYYYY',
             'YYYYYYYYYYYYYYY......YYYYYYYYYYY.....YYYYY',
             'YYYYYYYYYYYYYYYYYY...YYYYYYYYYY..YYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYY...YYYYYYY....YYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY....YYYYY....YYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYY.....YYY...YYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY.........YYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYYYYYY+YYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYY.....YYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY........YYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY..YYYYYYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY']


tilesObject = {".":{"cls": Floor,  'args': {"name": 'floor', "bgcolor": (233, 207, 177)}},
               "Y":{"cls": Floor,  'args': {"name": 'forest', "bgcolor": (25, 150, 64), "blocked": True}},
               "|":{"cls": Floor,  'args': {"name": 'pont',  "bgcolor": (190, 150, 35)}},
               "~":{"cls": Floor,  'args': {"name": 'water',  "bgcolor": (10, 21, 35)}},
               "+":{"cls": Door,  'args': {"name": 'doors', "bgcolor": (10, 10, 25), "key":"42"}}}
