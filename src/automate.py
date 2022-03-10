# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from itertools import product
from automateBase import AutomateBase



class Automate(AutomateBase):
        
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ (self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        res = set()
        for state in listStates:
            # .update() == |= ajout des element d'un tableau à un ensemble --> éviter doublons
            res.update(self.succElem(state, lettre))
            
        return list(res)




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        tmpStateList = auto.getListInitialStates()
        

        for i in range(len(mot)):
            # Obtention de la liste des états accessible 
            tmpStateList = Automate.succ(auto, tmpStateList, mot[i])
        
        #On regarde dans la liste d'états si il y a un état final
        return State.isFinalIn(tmpStateList)


    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        for state in auto.listStates:
            for lettre in alphabet:
                if(len(auto.succElem(state, lettre)) < 1):
                    return False
        return True


        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        if(len(auto.getListInitialStates()) > 1):
            return False
        for state in auto.listStates:
            for lettre in auto.getAlphabetFromTransitions():
                if(len(auto.succElem(state, lettre)) > 1):
                    return False
        return True
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        res = copy.deepcopy(auto)
        
        # Creation d'un état "poubelle", on a pour hypothèse qu'aucun état a un label -1
        poubelle = State(-1, False, False)
        res.addState(poubelle)
        
        for state in auto.listStates:
            for lettre in auto.getAlphabetFromTransitions():
                if(len(auto.succElem(state, lettre)) < 1):
                    t = Transition(state, lettre, poubelle)
                    res.addTransition(t)
        return res

       

    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        if(Automate.estDeterministe(auto)):
            return copy.deepcopy(auto)
        
        alphabet = auto.getAlphabetFromTransitions()

        # Liste d'états qui sont chacun sous la forme d'une liste et non d'instance de State
        stateList = []
        transitionList = []
        
        initStateList = auto.getListInitialStates()
                
        stateList.append(initStateList)
        
        # state: liste d'états vers lequelles ils existent une transition en lettre
        for state in stateList:
            for lettre in alphabet:
                
                # On obtient la liste des états atteignable à partir de state et de la lettre
                newState = auto.succ(state, lettre)
                

                if(newState != []):
                    if(newState not in stateList):
                        stateList.append(newState)

                    transitionList.append(
                        Transition(
                            State(str(set([s.label for s in state])), state == initStateList, State.isFinalIn(state)), 
                            lettre, 
                            State(str(set([s.label for s in newState])), False, State.isFinalIn(newState))
                        )
                    )
        
        # print(stateList)
        # print(transitionList)
        
        return Automate(transitionList)
            
        
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
              
   
    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return
        

   
       

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return




