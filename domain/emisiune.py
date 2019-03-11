'''
Created on Feb 4, 2019

@author: Cristina
'''

class Emisiune:
    
    def __init__(self,nume,tip,durata,descriere):
        self.__nume = nume
        self.__tip = tip
        self.__durata = durata
        self.__descriere = descriere
        
    def getID(self):
        return self.__nume,self.__tip

    def getNume(self):
        return self.__nume


    def getTip(self):
        return self.__tip


    def getDurata(self):
        return self.__durata


    def getDescriere(self):
        return self.__descriere
    
    def __str__(self):
        return 'NUME: ' + self.__nume + ' | ' + \
               'TIP: ' + self.__tip + ' | ' + \
               'DURATA: ' + self.__durata + ' | ' + \
               'DESCRIERE: ' + self.__descriere