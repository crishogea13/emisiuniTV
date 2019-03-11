'''
Created on Feb 4, 2019

@author: Cristina
'''
from ui.menu import Menu

class UI:
    
    def __init__(self,service):
        self.__service = service
    
    def __afiseazaEmisiuni(self):
        for emisiune in self.__service.getAll():
            print(emisiune)
            
        print('\n')
        
    def __stergeEmisiune(self):
        nume = input('Dati numele emisiunii: ')
        tip = input('Dati tipul emisiunii: ')
        emisiuneStearsa = self.__service.stergeEmisiune((nume,tip))
        if emisiuneStearsa == None:
            print('Nu exista emisiunea pe care doriti sa o stergeti!\n')
        else:
            print('Emisiunea a fost stearsa cu succes!\n')
            
    def __modificaEmisiune(self):
        nume = input('Dati numele emisiunii: ')
        tip = input('Dati tipul emisiunii: ')
        durata = input('Dati noua durata a emisiunii: ')
        descriere = input('Dati noua descriere a emisiunii: ')
        emisiuneModificata = self.__service.updateEmisiune(nume,tip,durata,descriere)
        if emisiuneModificata == None:
            print('Nu exista emisiunea pe care doriti sa o modificati!\n')
        else:
            print('Emisiunea a fost modificata cu succes!\n')
            
    def __genereazaProgramTV(self):
        program = self.__service.genereazaProgramTV()
        print('Ora        Nume           Tip        Descriere\n')
        for ora in program.keys():
            emisiune = program[ora]
            print(ora,'       ',emisiune.getNume(),'        ',emisiune.getTip(),'        ',emisiune.getDescriere(),'\n')
        print('\n')
        
    def __tipuriBlocate(self):
        tipuriBlocate = self.__service.tipuriBlocate()
        if len(tipuriBlocate) == 0:
            print('Nu exista niciun tip blocat!\n')
        else:
            for tip in tipuriBlocate:
                print(tip)
            print('\n')
            
    def __deblocheazaTip(self):
        tip = input('Introduceti tipul pe care doriti sa il deblocati: ')
        tipuriBlocate = self.__service.tipuriBlocate()
        if tip not in tipuriBlocate:
            print('Tipul nu e blocat!\n')
        else:
            self.__service.deblocheazaTip(tip)
            print('Tipul a fost deblocat!\n')
        
    def __deblocheazaTot(self):
        tipuriBlocate = self.__service.tipuriBlocate()
        if len(tipuriBlocate) == 0:
            print('Nu exista niciun tip blocat!\n')
        else:
            self.__service.deblocheazaTot()
            print('Toate tipurile au fost deblocate!\n')
        
    def __blocheazaTip(self):
        tip = input('Introduceti tipul pe care doriti sa il blocati: ')
        tipuriBlocate = self.__service.tipuriBlocate()
        if tip in tipuriBlocate:
            print('Tipul e deja blocat!\n')
        else:
            self.__service.blocheaza(tip)
            print('Tipul a fost blocat!\n')
        
    def __operatiiBlocare(self):
        comenzi = {'1':self.__tipuriBlocate,'2':self.__deblocheazaTip,'3':self.__deblocheazaTot,'4':self.__blocheazaTip}
        while True:
            Menu.showMenuBlocare(self)
            comanda = input('Dati comanda dorita: ')
            if comanda == "0":
                print("La revedere!")
                break
            if not comenzi.__contains__(comanda):
                print("Ati introdus o comanda invalida!\n\n")
            else:
                comenzi[comanda]()
        
        
        
    def start(self):
        comenzi = {'1':self.__afiseazaEmisiuni, '2':self.__stergeEmisiune,'3':self.__modificaEmisiune,'4':self.__genereazaProgramTV,'5':self.__operatiiBlocare}
        
        while True:
            Menu.showMenu(self)
            comanda = input('Dati comanda dorita: ')
            if comanda == "0":
                print("La revedere!")
                break
            if not comenzi.__contains__(comanda):
                print("Ati introdus o comanda invalida!\n\n")
            else:
                comenzi[comanda]()
