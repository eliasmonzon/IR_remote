import machine
import utime
import micropython

class ir_receptor(object):
    def __init__(self, gpioNum):
        self.irRecv = machine.Pin(gpioNum, machine.Pin.IN, machine.Pin.PULL_UP)
        self.irRecv.irq(
            trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING,
            handler = self.__logHandler)
        self.logList = []
        self.index = 0
        self.start = 0
        self.dictKeyNum = 0
        self.irDict = {}

    def __logHandler(self, source):
        thisComeInTime = utime.ticks_us()
        if self.start == 0:
            self.start = thisComeInTime
            self.index = 0
            return
        self.logList.append(utime.ticks_diff(thisComeInTime, self.start))
        self.start = thisComeInTime
        self.index += 1

    def ir_read(self):
        utime.sleep_ms(200) 
        if utime.ticks_diff(utime.ticks_us(), self.start) > 800000 and self.index > 0:
           ir_buffer = [1 if duration > 800 else 0 for duration in self.logList[3:66:2]]
           irValue = 0
           for bit in ir_buffer:
               irValue = (irValue << 1) | bit
           # Reiniciar los valores
           self.logList = []
           self.index = 0
           self.start = 0
           return hex(irValue)
