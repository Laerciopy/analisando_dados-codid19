import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import requests
import json
import pandas as pd
import numpy as np
##### matplotlib #####
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from dados import *

########### criando janela ##########
janela = Tk()
janela.title('')
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('1100x550')

#cores
cor_fundo = "#3a3a4d"
cor_letra = "#403d3d"
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#6dd695"   # + profit
fundo = "#3F729B"

######### frames ##########
frame_app_nome = Frame(janela, width=1365, height=45, pady=0,padx=0, bg=co1,  relief="flat",)
frame_app_nome.grid(row=0, column=0)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_quadros = Frame(janela, width=1365, height=500,bg=cor_fundo, pady=10, padx=10, relief="flat",)
frame_quadros.grid(row=3, column=0, sticky=NW)

#definindo o nome do app
app_nome = Label(frame_app_nome, text="DASHBOARD COVID-19", width=32, height=2, pady=5, padx=0, anchor='nw', font=("Ivy 17 bold"), bg=co1, fg=cor_letra)
app_nome.place(x=0, y=10)

#frames e labes para o frame quadro

#total de casos----------
frame_Total = Frame(frame_quadros, width=178, height=70, bg=co1)
frame_Total.place(x=0, y=0)

#borda azul
app_ = Label(frame_Total, text="", width=1, height=10, pady=0, padx=0, anchor='nw', font=("Ivy 1 bold"), bg=co2, fg=cor_letra)
app_.place(x=0, y=0)

app_total = Label(frame_Total, text="Total de casos", height=1, pady=0, padx=0, anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=cor_letra)
app_total.place(x=10, y=5)

app_total_numero = Label(frame_Total, text='{:,}'.format(Total[1]['casos']), height=1, pady=0, padx=0,relief="flat", anchor=CENTER, font=('Roboto 16 '), bg=co1, fg="#202124")
app_total_numero.place(x=10, y=35)

#total recuperados----------
frame_Recuperados = Frame(frame_quadros, width=178, height=70, bg=co1)
frame_Recuperados.place(x=188, y=0)

#borda azul
app_ = Label(frame_Recuperados, text="", width=1, height=10, pady=0, padx=0, anchor='nw', font=("Ivy 1 bold"), bg=co2, fg=cor_letra)
app_.place(x=0, y=0)

app_total = Label(frame_Recuperados, text="Total Recuperados", height=1, pady=0, padx=0, anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=cor_letra)
app_total.place(x=10, y=5)

app_total_numero = Label(frame_Recuperados, text='{:,}'.format(Total[1]['recuperados']), height=1, pady=0, padx=0, anchor=CENTER, font=("Roboto 16"), bg=co1, fg=cor_letra)
app_total_numero.place(x=10, y=35)

#total mortes----------
frame_Mortes = Frame(frame_quadros, width=178, height=70, bg=co1)
frame_Mortes.place(x=375, y=0)

#borda azul
app_ = Label(frame_Mortes, text="", width=1, height=10, pady=0, padx=0, anchor='nw', font=("Ivy 1 bold"), bg=co2, fg=cor_letra)
app_.place(x=0, y=0)

app_total = Label(frame_Mortes, text="Total Mortes", height=1, pady=0, padx=0, anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=cor_letra)
app_total.place(x=10, y=5)

app_total_numero = Label(frame_Mortes, text='{:,}'.format(Total[1]['mortes']), height=1, pady=0, padx=0, anchor=CENTER, font=("Roboto 16"), bg=co1, fg=cor_letra)
app_total_numero.place(x=10, y=35)


#Top paises mais afetados pela Covid-19

cores = ['#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']
lista_paizes_top_nome = [] 
lista_paizes_top_valor = []

for i in lista_paizes_top:
 lista_paizes_top_nome.append(i[0])
 lista_paizes_top_valor.append(i[1])

frame_top = Frame(frame_quadros, width=200, height=500, bg=co1, relief="flat",)
frame_top.place(x=560, y=0)


# obtendo valores de meses
lista_pais = lista_paizes_top_nome 
lista_valores = lista_paizes_top_valor

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(8.7, 3), dpi=60)
ax = figura.add_subplot(111)

ax.barh(lista_pais, lista_valores,
        align='center', color=cores)
ax.set_alpha(0.3)

c = 0

for i in ax.patches:
    ax.text(i.get_width()+.3, i.get_y()+.50,
            
            str(lista_valores[c]), fontsize=12, verticalalignment='center', fontstyle='italic', weight='bold', color='dimgrey'
            )
    c += 1


ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(False)
ax.xaxis.grid(False)


app_nome_rev = Label(frame_top, text="Top países mais afetados", height=1,
                     pady=5, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
canva = FigureCanvasTkAgg(figura, frame_top)
canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW, columnspan=2)

####################### Frame paises #######################

frame_paises = Frame(frame_quadros, width=700, height=500, bg=co1, relief="flat",)
frame_paises.place(x=0, y=80)

# este codigo serve para estilizar a tabela em Tkinter
style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading", background="#494d4a", foreground="white", relief="raised")
style.map("Custom.Treeview.Heading",
          relief=[('active', 'groove'), ('pressed', 'sunken')])


# cabeçalho da tabela
lista_head = ['País',  'Total Confirmado', 'Total Recuperado', 'Total mortes', 'Data']

tree = ttk.Treeview(frame_paises, selectmode="extended", style="Custom.Treeview", height=18, columns=lista_head, show="headings")
# vertical scrollbar
vsb = ttk.Scrollbar(frame_paises, orient="vertical", command=tree.yview)
# horizontal scrollbar
hsb = ttk.Scrollbar(frame_paises, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=1, sticky='nsew')
vsb.grid(column=1, row=1, sticky='ns')
hsb.grid(column=0, row=2, sticky='ew')
frame_paises.grid_rowconfigure(0, weight=2)


# definindo algumas propriedades para a tabela
hd = ["nw", "center", "center", "center", "center", "center", "center"]
h = [140, 100, 100, 100, 91]
n = 0

for col in lista_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])

    n += 1


for item in lista_paizes:
    tree.insert('', 'end', values=item)

frame_categoria = Frame(frame_quadros, width=200,
                        height=200, bg=co1, relief="flat",)
frame_categoria.place(x=562, y=220)

lista_continentes_valor = lista_continentes_valor 
lista_continentes_nome = lista_continentes_nome

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(8.65, 3.9), dpi=60)
ax = figura.add_subplot(111)

colors = ['#5588bb', '#66bbbb', '#aa6644',
          '#99bb55', '#ee9944', '#444466', '#bb5555']

wedges, texts = ax.pie(lista_continentes_valor, wedgeprops=dict(width=0.2), colors=colors, shadow=True, startangle=-90)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(lista_continentes_nome[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

app_categoria = Label(frame_categoria, text="Continente mais afetado", height=1, pady=5, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_categoria.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
canva_cont = FigureCanvasTkAgg(figura, frame_categoria)
canva_cont.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

janela.mainloop()