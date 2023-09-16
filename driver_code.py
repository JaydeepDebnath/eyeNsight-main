import predictor
from pynput import keyboard

while True:
    choice = predictor.pred()
    print(choice)