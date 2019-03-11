'''
Created on Feb 4, 2019

@author: Cristina
'''
from ui.userInterface import UI
from service.service import Service
from repository.repository import Repository

ui = UI(Service(Repository("./files/Emisiuni.txt")))
ui.start()


