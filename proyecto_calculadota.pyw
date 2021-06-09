from tkinter import *

ventana = Tk()

ventana.title("calculadora")

ventana.resizable(False,False)

ventana.iconbitmap("calculadora.ico")

ventana.config(bg="black")

ventana.config(bd=15)

ventana.config(relief="groove")


i = 0

#----------------------------Entrada----------------------------------
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4,padx = 5, pady = 5)
e_texto.config(bg="#03f943", fg="black", justify="right")

#--------------------------------Funciones-------------------------------------
def click_boton(valor):
	global i
	e_texto.insert(i, valor)
	i += 1

def borrar():
	e_texto.delete(0, END)
	i = 0

def operacion():
	ecuacion = e_texto.get()
	resultado = eval(ecuacion)
	e_texto.delete(0, END)
	e_texto.insert(0,resultado)
	i = 0

#-------------------------------------------Botones------------------------------------------
boton1 = Button(ventana, text = "1", width = 4, height = 2, command = lambda: click_boton(1))
boton1.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton2 = Button(ventana, text = "2", width = 4, height = 2, command = lambda: click_boton(2))
boton2.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton3 = Button(ventana, text = "3", width = 4, height = 2, command = lambda: click_boton(3))
boton3.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton4 = Button(ventana, text = "4", width = 4, height = 2, command = lambda: click_boton(4))
boton4.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton5 = Button(ventana, text = "5", width = 4, height = 2, command = lambda: click_boton(5))
boton5.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton6 = Button(ventana, text = "6", width = 4, height = 2, command = lambda: click_boton(6))
boton6.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton7 = Button(ventana, text = "7", width = 4, height = 2, command = lambda: click_boton(7))
boton7.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton8 = Button(ventana, text = "8", width = 4, height = 2, command = lambda: click_boton(8))
boton8.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton9 = Button(ventana, text = "9", width = 4, height = 2, command = lambda: click_boton(9))
boton9.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton0 = Button(ventana, text = "0", width = 13, height = 2, command = lambda: click_boton(0))
boton0.config(cursor="hand2", bg="#03f943", fg="black", justify="right")

boton_borrar = Button(ventana, text = "AC", width = 4, height = 2, command = lambda: borrar())
boton_borrar.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_parentesis1 = Button(ventana, text = "(", width = 4, height = 2, command = lambda: click_boton("("))
boton_parentesis1.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_parentesis2 = Button(ventana, text = ")", width = 4, height = 2, command = lambda: click_boton(")"))
boton_parentesis2.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_punto = Button(ventana, text = ".", width = 4, height = 2, command = lambda: click_boton("."))
boton_punto.config(cursor="hand2", bg="#03f943", fg="black", justify="right")

boton_div = Button(ventana, text = "/", width = 4, height = 2, command = lambda: click_boton("/"))
boton_div.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_mult = Button(ventana, text = "x", width = 4, height = 2, command = lambda: click_boton("*"))
boton_mult.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_suma = Button(ventana, text = "+", width = 4, height = 2, command = lambda: click_boton("+"))
boton_suma.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_resta = Button(ventana, text = "-", width = 4, height = 2, command = lambda: click_boton("-"))
boton_resta.config(cursor="hand2", bg="#03f943", fg="black", justify="right")
boton_igual = Button(ventana, text = "=", width = 4, height = 2, command = lambda: operacion())
boton_igual.config(cursor="hand2", bg="#03f943", fg="black", justify="right")


#------------------------Agregar botones en pantalla----------------------------------.
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0,columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop()