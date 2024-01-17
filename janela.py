import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark") # Alterar o bg - janela
customtkinter.set_default_color_theme("dark-blue")

janela  = customtkinter.CTk()
janela.geometry("500x500")
janela.title('Painel de Login')
#icon_image = tkinter.PhotoImage(file='74472.png')
janela.resizable(False, False)

def clique():
    print('Fazer login')

texto = customtkinter.CTkLabel(janela, text="Fazer login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail") # 'Entry' para o usuário preencher
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua Senha", show="*") # 'show' para não visualizar os dígitos
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=10, pady=20)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()
