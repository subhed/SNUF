import serial
import SendKeys
import os
ser = serial.Serial('/dev/ttyACM1', 9600)
#os.system('start "C:\Games\StepMania 5\Program\StepMania.exe"')
LButton = False;
RButton = False;
UButton = False;
DButton = False;
BButton = False;
SButton = False;
while 1:
	x=ser.read()
	print x
	if x == 'l':
		LButton = not LButton
		if LButton:SendKeys.key_down(39)
		else: SendKeys.key_up(39)
	elif x == 'r':
		RButton = not RButton
		if RButton:SendKeys.key_down(37)
		else: SendKeys.key_up(37)
	elif x == 'u':
		UButton = not UButton
		if UButton:SendKeys.key_down(40)
		else: SendKeys.key_up(40)
	elif x == 'd':
		DButton = not DButton
		if DButton:SendKeys.key_down(38)
		else: SendKeys.key_up(38)
	elif x == 's':
		SButton = not SButton
		if SButton:SendKeys.key_down(13)
		else: SendKeys.key_up(13)
	elif x == 'b':
		BButton = not BButton
		if BButton:SendKeys.key_down(8)
		else: SendKeys.key_up(8)
	else:
		pass


ser.close()
