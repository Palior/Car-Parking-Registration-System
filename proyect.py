import pymysql
from tkinter import *
import datetime

#DEFINICION DE LA INTERFAZ GRAFICA
formulario = Tk()
formulario.geometry("500x500")
paten = Entry(formulario, width=15)
paten.pack()
paten.place(x=200, y=100)
etiqueta1 = Label(formulario, text="PATENTE")
etiqueta1.pack()
etiqueta1.place(x=220, y=120)

ano = Entry(formulario, width=10)
ano.pack()
ano.place(x=100 , y=150)
anio = Label(formulario, text="ANIO")
anio.pack()
anio.place(x=120 , y=170)

mes = Entry(formulario, width=10)
mes.pack()
mes.place(x=185 , y=150)
mesEtiq = Label(formulario, text="MES")
mesEtiq.pack()
mesEtiq.place(x=200 , y=170)

dia = Entry(formulario, width=10)
dia.pack()
dia.place(x=270 , y=150)
diaEtiq = Label(formulario, text="DIA")
diaEtiq.pack()
diaEtiq.place(x=290 , y=170)

hora = Entry(formulario, width=8)
hora.pack()
hora.place(x=170 , y=200)
horaEtiq = Label(formulario, text="HORA")
horaEtiq.pack()
horaEtiq.place(x=180 , y=220)

minuto = Entry(formulario, width=10)
minuto.pack()
minuto.place(x=250 , y=200)
minutoEtiq = Label(formulario, text="MINUTO")
minutoEtiq.pack()
minutoEtiq.place(x=260 , y=220)


#CREACION DE FUNCIONES USO INTERFAZ

def registrarEntrada():
        if(paten.get()!="" and int(ano.get())!="" and (int(mes.get())>0 and int(mes.get())<13) and dia.get()!="" and (hora.get()!="" and int(hora.get())<24) and (minuto.get()!="" and int(minuto.get())<60)):
                entrada=str(dia.get())+" "+str(mes.get())+" "+str(ano.get())+", "+str(hora.get())+":"+str(minuto.get())
                patente=str(paten.get()).upper()
                try:
                    db=pymysql.connect(host='localhost',user='root',password='Aa59552242',database='VEHICULOS')
                    cursor=db.cursor()
                    crear="""CREATE TABLE AUTOS(
                        PATENTE CHAR(10) NOT NULL,
                        COSTO CHAR(25) NOT NULL,
                        ENTRADA CHAR(25) NOT NULL,
                        SALIDA CHAR(25) NOT NULL)"""
                    cursor.execute(crear)
                except:
                    None
                instruccion="INSERT INTO AUTOS(PATENTE, COSTO, ENTRADA, SALIDA)VALUES(%s,%s,%s,%s)"
                cursor.execute(instruccion, (patente, 0, entrada, 0))
                textoResultado = Label(formulario, text="Registro Existoso")
                textoResultado.pack()
                textoResultado.place(x=90, y=320)
                textoResultado.config(width=50, heigh=5)
                db.commit()
                db.close()
        else:
                textoResul="FAVOR INGRESAR TODOS LOS CAMPOS REQUERIDOS: \n PATENTE Y FECHA COMPLETA CON HORA"
                texto = Label(formulario, text=textoResul)
                texto.pack()
                texto.place(x=90, y=320)
                texto.config(width=50, heigh=5, background="white")
                
        
def calcularTiempo(inicio, fin):
        entrada=datetime.datetime.strptime(inicio, "%d %m %Y, %H:%M")
        salida=datetime.datetime.strptime(fin, "%d %m %Y, %H:%M")
        diferencia = salida-entrada
        diferenciaHora = diferencia.seconds/3600 + diferencia.days*24
        return diferenciaHora
    
def registrarSalida():
        if(paten.get()!="" and int(ano.get())!="" and (int(mes.get())>0 and int(mes.get())<13) and dia.get()!="" and (hora.get()!="" and int(hora.get())<24) and (minuto.get()!="" and int(minuto.get())<60)):
                db=pymysql.connect(host='localhost',user='root',password='Aa59552242',database='vehiculos')
                cursor=db.cursor()
                instruccion="SELECT ENTRADA FROM AUTOS WHERE COSTO=0 AND PATENTE=%s"
                patente=str(paten.get()).upper()
                cursor.execute(instruccion, patente)
                entrada=cursor.fetchall()
                if (len(entrada)==0): #SI ENTRADA NO TIENE LARGO SIGNIFICA QUE NO HAY SALIDA PENDIENTE PARA LA PATENTE
                        textoResultado = Label(formulario, text="VEHICULO NO POSEE SALIDA PENDIENTE")
                        textoResultado.pack()
                        textoResultado.place(x=200, y=120)
                else:
                        salida=str(dia.get())+" "+str(mes.get())+" "+str(ano.get())+", "+str(hora.get())+":"+str(minuto.get())
                        tiempo = calcularTiempo(entrada[0][0], salida)
                        valorHora = 3000 #VALOR POR HORA DE ESTACIONAMIENTO
                        precio = str(tiempo*valorHora)
                        registrar="UPDATE AUTOS SET COSTO=%s, SALIDA=%s WHERE COSTO=0 AND PATENTE=%s"
                        cursor.execute(registrar, (precio, salida, patente))
                        db.commit()
                        db.close()
                        textoResultado = Label(formulario, text="Salida registrada")
                        textoResultado.pack()
                        textoResultado.place(x=100, y=100)
                        textoPrecio="El valor a pagar por uso de estacionamiento es: "+precio
                        textoCosto = Label(formulario, text=textoPrecio)
                        textoCosto.pack()
                        textoCosto.place(x=90, y=320)
                        textoCosto.config(width=50, heigh=5)
        else:
                textoResul="FAVOR INGRESAR TODOS LOS CAMPOS REQUERIDOS: \n PATENTE Y FECHA COMPLETA CON HORA"
                texto = Label(formulario, text=textoResul)
                texto.pack()
                texto.place(x=90, y=320)
                texto.config(width=50, heigh=5, background="white")
                


def calcularPatente():
        if (paten.get()!=""):
                db=pymysql.connect(host='localhost',user='root',password='Aa59552242',database='vehiculos')
                cursor=db.cursor()
                instruccion="SELECT COSTO FROM AUTOS WHERE PATENTE=%s"
                patente=str(paten.get()).upper()
                cursor.execute(instruccion, patente)
                costos=cursor.fetchall()
                acumulado=0.0
                for precio in costos:
                        acumulado=acumulado+float(precio[0])
                textoPrecio="El total pagado por esta patente es "+str(acumulado)
                textoCosto = Label(formulario, text=textoPrecio)
                textoCosto.pack()
                textoCosto.place(x=90, y=320)
                textoCosto.config(width=50, heigh=5, background="white")
                
        else:
                textoResul="FAVOR INGRESAR PATENTE PARA REALIZAR CONSULTA"
                texto = Label(formulario, text=textoResul)
                texto.pack()
                texto.place(x=90, y=320)
                texto.config(width=50, heigh=5, background="white")
                

def calcularDisponibles():
        db=pymysql.connect(host='localhost',user='root',password='Aa59552242',database='vehiculos')
        cursor=db.cursor()
        instruccion="SELECT COSTO FROM AUTOS WHERE COSTO=%s"
        cursor.execute(instruccion, "0")#SE EVALUA CON COSTO=0 DADO QUE SIGNIFICA QUE SIGUEN EN EL ESTACIONAMIENTO
        costos=cursor.fetchall()
        contador=0
        for e in costos:
                contador=contador+1
        estacionamientos=300 #Se establecen los estacionamientos en 300
        textoResul="EL TOTAL DE ESTACIONAMIENTOS DISPONIBLES ES: "+str(estacionamientos-contador)
        texto = Label(formulario, text=textoResul)
        texto.pack()
        texto.place(x=90, y=320)
        texto.config(width=50, heigh=5, background="white")

#Esta funcion para calcular costos lo hara de acuerdo a la fecha ingresada y a partir de esta las ganancias percividas en los dias que corresponda(dia, mes u anio)
def calcularCostos(dias):
        if(int(ano.get())!="" and (int(mes.get())>0 and int(mes.get())<13) and dia.get()!="" and (hora.get()!="" and int(hora.get())<24) and (minuto.get()!="" and int(minuto.get())<60)):
                db=pymysql.connect(host='localhost',user='root',password='Aa59552242',database='vehiculos')
                cursor=db.cursor()
                instruccion="SELECT COSTO, SALIDA FROM AUTOS WHERE COSTO!=0"
                cursor.execute(instruccion)
                costos=cursor.fetchall()
                diaActual=str(dia.get())+" "+str(mes.get())+" "+str(ano.get())+", "+str(hora.get())+":"+str(minuto.get())
                ganancia=0.0
                for registro in costos:
                        horasDif = calcularTiempo(registro[1], diaActual)
                        if (horasDif/24<dias):
                                ganancia=ganancia+float(registro[0])
                return ganancia
        else:
                textoResul="FAVOR INGRESAR FECHA CON HORA PARA CALCULAR COSTOS"
                texto = Label(formulario, text=textoResul)
                texto.pack()
                texto.place(x=90, y=320)
                texto.config(width=50, heigh=5, background="white")
                return "no"
        
def mostrarGanancia():
        diaGanan=calcularCostos(1)
        mesGanan=calcularCostos(30)
        anioGanan=calcularCostos(365)
        if (diaGanan!="no"):
                textoResul="EL TOTAL DE GANANCIAS A PARTIR DE LA FECHA INGRESADA ES: \n DIA="+str(diaGanan)+"\n MES="+str(mesGanan)+"\n ANIO"+str(anioGanan)
                texto = Label(formulario, text=textoResul)
                texto.pack()
                texto.place(x=90, y=320)
                texto.config(width=50, heigh=5, background="white")

                
#BOTONES DE ACCION
registro = Button(formulario, text='REGISTRAR ENTRADA', command=registrarEntrada)
registro.pack()
registro.place(x=200, y=50)

salida = Button(formulario, text='REGISTRAR SALIDA', command=registrarSalida)
salida.pack()
salida.place(x=200, y=250)

costoAuto = Button(formulario, text='CALCULAR COSTO TOTAL PATENTE', command=calcularPatente)
costoAuto.pack()
costoAuto.place(x=160, y=300)

cupos= Button(formulario, text='REVISAR ESTACIONAMIENTOS DISPONIBLES', command=calcularDisponibles)
cupos.pack()

costos = Button(formulario, text='VER COSTOS GENERALES', command=mostrarGanancia)
costos.pack()
costos.place(x=185, y=450)
formulario.mainloop()

