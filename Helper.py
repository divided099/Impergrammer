import os
import platform
import time

def clear():
  if platform.system() == "Windows":
      os.system("cls")
  else:
      os.system("clear")

def Install():
  os.system("pip install Used.txt")
  os.system("pip3 install Used.txt")
  clear()

try:
  import pyfiglet
except Exception as e:
  Install()

def banner():
    print(pyfiglet.figlet_format("Impergrammer"))

def Startup():
  time.sleep(1)
  clear()
  banner()
