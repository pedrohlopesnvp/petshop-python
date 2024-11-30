from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime
import os

# Funções
def open_image():
    # Obtém o caminho do arquivo da entrada de texto
    file_path = entry.get()
    
    try:
        # Abre a imagem usando PIL
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Redimensiona a imagem para caber na Label
        img_tk = ImageTk.PhotoImage(img)
        
        # Atualiza a Label com a nova imagem
        label_img.config(image=img_tk)
        label_img.image = img_tk
    except Exception as e:
        # Caso ocorra um erro (por exemplo, arquivo não encontrado)
        label_img.config(text=f"Erro: {str(e)}")
        label_img.image = None

def criar_tabela():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="petshop")
    
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

def adicionar_animal():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="petshop")
    cursor = conexao.cursor()

    animal = str(entrada2_animal.get())
    especie = str(entrada3_especie.get())
    raca = str(entrada4_raca.get())
    cor_predom = str(entrada5_cor_predom.get())
    data_str = entrada6_nascimento.get()
    nascimento = datetime.strptime(data_str, '%Y-%m-%d').date()
    observacao = str(entrada7_observacao.get())
    foto_animal = str(entrada8_foto_animal.get())
    tutor = str(entrada9_tutor.get())
    fone = str(entrada10_fone.get())

    sql = "INSERT INTO animais (animal, especie, raca, cor_predom, nascimento, observacao, foto_animal, tutor, fone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (animal, especie, raca, cor_predom, nascimento, observacao, foto_animal, tutor, fone)
    cursor.execute(sql, val)

    conexao.commit()
    conexao.close()

    print("Animal adicionado com sucesso.")
    messagebox.showinfo("Sucesso", "Animal adicionado com sucesso!")

def consultar_animal():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="petshop")
    cursor = conexao.cursor()

    cod_animal = str(entrada1_cod_animal.get())

    sql = "SELECT * FROM animais WHERE cod_animal = %s"
    val = (cod_animal,)
    cursor.execute(sql, val)

    # Recuperar todos os registros
    animais = cursor.fetchall()
    print(animais)

    conexao.close()

    print("Animal consultado com sucesso.")

    abrir_janela_imagem(animais)

def abrir_janela_imagem(animais):

    for animal in animais:
        this_animal = animal

    (id_animal, nome, especie, raca, cor, data_nascimento, obs, caminho_imagem, responsavel, telefone) = this_animal

    janela_imagem = Toplevel()
    janela_imagem.title(f"{nome} - {especie}")
    janela_imagem.geometry("290x550")

    clabel1_cod_animal = Label(janela_imagem, text=f"ID do Animal: {id_animal}")
    clabel1_cod_animal.grid(column=0, row=0, padx=15, pady=5, sticky='w')

    clabel1_nome = Label(janela_imagem, text=f"Nome: {nome}")
    clabel1_nome.grid(column=0, row=1, padx=15, pady=5, sticky='w')

    clabel1_especie = Label(janela_imagem, text=f"Espécie: {especie}")
    clabel1_especie.grid(column=0, row=2, padx=15, pady=5, sticky='w')

    clabel1_raca = Label(janela_imagem, text=f"Raça: {raca}")
    clabel1_raca.grid(column=0, row=3, padx=15, pady=5, sticky='w')

    clabel1_cor = Label(janela_imagem, text=f"Cor: {cor}")
    clabel1_cor.grid(column=0, row=4, padx=15, pady=5, sticky='w')

    clabel1_data_nascimento = Label(janela_imagem, text=f"Data de Nascimento: {data_nascimento}")
    clabel1_data_nascimento.grid(column=0, row=5, padx=15, pady=5, sticky='w')

    clabel1_obs = Label(janela_imagem, text=f"Observação: {obs}")
    clabel1_obs.grid(column=0, row=6, padx=15, pady=5, sticky='w')

    # clabel1_caminho_imagem = Label(janela_imagem, text=f"Caminho da imagem: {caminho_imagem}")
    # clabel1_caminho_imagem.grid(column=0, row=7, padx=15, pady=10, sticky='w')

    # Exibir Imagem

    # Adicionar o Label para a imagem
    img_label = Label(janela_imagem)
    img_label.grid(column=0, row=7, padx=15, pady=5)

    # Exibir Imagem
    try:
        img = Image.open(caminho_imagem)
        img = img.resize((250, 250))  # Redimensiona a imagem para caber no Label
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk  # Manter uma referência para a imagem
    except Exception as e:
        img_label.config(text=f"Erro ao carregar imagem: {str(e)}")

    clabel1_responsavel = Label(janela_imagem, text=f"Responsável: {responsavel}")
    clabel1_responsavel.grid(column=0, row=8, padx=15, pady=5, sticky='w')

    clabel1_telefone = Label(janela_imagem, text=f"Telefone do Responsável: {telefone}")
    clabel1_telefone.grid(column=0, row=9, padx=15, pady=5, sticky='w')
    
def atualizar_animal():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="petshop")
    cursor = conexao.cursor()

    cod_animal = str(entrada1_cod_animal.get())
    animal = str(entrada2_animal.get())
    especie = str(entrada3_especie.get())
    raca = str(entrada4_raca.get())
    cor_predom = str(entrada5_cor_predom.get())
    data_str = entrada6_nascimento.get()
    nascimento = datetime.strptime(data_str, '%Y-%m-%d').date()
    observacao = str(entrada7_observacao.get())
    foto_animal = str(entrada8_foto_animal.get())
    tutor = str(entrada9_tutor.get())
    fone = str(entrada10_fone.get())

    sql = "UPDATE animais SET animal=%s, especie=%s, raca=%s, cor_predom=%s, nascimento=%s, observacao=%s, foto_animal=%s, tutor=%s, fone=%s WHERE cod_animal = %s"
    val = (animal, especie, raca, cor_predom, nascimento, observacao, foto_animal, tutor, fone, cod_animal)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()

    print("Animal atualizado com sucesso.")
    messagebox.showinfo("Sucesso", "Animal atualizado com sucesso!")

def deletar_animal():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="petshop")
    cursor = conexao.cursor()
    
    cod_animal = str(entrada1_cod_animal.get())

    sql = "DELETE FROM animais WHERE cod_animal = %s"
    val = (cod_animal,)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()

    print("Animal excluído com sucesso.")
    messagebox.showinfo("Sucesso", "Animal excluído com sucesso!")

# Tela gráfica
janela = Tk()
janela.title("Petshop - PalPet")
janela.geometry('760x480')

# Entradas e Labels para informações do animal
label1_cod_animal = Label(janela, text="Código do animal:")
label1_cod_animal.grid(column=0, row=0, padx=15, pady=10, sticky='w')

entrada1_cod_animal = Entry(janela, width=10)
entrada1_cod_animal.grid(column=1, row=0, padx=5, pady=10, sticky='w')
# entrada1_cod_animal.config(state='disabled')

label2_animal = Label(janela, text="Digite o nome animal:")
label2_animal.grid(column=0, row=1, padx=15, pady=10, sticky='w')

entrada2_animal = Entry(janela, width=40)
entrada2_animal.grid(column=1, row=1, padx=5, pady=10, sticky='w')

label3_especie = Label(janela, text="Digite a especie do animal:")
label3_especie.grid(column=0, row=2, padx=15, pady=10, sticky='w')

entrada3_especie = Entry(janela, width=25)
entrada3_especie.grid(column=1, row=2, padx=5, pady=10, sticky='w')

label4_raca = Label(janela, text="Digite a raca do animal:")
label4_raca.grid(column=0, row=3, padx=15, pady=10, sticky='w')

entrada4_raca = Entry(janela, width=25)
entrada4_raca.grid(column=1, row=3, padx=5, pady=10, sticky='w')

label5_cor_predom = Label(janela, text="Digite a cor do animal:")
label5_cor_predom.grid(column=0, row=4, padx=15, pady=10, sticky='w')

entrada5_cor_predom = Entry(janela, width=10)
entrada5_cor_predom.grid(column=1, row=4, padx=5, pady=10, sticky='w')

label6_nascimento = Label(janela, text="Digite a data de nascimento do animal:")
label6_nascimento.grid(column=0, row=5, padx=15, pady=10, sticky='w')

entrada6_nascimento = Entry(janela, width=15)
entrada6_nascimento.grid(column=1, row=5, padx=5, pady=10, sticky='w')

label7_observacao = Label(janela, text="Digite uma observação:")
label7_observacao.grid(column=0, row=6, padx=15, pady=10, sticky='w')

entrada7_observacao = Entry(janela, width=50)
entrada7_observacao.grid(column=1, row=6, padx=5, pady=10, sticky='w')

label8_foto_animal = Label(janela, text="Cole o diretório da foto do animal:")
label8_foto_animal.grid(column=0, row=7, padx=15, pady=10, sticky='w')

entrada8_foto_animal = Entry(janela, width=80)
entrada8_foto_animal.grid(column=1, row=7, padx=5, pady=10, sticky='w')

label9_tutor = Label(janela, text="Digite o nome do tutor:")
label9_tutor.grid(column=0, row=8, padx=10, pady=10, sticky='w')

entrada9_tutor = Entry(janela, width=20)
entrada9_tutor.grid(column=1, row=8, padx=5, pady=10, sticky='w')

label10_fone = Label(janela, text="Digite o telefone do proprietário do animal:")
label10_fone.grid(column=0, row=9, padx=10, pady=10, sticky='w')

entrada10_fone = Entry(janela, width=20)
entrada10_fone.grid(column=1, row=9, padx=5, pady=10, sticky='w')

# Botões
botao_adicionar = Button(janela, text="Adicionar", command=adicionar_animal, bg="green", fg="#ffffff")
botao_adicionar.grid(column=1, row=10, padx=5, pady=20, sticky='w')

botao_listar = Button(janela, text="Consultar", command=consultar_animal, bg="blue", fg="#ffffff")
botao_listar.grid(column=1, row=10, padx=75, pady=20, sticky='w')

botao_atualizar = Button(janela, text="Atualizar", command=atualizar_animal, bg="yellow")
botao_atualizar.grid(column=1, row=10, padx=140, pady=20, sticky='w')

botao_deletar = Button(janela, text="Deletar", command=deletar_animal, bg="red", fg="#ffffff")
botao_deletar.grid(column=1, row=10, padx=200, pady=20, sticky='w')

janela.mainloop()