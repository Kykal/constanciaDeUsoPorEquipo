from locale import normalize
from fpdf import FPDF
import os

os.system( "wmic /output: wmicTemp.txt product get vendor,installdate,version,name /format:csv" )
wmicTemp = open('./wmicTemp.txt', 'rb') # Open file, read in binaries
wmicWrite = open( 'wmic.txt', 'w+' )
contents = wmicTemp.read() # Read content
contents = contents.decode('utf-16') # Decode
lines = contents.split('\n') # Separate the whole string by \n
lines = lines[1:len(lines)] # Remove first \r line
headers = lines[0] # Extract headers
info = [line.replace('\r','').split(',')[1:5] for line in lines[2:len(lines)]] # List of lists of information

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 14)
pdf.cell( 200, 10, txt="Instalación Versión\t\tEditor\tNombre del producto", ln=1, align='L' )

nuevaLista = []

# Iterate through info list
for i in range(len(info)) :
    nuevaLista.clear()
    fecha = info[i][0]
    ver = info[i][3]
    editor = info[i][2]
    nombre = info[i][1]

    nuevaLista.append( fecha )
    nuevaLista.append( ver )
    nuevaLista.append( editor )
    nuevaLista.append( nombre )

    nuevoTexto = ' '.join(nuevaLista)

    textoString = str(nuevoTexto)

    wmicWrite.write(textoString+"\n")
    del nuevoTexto

wmicWrite.close()
wmic = open('wmic.txt', 'r')

for x in wmic :
    pdf.cell( 200, 10, txt=x, ln=1, align='L' )
    print(x)

pdf.output('test.pdf')
wmicTemp.close()
wmic.close()

os.remove('wmic.txt')
os.remove('wmicTemp.txt')