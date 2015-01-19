from controller.ctr import AgendaController
from domain.validator import DuplicationException
from repository.repo import ContactRepository

__author__ = 'motan'

import unittest

class TestController(unittest.TestCase):

    def test_ctr(self):
        repo = ContactRepository("/home/motan/work/py/examen-fp/src/contacte.txt")
        ctr = AgendaController(repo)

        # ctr.addContact("1", "Giuseppe", "1234", "Altele")
        # ctr.addContact("1", "Giuseppe", "1234", "Altele")
        #
        # this throws DuplicationException.

        ctr.exportCSV("Prieteni", "/home/motan/work/py/examen-fp/src/contacte.csv")
