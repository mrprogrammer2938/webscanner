#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    End = '\033[0m'
def menu():
    os.system("clear")
    time.sleep(1)
    print(color.green + '''

Yb        dP 888888 88""Yb .dP"Y8  dP""b8    db    88b 88 88b 88 888888 88""Yb 
 Yb  db  dP  88__   88__dP `Ybo." dP   `"   dPYb   88Yb88 88Yb88 88__   88__dP 
  YbdPYbdP   88""   88""Yb o.`Y8b Yb       dP__Yb  88 Y88 88 Y88 88""   88"Yb  
   YP  YP    888888 88oodP 8bodP'  YboodP dP""""Yb 88  Y8 88  Y8 888888 88  Yb
 ''' + color.End)
    print("\t1.start")
    print("\t2.Exit")
    choose = str(input("\nwebscanner/> "))
    if(str(choose) == '1'):
      tryagain()
    elif choose == '2':
        os.system("clear")
        print(color.green + "Exiting..." + color.End)
        exit()
    elif choose == '' or ' ' or '  ':
        menu()
    else:
        time.sleep(1)
        os.system("clear")
        print(color.red + "Error webscanner!" + color.End)
        time.sleep(2)
        try3 = input("press Enter... ")
        if try3 == '':
          menu()
        else:
            menu()
def tryagain():
    time.sleep(1)
    os.system("clear")
    time.sleep(1) 
    os.system("figlet webscanner")
    try1 = str(input("Enter ip: "))
    time.sleep(2)
    os.system("nmap -V -p " + try1)
    try2 = input("Do you want try again? [y/n] ")
    if try2 == 'y':
      tryagain()
    elif try2 == 'n':
        tryagain2()
    else:
        tryagain()
def tryagain2():
    try3 = input("Do you want back to mein menu ? [y/n] ")
    if try3 == 'y':
      menu()
    elif try3 == 'n':
        os.system("clear")
        print(color.green + "Exiting..." + color.End)
        exit(1)
if __name__ == '__main__':
  try:
     menu()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("Exiting...")
      exit()
# webscanner
