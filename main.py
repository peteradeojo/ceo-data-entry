from os import system
from time import sleep

words = ["bolu", "pelu", "folu", "toyin", "mummy", "daddy"]

for i in range(100):
  for w in words:
    print(w)
    sleep(0.5)
    system("clear")