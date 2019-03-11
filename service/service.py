'''
Created on Feb 4, 2019

@author: Cristina
'''
from domain.emisiune import Emisiune
import random

class Service:
    
    def __init__(self,repository):
        self.__repository = repository
        self.__blocate = []
    
    def getAll(self):
        return self.__repository.getAll()
    
    def stergeEmisiune(self,idEmisiune):
        tipuriBlocate = self.tipuriBlocate()
        emisiune = self.__repository.findOne(idEmisiune)
        if emisiune != None and emisiune.getTip() not in tipuriBlocate:
            return self.__repository.delete(idEmisiune)
    
    def updateEmisiune(self,nume,tip,durata,descriere):
        tipuriBlocate = self.tipuriBlocate()
        if tip not in tipuriBlocate:
            return self.__repository.update(Emisiune(nume,tip,durata,descriere))
    
    def genereazaProgramTV(self):
        listaEmisiuni = [emisiune for emisiune in self.getAll() if emisiune.getTip() not in self.tipuriBlocate()]
        if len(listaEmisiuni) == 0:
            return {}
        program = {}
        durataCurenta = 0
        while durataCurenta < 12 and listaEmisiuni != []:
            index = random.randint(0,len(listaEmisiuni)-1)
            emisiune = listaEmisiuni[index]
            program[durataCurenta+10] = emisiune
            durataCurenta += int(emisiune.getDurata())
            listaEmisiuni.pop(index)
        
        if durataCurenta < 12:
            while durataCurenta < 12:   
                listaEmisiuni = [emisiune for emisiune in self.getAll() if emisiune.getTip() not in self.tipuriBlocate()]
                while durataCurenta < 12 and listaEmisiuni != []:
                    index = random.randint(0,len(listaEmisiuni)-1)
                    emisiune = listaEmisiuni[index]
                    program[durataCurenta+10] = Emisiune(emisiune.getNume(),emisiune.getTip(),emisiune.getDurata(),emisiune.getDescriere()+'*')
                    durataCurenta += int(emisiune.getDurata())
                    listaEmisiuni.pop(index)  
                    
        return program
    
    def blocheaza(self,tip):
        self.__blocate.append(tip)
        
    def tipuriBlocate(self):
        return self.__blocate
    
    def deblocheazaTip(self,tip):
        self.__blocate.remove(tip)
        
    def deblocheazaTot(self):
        self.__blocate.clear()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    