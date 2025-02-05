from PropBank.Argument import Argument


class ArgumentList:

    arguments: [Argument]

    def __init__(self, argumentList: str):
        """
        Constructor of argument list from a string. The arguments for a word is a concatenated list of arguments
        separated via '#' character.
        :param argumentList: String consisting of arguments separated with '#' character.
        """
        self.arguments = []
        items = argumentList.split('#')
        for item in items:
            self.arguments.append(Argument(item))

    def __str__(self) -> str:
        """
        Overloaded toString method to convert an argument list to a string. Concatenates the string forms of all
        arguments with '#' character.
        :return: String form of the argument list.
        """
        if len(self.arguments) == 0:
            return "NONE"
        else:
            result = self.arguments[0].__str__()
            for i in range(1, len(self.arguments)):
                result += "#" + self.arguments[i].__str__()
            return result

    def updateConnectedId(self, previousId: str, currentId: str):
        """
        Replaces id's of predicates, which have previousId as synset id, with currentId.
        :param previousId: Previous id of the synset.
        :param currentId: Replacement id.
        """
        for argument in self.arguments:
            if argument.getId() == previousId:
                argument.setId(currentId)

    def addPredicate(self, predicateId: str):
        """
        Adds a predicate argument to the argument list of this word.
        :param predicateId: Synset id of this predicate.
        """
        if len(self.arguments) != 0 and self.arguments[0].getArgumentType() == "NONE":
            self.arguments.pop(0)
        self.arguments.append(Argument("PREDICATE", predicateId))

    def removePredicate(self):
        """
        Removes the predicate with the given predicate id.
        """
        for argument in self.arguments:
            if argument.getArgumentType() == "PREDICATE":
                self.arguments.remove(argument)
                break

    def containsPredicate(self) -> bool:
        """
        Checks if one of the arguments is a predicate.
        :return: True, if one of the arguments is predicate; false otherwise.
        """
        for argument in self.arguments:
            if argument.getArgumentType() == "PREDICATE":
                return True
        return False

    def containsPredicateWithId(self, predicateId: str) -> bool:
        """
        Checks if one of the arguments is a predicate with the given id.
        :param predicateId: Synset id to check.
        :return: True, if one of the arguments is predicate; false otherwise.
        """
        for argument in self.arguments:
            if argument.getArgumentType() == "PREDICATE" and argument.getId() == predicateId:
                return True
        return False

    def getArguments(self) -> [str]:
        """
        Returns the arguments as an array list of strings.
        :return: Arguments as an array list of strings.
        """
        result = []
        for argument in self.arguments:
            result.append(argument.__str__())
        return result

    def containsArgument(self, argumentType: str, _id: str) -> bool:
        """
        Checks if the given argument with the given type and id exists or not.
        :param argumentType: Type of the argument to search for.
        :param _id: Id of the argument to search for.
        :return: True if the argument exists, false otherwise.
        """
        for argument in self.arguments:
            if argument.getArgumentType() == argumentType and argument.getId() == _id:
                return True
        return False
