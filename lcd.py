import machine
import utime

rs = machine.Pin(16,machine.Pin.OUT)
e = machine.Pin(17,machine.Pin.OUT)
d4 = machine.Pin(18,machine.Pin.OUT)
d5 = machine.Pin(19,machine.Pin.OUT)
d6 = machine.Pin(20,machine.Pin.OUT)
d7 = machine.Pin(21,machine.Pin.OUT)

def _pulseE():
    e.value(1)
    utime.sleep_us(40)
    e.value(0)
    utime.sleep_us(40)

def longDelay(t):
    utime.sleep_ms(t)

def shortDelay(t):
    utime.sleep_us(t)
    
    
def send2LCD4(BinNum):
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    _pulseE()
    
def out(BinNum):
    d4.value((BinNum & 0b00010000) >>4)
    d5.value((BinNum & 0b00100000) >>5)
    d6.value((BinNum & 0b01000000) >>6)
    d7.value((BinNum & 0b10000000) >>7)
    _pulseE()
    d4.value((BinNum & 0b00000001) >> 0)
    d5.value((BinNum & 0b00000010) >> 1)
    d6.value((BinNum & 0b00000100) >> 2)
    d7.value((BinNum & 0b00001000) >> 3)
    _pulseE()
    
def setCursor(line, pos):
    b = 0
    if line==0:
        b=0
    elif line==1:
        b=40
    returnHome()
    for i in range(0, b+pos):
        moveCursorRight()
    
def returnHome():
    rs.value(0)
    out(0b00000010)
    rs.value(1)
    longDelay(2)

def moveCursorRight():
    rs.value(0)
    out(0b00010100)
    rs.value(1)
    
def setupLCD():
    
    rs = machine.Pin(16,machine.Pin.OUT)
    e = machine.Pin(17,machine.Pin.OUT)
    d4 = machine.Pin(18,machine.Pin.OUT)
    d5 = machine.Pin(19,machine.Pin.OUT)
    d6 = machine.Pin(20,machine.Pin.OUT)
    d7 = machine.Pin(21,machine.Pin.OUT)
    rs.value(0)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0010)
    out(0b00101000)
    out(0b00001100)#lcd on, blink off, cursor off.
    out(0b00000110)#increment cursor, no display shift
    out(0b00000001)#clear screen
    longDelay(2)#clear screen needs a long delay
    rs.value(1)
 


def prnt(input_string):
    for x in input_string:
        out(ord(x))
        
        
def prntSpecial(row, col, input_string):
    setCursor(row, col)
    for x in input_string:
        out(ord(x))
        
def clear():
    setCursor(0, 0)
    for x in "                ":
        out(ord(x))
    setCursor(1, 0)
    for x in "                ":
        out(ord(x))
    setCursor(0, 0)
    
def clearBottom():
    setCursor(1, 0)
    for x in "                ":
        out(ord(x))
    setCursor(1, 0)
    
def clearTop():
    setCursor(0, 0)
    for x in "                ":
        out(ord(x))
    setCursor(0, 0)


