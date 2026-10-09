
import tkinter

janela = tkinter.Tk()
janela.title("Pomodoro Timer")
janela.geometry("400x500")

texto = tkinter.Label(janela, text="Tempo para focar")
texto.pack()

texto_tempo = tkinter.Label(janela, text="25:00")
texto_tempo.pack()

tempo_inicial = 25 * 60
tempo_restante = tempo_inicial
temporizador_ativo = False
after_id = None


def atualizar_tempo():
    global tempo_restante, after_id

    minutos = tempo_restante // 60
    segundos = tempo_restante % 60

    texto_tempo.config(text=f"{minutos:02d}:{segundos:02d}")

    if tempo_restante > 0:
        tempo_restante -= 1
        after_id = janela.after(1000, atualizar_tempo)
    else:
        temporizador_ativo = False
        after_id = None


def iniciar():
    global temporizador_ativo

    if not temporizador_ativo and tempo_restante > 0:
        temporizador_ativo = True
        atualizar_tempo()


def pausar():
    global temporizador_ativo, after_id

    temporizador_ativo = False

    if after_id is not None:
        janela.after_cancel(after_id)
        after_id = None


def reiniciar():
    global tempo_restante

    pausar()
    tempo_restante = tempo_inicial
    texto_tempo.config(text="25:00")


botao_iniciar = tkinter.Button(
    janela, text="Iniciar", command=iniciar)
botao_iniciar.pack()

botao_pausar = tkinter.Button(
    janela, text="Pausar", command=pausar)
botao_pausar.pack()

botao_reiniciar = tkinter.Button(
    janela, text="Reiniciar", command=reiniciar)

botao_reiniciar.pack()

janela.mainloop()