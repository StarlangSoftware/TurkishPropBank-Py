from PropBank import Role


class RoleSet(object):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.roles = []

    def getId(self) -> str:
        return self.id

    def getName(self) -> str:
        return self.name

    def size(self) -> int:
        return len(self.roles)

    def addRole(self, role: Role):
        self.roles.append(role)

    def getRole(self, index: int) -> Role:
        return self.roles[index]