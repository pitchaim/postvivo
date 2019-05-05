import argparse
import random
import time
import numpy as np

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  t_arr = np.random.randint(0,255,(4,20,20)).tolist()
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="192.168.1.8",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=7776,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)


  for x in range(20):
      for y in range(20):
          a = t_arr[3][x][y]
          r = t_arr[0][x][y]
          g = t_arr[1][x][y]
          b = t_arr[2][x][y]
          client.send_message("/X", x)
          client.send_message("/Y", y)
          client.send_message("/A", a)
          client.send_message("/R", r)
          client.send_message("/G", g)
          client.send_message("/B", b)
          #client.send_message("/SYGOGGLIN", "STROMBOOBLE ON DOWN YIPPEE")
  #time.sleep(2)
