import cv2
import numpy as np
from copy import copy
class Otsu:
	def __init__(self,img,output='outOtsu.jpg'):
		self.img=img
		#crio imagem com mesmas dimensoes da original toda preta.
		self.imgFinal=np.zeros((len(img),len(img[0]),1))
		self.freq={}
		self.histograma().normalize().binarizacao()
		self.save(output)

	'''
		Calcula a frequencia para cada intensidade da imagem.
	'''
	def histograma(self):
		for i in range(len(self.img)):
			for j in range(len(self.img[i])):
				if self.img[i][j] in self.freq:
					self.freq[self.img[i][j]]+=1
				else:
					self.freq[self.img[i][j]]=1
		return self
	def normalize(self):
		total_pixels=len(self.img)*len(self.img[0])
		for tom in self.freq:
			self.freq[tom]=(float(self.freq[tom])/(total_pixels))
		return self
	def otsu(self):
		probabilidade=list()
		media=list()
		max_between=float(0)
		between=list()
		limear=float(0)
		#criando histograma acumulado
		if 0 in self.freq:
			probabilidade.append(self.freq[0])
		else:
			probabilidade.append(0)
		media.append(0)
		for i in range(1,256):
			if i not in self.freq:
				probabilidade.append(0)
				media.append(0)
			else:
				probabilidade.append(probabilidade[i-1]+self.freq[i])
				media.append(media[i-1]+i*self.freq[i])
		#encontra o otimo limear, pela variancia entre grupos
		for i in range(0,255):
			if probabilidade[i]!=float(0) and probabilidade[i]!=float(1):
				between.append((media[255]*probabilidade[i]-media[i])**2/(probabilidade[i]*(1-probabilidade[i])))
			else:
				between.append(float(0))
			if between[i]>max_between:
				max_between=between[i]
				limear=i
		return limear
	def binarizacao(self):
		limear=self.otsu()
		for i in range(len(self.img)):
			for j in range(len(self.img[i])):
				if self.img[i,j]<limear:
					self.imgFinal[i,j]=0
				else:
					self.imgFinal[i,j]=255
	def save(self,path):
		cv2.imwrite(path,self.imgFinal)




