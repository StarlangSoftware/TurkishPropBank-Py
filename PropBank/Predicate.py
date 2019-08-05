from PropBank import RoleSet


class Predicate(object):

    def __init__(self, lemma: str):
        self.lemma = lemma
        self.roleSets = []

    def getLemma(self) -> str:
        return self.lemma

    def addRoleSet(self, roleSet: RoleSet):
        self.roleSets.append(roleSet)

    def size(self) -> int:
        return len(self.roleSets)

    def getRoleSet(self, index: int) -> RoleSet:
        return self.roleSets[index]

    def getRoleSetWithId(self, roleId: str) -> RoleSet:
        for roleSet in self.roleSets:
            if roleSet.getId() == roleId:
                return roleSet
        return None