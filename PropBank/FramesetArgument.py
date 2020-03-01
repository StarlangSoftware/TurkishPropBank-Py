class FramesetArgument(object):

    __argumentType: str
    __definition: str
    __function: str

    def __init__(self, argumentType: str, definition: str, function: str = None):
        """
        A constructor of FramesetArgument class which takes argumentType and definition as input and initializes
        corresponding attributes

        PARAMETERS
        ----------
        argumentType : str
            ArgumentType of the frameset argument
        definition : str
            Definition of the frameset argument
        function : str
            Function of the frameset argument
        """
        self.__argumentType = argumentType
        self.__definition = definition
        self.__function = function

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

    def getFunction(self) -> str:
        """
        Accessor for function.

        RETURNS
        -------
        str
            function.
        """
        return self.__function

    def setDefinition(self, definition: str):
        """
        Mutator for definition.

        PARAMETERS
        ----------
        definition : str
            definition to set.
        """
        self.__definition = definition

    def setFunction(self, function: str):
        """
        Mutator for definition.

        PARAMETERS
        ----------
        function : str
            function to set.
        """
        self.__function = function

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
