class Argument(object):

    def __init__(self, argument: str):
        if "$" in argument:
            self.argumentType = argument[0:argument.index("$")]
            self.id = argument[argument.index("$") + 1:]
        else:
            self.argumentType = "NONE"

    def initWithId(self, argumentType: str, id: str):
        self.argumentType = argumentType
        self.id = id

    def getArgumentType(self) -> str:
        return self.argumentType

    def getId(self) -> str:
        return self.id

    def __str__(self) -> str:
        if self.argumentType == "NONE":
            return self.argumentType
        else:
            return self.argumentType + "$" + self.id