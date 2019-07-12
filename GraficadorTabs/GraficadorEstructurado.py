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


pygame.init()
#Asignamos de fuentes y tamano de Texto a variables global
Numero2 = pygame.font.Font("dalila.ttf",35)

def main():
    root = Tkinter.Tk()
    root.title("Interprete Graficador")
    root.geometry("300x300")
    root.resizable(False, False)
    photo = PhotoImage(file='Intro.gif')
    fondo=Label(root,image=photo)
    fondo.pack()
    R=tablatura()
    boton = Tkinter.Button(root,text="Grabar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=R.Graficar1)
    boton.place(x=80, y=160, width=150, height=30)
    boton1 = Tkinter.Button(root,text="Revisualizar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=R.GraficarL)
    boton1.place(x=80 , y=210, width=150, height=30)
    boton2 = Tkinter.Button(root,text="Salir",activeforeground="#6e0987", relief='flat',cursor='hand1', command=root.destroy)
    boton2.place(x=177, y=260, width=100, height=30)
    root.mainloop()

class Frecuencia:
    def Rms(self,frame):
        count = len(frame)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, frame )
        sum_squares = 0.0
        for sample in shorts:
            n = sample * (1.0/32768.0)
            sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5);
        return rms * 1000
################################################################################
    def PassiveListen(self,audio):
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
            rms_value = self.Rms(input)
            #print rms_value
            if (rms_value < THRESHOLD):
                didDetect = True
                #print "Listening...\n"
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
###############################################################################
    def Cargar(self):
          mic = Frecuencia()
          a=mic.PassiveListen('ok Google')
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

class Nota_Mastil:
        def __init__(self,frecuencia):
            self.cuerda=0
            self.traste=0
            self.frec=frecuencia
            self.valid=False

        def Comparar(self):
            frec=int(Frecuencia().Cargar())
            #print frec
            if frec>(70) and frec<(276):
                if frec>=(80) and frec<=(82):
                    self.cuerda= 4
                    self.traste =0
                    self.valid=True

                if frec>=(105) and frec<=(109):
                        self.cuerda=3
                        self.traste=0

                if frec>=(137) and frec<=(141):
                        self.cuerda=2
                        self.traste=0
                        self.valid=True

                if frec>=(187) and frec<=(190):
                        self.cuerda=1
                        self.traste=0
                        self.valid=True
    ###############################################################################
                if frec>=(207) and frec<=(276):
                    if frec>=(208) and frec<=(210):
                            self.cuerda=1
                            self.traste=1
                            self.valid=True

                    if frec>=(219) and frec<=(222):
                            self.cuerda=1
                            self.traste=2
                            self.valid=True

                    if frec>=(229) and frec<=(233):
                            self.cuerda=1
                            self.traste=3
                            self.valid=True

                    if frec>=(245) and frec<=(249):
                            self.cuerda=1
                            self.traste=4
                            self.valid=True

                    if frec>=(256) and frec<=(259):
                            self.cuerda=1
                            self.traste=5
                            self.valid=True

                    if frec>=(272) and frec<=(276):
                            self.cuerda=1
                            self.traste=6
                            self.valid=True

                if frec>=(152) and frec<=(206):
                    if frec>=(148) and frec<=(152):
                            self.cuerda=2
                            self.traste=1
                            self.valid=True

                    if frec>=(164) and frec<=(168):
                            self.cuerda=2
                            self.traste=2
                            self.valid=True

                    if frec>=(175) and frec<=(179):
                            self.traste=3
                            self.cuerda=2
                            self.valid=True

                    if frec>=(186) and frec<=(190):
                            self.cuerda=2
                            self.traste=4
                            self.valid=True

                    if frec>=(197) and frec<=(201):
                            self.cuerda=2
                            self.traste=5
                            self.valid=True

                    if frec>=(203) and frec<=(205):
                            self.cuerda=2
                            self.traste=6
                            self.valid=True

                if frec>=(152) and frec<=(206):

                    if frec>=(155) and frec<=(157):
                            self.cuerda=3
                            self.traste=1
                            self.valid=True

                    if frec>=(122) and frec<=(124):
                            self.cuerda=3
                            self.traste=2
                            self.valid=True

                    if frec>=(192) and frec<=(194):
                            self.cuerda=3
                            self.traste=3
                            self.valid=True

                    if frec>=(133) and frec<=(135):
                            self.cuerda=3
                            self.traste=4
                            self.valid=True

                    if frec>=(138) and frec<=(140):
                            self.cuerda=3
                            self.traste=5
                            self.valid=True

                    if frec>=(149) and frec<=(151):
                            self.cuerda=3
                            self.traste=6
                            self.valid=True

                if frec>=(152) and frec<=(206):

                    if frec>=(84) and frec<=(87):
                            self.cuerda=4
                            self.traste=1
                            self.valid=True

                    if frec>=(90) and frec<=(92):
                            self.cuerda=4
                            self.traste=2
                            self.valid=True

                    if frec>=(95) and frec<=(97):
                            self.cuerda=4
                            self.traste=3
                            self.valid=True

                    if frec>=(101) and frec<=(103):
                            self.cuerda=4
                            self.traste=4
                            self.valid=True

                    if frec>=(106) and frec<=(108):
                            self.cuerda=4
                            self.traste=5
                            self.valid=True

                    if frec>=(112) and frec<=(114):
                            self.cuerda=4
                            self.traste=6
                            self.valid=True
    ################################################################################
                if frec>=(138) and frec<=(178):

                    if frec>=(138) and frec<=(140):
                            self.cuerda=1
                            self.traste=7
                            self.valid=True

                    if frec>=(149) and frec<=(151):
                            self.cuerda=1
                            self.traste=8
                            self.valid=True

                    if frec>=(160) and frec<=(162):
                            self.cuerda=1
                            self.traste=9
                            self.valid=True

                    if frec>=(165) and frec<=(167):
                            self.cuerda=1
                            self.traste=10
                            self.valid=True

                    if frec>=(176) and frec<=(178):
                            self.cuerda=1
                            self.traste=11
                            self.valid=True

                if frec>=(117) and frec<=(222):

                    if frec>=(117) and frec<=(119):
                            self.cuerda=2
                            self.traste=8
                            self.valid=True

                    if frec>=(120) and frec<=(122):
                            self.cuerda=2
                            self.traste=11
                            self.valid=True

                    if frec>=(122) and frec<=(124):
                            self.cuerda=2
                            self.traste=9
                            self.valid=True

                    if frec>=(133) and frec<=(135):
                            self.cuerda=2
                            self.traste=10
                            self.valid=True

                    if frec>=(219) and frec<=(221):
                            self.cuerda=2
                            self.traste=7
                            self.valid=True

                if frec>=(79) and frec<=(103):

                    if frec>=(79) and frec<=(81):
                            self.cuerda=3
                            self.traste=7
                            self.valid=True

                    if frec>=(85) and frec<=(87):
                            self.cuerda=3
                            self.traste=8
                            self.valid=True

                    if frec>=(90) and frec<=(92):
                            self.cuerda=3
                            self.traste=9
                            self.valid=True

                    if frec>=(95) and frec<=(97):
                            self.cuerda=3
                            self.traste=10
                            self.valid=True

                    if frec>=(101) and frec<=(103):
                            self.cuerda=3
                            self.traste=11
                            self.valid=True

                if frec>=(74) and frec<=(124):

                    if frec>=(74) and frec<=(76):
                            self.cuerda=4
                            self.traste=11
                            self.valid=True

                    if frec>=(122) and frec<=(124):
                            self.cuerda=4
                            self.traste=7
                            self.valid=True

                    if frec>=(128) and frec<=(130):
                            self.cuerda=4
                            self.traste=8
                            self.valid=True

                    if frec>=(133) and frec<=(135):
                            self.cuerda=4
                            self.traste=9
                            self.valid=True

class tablatura:
    def __init__(self):
        self.lista_notas=[]

    def Llenar_lista(self):
        i=0
        limite=2
        while i<limite:
            f_n=Frecuencia()
            f1=f_n.Cargar()
            f=Nota_Mastil(f1)
            f.Comparar()
            if f.valid:
                self.lista_notas.append(f)
                i+=1

    def Grabar(self):
        with open('save.bin', 'w') as archivo:
            pickle.dump(self.lista_notas,archivo)

    def Load(self):
        with open("save.bin","r") as archivo:
            notas=pickle.load(archivo)
            return notas

    def Graficar1(self):
        running=True
        while True:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    exit()
            if running:
                pantalla=pygame.display.set_mode([500,708])
                pygame.display.set_caption("Interprete Graficador")
                fondo=pygame.image.load('Blanco.jpg')
                pantalla.blit(fondo,(0,0))
                pygame.display.update()
                self.Llenar_lista()
                self.Grabar()
                lista_graficar=self.lista_notas
                pygame.display.update()
                j=0
                k=0
                for e in self.lista_notas:
                    pantalla.blit(Numero2.render(str(e.traste),True,[254,127,156]),[70 + (j*35),42+(e.cuerda*14)+ (k*102)])
                    j+=1
                    if j==10:
                        j=0
                        k+=1
                    pygame.display.update()
                running=False

    def GraficarL(self):
        while True:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    exit()
            pantalla=pygame.display.set_mode([500,708])
            pygame.display.set_caption("ultima guardada")
            fondo=pygame.image.load('Blanco.jpg')
            pantalla.blit(fondo,(0,0))
            #pantalla.blit(Numero2.render("Volver", True, (254,127,156)),(100,100))
            lista_graficar=self.Load()

            pygame.display.update()
            j=0
            k=0
            for e in lista_graficar:
                pantalla.blit(Numero2.render(str(e.traste),True,[254,127,156]),[70 + (j*35),42+(e.cuerda*14)+ (k*102)])
                j+=1
                if j==10:
                    j=0
                    k+=1
            pygame.display.update()
if __name__ == '__main__':
    main()
