import os
import xml.etree.ElementTree
from PropBank import Predicate, RoleSet, Role


class PredicateList(object):

    def __init__(self):
        self.list = {}
        for r, d, f in os.walk("Frames/"):
            for file in f:
                root = xml.etree.ElementTree.parse(os.path.join(r, file)).getroot()
                for predicate in root:
                    lemma = predicate.attrib["lemma"]
                    newPredicate = Predicate.Predicate(lemma)
                    for roleSet in predicate:
                        id = roleSet.attrib["id"]
                        name = roleSet.attrib["name"]
                        newRoleSet = RoleSet.RoleSet(id, name)
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
                                newRole = Role.Role(descr, f, n)
                                newRoleSet.addRole(newRole)
                        newPredicate.addRoleSet(newRoleSet)
                    self.list[lemma] = newPredicate

    def size(self):
        return len(self.list)

    def getPredicate(self, lemma: str) -> Predicate:
        return self.list[lemma]
