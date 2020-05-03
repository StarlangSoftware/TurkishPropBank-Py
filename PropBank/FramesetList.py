from PropBank.Frameset import Frameset
import os


class FramesetList(object):

    __frames: list

    def __init__(self, directory = "Predicates/"):
        """
        A constructor of FramesetList class which reads all frameset files inside the Predicates folder. For each
        file inside that folder, the constructor creates a Frameset and puts in inside the frames list.
        """
        self.__frames = []
        for r, d, f in os.walk(directory):
            for file in f:
                frameset = Frameset(os.path.join(r, file))
                self.__frames.append(frameset)

    def readFromXml(self, synSetId: str) -> dict:
        """
        readFromXmL method searches the Frameset with a given synSetId if there is a Frameset with the given synSet id,
        returns the arguments of that Frameset as a dictionary.

        PARAMETERS
        ----------
        synSetId : str
            Id of the searched Frameset

        RETURNS
        -------
        dict
            a dict containing the arguments of the searched Frameset
        """
        frameset = {}
        for f in self.__frames:
            if f.getId() == synSetId:
                for i in range(len(f.getFramesetArguments())):
                    framesetArgument = f.getFramesetArguments()[i]
                    frameset[framesetArgument.getArgumentType()] = framesetArgument.getDefinition()
        return frameset

    def frameExists(self, synSetId: str) -> bool:
        """
        frameExists method checks if there is a Frameset with the given synSet id.

        PARAMETERS
        ----------
        synSetId : str
            Id of the searched Frameset

        RETURNS
        -------
        bool
            true if the Frameset with the given id exists, false otherwise.
        """
        for f in self.__frames:
            if f.getId == synSetId:
                return True
        return False

    def getFrameSet(self, synSetIdOrIndex) -> Frameset:
        """
        getFrameSet method returns the Frameset with the given synSet id or index

        PARAMETERS
        ----------
        synSetIdOrIndex
            Id of the searched Frameset

        RETURNS
        -------
        Frameset
            Frameset which has the given id.
        """
        if isinstance(synSetIdOrIndex, str):
            for f in self.__frames:
                if f.getId == synSetIdOrIndex:
                   return f
        elif isinstance(synSetIdOrIndex, int):
            return self.__frames[synSetIdOrIndex]
        return None

    def addFrameset(self, frameset: Frameset):
        """
        The addFrameset method takes a Frameset as input and adds it to the frames list.

        PARAMETERS
        ----------
        frameset : Frameset
            Frameset to be added
        """
        self.__frames.append(frameset)

    def size(self) -> int:
        """
        The size method returns the size of the frames list.

        RETURNS
        -------
        int
            the size of the frames list.
        """
        return len(self.__frames)
