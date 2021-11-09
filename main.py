serial.redirect_to_usb()
Temp = 0
Timer = 15
Timer = Timer * 60
Timer = Timer - 1
Timer = Timer * 1000
Timer = Timer * 1000
Timer = 10000

def on_forever():
    global Temp
    Temp = dstemp.celsius(DigitalPin.P3)
    Temp = Temp * 10
    Temp = Math.round(Temp)
    Temp = Temp / 10
    serial.write_line("" + str((Temp)))
    basic.show_string("" + str((Temp)))
    control.wait_micros(Timer)
    Temp = 0
basic.forever(on_forever)
