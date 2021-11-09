let Temp = 0
serial.redirectToUSB()
let Timer = 15
Timer = Timer * 60
Timer = Timer - 1
Timer = Timer * 1000
Timer = Timer * 1000
Timer = 10000
basic.forever(function () {
    Temp = dstemp.celsius(DigitalPin.P3)
    Temp = Temp * 10
    Temp = Math.round(Temp)
    Temp = Temp / 10
    serial.writeLine("" + Temp)
    basic.showString("" + Temp)
    control.waitMicros(Timer)
    Temp = 0
})
