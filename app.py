#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import cv2
import math
import sys
from kmeans import KMeans
#from crescimento import Crescimento
from otsu import Otsu
from descontinuidade import Descontinuidade
def input_kmeans():
	output='output.png'
	if(len(sys.argv)==5):
		output=sys.argv[4]
		nomeImagem=sys.argv[2]
		centrosK=sys.argv[3]

	elif(len(sys.argv)==4):
		nomeImagem=sys.argv[2]
		centrosK=sys.argv[3]
	elif(len(sys.argv)==3):
		nomeImagem=sys.argv[2]
		centrosK=5
	else:
		nomeImagem=None
		centrosK=None
		print(u'Número de parametros invalido!!! é necessario seguir esse padrão de entrada: \n python app.py kmeans [caminho da imagem] [numero de K]')
	if nomeImagem!=None and centrosK!=None:
		img=cv2.imread(nomeImagem)
		k=KMeans(int(centrosK),img,output)
		k.agrupa()
#def input_crescimento():
#	pass
def input_otsu():
	if(len(sys.argv)==4):
		img=cv2.imread(sys.argv[2],2)
		otsu=Otsu(img,sys.argv[3])
	else:
		img=cv2.imread(sys.argv[2],2)
		otsu=Otsu(img)
def input_bordas():
	if(len(sys.argv)==4):
		img=cv2.imread(sys.argv[2],2)
		d=Descontinuidade(img,sys.argv[3])
	elif(len(sys.argv)==3):
		img=cv2.imread(sys.argv[2],2)
		d=Descontinuidade(img)
	else:
		print(u'Número de parametros invalido!!! é necessario seguir esse padrão de entrada: \n python app.py sobel [caminho da imagem] [caminho da imagem_saida]')


if(len(sys.argv)>1):
	if(sys.argv[1]=='kmeans'):
		input_kmeans()
	#elif(sys.argv[1]=='crescimento'):
	#	input_crescimento()
	elif(sys.argv[1]=='otsu'):
		input_otsu()
	elif(sys.argv[1]=='sobel'):
		input_bordas()
	else:
		print(u'Estão disponiveis os algoritmos de kmeans[kmeans], detecção de bordas[sobel] e limearização[otsu]')

