import serial
from serverHandler import *
from tristar_serial import *
from load_controller import *

	#Make sure the location of the controllers are correct
ts = Tristar_Serial('/dev/ttyUSB1')
lc = Load_Controller('/dev/ttyUSB0')
dFlag = 0
lc.qr = lc.client.write_coil(255,1)
ts.wr = ts.client.write_coil(2,0)
while(True):
	while(time.strftime("%S") != "00"): None 
	ser = serial.Serial(port = '/dev/ttyUSB2', baudrate = 9600, bytesize = 8, parity = 'E', stopbits = 1, timeout = 1)
	data = ser.write(b':0322F100\n')   # cell Voltage
	#print ser.is_open
	data = ser.read(57) Add 4 bits to this number to add a battery 
        	print (data)
            
            vat_1 = data[-48:-44]
        	print (vat_1)
        	vat_1_vol = int(vat_1, 16) * 0.0001
        	print "vat_1: ", vat_1_vol
            
            vat_2 = data[-44:-40]
        	print (vat_2)
        	vat_2_vol = int(vat_2, 16) * 0.0001
        	print "vat_2: ", vat_2_vol
            
            vat_3 = data[-40:-36]
        	print (vat_3)
        	vat_3_vol = int(vat_3, 16) * 0.0001
        	print "vat_3: ", vat_3_vol
            
            vat_4 = data[-36:-32]
        	print (vat_4)
        	vat_4_vol = int(vat_4, 16) * 0.0001
        	print "vat_4: ", vat_4_vol
            
            vat_5 = data[-32:-28]
        	print (vat_5)
        	vat_5_vol = int(vat_5, 16) * 0.0001
        	print "vat_5: ", vat_5_vol
            
            vat_6 = data[-28:-24]
        	print (vat_6)
        	vat_6_vol = int(vat_6, 16) * 0.0001
        	print "vat_6: ", vat_6_vol
    
            vat_7 = data[-24:-20]
        	print (vat_7)
        	vat_7_vol = int(vat_7, 16) * 0.0001
        	print "vat_7: ", vat_7_vol
            
	        vat_8 = data[-20:-16]
        	print (vat_8)
        	vat_8_vol = int(vat_8, 16) * 0.0001
        	print "vat_8: ", vat_8_vol
 
        	vat_9 = data[-16:-12]
        	print (vat_9)
        	vat_9_vol = int(vat_9, 16) * 0.0001
        	print "vat_9: ", vat_9_vol
 
        	vat_10 = data[-12:-8]
        	print (vat_10)
        	vat_10_vol = int(vat_10, 16) * 0.0001
        	print "vat_10: ", vat_10_vol
 
        	vat_11 = data[-8:-4]
        	print (vat_11)
        	vat_11_vol = int(vat_11, 16) * 0.0001
        	print "vat_11: ", vat_11_vol

	        vat_12 = data[-4:]
        	print (vat_12)
        	vat_12_vol = int(vat_12, 16) * 0.0001
        	print "vat_12: ", vat_12_vol
           

#	ts.set_debug_mode()
	ts.update_values_of_interest()
	lc.update_values_of_interest()
#	print postTableData(ts.get_current(), ts.get_voltage(), 0, 0, 5)
#
#	postTableData(ts.get_current(), ts.get_voltage(), 0, 0, 5)   
#	postTristarData(ts,lc)
#	postTristarDataTest()
	time.sleep(1) #time of sleep is in seconds
	if vat_1_vol > 3.6 or vat_2_vol > 3.6 or vat_3_vol > 3.6 or vat_4_vol > 3.6 or vat_5_vol > 3.6 or vat_6_vol > 3.6 or  vat_7_vol > 3.6 or  vat_8_vol > 3.6 or vat_9_vol > 3.6 or vat_10_vol > 3.6 or vat_11_vol > 3.6 or  vat_12_vol > 3.6:
		if dFlag:
			print ("Charge controller disconnected")
			time.sleep(1)		
		elif not dFlag:		
			#1 for disconnect charge and 0 to reconnect charge
			ts.wr = ts.client.write_coil(2,1)
			print "disconnecting charge controller...\n"
			dFlag = 1
			time.sleep(1)
		
	//battery lower limit is 2.8 but keep above 3.1 so it doesn’t drain battery
	elif vat_1_vol < 3.1 or vat_2_vol < 3.1or vat_3_vol <3.1 or vat_4_vol < 3.1 or vat_5_vol < 3.1 or vat_6_vol <3.1  or  vat_7_vol  < 3.1 or  vat_8_vol  < 3.1 or vat_9_vol < 3.1 or vat_10_vol < 3.1 or vat_11_vol  < 3.1 or vat_12_vol  < 3.1: 
		if dFlag:
			print ("Load controller disconnected")
			time.sleep(1)		
		if not dFlag:		
			dFlag = 1
			print "disconnecting load controller...\n"
			#1 for desconnect charge
			lc.qr = lc.client.write_coil(1,1)
			#to reconnect load controller run the below command and comment out the above command to reset
			#lc.qr = lc.client.write_coil(255,1)
			time.sleep(1)
		
	elif dFlag:
		If (vat_1_vol <= 3.3 or vat_2_vol <= 3.3 or vat_3_vol <= 3.3 or vat_4_vol <= 3.3 or vat_5_vol <= 3.3 or vat_6_vol <= 3.3 or vat_7_vol <= 3.3 or vat_8_vol <= 3.3 or vat_9_vol <= 3.3 or vat_10_vol <= 3.3 or vat_11_vol <= 3.3 or vat_12_vol <= 3.3):
		print ("reconnecting charge controller...")
		dFlag = 0
		ts.wr = ts.client.write_coil(2,0)
		time.sleep(1)
		if (vat_1_vol >= 3.1 or vat_2_vol >= 3.1 or vat_3_vol >= 3.1 or vat_4_vol >= 3.1 or vat_5_vol >= 3.1 or vat_6_vol >= 3.1  or vat_7_vol >= 3.1  or vat_8_vol >= 3.1  or vat_9_vol >= 3.1  or vat_10_vol >= 3.1  or vat_11_vol >= 3.1  or vat_12_vol >= 3.1):
		print ("reconnecting load controller...")
		dFlag = 0
		lc.qr = lc.client.write_coil(255, 1)
		time.sleep(1)
	else:
		dFlag = 0
		print "Sent Data\n"
		time.sleep(1)

ts.close_meter()
lc.close_meter()

