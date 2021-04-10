from pywebio.input import textarea, input
from pywebio import start_server
from pywebio.output import output
from fpdf import FPDF


def app_main():
    text = textarea("Enter your text to generate pdf",
                    placeholder="Input text", required=True)

    save_location = input("Enter a name for your input file",
                          required=True)
    put_text("Tadaaa.." + save_location + "pdf is generated.")


def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('arial', '', 16)

    lines = text.split('\n')
    for i, sent in enumerate(lines):
        pdf.cell(40, 10, sent, 0, i + 1)

    pdf.output(save_location, 'F')


if __name__ == '__main__':
    start_server(app_main, port=36535, debug=True)
