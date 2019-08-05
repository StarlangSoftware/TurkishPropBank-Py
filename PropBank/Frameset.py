from PropBank import ArgumentType, FramesetArgument
import xml.etree.ElementTree


class Frameset(object):

    def __init__(self, id: str):
        self.id = id
        self.framesetArguments = []

    def initWithFile(self, fileName: str):
        root = xml.etree.ElementTree.parse(fileName).getroot()
        self.id = root.attrib["id"]
        for child in root:
            self.framesetArguments.append(FramesetArgument.FramesetArgument(child.attrib["name"], child.text))

    def containsArgument(self, argumentType: ArgumentType) -> bool:
        for framesetArgument in self.framesetArguments:
            if ArgumentType.ArgumentType.getArguments(framesetArgument.getArgumentType()) == argumentType:
                return True
        return False

    def addArgument(self, type: str, definition: str):
        check = False
        for framesetArgument in self.framesetArguments:
            if framesetArgument.getArgumentType() == type:
                framesetArgument.setDefinition(definition)
                check = True
                break
        if not check:
            arg = FramesetArgument.FramesetArgument(type, definition)
            self.framesetArguments.append(arg)

    def deleteArgument(self, type: str, definition: str):
        for framesetArgument in self.framesetArguments:
            if framesetArgument.getArgumentType() == type and framesetArgument.getDefinition() == definition:
                self.framesetArguments.remove(framesetArgument)
                break

    def getFramesetArguments(self) -> list:
        return self.framesetArguments

    def getId(self) -> str:
        return self.id

    def setId(self, id: str):
        self.id = id