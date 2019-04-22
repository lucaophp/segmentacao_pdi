import cv2
import numpy as np
from copy import copy
class Descontinuidade:
	
	def __init__(self,img,output='outDescontinuidade.jpg'):
		self.img=img
		#crio imagem com mesmas dimensoes da original toda preta.
		self.imgFinal=np.zeros((len(img),len(img[0]),1))
		#filtro sobel linhas horizontais
		self.mascara=[[1,0,-1],[2,0,-2],[1,0,-1]]
		#filtro roberts horizontal
		#self.mascara=[[1,0],[-1,0]]
		self.convolucao()
		self.save(output)
		
	def vizinhaca(self,x,y):
		soma=0
		for i in range(-1,len(self.mascara)-1):
			for j in range(-1,len(self.mascara)-1):
				if x-i<0 or x-i>len(self.img)-1 or y-j<0 or y-j>len(self.img[x])-1:
					soma+=0
				else:
					soma+=self.img[x-i][y-j]*self.mascara[(i+len(self.mascara))
					%len(self.mascara)][(j+len(self.mascara))%len(self.mascara)]
		return soma/9
		
	def convolucao(self):
		for i in range(len(self.img)):
			for j in range(len(self.img[i])):
				self.imgFinal[i,j]=self.vizinhaca(i,j)

	
	def save(self,path):
		cv2.imwrite(path,self.imgFinal)





