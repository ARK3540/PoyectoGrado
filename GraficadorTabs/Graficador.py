import math                                                                      #Operaciones matematicas simples
import pygame
from pygame.locals import*                                                                    #Entorno grafico de python
import random                                                                    #Uso de variables ramdom
import seaborn                                                                   #representacion de datos graficos
import librosa                                                                   #Analalisis manejo de audio
import numpy, scipy, matplotlib.pyplot as plt, pandas, librosa                   #Funciones matematicas alto nivel fourier
from numpy import exp, array, random, dot                                        #Herramientas algoritmos matematicos
import pyaudio                                                                   #Grabar, reproducir y trasmitir pyaudio
import struct                                                                    #Manejo de estructuras de datos
import wave                                                                      #Manejo de archivos wav
from scipy.io import wavfile                                                     #Transformar archivos numpy a wav
import os
import sys
import Tkinter
from Tkinter import*                                                                       #Interactua con el sistema operativo
import pickle


#Asignamos colores a variables (R,G,B)
BLANCO=(200,200,200)
LETRA=(55,0,55)
aux=True
NEGRO=(0,0,0)
ROJO=(180,0,20)
VERDE=(50,100,0)
AZUL=(0,0,200)
NARANJA=(255,128,0)
AMARILLO=(255,255,0)
GRIS=(145,145,145)
centro=(10,220)
ANCHO=300
ALTO=300
pygame.init()
#Asignamos de fuentes y tamano de Texto a variables global
fuente=pygame.font.Font("dalila.ttf",25)
Numero = pygame.font.Font("dalila.ttf",25)
Numero2 = pygame.font.Font("dalila.ttf",35)
tiponota = pygame.font.Font("dalila.ttf",90)
simbolo = pygame.font.Font("dalila.ttf",120)
#microfono
class Microphone:

    def rms(self,frame):
        count = len(frame)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, frame )
        sum_squares = 0.0
        for sample in shorts:
            n = sample * (1.0/32768.0)
            sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5);
        return rms * 1000

    def passiveListen(self,persona):
        CHUNK = 1024; RATE = 8000; THRESHOLD = 200; LISTEN_TIME = 20
        didDetect = False
        # prepare recording stream
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
        # stores the audio data
        all =[]
        # starts passive listening for disturbances
        #print RATE / CHUNK * LISTEN_TIME
        for i in range(0, RATE / CHUNK * LISTEN_TIME):
            input = stream.read(CHUNK)
            rms_value = self.rms(input)
            #print rms_value
            if (rms_value < THRESHOLD):
                didDetect = True
                print "Listening...\n"
                break

        if not didDetect:
            stream.stop_stream()
            stream.close()
            return False
        # append all the chunks
        all.append(input)
        for i in range(0, 7):
            data = stream.read(CHUNK)
            all.append(data)
        # save the audio data
        data = ''.join(all)
        stream.stop_stream()
        stream.close()
        wf = wave.open('Audio.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
        return True

class Nota_mastil:
    def __init__(self,cuerda,traste):
        self.cuerda=cuerda
        self.traste=traste

def cargar():
      mic = Microphone()
      a=mic.passiveListen('ok Google')
      x, fs = librosa.load('Audio.wav', sr=44100)
      f = numpy.linspace(0, fs, 8192)
      X = scipy.fft(x[:8192])
      X_mag = numpy.absolute(X)
      temp = numpy.argpartition(-X_mag, 10)
      result_args = temp[:10]
      result_args.sort()
      plt.plot(f[:1000], X_mag[:1000]) # magnitude spectrum
      plt.xlabel('Frequency (Hz)')
      FrecNota=f[result_args[0]]
      print FrecNota                                                            #<<<<<--------
      return FrecNota

def Stop (boolean):
    if boolean == (True):
     boolean=False

def Comparar(chulo):
    cuerda=0
    traste=0
    i=0
    while (Valid==TRUE):
        frec=int(cargar())
        i=i+1
        if i ==(5):
            break
        if frec>(70) and frec<(276):
            if frec>=(80) and frec<=(82):
                cuerda= 4
                traste =0
                e=Nota_mastil(cuerda,traste)
                chulo.append(e)
                continue

            if frec>=(105) and frec<=(109):
                    cuerda=3
                    traste=0
                    e=Nota_mastil(cuerda,traste)
                    chulo.append(e)
                    continue

            if frec>=(137) and frec<=(141):
                    cuerda=2
                    traste=0
                    e=Nota_mastil(cuerda,traste)
                    chulo.append(e)

                    continue

            if frec>=(187) and frec<=(190):
                    cuerda=1
                    traste=0
                    e=Nota_mastil(cuerda,traste)
                    chulo.append(e)
                    continue

###############################################################################
            if frec>=(207) and frec<=(276):
                if frec>=(208) and frec<=(210):
                        cuerda=1
                        traste=1
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(219) and frec<=(222):
                        cuerda=1
                        traste=2
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(229) and frec<=(233):
                        cuerda=1
                        traste=3
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(245) and frec<=(249):
                        cuerda=1
                        traste=4
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(256) and frec<=(259):
                        cuerda=1
                        traste=5
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(272) and frec<=(276):
                        cuerda=1
                        traste=6
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(152) and frec<=(206):
                if frec>=(148) and frec<=(152):
                        cuerda=2
                        traste=1
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(164) and frec<=(168):
                        cuerda=2
                        traste=2
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(175) and frec<=(179):
                        traste=3
                        cuerda=2
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(186) and frec<=(190):
                        cuerda=2
                        traste=4
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(197) and frec<=(201):
                        cuerda=2
                        traste=5
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(203) and frec<=(205):
                        cuerda=2
                        traste=6
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(152) and frec<=(206):

                if frec>=(155) and frec<=(157):
                        cuerda=3
                        traste=1
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(122) and frec<=(124):
                        cuerda=3
                        traste=2
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(192) and frec<=(194):
                        cuerda=3
                        traste=3
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(133) and frec<=(135):
                        cuerda=3
                        traste=4
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(138) and frec<=(140):
                        cuerda=3
                        traste=5
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(149) and frec<=(151):
                        cuerda=3
                        traste=6
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(152) and frec<=(206):

                if frec>=(84) and frec<=(87):
                        cuerda=4
                        traste=1
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(90) and frec<=(92):
                        cuerda=4
                        traste=2
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(95) and frec<=(97):
                        cuerda=4
                        traste=3
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        return

                if frec>=(101) and frec<=(103):
                        cuerda=4
                        traste=4
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(106) and frec<=(108):
                        cuerda=4
                        traste=5
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(112) and frec<=(114):
                        cuerda=4
                        traste=6
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue
################################################################################
            if frec>=(138) and frec<=(178):

                if frec>=(138) and frec<=(140):
                        cuerda=1
                        traste=7
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(149) and frec<=(151):
                        cuerda=1
                        traste=8
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(160) and frec<=(162):
                        cuerda=1
                        traste=9
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(165) and frec<=(167):
                        cuerda=1
                        traste=10
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(176) and frec<=(178):
                        cuerda=1
                        traste=11
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(117) and frec<=(222):

                if frec>=(117) and frec<=(119):
                        cuerda=2
                        traste=8
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(120) and frec<=(122):
                        cuerda=2
                        traste=11
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(122) and frec<=(124):
                        cuerda=2
                        traste=9
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(133) and frec<=(135):
                        cuerda=2
                        traste=10
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(219) and frec<=(221):
                        cuerda=2
                        traste=7
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(79) and frec<=(103):

                if frec>=(79) and frec<=(81):
                        cuerda=3
                        traste=7
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(85) and frec<=(87):
                        cuerda=3
                        traste=8
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(90) and frec<=(92):
                        cuerda=3
                        traste=9
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(95) and frec<=(97):
                        cuerda=3
                        traste=10
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(101) and frec<=(103):
                        cuerda=3
                        traste=11
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

            if frec>=(74) and frec<=(124):

                if frec>=(74) and frec<=(76):
                        cuerda=4
                        traste=11
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(122) and frec<=(124):
                        cuerda=4
                        traste=7
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(128) and frec<=(130):
                        cuerda=4
                        traste=8
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue

                if frec>=(133) and frec<=(135):
                        cuerda=4
                        traste=9
                        e=Nota_mastil(cuerda,traste)
                        chulo.append(e)
                        continue
################################################################################
def VentanaPy():
    pantalla=pygame.display.set_mode([500,708])
    pygame.display.set_caption("Interprete Graficador")
    fondo=pygame.image.load('Blanco.jpg')
    pantalla.blit(fondo,(0,0))
    pygame.display.update()
    lista_notas=[]
    Comparar(lista_notas)
    j=0
    k=0
    with open('save.bin', 'w') as archivo:
        pickle.dump(lista_notas,archivo)
    for e in lista_notas:
        pantalla.blit(Numero2.render(str(e.traste),True,[254,127,156]),[70 + (j*35),58+(e.cuerda*14)+ (k*102)])
        j+=1
        if j==10:
            j=0
            k+=1
    pygame.display.update()

def graficar_recuperado():
    pantalla=pygame.display.set_mode([500,708])
    pygame.display.set_caption("ultima guardada")
    fondo=pygame.image.load('Blanco.jpg')
    pantalla.blit(fondo,(0,0))
    pygame.display.update()
    with open("save.bin","r") as archivo:
        lista_graficar=pickle.load(archivo)
    j=0
    k=0
    for e in lista_graficar:
        pantalla.blit(Numero2.render(str(e.traste),True,[254,127,156]),[70 + (j*35),58+(e.cuerda*14)+ (k*102)])
        j+=1
        if j==10:
            j=0
            k+=1
    pygame.display.update()
#main
if __name__ == '__main__':
    i=0
    a=0
    nota=0
    cuerda=0
    traste=0
    time=2000
    Valid=True

root = Tkinter.Tk()
root.title("Interprete Graficador")
root.geometry("300x300")
root.resizable(False, False)
photo = PhotoImage(file='Intro.gif')
fondo=Label(root,image=photo)
fondo.pack()
boton = Tkinter.Button(root,text="Grabar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=VentanaPy)
boton.place(x=80, y=160, width=150, height=30)
boton1 = Tkinter.Button(root,text="Revisualizar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=graficar_recuperado)
boton1.place(x=80 , y=210, width=150, height=30)
boton2 = Tkinter.Button(root,text="Salir",activeforeground="#6e0987", relief='flat',cursor='hand1', command=root.destroy)
boton2.place(x=177, y=260, width=100, height=30)
root.mainloop()
