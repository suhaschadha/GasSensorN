
import sys, datetime, json
import random
import datetime
import time
import sys
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue
#from iothub_client import IoTHubClientRetryPolicy, GetRetryPolicyReturnValue
#from iothub_client_args import get_iothub_opt, OptionError
import sys
import Adafruit_DHT
import RPi.GPIO as IO  
from mq import *
         


IO.setmode (IO.BOARD)

IO.setup(13,IO.OUT)
IO.output(13,0)


i=1
x=1
DEVICE_ID = "Device1.0"
#msg_txt_formatted = "{\"deviceId\": \"MyFirstPythonDevice\",\"Temperature\": \"15\"}" 
connectionString =str('HostName=Arvind.azure-devices.net;DeviceId=Device1.0;SharedAccessKey=LN4dUTR5lNUiBrZbhL5VtdpaGeixy88Sg0RcbDmi4CI=')
PROTOCOL = IoTHubTransportProvider.MQTT 
message_counter = 0


mq = MQ();
perc = mq.MQPercentage()



for x in range(1,31):
    dt = str(datetime.datetime.now().replace(microsecond=0))	
    #now = datetime.datetime.now().replace(microsecond=0)
    #print now

    perc = mq.MQPercentage()
    print(perc["GAS_LPG"])
    
    #if humidity is not None and temperature is not None:                
   	#a=('{0:0.1f}  {1:0.1f}'.format(temperature, humidity))
	#b = a
	#b=b.split(" ")
	#print b[0]
	#print b[2]
	#c="temp=" + b[0] +" "+ "humidity=" + b[2] + " " + "time=" +dt
	#d = '"' + c + '"'
	#dt2= '"'+dt+'"'
	#print (d)
	#print type(b[0])


	#if float(b[0])>25:
	   #print('hi')	
           #IO.output(13,1)                      

	#MSG_TXT = "{\"deviceId\": \"Raspberry Pi-1\",\"temperature\": %s,\"humidity\":%s,\"Datetime\":%s}"        
	#msg_txt_formatted = "{\"deviceId\": \"MyFirstPythonDevice\",\"temperature\": ,\"humidity\": }"
	#msg_txt_formatted = "{\"deviceId\": \"MyFirstPythonDevice\",\"temperature\": %f,\"humidity\"}"%a
	#msg_txt_formatted = MSG_TXT %(b[0],b[2],dt2)
        
        

    #else:
       # print('Failed to get reading. Try again!')
    #time.sleep(2)


    
    #message = IoTHubMessage(msg_txt_formatted)

    def send_confirmation_callback(message, result, userContext):
        print "Confirmation[%d] received for message with result = %s" % (userContext, result)

    def receive_message_callback(message, counter):
        buffer = message.get_bytearray()
        size = len(buffer)
        print "Received Message"
        print "    Data: <<<%s>>> & Size=%d" % (buffer[:size], size)
        return IoTHubMessageDispositionResult.ACCEPTED

    for i in range(1,2):
            

            iotHubClient = IoTHubClient(connectionString,PROTOCOL)
            iotHubClient.send_event_async(message, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            time.sleep(3)
            status = iotHubClient.get_send_status()
            print ( "Send status: %s" % status )
exit;
