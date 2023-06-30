import serial,time,csv
arduino = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)

boton = (arduino.readline())
botonV = boton[0:][:-2]
valorB1 = botonV.decode('utf-8')
botonF = valorB1.strip('b')
#print(boton)
dedo1 = (arduino.readline())
dedo1V = dedo1[0:][:-2]
valorD1 = dedo1V.decode('utf-8')
valorFD1 = valorD1.strip('b')
#print(dedo1)
dedo2 = (arduino.readline())
dedo2V = dedo2[0:][:-2]
valorD2 = dedo2V.decode('utf-8')
valorFD2 = valorD2.strip('b')
##print(dedo2)
dedo3 = (arduino.readline())
dedo3V = dedo3[0:][:-2]
valorD3 = dedo3V.decode('utf-8')
valorFD3 = valorD3.strip('b') 
##print(dedo3)
dedo4 = (arduino.readline())
dedo4V = dedo4[0:][:-2]
valorD4 = dedo4V.decode('utf-8')
valorFD4 = valorD4.strip('b')
##print(dedo4)
dedo5 = (arduino.readline())
dedo5V = dedo5[0:][:-2]
valorD5 = dedo5V.decode('utf-8')
valorFD5 = valorD5.strip('b')
##print(dedo5)
arduino.close()
valores =[
    [valorFD1,valorFD2,valorFD3,valorFD4,valorFD5],
]
with open('valoresSensor.cvs','a',newline='')as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerows(valores)
