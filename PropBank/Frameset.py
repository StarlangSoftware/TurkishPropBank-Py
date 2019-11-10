from PropBank.ArgumentType import ArgumentType
from PropBank.FramesetArgument import FramesetArgument
import xml.etree.ElementTree


class Frameset(object):

    _framesetArguments: list
    _id: str

    """
    A constructor of Frameset class which takes id as input and initializes corresponding attribute

    PARAMETERS
    ----------
    id : str
        Id of the frameset
    """
    def __init__(self, id: str):
        self._id = id
        self._framesetArguments = []

    """
    Another constructor of Frameset class which takes filename as input and reads the frameset

    PARAMETERS
    ----------
    fileName : str  
        File name of the file to read frameset
    """
    def initWithFile(self, fileName: str):
        root = xml.etree.ElementTree.parse(fileName).getroot()
        self._id = root.attrib["id"]
        for child in root:
            self._framesetArguments.append(FramesetArgument(child.attrib["name"], child.text))

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
    def containsArgument(self, argumentType: ArgumentType) -> bool:
        for framesetArgument in self._framesetArguments:
            if ArgumentType.getArguments(framesetArgument.getArgumentType()) == argumentType:
                return True
        return False

    """
    The addArgument method takes a type and a definition of a FramesetArgument as input, then it creates a new FramesetArgument from these inputs and
    adds it to the framesetArguments list.

    PARAMETERS
    ----------
    type : str 
        Type of the new FramesetArgument
    definition : str
        Definition of the new FramesetArgument
    """
    def addArgument(self, argumentType: str, definition: str):
        check = False
        for framesetArgument in self._framesetArguments:
            if framesetArgument.getArgumentType() == argumentType:
                framesetArgument.setDefinition(definition)
                check = True
                break
        if not check:
            arg = FramesetArgument(argumentType, definition)
            self._framesetArguments.append(arg)

    """
    The deleteArgument method takes a type and a definition of a FramesetArgument as input, then it searches for the FramesetArgument with these type and
    definition, and if it finds removes it from the framesetArguments list.

    PARAMETERS
    ----------
    type : str 
        Type of the to be deleted FramesetArgument
    definition : str 
        Definition of the to be deleted FramesetArgument
    """
    def deleteArgument(self, argumentType: str, definition: str):
        for framesetArgument in self._framesetArguments:
            if framesetArgument.getArgumentType() == argumentType and framesetArgument.getDefinition() == definition:
                self._framesetArguments.remove(framesetArgument)
                break

    """
    Accessor for framesetArguments.

    RETURNS
    -------
    list
        framesetArguments.
    """
    def getFramesetArguments(self) -> list:
        return self._framesetArguments

    """
    Accessor for id.

    RETURNS
    -------
    str
        id.
    """
    def getId(self) -> str:
        return self._id

    """
    Mutator for id.

    PARAMETERS
    ----------
    id : str 
        id to set.
    """
    def setId(self, id: str):
        self._id = id