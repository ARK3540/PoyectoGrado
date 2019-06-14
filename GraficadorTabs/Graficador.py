import math                                                                      #Operaciones matematicas simples
import pygame                                                                    #Entorno grafico de python
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
import sys                                                                        #Interactua con el sistema operativo



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
pygame.init()                                                                   #Inicializamos los modulos de pygame
pantalla=pygame.display.set_mode([ANCHO,ALTO])					#Creamos una ventana
pantalla.fill(BLANCO)                                                           #Llenamos la ventana de un color solido
#pygame.draw.circle(pantalla,NEGRO,centro,3)                                     #Funcion circulo (plano,color,posicion,radio)
fuente=pygame.font.Font("dalila.ttf",25)                                        #fuente y tamanos a variables
Numero = pygame.font.Font("dalila.ttf",25)
Numero2 = pygame.font.Font("dalila.ttf",18)
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
# Clase  menu
class Opcion :
    ver=False
    def __init__(self,texto, pos,tam,ido,actual):
        self.ido=ido
        self.actual=actual
        self.texto=texto
        self.pos=pos
        self.fuente=pygame.font.Font("dalila.ttf",tam)
        self.set_rect()
        self.dibujar()
    def set_rect(self):
        self.Enunciado()
        self.rect=self.txt.get_rect()
        self.rect.topleft=self.pos

    def colortxt(self):
        if self.ver:
            if self.actual:
                return(AZUL)
            else:
                return(VERDE)

        else:
            if self.actual:
                return(AZUL)
            else:
                return(LETRA)

    def Enunciado(self):
        self.txt=self.fuente.render(self.texto,True,self.colortxt())
    def dibujar(self):
        self.Enunciado()
        pantalla.blit(self.txt,self.rect)

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
      print FrecNota,                                                            #<<<<<--------
      return FrecNota


#main
if __name__ == '__main__':


    pygame.display.flip()
    dibujo=0
    nota=0
    time=2000
    lttnota='O'
    vatTerminal=0

    
    '''
    opciones=[Opcion("Grabar",(60,25),60,1,0),Opcion("Prueba",(60,80),60,2,0),Opcion("Prueba",(60,135),60,3,0),Opcion("Cerrar",(60,190),60,4,0)]
    fondo=pygame.image.load('fondovioleta.jpg').convert()
    todos=pygame.sprite.Group()
    #todos.add(n)
    while aux:
        puntos=[]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aux=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                for op in opciones:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        if op.ido==1:
                            dibujo=1
                            op.actual=1
                            pygame.display.set_mode([600,300])
                            fondo=pygame.image.load('TablaturaPlantilla.png').convert()

                        if op.ido==2:
                            dibujo=2
                            op.actual=1

                        if op.ido==3:
                            dibujo=3
                            op.actual=1

                        if op.ido==4:
                            dibujo=4
                            op.actual=1
                            sys.exit()

                    for op2 in opciones:
                        if op2.ido!=dibujo:
                            op2.actual=0
        #pantalla.fill(BLANCO)
        pantalla.blit(fondo,(0,0))
        for op in opciones:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                op.ver=True
            else:
                op.ver=False
            op.dibujar()
        #Redibujado y actualizacion

        #Acoplar frecuencia en  la escala segun la nota a afinar'''
	'''if time==2000:
           frec=int(cargar())
	   time=0
	time+=1'''
        '''if frec>=(nota-5) and frec <= (nota+5):
		          notadp = tiponota.render(lttnota,0,VERDE)
        else:
		notadp = tiponota.render(lttnota,0,ROJO)

        pantalla.blit(notadp,[500,140])'''
        ########################################################
        todos.draw(pantalla)
        pygame.display.update()
