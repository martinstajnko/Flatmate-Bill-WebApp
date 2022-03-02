from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Add some text
pdf.set_font(family='Times', size=12, style='B')
pdf.cell(w=60, h=20, txt='Flatmate Bill', border=1, align='C')
pdf.cell(w=60, h=20, txt='Period: March', border=1, align='C')
#pdf.cell(w=60, h=20, txt='Payment: 250€', border=1, align='C', ln=1)
# pdf.cell(w=180, h=60, txt='Flatmate Marry', border=1, align='C')
# pdf.cell(w=120, h=60, txt='Period: March', border=1, align='C')
# pdf.cell(w=120, h=60, txt='Payment: 180€', border=1, align='C', ln=1)
pdf.output('bill.pdf')