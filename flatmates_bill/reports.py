from fpdf import FPDF
import webbrowser



class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Ad icon
        pdf.image('files/expenses_logo.jpeg', w=60, h=60)
        
        # Insert title
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=0, h=20, txt='Expenses payment', border=1, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=20, txt='Period:', border=1, align='C')
        pdf.cell(w=120, h=20, txt=bill.period, border=1, align='C', ln=1)

        # Total amount of expenses
        pdf.cell(w=140, h=20, txt='Total expenses:', border=1, align='C')
        pdf.cell(w=80, h=20, txt=str(bill.amount), border=1, align='C', ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=120, h=20, txt=flatmate1_pay, border=0, align='C', ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=120, h=20, txt=flatmate2_pay, border=0, align='C', ln=1)

        # If directory of the file does not work use line below:
        # os.chdir('files')

        # Output pdf
        pdf.output(f"files/{self.filename}")

        # Open pdf file in system, webbrowser etc. 
        #os.system(self.filename)
        webbrowser.open_new(f"files/{self.filename}")        

class FileSharer:

    def __init__(self, filepath, api_key=''):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url