# Sistema de monitoreo y alarma.

• Sistema de control de iluminación y Angulo de giro para una incubadora.

Materiales|
------------- 
* 1 Arduino Uno
* 1 Servo Motor
* 1 Sensor de Luz LDR
* 4 Botones
* 1 Potenciometro
* 2 Leds (Rojo y Verde)

Control de iluminación:
El porcentaje de iluminacion será dado por el sensor Idr, el led rojo sera la señal de máxima iluminación y verde minima iluminación. 
El porcentaje de max y minima iluminacion sera configurado por el usuario atravez de los pulsadores (20,40,60) seran valores acumulativos para setar la máxima iluminacion, la minima sera calculado: max-40%

En la interfaz de python se visualiza la configuracion max y min. Una con checkbuttom para control por potenciometro o por slider del Angulo del motor.
Se envia a la base de datos: % de iluminacion, valor para alarma de valor max y alarma de valor min

Simulacion: https://wokwi.com/projects/355571767522030593
