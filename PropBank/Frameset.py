from PropBank.ArgumentType import ArgumentType
from PropBank.FramesetArgument import FramesetArgument
import xml.etree.ElementTree


class Frameset(object):

    __framesetArguments: list
    __id: str

    def __init__(self, _id: str):
        """
        A constructor of Frameset class which takes id as input and initializes corresponding attribute

        PARAMETERS
        ----------
        _id : str
            Id of the frameset
        """
        self.__id = _id
        self.__framesetArguments = []

    def initWithFile(self, fileName: str):
        """
        Another constructor of Frameset class which takes filename as input and reads the frameset

        PARAMETERS
        ----------
        fileName : str
            File name of the file to read frameset
        """
        root = xml.etree.ElementTree.parse(fileName).getroot()
        self.__id = root.attrib["id"]
        for child in root:
            self.__framesetArguments.append(FramesetArgument(child.attrib["name"], child.text))

    def containsArgument(self, argumentType: ArgumentType) -> bool:
        """
        containsArgument method which checks if there is an Argument of the given argumentType.

        PARAMETERS
        ----------
        argumentType : ArgumentType
            ArgumentType of the searched Argument

        RETURNS
        -------
        bool
            true if the Argument with the given argumentType exists, false otherwise.
        """
        for framesetArgument in self.__framesetArguments:
            if ArgumentType.getArguments(framesetArgument.getArgumentType()) == argumentType:
                return True
        return False

    def addArgument(self, argumentType: str, definition: str):
        """
        The addArgument method takes a type and a definition of a FramesetArgument as input, then it creates a new
        FramesetArgument from these inputs and adds it to the framesetArguments list.

        PARAMETERS
        ----------
        argumentType : str
            Type of the new FramesetArgument
        definition : str
            Definition of the new FramesetArgument
        """
        check = False
        for framesetArgument in self.__framesetArguments:
            if framesetArgument.getArgumentType() == argumentType:
                framesetArgument.setDefinition(definition)
                check = True
                break
        if not check:
            arg = FramesetArgument(argumentType, definition)
            self.__framesetArguments.append(arg)

    def deleteArgument(self, argumentType: str, definition: str):
        """
        The deleteArgument method takes a type and a definition of a FramesetArgument as input, then it searches for the
        FramesetArgument with these type and definition, and if it finds removes it from the framesetArguments list.

        PARAMETERS
        ----------
        argumentType : str
            Type of the to be deleted FramesetArgument
        definition : str
            Definition of the to be deleted FramesetArgument
        """
        for framesetArgument in self.__framesetArguments:
            if framesetArgument.getArgumentType() == argumentType and framesetArgument.getDefinition() == definition:
                self.__framesetArguments.remove(framesetArgument)
                break

    def getFramesetArguments(self) -> list:
        """
        Accessor for framesetArguments.

        RETURNS
        -------
        list
            framesetArguments.
        """
        return self.__framesetArguments

    def getId(self) -> str:
        """
        Accessor for id.

        RETURNS
        -------
        str
            id.
        """
        return self.__id

    def setId(self, _id: str):
        """
        Mutator for id.

        PARAMETERS
        ----------
        _id : str
            id to set.
        """
        self.__id = _id
