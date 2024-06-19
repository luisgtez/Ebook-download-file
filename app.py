from flask import Flask, redirect, send_file, render_template
import os
import sys

app = Flask(__name__)


@app.route("/")
def root():
    files = get_file_epub_pdf(os.listdir())
    file = files[0]
    print("Enviando único archivo: ", file)
    return send_file(file, as_attachment=True)

def check_unique_file_epub_pdf(files):
    files_epub_pdf = get_file_epub_pdf(files)
    if len(files_epub_pdf) != 1:
        return False
    return True


def get_file_epub_pdf(files):
    files_epub_pdf = [x for x in files if x.endswith(".pdf") or x.endswith(".epub")]
    return files_epub_pdf


if __name__ == "__main__":
    if check_unique_file_epub_pdf(os.listdir()):

        print("---------------------------------------------------------------------------")
        print("Se encontró un único archivo .pdf o .epub en el directorio actual:")
        print("*  ", get_file_epub_pdf(os.listdir())[0])
        print("Sirviendo archivo...")
        print("---------------------------------------------------------------------------")

        app.run(debug=False, host="0.0.0.0", port=5001)
 
    else:
        
        print("---------------------------------------------------------------------------------------------------------------------")
        print(
            "Error: Se esperaba un único archivo .pdf o .epub en el directorio actual. Se encontraron los siguientes archivos: "
        )
        for file in get_file_epub_pdf(os.listdir()):
            print("*  ", file)
        print("---------------------------------------------------------------------------------------------------------------------")

        sys.exit(1)
