# Arduino ECG
# Proyecto de Lectura de Señal Cardíaca con Arduino y Módulo AD8232

Este proyecto tiene como objetivo la lectura de señales cardíacas utilizando un **Arduino Uno** y el módulo **AD8232** para el monitoreo del ECG (Electrocardiograma).

## Descripción

El código cargado en el Arduino se obtuvo de [este artículo](https://blog.uelectronics.com/tarjetas-desarrollo/arduino/como-realizar-la-programacion-conexion-del-modulo-ad8232-ecg-con-arduino-uno/) del blog de Uelectronics, donde se explica cómo realizar la programación y conexión del módulo **AD8232** con un **Arduino Uno**. Este módulo permite capturar y visualizar la señal cardíaca de una forma sencilla y económica.

## Componentes Utilizados

- **Arduino Uno**
- **Módulo AD8232** para la lectura de la señal ECG
- **Cables** y conexiones necesarias

## Instrucciones de Uso

### Paso 1: Preparación del Hardware

Conecta el módulo AD8232 al Arduino Uno siguiendo las instrucciones detalladas en el artículo mencionado.

### Paso 2: Carga del Código al Arduino

1. Abre el archivo con el código en el entorno de desarrollo de Arduino.
2. Conecta tu Arduino Uno a la computadora.
3. Selecciona el puerto y la placa correspondiente.
4. Carga el código en la placa.

### Paso 3: Configuración del Entorno Virtual

Para ejecutar el software de procesamiento de la señal cardíaca, se recomienda crear un entorno virtual en Python y usar las dependencias especificadas en el archivo `requirements.txt`.

#### Creación del Entorno Virtual

1. Asegúrate de tener **Python** y **pip** instalados en tu sistema.
2. Crea un entorno virtual ejecutando el siguiente comando:

    ```bash
    python -m venv env
    ```

3. Activa el entorno virtual:

    - En Windows:
    
      ```bash
      .\env\Scripts\activate
      ```
    
    - En macOS/Linux:
    
      ```bash
      source env/bin/activate
      ```

4. Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Paso 4: Ejecución

Con el entorno virtual activado y las dependencias instaladas, puedes ejecutar el código Python que procesa y muestra la señal cardíaca:

```bash
python nombre_del_archivo.py

###NOTAS:

Asegúrate de seguir las instrucciones de conexión adecuadamente para evitar daños en el hardware.
Para cualquier duda sobre el código cargado en el Arduino, consulta la fuente original en el blog de Uelectronics aquí https://blog.uelectronics.com/tarjetas-desarrollo/arduino/como-realizar-la-programacion-conexion-del-modulo-ad8232-ecg-con-arduino-uno/.
Este proyecto está diseñado para fines educativos y experimentales. No se recomienda su uso para diagnósticos médicos.
