#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
os.system("clear")
time.sleep(1)
print(color.green + """

Yb        dP 888888 88""Yb .dP"Y8  dP""b8    db    88b 88 88b 88 888888 88""Yb 
 Yb  db  dP  88__   88__dP `Ybo." dP   `"   dPYb   88Yb88 88Yb88 88__   88__dP 
  YbdPYbdP   88""   88""Yb o.`Y8b Yb       dP__Yb  88 Y88 88 Y88 88""   88"Yb  
   YP  YP    888888 88oodP 8bodP'  YboodP dP""""Yb 88  Y8 88  Y8 888888 88  Yb """ + color.red + """

                            (🅦🅔🅑🅢🅒🅐🅝🅝🅔🅡)""" + color.white)
print("\t1.start")
print("\t2.Exit")
choose = str(input("\nwebscanner/> "))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  time.sleep(1)
  os.system("figlet webscanner")
  try1 = str(input("Enter ip: "))
  time.sleep(2)
  os.system("nmap -V -p " + try1)
  try2 = str(input("Do you want try again? [y/n] "))
  if(str(try2) == 'y'):
    os.system("python3 webscanner.py")
  elif(str(try2) == 'n'):
      time.sleep(1)
      os.system("clear")
      print("good bye")
      exit(1)
  else:
      time.sleep(1)
      os.system("clear")
      print(color.red + "Error webscanner" + color.white)
      time.sleep(2)
      try3 = str(input("press Enter... "))
      if(str(try3) == ''):
        os.system("python3 webscanner.py")
      else:
          os.system("python3 webscanner.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("good bye")
    exit(1)
else:
    time.sleep(1)
    os.system("clear")
    print(color.red + "Error webscanner" + color.white)
    time.sleep(2)
    try3 = str(input("press Enter... "))
    if(str(try3) == ''):
      os.system("python3 webscanner.py")
    else:
        os.system("python3 webscanner.py")
# webscanner
