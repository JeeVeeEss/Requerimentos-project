from PIL import ImageDraw, ImageFont, Image

def gerar_doc():

    my_image = Image.open('test\procuracao.png') # Open the image

    font_to_be_used = ImageFont.truetype('font\Inter-VariableFont_slnt,wght.ttf', 25) # Select the font

    draw = ImageDraw.Draw(my_image) # --> Editable image

    #########################################################
    # - Fields -> Outorgante:

    # Nome da empresa
    draw.text(xy=(300, 977), text="Facebook", fill=(0,0,0), font=font_to_be_used)

    # RG
    draw.text(xy = (150, 1017), text="1081", fill=(0,0,0), font=font_to_be_used)

    # CPF
    draw.text(xy = (700, 1017), text="140.41.51.2.1-54", fill=(0,0,0), font=font_to_be_used)

    # Endereço
    draw.text(xy = (230, 1056), text="Rua do cérebro", fill=(0,0,0), font=font_to_be_used)

    # Bairro
    draw.text(xy = (208, 1094), text="Bairro Cabeça", fill=(0,0,0), font=font_to_be_used)
    
    # Cidade
    draw.text(xy = (886, 1094), text="Cidade do Conhecimento", fill=(0,0,0), font=font_to_be_used)
    
    # UF
    draw.text(xy = (150, 1133), text="AL", fill=(0,0,0), font=font_to_be_used)
    
    # CEP
    draw.text(xy = (340, 1133), text="57.061-410", fill=(0,0,0), font=font_to_be_used)

    ##---------------------------------------------------------------------------------##
    # Fields -> Dados do Veículo
    
    # Placa
    draw.text(xy=(194, 1253), text="MUA1902", fill=(0,0,0), font=font_to_be_used)

    # RENAVAM
    draw.text(xy=(649, 1253), text="10101010101", fill=(0,0,0), font=font_to_be_used)

     # Ano/Fab
    draw.text(xy=(988, 1253), text="2022", fill=(0,0,0), font=font_to_be_used)

    # Ano/Mod
    draw.text(xy=(1280, 1253), text="2023", fill=(0,0,0), font=font_to_be_used)

     # Marca/Modelo
    draw.text(xy=(320, 1291), text="Renault/Clio", fill=(0,0,0), font=font_to_be_used)

    # Chassi
    draw.text(xy=(920, 1291), text="asjhfdçoawehfoiadif", fill=(0,0,0), font=font_to_be_used)


    my_image.show()



gerar_doc()