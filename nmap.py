import subprocess
import os
import sys
RED = "\033[0;31m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
if len(sys.argv)>-4:
    os.system("cls||clear")
    sys.stdout.write(RED+"""                                 ___   ________                                  ___    
  ____   _____ _____  ______     /  /     /  _____/_____   __ ______________ ___  __ \  \   
 /    \ /     \\__  \ \____ \   /  /    /   \  ___\__  \ |  |  \_  __ \__  \\  \/ /  \  \  
|   |  \  Y Y  \/ __ \|  |_> > (  (  by \    \_\  \/ __ \|  |  /|  | \// __ \\   /    )  ) 
|___|  /__|_|  (____  /   __/   \  \     \______  (____  /____/ |__|  (____  /\_/    /  /  
     \/      \/     \/|__|       \__\           \/     \/                  \/       /__/   \n""" )
else:
    sys.exit("usage:To scan any address by Kumar Gaurav")

def mainMenu():
           print("-" *80)
           print("\t\t\tNMAP SCANNER BY KUMAR GAURAV")
           print("-" *80)
           print()
           print("\t\t\t1=========> discover host")
           print("\t\t\t2=========> discover port")
           print("\t\t\t3=========> discover os")
           print("\t\t\t4=========> clear screen")
           print("\t\t\t5=========> quit screen")
           print()

           choice = int(input("enter your choice:-"))
           if choice==1:
               host_discovery()
               mainMenu()
           elif choice==2:
                port_discovery()
                mainMenu()
           elif choice==3:
                os_discovery()
                mainMenu()
           elif choice==4:
               clear()
               mainMenu()
           elif choice==5:
               clear()
               quit_program()
           else :
               print("enter correct choice")

def host_discovery():
  host=input("enter the host:-")
  print("." *80)
  subprocess.check_call(['nmap','-Pn','-n','-V','-sL','-sN','-PE','-PP','-oN','host.txt','host'])
  print("." *80)

def port_discovery():
  port_range=input("enter the host:-")
  print("." *80)
  subprocess.check_call(['nmap','-p','1-500','-oN','port_range.txt', port_range])
  print("." *80)

def os_discovery():
  os=input("enter the host:-")
  print("." *80)
  subprocess.check_call(['nmap','-Pn','-n','-F','-A','-O','-oN','os.txt',os])
  print("." *80)

def clear():
    os.system('cls||clear')

def quit_program():
    clear()
    quit()

if __name__== "__main__":
    mainMenu()

