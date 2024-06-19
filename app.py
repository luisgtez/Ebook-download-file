from flask import Flask, redirect, send_file
import os
app = Flask(__name__)

@app.route("/alas")
def redirigir_a_archivo():
    url_externa = "https://ia904500.us.archive.org/9/items/1234567_202312/Alas_de_sangre_Rebecca_Yarros.pdf"
    return redirect(url_externa)

@app.route("/")
def root():
    print("Listando archivos en directorio actual: ", os.getcwd())
    files = os.listdir()
    files_epub_pdf = [x for x in files if x.endswith(".pdf") or x.endswith(".epub")]
    if len(files_epub_pdf) != 1:
        file =""
        print("No se encontró epub o pdf unico. Enviando archivo:", file) 
        return send_file(file, as_attachment=True)
    
    else:
        file = files_epub_pdf[0]
        print("Enviando único archivo: ", file)
        return send_file(file, as_attachment=True)

# @app.route("/")
# def root():
#     return "Hola mundo"

if __name__ == "__main__":
# flask run --host=192.168.1.223 --port=5001
    app.run(debug=False, host='192.168.1.223', port=5001)

