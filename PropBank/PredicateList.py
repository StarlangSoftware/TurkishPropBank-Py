import os
import xml.etree.ElementTree
from collections import KeysView

from PropBank.Predicate import Predicate
from PropBank.RoleSet import RoleSet
from PropBank.Role import Role


class PredicateList(object):

    __list: dict

    def __init__(self):
        """
        A constructor of PredicateList class which reads all predicate files inside the 'Frames' folder. For each
        file inside that folder, the constructor creates a Predicate and puts in inside the list dictionary.
        """
        self.__list = {}
        for r, d, f in os.walk("Frames/"):
            for file in f:
                root = xml.etree.ElementTree.parse(os.path.join(r, file)).getroot()
                for predicate in root:
                    lemma = predicate.attrib["lemma"]
                    newPredicate = Predicate(lemma)
                    for roleSet in predicate:
                        _id = roleSet.attrib["id"]
                        name = roleSet.attrib["name"]
                        newRoleSet = RoleSet(_id, name)
                        for roles in roleSet:
                            for role in roles:
                                if "descr" in role.attrib:
                                    descr = role.attrib["descr"]
                                else:
                                    descr = ""
                                if "f" in role.attrib:
                                    f = role.attrib["f"]
                                else:
                                    f = ""
                                if "n" in role.attrib:
                                    n = role.attrib["n"]
                                else:
                                    n = ""
                                newRole = Role(descr, f, n)
                                newRoleSet.addRole(newRole)
                        newPredicate.addRoleSet(newRoleSet)
                    self.__list[lemma] = newPredicate

    def size(self):
        """
        The size method returns the number of predicates inside the list.

        RETURNS
        -------
        int
            the size of the list dict.
        """
        return len(self.__list)

    def getPredicate(self, lemma: str) -> Predicate:
        """
        getPredicate method returns the Predicate with the given lemma.

        PARAMETERS
        ----------
        lemma : str
            Lemma of the searched predicate

        RETURNS
        -------
        Predicate
            Predicate which has the given lemma.
        """
        return self.__list[lemma]

    def getLemmaList(self) -> KeysView:
        """
        The method returns all lemma in the predicate list.

        RETURNS
        -------
        dict
            All lemma in the predicate list.
        """
        return self.__list.keys()
