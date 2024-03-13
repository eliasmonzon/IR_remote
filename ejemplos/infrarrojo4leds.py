from machine import Pin
from IR_remote import ir_receptor
Receptor_pin = ir_receptor(23)
Led1 = Pin(16, Pin.OUT)
Led2 = Pin(17,Pin.OUT)
Led3 = Pin(5,Pin.OUT)
Led4 = Pin(18,Pin.OUT)
led1_state = False
led2_state = False
led3_state = False
led4_state = False
while True:
    irValue = Receptor_pin.ir_read()
    if irValue == '0x1fe50af':
      led1_state = not led1_state  # Cambiar el estado del LED
      Led1.value(led1_state)  # Encender o apagar el LED según el estado
    elif irValue == '0x1fed827':
      led2_state = not led2_state  # Cambiar el estado del LED
      Led2.value(led2_state)  # Encender o apagar el LED según el estado
    elif irValue == '0x1fef807':
      led3_state = not led3_state  # Cambiar el estado del LED
      Led3.value(led3_state)  # Encender o apagar el LED según el estado
    elif irValue == '0x1fe30cf':
      led4_state = not led4_state  # Cambiar el estado del LED
      Led4.value(led4_state)  # Encender o apagar el LED según el estado
      
 
