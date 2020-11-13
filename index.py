from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['parking']
collection = db['coordenadas']

import RPi.GPIO as GPIO
import time

#Configuracionde pines
GPIO.setmode(GPIO.BOARD)

Trigger = 10
Echo = 12
Verde = 16
Rojo = 22
Amarillo = 18
Buzzer = 24

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

#Pines de salida
GPIO.setup(Verde,GPIO.OUT)
GPIO.setup(Rojo,GPIO.OUT)
GPIO.setup(Amarillo, GPIO.OUT)


print "Sensor Ultrasonico"

GPIO.output(Verde, GPIO.HIGH)
GPIO.output(Rojo, GPIO.HIGH)
GPIO.output(Amarillo, GPIO.HIGH)


#PWM = input(50)
#HZ = input(1000)
#pwm = int(PWM)
#hz = int(HZ)


#pwm_buzzer = GPIO.PWM(Buzzer, hz)
#pwm_led.start(pwm)

#global Buzz
#Buzz = GPIO.PWM(Buzzer, 4)



try:
	while True:
		#establece el trigger EN BAJO 
		GPIO.output(Trigger,False)
		time.sleep(0.5)

		GPIO.output(Trigger,True)
		time.sleep(0.00001)
		GPIO.output(Trigger,False)
		inicio = time.time()
	
		#mientras no se reciba nada el tiempo 
		while GPIO.input(Echo)==0:
			inicio=time.time()

		while GPIO.input(Echo)==1:
			final=time.time()


		#calcular el tiempo transcurrido
		t_transcurrido=final-inicio

		#la distancia recorrida en ese momento
		distancia=t_transcurrido*34000


		#se divide la distancia en 2 por el recorrido de ida y vuelta
		distancia=distancia/2

		if distancia >= 10 and distancia < 20:
			GPIO.output(Verde, GPIO.LOW)
			GPIO.output(Rojo, GPIO.LOW)
			GPIO.output(Amarillo, GPIO.HIGH)
			GPIO.setup(Buzzer, GPIO.IN)	
		elif distancia < 10:
			GPIO.output(Rojo, GPIO.HIGH)
			GPIO.output(Verde, GPIO.LOW)
			GPIO.output(Amarillo, GPIO.LOW)
			GPIO.setup(Buzzer, GPIO.OUT)			
		elif distancia > 20:
			GPIO.output(Rojo, GPIO.LOW)
			GPIO.output(Verde, GPIO.HIGH)
			GPIO.output(Amarillo, GPIO.LOW)
			GPIO.setup(Buzzer, GPIO.IN)		
		print "Distancia=%.1fcm"%distancia
		collection.insert_one({'distancia': distancia})
except KeyboardInterrupt:
	GPIO.cleanup()
