class FramesetArgument(object):

    __argumentType: str
    __definition: str

    """
    A constructor of FramesetArgument class which takes argumentType and definition as input and initializes
    corresponding attributes

    PARAMETERS
    ----------
    argumentType : str
        ArgumentType of the frameset argument
    definition : str
        Definition of the frameset argument
    """
    def __init__(self, argumentType: str, definition: str):
        self.__argumentType = argumentType
        self.__definition = definition

    """
    Accessor for argumentType.

    RETURNS
    -------
    str
        argumentType.
    """
    def getArgumentType(self) -> str:
        return self.__argumentType

    """
    Accessor for definition.

    RETURNS
    -------
    str
        definition.
    """
    def getDefinition(self) -> str:
        return self.__definition

    """
    Mutator for definition.
    
    PARAMETERS
    ----------
    definition : str
        definition to set.
    """
    def setDefinition(self, definition: str):
        self.__definition = definition

    """
    __str__ converts an FramesetArgument to a string. It returns argument string which is in the form of
    argumentType:definition

    RETURNS
    -------
    str
        string form of frameset argument
    """
    def __str__(self) -> str:
        return self.__argumentType + ":" + self.__definition
