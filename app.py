from pywebio.input import textarea, input
from pywebio import start_server
from pywebio.output import output


def app_main():
    text = textarea("Enter your text to generate pdf",
                    placeholder="Input text", required=True)

    save_location = input("Enter a name for your input file",
                          required=True)
    put_text("Tadaaa.." + save_location + "pdf is generated.")


if __name__ == '__main__':
    start_server(app_main, port=36535, debug=True)
