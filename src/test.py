# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from myparser import *

# -------------------------------PARTIE DECOUVERTE------------------------------------------------------------------

# automate = Automate.creationAutomate("exempleAutomate.txt")
# automate.show("exempleAutomate")

# s1= State(1, False, False)
# s2= State(2, False, False)
# print (s1==s2)
# print (s1!=s2)

#### 2 PRISE EN MAIN

## 2.1 Création d'automates

s0 = State(0, True, False)
s1 = State(1, False, False)
s2 = State(2, False, True)

# stest = State({s0, s1, s2}, True, False)
# print(stest)

t1 = Transition(s0, "a", s0)
t2 = Transition(s0, "b", s1)
t3 = Transition(s1, "a", s2)
t4 = Transition(s1, "b", s2)
t5 = Transition(s2, "a", s0)
t6 = Transition(s2, "b", s1)

listTransition1 = [ t1, t2, t3, t4, t5, t6 ]
listState1 = [ s0, s1, s2 ]

auto = Automate(listTransition1)
auto1 = Automate(listTransition1, listState1)
auto2 = Automate.creationAutomate("auto.txt")

# print(auto.succElem(s1, "a"))
# print(auto.succ([s0, s1, s2], "a"))

# print(auto)
# auto.show("A_ListeTrans")
# print(auto1)
# auto1.show("ex2.1.2")
# print(auto2)
# auto2.show("ex2.1.3")


## 2.2 Premières manipulations
# print("Before removal")
# print(auto)

# t = Transition(s0, "a", s1)
# renvoie false
# auto.removeTransition(t)
# print("After removal")
# print(auto)

# print("Before adding transition")
# print(auto)
# auto.addTransition(t1)
# print("After adding transition")
# print(auto)

# auto.removeState(s1)
# print(auto)
# auto.addState(s1)
# print(auto)
# On remarque que ça enlève toutes les transitions
# associés à l'état et que lors du add cela ne 
# remet pas en place les transitions

# print(auto1.getListTransitionsFrom(s1))
# auto1.show("test")

# -----------------------------------PARTIE IMPLEMENTATION ALGO--------------------------------------------------------------
# TEST SUCC ACCEPTE ESTCOMPLET


# print("TEST SUCC ACCEPTE ESTCOMPLET")

# auto1.show("tmp")
# print(auto1.succ(listState1, 'b'))
# print(Automate.accepte(auto1, "aba"))
# print(Automate.accepte(auto1, "aaabba"))
# print(auto1.listStates)
# auto1.removeTransition(t4)
# print(Automate.estComplet(auto1, auto1.getAlphabetFromTransitions()))
# auto1.addTransition(t4)
# print(Automate.estComplet(auto1, auto1.getAlphabetFromTransitions()))

# TEST DETERMINISATION AUTOMATE
print("TEST DETERMINISATION D'AUTOMATE")

sA = State('A', True, False)
sB = State('B', False, False)
sC = State('C', False, True)

listTransi = [
    Transition(sA, 0, sA),
    Transition(sA, 1, sA),
    Transition(sA, 1, sB),
    Transition(sB, 0, sC),
    Transition(sB, 1, sC)    
]

autoTest = Automate(listTransi)
autoTestDeterministe = Automate.determinisation(autoTest)
print("AutoTest: \n")
print(autoTest)
print("AutoTest déterminiser: \n")
print(autoTestDeterministe)

# :( Error: test.dot: syntax error in line 3 near '''gio: file:///home/agape/Documents/Cours/MATHS/PROJET/src/qsdf.pdf: Error when getting information for file “/home/agape/Documents/Cours/MATHS/PROJET/src/qsdf.pdf”: No such file or directory
# pas de stack d'erreur du coup dur a debugger, ça doit être à cause du label... (problème d'affichage et non d'algo normalement)
# autoTestDeterministe.show('test')

print("\n\n\n")

auto3 = Automate.creationAutomate("./auto2.txt")
print("Automate 3: \n")
print(auto3)

auto3Deterministe = Automate.determinisation(auto3)
print("Automate 3 déterminiser: \n")
print(auto3Deterministe)
# problème de label pour la conversion en .dot puis en pdf à mon avis...
# auto3Deterministe.show("test")