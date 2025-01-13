# This is done using simple keyboard input as the argument 
import pywhatkit as pk
def main():
  video = input("search:")
  pk.playonyt(video)
try:
  main()
except:
  print("An error occurred")
finally:
  print("Search Completed")
