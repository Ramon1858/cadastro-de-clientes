import tkinter as tk


def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")

# Campo Nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

# Campo Idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

# Campo E-mail
label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(janela)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Campo Endereço
label_endereco = tk.Label(janela, text="Endereço:")
label_endereco.grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

# Campo Celular
label_celular = tk.Label(janela, text="Celular:")
label_celular.grid(row=4, column=0, padx=10, pady=5)
entry_celular = tk.Entry(janela)
entry_celular.grid(row=4, column=1, padx=10, pady=5)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_dados)
botao_enviar.grid(row=5, columnspan=2, pady=10)

janela.mainloop()
