'''
Created on Feb 4, 2019

@author: Cristina
'''

class Menu:
    
    def showMenu(self):
        print('---------- MENIU APLICATIE ----------\n')
        print('1. Afiseaza toate emisiunile')
        print('2. Sterge o emisiune')
        print('3. Actualizeaza o emisiune')
        print('4. Genereaza')
        print('5. BLOCARE')
        print('0. Inchide aplicatia')
        
    def showMenuBlocare(self):
        print('---- BLOCARE ----')
        print('1. Afisati lista cu tipuri blocate')
        print('2. Deblocheaza un tip')
        print('3. Deblocheaza toate tipurile')
        print('4. Blocheaza tip')
        print('0. Revenire la meniul principal')