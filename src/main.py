from tkinter import *
from tkinter import filedialog
from funcoes import *

bg_color = "white"
button_color = "cyan"
option_button_font = ("Arial", "15", "bold")
confirmation_button_font = ("Arial", "10", "bold")
error_msg_font = ("Arial", "10", "bold")
text_font = ("Arial", "20", "bold")
estatistica_font = ("Arial", "15", "bold")

def verificar_idade(idade):
    if len(idade) == 0:
        return "Idade nao pode estar em branco"

    if idade.isdecimal() == False:
        return "Idade deve ser apenas numeros"
    
    return int(idade)

class Interface:
    def __init__(self, instancia_Tk):
        self.fila = []
        self.desordenado = []
        self.ordenado = False
        
        topo = Frame(instancia_Tk, background=bg_color, pady=50)
        topo.pack()
        frame1 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame1.pack()
        frame2 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame2.pack()
        frame3 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame3.pack()
        frame4 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame4.pack()
        frame5 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame5.pack()
        frame6 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame6.pack()

        self.msgFila = Label(topo, text = "Quantidade de Pessoas: 0")
        self.msgFila.config(background=bg_color, font=text_font, padx=150)
        self.msgFila.pack(side=LEFT)

        self.msgOrdenacao = Label(topo, text = "Tipo de Ordenacao: Nenhuma")
        self.msgOrdenacao.config(background=bg_color, font=text_font, padx=150)
        self.msgOrdenacao.pack(side=RIGHT)

        B1 = Button(frame1, text="Gerar Pacientes Aleatoriamente", width=55, bg=button_color, font=option_button_font, command=self.gerar_regist_aleat)
        B1.pack(side=LEFT)

        B2 = Button(frame1, text="Cadastrar Paciente Individual", width=55, bg=button_color, font=option_button_font, command=self.cadastro)
        B2.pack(side=RIGHT)

        B3 = Button(frame2, text="Ordenar", width=112, bg=button_color, font=option_button_font, command=self.ordenar)
        B3.pack(side=LEFT)

        B4 = Button(frame3, text="Mostrar Fila (Ordem de Chegada)", width=55, bg=button_color, font=option_button_font, command=lambda: mostrar_fila(self.desordenado, len(self.desordenado)))
        B4.pack(side=LEFT)

        B5 = Button(frame3, text="Mostrar Fila (Ordenado por Gravidade e Idade)", width=55, bg=button_color, font=option_button_font, command=self.mostrar_fila_ordenada)
        B5.pack(side=RIGHT)

        B6 = Button(frame4, text="Comparar Metodos de Ordenacao (Fila atual)", width=55, bg=button_color, font=option_button_font, command=lambda: comparar_ordenacoes(self.fila, self.desordenado))
        B6.pack(side=LEFT)

        B7 = Button(frame4, text="Comparar Metodos de Ordenacao (Varias Filas Aleatorias)", width=55, bg=button_color, font=option_button_font, command=comparacoes)
        B7.pack(side=RIGHT)

        B8 = Button(frame5, text="Abrir Arquivo", width=55, bg=button_color, font=option_button_font, command=self.abre_arquivo)
        B8.pack(side=LEFT)

        B9 = Button(frame5, text="Salvar", width=55, bg=button_color, font=option_button_font, command=self.salva_arquivo)
        B9.pack(side=RIGHT)

        B10 = Button(frame6, text="Gerar Arvore", width=112, bg=button_color, font=option_button_font, command=self.mostrar_arvore)
        B10.pack(side=LEFT)
    

    def gerar_regist_aleat(self):
        tela = Tk()
        tela.title('Gerar Pessoas Aleatoriamente')

        texto = Frame(tela, pady=10)
        texto.pack()
        campo = Frame(tela, pady=10)
        campo.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite quantas pessoas voce quer criar", font=text_font)
        text.pack()

        valor = Entry(campo)
        valor.pack()

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_valor(valor.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("600x200+700+400")
        tela.mainloop()
    

    def verif_valor(self, valor, mensagem, tela):
        try:
            valor = int(valor)
            if valor > 0:
                self.fila = gerar_pacientes_aleatorios(valor)
                self.desordenado = self.fila.copy()
                self.ordenado = False
                tela.destroy()
                self.msgFila["text"] = "Quantidade de Pessoas: {}".format(len(self.fila))
                self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
            else:
                mensagem["text"] = "Numero deve ser maior do que 0"
        except ValueError:
            mensagem["text"] = "Deve ser um numero valido"
    

    def cadastro(self):
        tela = Tk()
        tela.title('Cadastrar Paciente Individual')

        texto = Frame(tela, pady=10)
        texto.pack()
        frame1 = Frame(tela, pady=10)
        frame1.pack()
        frame2 = Frame(tela, pady=10)
        frame2.pack()
        frame3 = Frame(tela, pady=10)
        frame3.pack()
        frame4 = Frame(tela, pady=10)
        frame4.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()        
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite os dados do Paciente", font=text_font, pady=10)
        text.pack()

        nometext = Label(frame1, text="Nome:           ", padx=13)
        nometext.pack(side=LEFT)
        nome = Entry(frame1, width=25)
        nome.pack(side=RIGHT)

        sexotext = Label(frame2, text="Sexo (M/F):      ", padx=8)
        sexotext.pack(side=LEFT)
        sexo = Entry(frame2, width=25)
        sexo.pack(side=RIGHT)

        idadetext = Label(frame3, text="Idade:              ", padx=8)
        idadetext.pack(side=LEFT)
        idade = Entry(frame3, width=25)
        idade.pack(side=RIGHT)

        gravidadetext = Label(frame4, text="Gravidade (1-5): ")
        gravidadetext.pack(side=LEFT)
        gravidade = Entry(frame4, width=25)
        gravidade.pack(side=RIGHT)

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_cadastro(nome.get(), sexo.get(), idade.get(), gravidade.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("650x350+650+300")
        tela.mainloop()
    

    def verif_cadastro(self, nome, sexo, idade, gravidade, mensagem, tela):
        try:
            idade = verificar_idade(idade)
            idade = int(idade)
            if len(nome) == 0:
                mensagem["text"] = "Nome nao pode estar em branco"
            elif sexo != "M" and sexo != "F":
                mensagem["text"] = "Sexo deve ser M ou F"
            elif len(gravidade) == 0:
                mensagem["text"] = "Gravidade nao pode estar em branco"
            elif int(gravidade) < 1 or int(gravidade) > 5:
                mensagem["text"] = "Gravidade deve estar entre 1 e 5"
            else:
                paciente_unico(self.fila, nome, sexo, idade, int(gravidade))
                self.desordenado.append(self.fila[len(self.fila)-1])
                self.ordenado = False
                self.msgFila["text"] = "Quantidade de Pessoas: {}".format(len(self.fila))
                self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
                tela.destroy()
        except ValueError:
            mensagem["text"] = idade

    def ord_aux(self, tipo, fila, tela):
        swaps, quant_heapify, tempo = 0, 0, 0
        if tipo == "HSR":
            inicio = time.perf_counter()
            swaps, quant_heapify = heap_sort_recursivo(fila)
            fim = time.perf_counter()
            tempo = fim - inicio
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Heap Sort Recursivo"
        elif tipo == "HSI":
            inicio = time.perf_counter()
            swaps = heap_sort_interativo(fila)
            fim = time.perf_counter()
            tempo = fim - inicio
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Heap Sort Interativo"
        
        self.ordenado = True
        tela.destroy()

        est = Tk()
        est.title('Estatisticas')

        msg = Frame(est)
        f1 = Frame(est)
        f2 = Frame(est)
        f3 = Frame(est)
        vazio = Frame(est)
        botaoFrame = Frame(est)
        msg.pack()
        f1.pack()
        f2.pack()
        f3.pack()
        vazio.pack()
        botaoFrame.pack()

        titulo = Label(msg, text='ESTATISTICAS DESTE HEAP SORT', font=text_font, pady=30)
        titulo.pack()

        textSwap = Label(f1, text='Tempo (segundos): ', font=estatistica_font, pady=5)
        textSwap.pack(side=LEFT)

        numSwap = Label(f1, text=str(tempo), font=estatistica_font, pady=5, fg='red')
        numSwap.pack(side=RIGHT)

        textSwap = Label(f2, text='Swaps: ', font=estatistica_font, pady=5)
        textSwap.pack(side=LEFT)

        numSwap = Label(f2, text=str(swaps), font=estatistica_font, pady=5, fg='red')
        numSwap.pack(side=RIGHT)

        vertical = 250

        if quant_heapify != 0:
            textQtH = Label(f3, text='Quantidade de Heapifys: ', font=estatistica_font, pady=5)
            textQtH.pack(side=LEFT)

            numQtH = Label(f3, text=str(quant_heapify), font=estatistica_font, pady=5, fg='red')
            numQtH.pack(side=RIGHT)
            vertical = 280
        
        vaziotext = Label(vazio, text=' ', pady=10)
        vaziotext.pack()

        botao = Button(botaoFrame, text=" OK ", command=est.destroy)
        botao.pack()

        est.geometry("550x"+str(vertical)+"+700+400")
        est.mainloop()


    def ordenar(self):
        if len(self.fila) == 0:
            self.aviso("Nao ha nenhuma pessoa")
        elif self.ordenado == True:
            self.aviso("A Fila ja esta Ordenada")
        else:
            tela = Tk()
            tela.title('Ordenar')

            top = Frame(tela)
            middle = Frame(tela)
            top.pack()
            middle.pack()

            text = Label(top, text="Escolha um dos metodos abaixo", font=text_font, pady=10)
            text.grid(row=0, pady=5)

            B1 = Button(middle, text="Heap Sort Recursivo", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("HSR", self.fila, tela))
            B1.grid(row=1, padx=10, pady=5)

            B2 = Button(middle, text="Heap Sort Interativo", width=30, bg=button_color, font=option_button_font, command=lambda: self.ord_aux("HSI", self.fila, tela))
            B2.grid(row=2, padx=10, pady=5)

            tela.geometry("500x180+750+300")
            tela.mainloop()
    

    def abre_arquivo(self):
        self.fila.clear()
        path = filedialog.askopenfilename(initialdir = "/",title = "Selecione o Arquivo",filetypes = [("L4 files","*.L4")])

        i = 0
        nome = ""
        sexo = ""
        idade = ""
        gravidade = ""
        ordemChegada = ""
        try:
            with open(path, 'r') as arq:
                for linha in arq:
                    linha = linha.strip()
                    if i == 0:
                        nome = linha
                    elif i == 1:
                        sexo = linha
                    elif i == 2:
                        idade = int(linha)
                    elif i == 3:
                        gravidade = int(linha)
                    else:
                        ordemChegada = int(linha)
                
                    i += 1

                    if i == 5:
                        self.fila.append(Paciente(nome, sexo, idade, gravidade, ordemChegada))
                        i = 0

            arq.close()
            self.msgFila["text"] = "Quantidade de Pessoas: {}".format(len(self.fila))
            self.msgOrdenacao["text"] = "Tipo de Ordenacao: Nenhuma"
            self.ordenado = False
        except:
            return


    def salva_arquivo(self):
        path = filedialog.asksaveasfilename(initialdir = "/",title = "Selecione o Local para Salvar",filetypes = [("L4 files","*.L4")])
        
        try:
            arq = open(path, 'w')

            for i in range(len(self.fila)):
                arq.write('{}\n'.format(self.fila[i].nome))
                arq.write('{}\n'.format(self.fila[i].sexo))
                arq.write('{}\n'.format(self.fila[i].idade))
                arq.write('{}\n'.format(self.fila[i].gravidade))
                arq.write('{}\n'.format(self.fila[i].ordemChegada))
        
            arq.close()
        except:
            return
    
    def aviso(self, mensagem):
        tela = Tk()
        tela.title('Aviso')

        msg = Frame(tela)
        botaoFrame = Frame(tela)
        msg.pack()
        botaoFrame.pack()

        text = Label(msg, text=mensagem, font=text_font, pady=10)
        text.pack()

        botao = Button(botaoFrame, text=" OK ", command=tela.destroy)
        botao.pack()

        tela.geometry("550x100+700+400")
        tela.mainloop()

    def mostrar_fila_ordenada(self):
        if len(self.fila) == 0:
            self.aviso("Nao ha nenhuma pessoa na fila")
        elif self.ordenado == False:
            self.aviso("Primeiro use algum Metodo de Ordenacao")
        else:
            mostrar_fila(self.fila, len(self.fila))

    def mostrar_arvore(self):
        if len(self.fila) == 0:
            self.aviso("Nao ha nenhuma pessoa na fila")
        else:
            printar_arvore(self.fila)

if __name__ == '__main__':
    menu=Tk()
    menu.title('LISTA 4 - ESTRUTURA DE DADOS 2')
    menu.config(background=bg_color)
    menu.geometry("1400x450+300+200")
    Interface(menu)
    menu.mainloop()