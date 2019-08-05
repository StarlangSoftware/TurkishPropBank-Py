class FramesetArgument(object):

    def __init__(self, argumentType: str, definition: str):
        self.argumentType = argumentType
        self.definition = definition

    def getArgumentType(self) -> str:
        return self.argumentType

    def getDefinition(self) -> str:
        return self.definition

    def setDefinition(self, definition: str):
        self.definition = definition

    def __str__(self) -> str:
        return self.argumentType + ":" + self.definition