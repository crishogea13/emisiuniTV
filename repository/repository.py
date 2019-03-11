'''
Created on Feb 4, 2019

@author: Cristina
'''
from domain.emisiune import Emisiune

class Repository:
    
    def __init__(self,fileName):
        self.__emisiuni = {}
        self.__fileName = fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        try:
            file = open(self.__fileName,'r')
        except IOError:
            return
        
        linie = file.readline().strip()
        
        while linie != "":
            atribute = linie.split('|')
            emisiune = self.__extrageEmisiune(atribute)
            self.save(emisiune)
            
            linie = file.readline().strip()
            
        file.close()
        
    def __writeAllToFile(self):
        try:
            file = open(self.__fileName,'w')
        except IOError:
            return
        
        for emisiune in self.getAll():
            file.write(self.__toString(emisiune))
            
        file.close()
            
        
    def getAll(self):
        return self.__emisiuni.values()
    
    def save(self,emisiune):
        if not self.__emisiuni.__contains__(emisiune.getID()):
            self.__emisiuni[emisiune.getID()] = emisiune
            return emisiune
    
    def delete(self,idEmisiune):
        try:
            emisiuneStearsa = self.__emisiuni.pop(idEmisiune)
            self.__writeAllToFile()
            return emisiuneStearsa
        except KeyError:
            pass
        
    def update(self,emisiune):
        if self.__emisiuni.__contains__(emisiune.getID()):
            self.__emisiuni[emisiune.getID()] = emisiune
            self.__writeAllToFile()
            return emisiune
    
    def findOne(self,idEmisiune):
        if self.__emisiuni.__contains__(idEmisiune):
            return self.__emisiuni[idEmisiune]
            
    def __toString(self,emisiune):
        return emisiune.getNume()+'|'+emisiune.getTip()+'|'+emisiune.getDurata()+'|'+emisiune.getDescriere()+'\n'

    def __extrageEmisiune(self,atribute):
        return Emisiune(atribute[0],atribute[1],atribute[2],atribute[3])






