import os
from sys import version
from fpdf import FPDF

print( ">> Obteniendo listado de programas (esto puede tardar unos segundos)..." )
os.system( "wmic /output: wmic.txt product get installdate,version,vendor,name" )
print( ">> Listado de programas obtenido." )

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 12)

wmic = open('wmic.txt', 'r')

pdf.cell( 200, 1, txt="PRUEBA", ln=1, align='C' )
x=wmic.readline()
pdf.multi_cell( 200, 10, txt=x, ln=1, align='L' )

pdf.output('file.pdf')

print()

wmic.close()