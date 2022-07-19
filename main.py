from PIL import Image, ImageFont, ImageDraw
from flask import Flask, render_template, request, send_file
app = Flask(__name__)
#######################################################################################
def gerar_doc(nm, rg, cpf, ende, bairro, cidade, uf, cep, placa, rena, anoF, anoM, MarMod, cha):

    my_image = Image.open('test\procuracao.png') # Open the image

    font_to_be_used = ImageFont.truetype('font\Inter-VariableFont_slnt,wght.ttf', 25) # Select the font

    draw = ImageDraw.Draw(my_image) # --> Editable image

    #########################################################
    # - Fields -> Outorgante:

    # Nome da empresa
    draw.text(xy=(300, 977), text=nm, fill=(0,0,0), font=font_to_be_used)

    # RG
    draw.text(xy = (150, 1017), text=rg, fill=(0,0,0), font=font_to_be_used)

    # CPF
    draw.text(xy = (700, 1017), text=cpf, fill=(0,0,0), font=font_to_be_used)

    # Endereço
    draw.text(xy = (230, 1056), text=ende, fill=(0,0,0), font=font_to_be_used)

    # Bairro
    draw.text(xy = (208, 1094), text=bairro, fill=(0,0,0), font=font_to_be_used)
    
    # Cidade
    draw.text(xy = (886, 1094), text=cidade, fill=(0,0,0), font=font_to_be_used)
    
    # UF
    draw.text(xy = (150, 1133), text=uf, fill=(0,0,0), font=font_to_be_used)
    
    # CEP
    draw.text(xy = (340, 1133), text=cep, fill=(0,0,0), font=font_to_be_used)

    ##---------------------------------------------------------------------------------##
    # Fields -> Dados do Veículo
    
    # Placa
    draw.text(xy=(194, 1253), text=placa, fill=(0,0,0), font=font_to_be_used)

    # RENAVAM
    draw.text(xy=(649, 1253), text=rena, fill=(0,0,0), font=font_to_be_used)

     # Ano/Fab
    draw.text(xy=(988, 1253), text=anoF, fill=(0,0,0), font=font_to_be_used)

    # Ano/Mod
    draw.text(xy=(1280, 1253), text=anoM, fill=(0,0,0), font=font_to_be_used)

     # Marca/Modelo
    draw.text(xy=(320, 1291), text=MarMod, fill=(0,0,0), font=font_to_be_used)

    # Chassi
    draw.text(xy=(920, 1291), text=cha, fill=(0,0,0), font=font_to_be_used)
##################################################################################################

    my_image.show()

# Vamos começar!
@app.route('/')
@app.route('/parte-1')
def main_page():
    return render_template('main.html')  

@app.route('/resultados', methods=('GET', 'POST'))
def results():

    if request.method == "GET":
        return render_template('main.html')

    elif request.method == 'POST':
        form_data = request.form

        nome_da_empresa =  form_data["nome_da_empresa"]
        rg = form_data["RG"]
        cpf = form_data["CPF"]
        endereco = form_data["Endereço"]
        bairro = form_data["Bairro"]
        cidade = form_data["Cidade"]
        uf = form_data["UF"]
        cep = form_data["CEP"]
        placa = form_data["Placa"]
        renavam = form_data["Renavam"]
        af = form_data['Ano_fab']
        am = form_data['Ano_mod']
        mm = form_data["Marca_modelo"]
        cha = form_data["Chassi"]

        gerar_doc(nome_da_empresa, rg=rg, cpf=cpf, ende=endereco, bairro=bairro, cidade=cidade, uf=uf, cep=cep, placa=placa, rena=renavam, anoF=af, anoM=am, MarMod=mm, cha=cha  )
        '''
        p1 = nome_da_empresa

        image_editable.text((15, 15), p1, (9, 10, 10), font = font_to_be_used )
        '''

        return render_template('image.html')


    


if __name__ == "__main__": # Just to set Debug mode on
    app.run(debug=True)
