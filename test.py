import os
from fpdf import FPDF
import subprocess

#Obtención de datos del usuario
username = input( "\nNombre completo de la persona a cargo de esta computadora: " )
userjob = input( "Puesto del trabajo de la persona a cargo de esta computadora: " )
userCURP = input( "CURP de la persona que está a cargo de esta computadora: " )
username = "Nombre: %s" %username
userjob = "Puesto: %s" %userjob
userCURP = "CURP: %s" %userCURP

print("\nObteniendo datos, por favor, espere...")

#Obtención de listado de hardware y programas del equipo
print( "\n>> Obteniendo listado de hardware..." )
os.system( "dxdiag /t dxdiag.txt" )
dxdiag = open("dxdiag.txt", "r")
print( ">> Listado de hardware obtenido." )

print( ">> Obteniendo listado de programas..." )
os.system( "wmic /output: wmic.csv product get vendor,installdate,version,name" )
wmic = open("wmic.csv", "r")
print( ">> Listado de programas obtenido." )

print( ">> Obteniendo dirección MAC..." )
os.system( "getmac > getmac.txt" )
print( ">> Dirección MAC obtenida." )
getmac = open( "getmac.txt", "r" )

#Se prepara el .pdf
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 14)

#Se abre el archivo 'dxdiag.txt', se obtienen sus datos y se cierra.
for x in range(0, 4) :
    dxdiag.readline()
nombreEquipo = dxdiag.readline().strip().split()[2]
nombreEquipo = str( "NOMBRE DEL EQUIPO: %s" %nombreEquipo )
for x in range(0, 6) :
    dxdiag.readline()
descripcionEquipo = ' '.join(dxdiag.readline().strip().split()[1:])
descripcionEquipo = str( "DESCRIPCIÓN: %s" %descripcionEquipo )
memoriaEquipo =  dxdiag.readline().strip().split()[1]
memoriaEquipo = memoriaEquipo.replace('MB', '')
memoriaEquipo = float( memoriaEquipo )
memoriaEquipo = memoriaEquipo/1024
memoriaEquipo = str( "MEMORIA INSTALADA: %i GB" %memoriaEquipo )
dxdiag.close()
os.remove( "dxdiag.txt" )

#Se abre el archivo 'getmac.txt', obtiene la dirección MAC y se cierra
for x in range(0, 3):
    getmac.readline()
direccionMAC = getmac.readline().split()[0]
direccionMAC = str( "DIRECCIÓN MAC: %s" %direccionMAC)
getmac.close()
os.remove( "getmac.txt" )

#Se escriben datos al .pdf
pdf.cell( 200, 8, txt="CONSTANCIA DE SOFTWARE DE USO POR EQUIPO",ln=1, align = 'C' )
pdf.cell( 200, 10, txt="------------------------------------------------------------------------------------------", ln=1, align='C')
pdf.set_font_size(9)
pdf.cell( 200, 7, txt=nombreEquipo, ln=1, align='J' )
pdf.cell( 200, 7, txt=direccionMAC, ln=1, align='J'  )
pdf.cell( 200, 7, txt=descripcionEquipo, ln=1, align='J'  )
pdf.cell( 200, 7, txt=memoriaEquipo, ln=1, align='J'  )
pdf.set_font_size(14)
pdf.cell( 200, 10, txt="------------------------------------------------------------------------------------------", ln=1, align='C')
pdf.set_font_size(6)
for x in wmic :
    pdf.cell(0, 5, txt=x, ln=1, align='L')

pdf.output("infoDiag.pdf")

wmic.close()
#os.remove( "wmic.txt" )

subprocess.Popen("infoDiag.pdf", shell=True)