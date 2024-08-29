from fpdf import FPDF
import glob

pdf = FPDF(orientation='P', unit='mm', format='A4')

files = glob.glob('Text+Files\\*.txt')

for file in files:
    with open(file, mode='r') as info:
        text = info.read()
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    animal = file.split('\\')[1].replace('.txt', '').capitalize()
    pdf.cell(w=50, h=10, txt=animal, ln=1)
    pdf.ln(10)
    pdf.set_font(family='Times', style='', size=12)
    pdf.multi_cell(w=0, h=10, txt=text)

pdf.output('animals_info.pdf')
