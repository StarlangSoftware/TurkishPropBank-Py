import os
import xml.etree.ElementTree
from PropBank.Predicate import Predicate
from PropBank.RoleSet import RoleSet
from PropBank.Role import Role


class PredicateList(object):

    """
    A constructor of PredicateList class which reads all predicate files inside the 'Frames' folder. For each
    file inside that folder, the constructor creates a Predicate and puts in inside the list dictionary.
    """
    def __init__(self):
        self.list = {}
        for r, d, f in os.walk("Frames/"):
            for file in f:
                root = xml.etree.ElementTree.parse(os.path.join(r, file)).getroot()
                for predicate in root:
                    lemma = predicate.attrib["lemma"]
                    newPredicate = Predicate(lemma)
                    for roleSet in predicate:
                        id = roleSet.attrib["id"]
                        name = roleSet.attrib["name"]
                        newRoleSet = RoleSet(id, name)
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
                    self.list[lemma] = newPredicate

    """
    The size method returns the number of predicates inside the list.
    
    RETURNS
    -------
    int
        the size of the list dict.
    """
    def size(self):
        return len(self.list)

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
    def getPredicate(self, lemma: str) -> Predicate:
        return self.list[lemma]
