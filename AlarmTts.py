#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from androidhelper import Android
from datetime import datetime
from time import sleep

a = Android()
h = int(input("hora: "))
m = int(input("min: "))
while True:
 d = datetime.now()
 h2 = d.hour
 m2 = d.minute
 if h2 == h and m2 == m:
  for i in range(3):
   a.ttsSpeak("ACORDA SEU ARROMBADO, TÁ NA HORA DE ACORDAR ANIMAL! São {} e {} porra!".format(h, m))
  break
 sleep(1)
