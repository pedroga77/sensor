from machine import Pin, ADC
import time


PINO_LDR = 14        
PINO_LED_ESCURO = 23  

sensor_ldr = ADC(Pin(PINO_LDR))
led_escuro = Pin(PINO_LED_ESCURO, Pin.OUT)

sensor_ldr.width(ADC.WIDTH_12BIT)  
sensor_ldr.atten(ADC.ATTN_11DB)    

while True:
    valor_luminosidade = sensor_ldr.read()
    print("Valor de luminosidade:", valor_luminosidade)

    LIMIAR_ESCURO = 150

    if valor_luminosidade < LIMIAR_ESCURO:
        print("Ambiente escuro! Acendendo o LED.")
        led_escuro.value(1)
    else:
        print("Ambiente claro. LED apagado.")
        led_escuro.value(0)

    time.sleep(1)


