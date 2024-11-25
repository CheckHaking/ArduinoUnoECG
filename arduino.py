import serial
import time

arduino_port = "COM6" #Aqui se escribe el nombre del puerto serial donde tenemos conectado el arduino
baud_rate = 9600 #Este valor tiene que ser el mismo que le cargamos a nuestro arduino 
timeout = 1 #Tiempo de espera de la conexion

#Archivo donde se guardaran los datos
output_file = 'file.txt'

try:
    #Conexion serial
    ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
    time.sleep(2)# Espera para la conexion
    
    with open(output_file, "w") as file:
        print("Leyendo datos de Arduino.... Presiona ctrl + c para detener")
        
        while True : 
            # Lee la línea de datos del Arduino
            line = ser.readline().decode('utf-8').strip()
            
            # Guarda la línea en el archivo
            if line:
                print(f'Dato recibido: {line}')
                file.write(line + '\n')
                
except KeyboardInterrupt:
    #Manejo de interrupocion de teclado 
    print("Lectura finalizada")
    
except Exception as e:
    print(f'Ocurrio un error inesperado:{e}')
    
finally:
    #Cerrar conexion serial abierta
    if ser.is_open:
        ser.close()
        print("Conexion cerrada")
    
                
            