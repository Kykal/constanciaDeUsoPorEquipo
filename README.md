# Instrucciones de descarga

Debido a que es un ejecutable nuevo es probable que al momento de descargar el .rar [Google Chrome](https://www.google.com/intl/es_mx/chrome/) no permita descargarlo por sospechas de virus. Esto es un falso positivo por la manera en la que se compiló, pero es totalmente seguro esto declarado por [Microsoft Security Intelligence](https://www.microsoft.com/en-us/wdsi/submission/9c5b8dbd-b6a9-4784-82b0-4d5ff8bae2fd):
![imagen](https://user-images.githubusercontent.com/54295964/119240891-774bd600-bb18-11eb-9ddb-2f7894ed364d.png)

Para [descargarlo](https://github.com/Kykal/constanciaDeUsoPorEquipo/releases/tag/v1.0) sugiero hacerlo desde el navegador web [Mozilla Firefox](https://www.mozilla.org/es-MX/firefox/new/) y después actualizar las definiciones de seguridad de Windows Defender siguiendo los pasos siguientes:
1. Abrir un CMD/PowerShell y cambiar la dirección a ``C:\Program Files\Windows Defender``
2. Escribir el comando ``MpCmdRun.exe -removedefinitions -dynamicsignatures``
3. Escribir el comando ``MpCmdRun.exe -SignatureUpdate``

Para que así, con la definición actualizada, no detecte el ejecutable como un virus.

# Instrucciones de uso
1. Hacer doble clic en el ejecutable ``constanciaUsoPorEquipoApp.exe``.
2. Seguir los pasos que el ejecutable indique:
  - Ingresar el nombre completo de la persona a cargo de la computadora en la cual se ejecute el código.
  - Ingresar el CURP de la persona a cargo de la computadora en la cual se ejecuta el código.
  - Esperar a que obtenga toda la información necesaria.
  - Se abrirá un documento en formato pdf, se puede cerrar el ejecutable.

## Comportamiento
Mientras se esté obteniendo la información, en el lugar en donde el usuario alojó el ejecutable se empezarán a crear archivos ``.txt``, estos son totalmente temporales y sirven para la obtención de la información necesaria. Una vez que el programa no los requiera serán borrados de la computadora. Se generará un archivo ``.pdf`` al final que es el resultado y objetivo del programa.
