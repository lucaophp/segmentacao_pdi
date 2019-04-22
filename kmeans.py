#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import cv2
import math
import copy
import sys
class KMeans:
	def __init__(self,K,img,output):
		self.K=K
		self.img=img
		self.centers=self.__init_centroids__()
		self.grupo=list()
		for i in range(self.K):
			self.grupo.append([])
		self.output=output



	def __init_centroids__(self):
		centers=[]
		for k in range(self.K):
			centers.append((int(random.random()*1000%len(self.img)),int(random.random()*1000%len(self.img[0])),int(random.random()*1000%255),int(random.random()*1000%255),(int(random.random()*1000%255))))
		print centers
		return centers
	def reset_groups(self):
		self.grupo=list()
		for i in range(self.K):
			self.grupo.append([])
	def dist(self,p1,p2):
		soma=0
		for i in range(2,len(self.centers[0])):
			soma=soma+(p2[i]-p1[i])**2

		return math.sqrt(soma)
	def recalcula_centroid(self):
		centers=[]
		
		for i,g in enumerate(self.grupo):
			tupla=list()
			soma=list()
			for ki in range(len(self.centers[0])):
				soma.append(0)
			for j,e in enumerate(g):
				for ki2 in range(len(self.centers[0])):
					soma[ki2]=soma[ki2]+e[ki2]
			for ki in range(len(self.centers[0])):
				if(len(g)!=0):
					tupla.append(soma[ki]/(len(g)))
				else:
					tupla.append(int(random.random()*1000)%255)
			centers.append(tuple(tupla))
		return centers
	def agrupa(self):
		iteracao=0
		im=()
		while True:
			nimg=copy.copy(self.img)
			self.reset_groups()
			for i,x in enumerate(self.img):
				for j,y in enumerate(self.img[x]):
					im=(i,j,self.img[i][j][0],self.img[i][j][1],self.img[i][j][2])
					distancia=range(self.K)
					for k in range(self.K):
						
						distancia[k]=self.dist(im,self.centers[k])
					
					menor=distancia.index(min(distancia))
					self.grupo[menor].append(im)
					nimg[i][j][0]=self.centers[menor][2]
					nimg[i][j][1]=self.centers[menor][3]
					nimg[i][j][2]=self.centers[menor][4]
					
			centers=self.recalcula_centroid()
			iteracao=iteracao+1
			if centers==self.centers or iteracao==5:
				cv2.imshow('kmeans',nimg)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
				cv2.imwrite(self.output,nimg)
				break
			self.centers=centers
			print self.centers