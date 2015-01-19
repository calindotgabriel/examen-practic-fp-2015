from controller.ctr import AgendaController
from repository.repo import ContactRepository
from ui.console import Console

__author__ = 'motan'

repo = ContactRepository("/home/motan/work/py/examen-fp/src/contacte.txt")
ctr = AgendaController(repo)

csl = Console(ctr)
csl.run_ui()