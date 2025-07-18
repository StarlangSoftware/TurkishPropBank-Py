class FramesetArgument(object):

    __argument_type: str
    __definition: str
    __function: str
    __grammatical_case: str

    def __init__(self,
                 argumentType: str,
                 definition: str,
                 function: str = None,
                 grammaticalCase: str = None):
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
        grammaticalCase : str
            GrammaticalCase of the frameset argument
        """
        self.__argument_type = argumentType
        self.__definition = definition
        self.__function = function
        self.__grammatical_case = grammaticalCase

    def getArgumentType(self) -> str:
        """
        Accessor for argumentType.

        RETURNS
        -------
        str
            argumentType.
        """
        return self.__argument_type

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

    def getGrammaticalCase(self) -> str:
        """
        Accessor for grammaticalCase.

        RETURNS
        -------
        str
            grammatical_case.
        """
        return self.__grammatical_case

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

    def setGrammaticalCase(self, grammaticalCase: str):
        """
        Mutator for grammatical_case.

        PARAMETERS
        ----------
        grammaticalCase : str
            grammatical case to set.
        """
        self.__grammatical_case = grammaticalCase

    def __str__(self) -> str:
        """
        __str__ converts an FramesetArgument to a string. It returns argument string which is in the form of
        argumentType:definition

        RETURNS
        -------
        str
            string form of frameset argument
        """
        return self.__argument_type + ":" + self.__definition
