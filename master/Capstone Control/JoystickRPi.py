from gpiozero import GPIODevice


pinx = 5
piny = 6

Rx = GPIODevice(pinx)
Ry = GPIODevice(piny)

while True:
    print(Rx.value)
    print(Ry.value)


