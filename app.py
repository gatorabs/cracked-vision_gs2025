from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from processamento import analyze_crack

UPLOAD_FOLDER = 'static/resultados'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
historico = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'imagem' not in request.files:
            return "Nenhum arquivo enviado", 400

        arquivo = request.files['imagem']
        if arquivo.filename == '':
            return "Nenhum arquivo selecionado", 400

        nome_seguro = secure_filename(arquivo.filename)
        caminho_original = os.path.join(app.config['UPLOAD_FOLDER'], nome_seguro)
        arquivo.save(caminho_original)

        nome_saida = f"resultado_{nome_seguro}"
        caminho_saida = os.path.join(app.config['UPLOAD_FOLDER'], nome_saida)

        resultado_path, status, area, comprimento = analyze_crack(caminho_original, caminho_saida)

        # Salva no histórico
        historico.insert(0, {
            'original': nome_seguro,
            'resultado': nome_saida,
            'status': status,
            'area': area,
            'comprimento': comprimento
        })

        return render_template("index.html",
                               imagem_original=nome_seguro,
                               imagem_resultado=nome_saida,
                               status=status,
                               area=area,
                               comprimento=comprimento,
                               historico=historico[:6])  # mostra os 6 mais recentes

    return render_template("index.html", historico=historico[:6])

@app.route("/limpar", methods=["POST"])
def limpar():

    historico.clear()

    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
