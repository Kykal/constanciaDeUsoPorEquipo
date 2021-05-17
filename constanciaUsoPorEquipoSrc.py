import os
from fpdf import FPDF
import subprocess
from datetime import date
from datetime import datetime

#Obtención de datos del usuario
username = input( "\nNombre completo de la persona a cargo de esta computadora: " )
userCURP = input( "CURP de la persona que está a cargo de esta computadora: " )
username = username.title()
userCURP = userCURP.upper()

tempUsername = "Nombre: %s" %username
tempUserCURP = "CURP: %s" %userCURP

print("\nObteniendo datos, por favor, espere...")

#Obtención de listado de hardware y programas del equipo
print( "\n>> Obteniendo dirección MAC..." )
os.system( "getmac > getmac.txt" )
print( ">> Dirección MAC obtenida." )
getmac = open( "getmac.txt", "r" )

print( ">> Obteniendo número de serie del equipo..." )
os.system( "wmic bios get serialnumber > serialnumber.txt" )
serialNumber = open( 'serialNumber.txt' )
print( ">> Número de serie del equipo obtenido." )

print( ">> Obteniendo listado de hardware..." )
os.system( "dxdiag /t dxdiag.txt" )
dxdiag = open("dxdiag.txt", "r")
print( ">> Listado de hardware obtenido." )

print( ">> Obteniendo listado de programas..." )
os.system( "wmic /output: wmic.txt product get installdate,version,vendor,name /format:table" )
wmic = open( 'wmic.txt', 'r' )
print( ">> Listado de programas obtenido." )

#Se prepara el .pdf
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 14)

#Se abre el archivo 'dxdiag.txt', se obtienen sus datos y se cierra.
for x in range(0, 4) :
    dxdiag.readline()
nombreEquipo = dxdiag.readline().strip().split()[2]
tempNombreEquipo = str( "NOMBRE DEL EQUIPO: %s" %nombreEquipo )
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

#Se abre el archivo 'serialNumber.txt', se obtiene el número de serie del equipo y se cierra.
for x in range(0, 2) :
    serialNumber.readline()
numeroSerie = serialNumber.readline()

tempNumeroSerie = "EQUIPO: "+numeroSerie

serialNumber.close()
os.remove('serialNumber.txt')

#Se escriben datos al .pdf
pdf.cell( 200, 8, txt="CONSTANCIA DE SOFTWARE DE USO POR EQUIPO",ln=1, align = 'C' )
pdf.cell( 200, 10, txt="------------------------------------------------------------------------------------------", ln=1, align='C')
pdf.set_font_size(9)
pdf.cell( 200, 7, txt=tempNumeroSerie, ln=1, align='J' )
pdf.cell( 200, 7, txt=tempNombreEquipo, ln=1, align='J' )
pdf.cell( 200, 7, txt=direccionMAC, ln=1, align='J'  )
pdf.cell( 200, 7, txt=descripcionEquipo, ln=1, align='J'  )
pdf.cell( 200, 7, txt=memoriaEquipo, ln=1, align='J'  )
pdf.set_font_size(14)
pdf.cell( 200, 10, txt="------------------------------------------------------------------------------------------", ln=1, align='C')
pdf.set_font_size(6)
for x in wmic :
    pdf.multi_cell(0, 4, txt=x, align='L')

fechaHoy = date.today()
fechaHoy = fechaHoy.strftime("%d/%m/%Y")
tempFechaHoy = "Fecha de firma de documento (DD/MM/AAAA): "+fechaHoy

pdf.set_font_size(14)
pdf.cell( 200, 10, txt="------------------------------------------------------------------------------------------", ln=1, align='C')
pdf.set_font_size(9)
pdf.cell(200, 5, txt=tempUserCURP, ln=1, align='L')
pdf.cell(200, 5, txt=tempUsername, ln=1, align='L')
pdf.cell(200, 5, txt=tempFechaHoy, ln=1, align='L')
pdf.cell(200, 5, txt="Firma:", ln=1, align='L')

fechaHoy = date.today()
horaHoy = datetime.now()
fechaHoy = fechaHoy.strftime("%d-%m-%Y")
horaHoy = horaHoy.strftime("%H-%M-%S")

filename = nombreEquipo+"_"+userCURP+"_"+fechaHoy+"_"+horaHoy+".pdf"

pdf.output(filename)

wmic.close()
os.remove( "wmic.txt" )

subprocess.Popen(filename, shell=True)