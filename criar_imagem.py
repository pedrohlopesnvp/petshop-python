import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

# Configuração da janela principal
janela = tk.Tk()
janela.title("Exibidor de Imagem")

# Cria e posiciona os widgets
entry = tk.Entry(janela, width=50)
entry.pack(pady=10)

button = tk.Button(janela, text="Abrir Imagem", command=open_image)
button.pack(pady=5)

label_img = tk.Label(janela, text="A imagem aparecerá aqui")
label_img.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
