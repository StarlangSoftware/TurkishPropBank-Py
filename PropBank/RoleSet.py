from PropBank.Role import Role


class RoleSet(object):

    __id: str
    __name: str
    __roles: list

    def __init__(self, _id: str, name: str):
        """
        A constructor of RoleSet class which takes id and name as inputs and initializes corresponding attributes
        with these inputs.

        PARAMETERS
        ----------
        _id : str
            Id of the roleSet
        name : str
            Name of the roleSet
        """
        self.__id = _id
        self.__name = name
        self.__roles = []

    def getId(self) -> str:
        """
        Accessor for id.

        RETURNS
        -------
        str
            id.
        """
        return self.__id

    def getName(self) -> str:
        """
        Accessor for name.

        RETURNS
        -------
        str
            name.
        """
        return self.__name

    def size(self) -> int:
        """
        The size method returns the size of the roles list.

        RETURNS
        -------
        int
            the size of the roles list.
        """
        return len(self.__roles)

    def addRole(self, role: Role):
        """
        The addRole method takes a Role as input and adds it to the roles list.

        PARAMETERS
        ----------
        role : Role
            Role to be added
        """
        self.__roles.append(role)

    def getRole(self, index: int) -> Role:
        """
        The getRole method returns the role at the given index.

        PARAMETERS
        ----------
        index : int
            Index of the role

        RETURNS
        -------
        Role
            Role at the given index.
        """
        return self.__roles[index]

    def getRoleWithArgument(self, n: str) -> Role:
        """
        Finds and returns the role with the given argument number n. For example, if n == 0, the method returns
        the argument ARG0.

        PARAMETERS
        ----------
        n : str
            Argument number

        RETURNS
        -------
        Role
            The role with the given argument number n.
        """
        for role in self.__roles:
            if role.getN() == n:
                return role
