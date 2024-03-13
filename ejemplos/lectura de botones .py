from machine import Pin
from IR_remote import ir_receptor
Receptor_pin = ir_receptor(23)
while True:
    irValue = Receptor_pin.ir_read()
    if irValue:
        print('boton precionado su codigo es:',irValue)
        
   