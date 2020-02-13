class FramesetArgument(object):

    __argumentType: str
    __definition: str

    def __init__(self, argumentType: str, definition: str):
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
        self.__argumentType = argumentType
        self.__definition = definition

    def getArgumentType(self) -> str:
        """
        Accessor for argumentType.

        RETURNS
        -------
        str
            argumentType.
        """
        return self.__argumentType

    def getDefinition(self) -> str:
        """
        Accessor for definition.

        RETURNS
        -------
        str
            definition.
        """
        return self.__definition

    def setDefinition(self, definition: str):
        """
        Mutator for definition.

        PARAMETERS
        ----------
        definition : str
            definition to set.
        """
        self.__definition = definition

    def __str__(self) -> str:
        """
        __str__ converts an FramesetArgument to a string. It returns argument string which is in the form of
        argumentType:definition

        RETURNS
        -------
        str
            string form of frameset argument
        """
        return self.__argumentType + ":" + self.__definition
