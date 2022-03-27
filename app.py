import re
from flask import Flask, render_template, request, send_file
app = Flask(__name__)



# Vamos começar!
@app.route('/')
@app.route('/parte-1')
def main_page():
    return render_template('info.htm')  

@app.route('/resultados', methods=('GET', 'POST'))
def results():

    mensagem = """À

(nome da instituição requerida)

(nome do requerente), inscrito(a) no CPF sob o nº (cpf) e RG nº (rg), brasileiro(a), (estado civil), residente à rua (rua), nº (cep), vem requerer marcação de audiência para fim de esclarecimentos acerca do processo judicial n.º (processo).

Termos em que pede deferimento.

(cidade), (dia) de (mês) de (ano).

(Assinatura do requerente)"""

    if request.method == "GET":
        return f"Trying to reach to the content!"

    if request.method == 'POST':
        form_data = request.form

        result_1 = mensagem.replace("(nome da instituição requerida)", form_data["Nome da instituição"])
        result_2 = result_1.replace("(nome do requerente)", form_data["Nome do requerente"])
        result_3 = result_2.replace("(cpf)", form_data["CPF"])
        result_4 = result_3.replace("(rg)", form_data["Rg"])
        result_5 = result_4.replace("(estado civil)", form_data["Estado civil"])
        result_6 = result_5.replace("(rua)", form_data["rua"])
        result_7 = result_6.replace("(cep)", form_data["Cep"])
        result_8 = result_7.replace("(processo)", form_data["Número de processo"])
        result_9 = result_8.replace("(cidade)", form_data["Cidade"])

        with open("test.txt", 'w') as arquivo:
            arquivo.write(result_9)
            arquivo.close()

        
        path = 'test.txt'
        return send_file(path, as_attachment = True)

        


    


if __name__ == "__main__": # Just to set Debug mode on
    app.run(debug=True)