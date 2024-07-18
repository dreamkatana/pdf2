from fpdf import FPDF

pdf = FPDF()
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font('helvetica', 'BIU', size=12)
pdf.cell(40, 10, text="hello world", border=1)
pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C', border=1)

pdf.output("hello_world2.pdf")