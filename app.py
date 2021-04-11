from pywebio.input import textarea, input
from pywebio import start_server
from pywebio.output import put_text
from fpdf import FPDF

FONTS = ['Helvetica', 'Calibri', 'Futura', 'Garamond', 'Times New Roman',
         'Arial', 'Cambria', 'Verdana', 'Rockwell', 'Franklin Gothic']


def app_main():
    add_more = True
    pages = []

    while add_more:
        page = textarea("Please insert the text for your PDF file",
                        placeholder="Type anything you like")
        pages.append(page)

        add_more = actions(label="Would you like to add another page?",
                           buttons=[{'label': 'Yes', 'value': True},
                                    {'label': 'No', 'value': False}])

    save_location = input("What is the name of your PDF file?")
    create_pdf(pages, font='Arial', size=16, save_location=save_location)
    put_text("Congratulations! A PDF file is generated for you.")


def create_page(pdf, text: str, font: str, size: int):
    pdf.add_page()
    pdf.set_font('arial', '', 16)

    lines = text.split('\n')
    for i, sent in enumerate(lines):
        pdf.cell(40, 10, sent, 0, i + 1)


def create_pdf(pages: list, font: str, size: int, save_location: str = "output.pdf"):
    pdf = FPDF()

    for page in pages:
        create_page(pdf, page, font, size)

    pdf.output(save_location, 'F')


if __name__ == '__main__':
    start_server(app_main, port=36535, debug=True)
