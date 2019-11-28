#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7
pin_to_circuit_2 = 8
pin_to_circuit_3 = 10
pin_to_circuit_4 = 11
status = 1
status_2 = 1
status_3 = 1
status_4 = 1

count = 0
temp = 0
temp_2 = 0
temp_3 = 0
temp_4 = 0



def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        temp = rc_time(pin_to_circuit)
        
        temp_2 = rc_time(pin_to_circuit_2)
        
        temp_3 = rc_time(pin_to_circuit_3)
        
        temp_4 = rc_time(pin_to_circuit_4)
    
        if rc_time(pin_to_circuit) > 4500:
            status = 0
            print('1 is Off')
            
        else:
            status = 1
        
        print('The 1st resistor value is ' + str(temp))
        
        if rc_time(pin_to_circuit_2) > 4500:
            status_2 = 0
            print('2 is Off')
            
        else:
            status_2 = 1
            
      #  print('The 2nd resistor value is ' + str(temp_2))
        
        if rc_time(pin_to_circuit_3) > 5000:
            status_3 = 0
         #   print('3 is Off')
            
        else:
            status_3 = 1
        
     #   print('The 3rd resistor value is ' + str(temp_3))
        
        if rc_time(pin_to_circuit_4) > 5000:
            status_4 = 0
       #     print('4 is Off')
            
        else:
            status_4 = 1
            
       # print('The 4th resistor value is ' + str(temp_4))
        
        count += 1
        
        if count%10 == 0:
            #status_full=status*10 + status_2
            file = open("data.txt", "w")
            file.write('%d' %status)
            file.close()
            file = open("data.txt", "a")
            file.write(', %d' %status_2)
            file.close()
            '''file = open("data.txt", "a")
            file.write(', %d' %status_3)
            file.close()
            file = open("data.txt", "a")
            file.write(', %d' %status_4)
            file.close()'''
            
        
except KeyboardInterrupt:
   pass
finally:
    GPIO.cleanup()
