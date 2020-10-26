import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

while True:
  line = proc.stdout.readline()
  print(line)
  if not line:
    break

  try:
    connected_ip = line.decode('utf-8').split()[3].replace(':', '')
    # print(connected_ip)
    if connected_ip == IP_DEVICE:
      subprocess.Popen(['say', 'your phone just connected to the network!'])
      break
    else:
      print('Pinging device...')
  except:
    pass