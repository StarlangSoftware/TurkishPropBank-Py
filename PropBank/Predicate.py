from PropBank.RoleSet import RoleSet


class Predicate(object):

    _lemma: str
    _roleSets: list

    """
    A constructor of Predicate class which takes lemma as input and initializes lemma with this input.
    The constructor also initializes the roleSets array.

    PARAMETERS
    ----------
    lemma : str
        Lemma of the predicate
    """
    def __init__(self, lemma: str):
        self._lemma = lemma
        self._roleSets = []

    """
    Accessor for lemma.

    RETURNS
    -------
    str
        lemma.
    """
    def getLemma(self) -> str:
        return self._lemma

    """
    The addRoleSet method takes a RoleSet as input and adds it to the roleSets list.

    PARAMETERS
    ----------
    roleSet : RoleSet 
        RoleSet to be added
    """
    def addRoleSet(self, roleSet: RoleSet):
        self._roleSets.append(roleSet)

    """
    The size method returns the size of the roleSets list.

    RETURNS
    -------
    int
        the size of the roleSets list.
    """
    def size(self) -> int:
        return len(self._roleSets)

    """
    The getRoleSet method returns the roleSet at the given index.

    PARAMETERS
    ----------
    index : int 
        Index of the roleSet
        
    RETURNS
    -------
    RoleSet
        RoleSet at the given index.
    """
    def getRoleSet(self, index: int) -> RoleSet:
        return self._roleSets[index]

    """
    Another getRoleSet method which returns the roleSet with the given roleSet id.

    PARAMETERS
    ----------
    roleId : str 
        Id of the searched roleSet

    RETURNS
    -------
    RoleSet
        RoleSet which has the given id.
    """
    def getRoleSetWithId(self, roleId: str) -> RoleSet:
        for roleSet in self._roleSets:
            if roleSet.getId() == roleId:
                return roleSet
        return None