from PropBank import ArgumentType


class Role(object):

    def __init__(self, description: str, f: str, n: str):
        self.description = description
        self.f = f
        self.n = n

    def getDescription(self) -> str:
        return self.description

    def getF(self) -> str:
        return self.f

    def getN(self) -> str:
        return self.n

    def getArgumentType(self) -> ArgumentType:
        return ArgumentType.ArgumentType.getArguments("ARG" + self.f.upper())