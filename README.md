Queda estrictamente prohibido el uso total o parcial del código fuente de este [repositorio](https://github.com/Kykal/constanciaDeUsoPorEquipo), esto protegido por el [uso de licencias por parte de GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#choosing-the-right-license).

# Instrucciones de descarga:

Debido a que es un ejecutable nuevo es probable que al momento de descargar el .rar [Google Chrome](https://www.google.com/intl/es_mx/chrome/) no permita descargarlo por sospechas de virus. Esto es un falso positivo por la manera en la que se compiló, pero es totalmente seguro esto declarado por [Microsoft Security Intelligence](https://www.microsoft.com/en-us/wdsi/submission/9c5b8dbd-b6a9-4784-82b0-4d5ff8bae2fd):
![imagen](https://user-images.githubusercontent.com/54295964/119240891-774bd600-bb18-11eb-9ddb-2f7894ed364d.png)

Para [descargarlo](https://github.com/Kykal/constanciaDeUsoPorEquipo/releases/tag/v1.0) sugiero hacerlo desde el navegador web [Mozilla Firefox](https://www.mozilla.org/es-MX/firefox/new/) y después actualizar las definiciones de seguridad de Windows Defender siguiendo los pasos siguientes:
1. Abrir un CMD/PowerShell y cambiar la dirección a ``C:\Program Files\Windows Defender``
2. Escribir el comando ``MpCmdRun.exe -removedefinitions -dynamicsignatures``
3. Escribir el comando ``MpCmdRun.exe -SignatureUpdate``
Para que así, con la definición actualizada, no detecte el ejecutable como un virus.

# Instrucciones de uso:
1. Hacer doble clic en el ejecutable ``constanciaUsoPorEquipoApp.exe`` 
