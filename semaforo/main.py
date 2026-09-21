import tkinter

#Criando a janela
janela = tkinter.Tk()
janela.title("Simulador de semáforo")
janela.geometry("400x600")

#Criando o semáforo
canvas = tkinter.Canvas(janela, width=300, height=500)
canvas.pack()
canvas.create_rectangle(90, 40, 210, 360, fill="black")

#Criando a luz vermelha 
luz_vermelha = canvas.create_oval(110, 70, 190, 150, fill="red")

#Criando a luz amarela
luz_amarela = canvas.create_oval(110, 170, 190, 250, fill="yellow")

#Criando a luz verde
luz_verde = canvas.create_oval(110, 270, 190, 350, fill="green")

#Logica de mudar as cores

#vermelho
def mostrar_vermelho ():
    canvas.itemconfig(luz_vermelha, fill="red")
    canvas.itemconfig(luz_amarela, fill="gray")
    canvas.itemconfig(luz_verde, fill="gray")
    janela.after(5000, mostrar_verde())

#amarelo
def mostrar_amarelo ():
    canvas.itemconfig(luz_vermelha, fill="gray")
    canvas.itemconfig(luz_amarela, fill="yellow")
    canvas.itemconfig(luz_verde, fill="gray")
    janela.after(5000, mostrar_amarelo())

#verde
def mostrar_verde ():
    canvas.itemconfig(luz_vermelha, fill="gray")
    canvas.itemconfig(luz_amarela, fill="gray")
    canvas.itemconfig(luz_verde, fill="green")
    janela.after(5000, mostrar_vermelho())
    







janela.mainloop()
