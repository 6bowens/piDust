import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#in retrospect, I should have built this with arrays ...

#Pin Defs
servoPIN1=11  #overhead
servoPIN2=13  #circsaw
servoPIN3=15  #bandsaw

#State Vars
gateNow1=0
gateNow2=0
gateNow3=0
gateBefore1=0
gateBefore2=0
gateBefore3=0

#System Vars
freq=50
close=2.5
open=12.5
stop=7.5

#GPIO Setup

GPIO.setup(servoPIN1, GPIO.OUT)
s1 = GPIO.PWM(servoPIN1, freq)
time.sleep(0.1)

GPIO.setup(servoPIN2, GPIO.OUT)
s2 = GPIO.PWM(servoPIN2, freq)
time.sleep(0.1)

GPIO.setup(servoPIN3, GPIO.OUT)
s3 = GPIO.PWM(servoPIN3, freq)
time.sleep(0.1)

def on_connect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))
   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("brett/toolSelect/tool")

def on_message(client, userdata, msg):
   print(msg.topic+" "+str( msg.payload))
   # Check if this is a message for the Pi:
   if msg.topic == 'brett/toolSelect/tool':
       # Look at the message data and perform the appropriate action.
       if msg.payload == b'CircSaw':
	   s1.start(close)
	   time.sleep(1)
	   s2.start(open)
	   time.sleep(1)
	   s3.start(close)
	   time.sleep(1)
	   print ('Switching to CircSaw')

       elif msg.payload == b'BandSaw':
           s1.start(close)
           time.sleep(1)
           s2.start(close)
           time.sleep(1)
           s3.start(open)
	   time.sleep(1)
	   print ('Switching to BandSaw')

       elif msg.payload == b'Ovrhead':
	   s1.start(open)
	   time.sleep(1)
	   s2.start(close)
	   time.sleep(1)
	   s3.start(close)
	   time.sleep(1)
	   print ('Switching to Overhead')

   s1.ChangeDutyCycle(0)
   s2.ChangeDutyCycle(0)
   s3.ChangeDutyCycle(0)
   print ("End of Message Function")

# Create MQTT client and connect to this mqtt server
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)

# Connect to the MQTT server and process messages in a background thread.
client.loop_start()

while True:

	print ("Processing...")
	time.sleep(1) #
