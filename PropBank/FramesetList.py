from PropBank.Frameset import Frameset
import os


class FramesetList(object):

    """
    A constructor of FramesetList class which reads all frameset files inside the Predicates folder. For each
    file inside that folder, the constructor creates a Frameset and puts in inside the frames list.
    """
    def __init__(self):
        self.frames = []
        for r, d, f in os.walk("Predicates/"):
            for file in f:
                frameset = Frameset("")
                frameset.initWithFile(os.path.join(r, file))
                self.frames.append(frameset)

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
    def readFromXml(self, synSetId: str) -> dict:
        frameset = {}
        for f in self.frames:
            if f.getId() == synSetId:
                for i in range(len(f.getFramesetArguments())):
                    framesetArgument = f.getFramesetArguments()[i]
                    frameset[framesetArgument.getArgumentType()] = framesetArgument.getDefinition()
        return frameset

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
    def frameExists(self, synSetId: str) -> bool:
        for f in self.frames:
            if f.getId == synSetId:
                return True
        return False

    """
    getFrameSet method returns the Frameset with the given synSet id.

    PARAMETERS
    ----------
    synSetId : str 
        Id of the searched Frameset
        
    RETURNS
    -------
    Frameset
        Frameset which has the given id.
    """
    def getFrameSet(self, synSetId: str) -> Frameset:
        for f in self.frames:
            if f.getId == synSetId:
                return f
        return None

    """
    The addFrameset method takes a Frameset as input and adds it to the frames list.

    PARAMETERS
    ----------
    frameset : Frameset 
        Frameset to be added
    """
    def addFrameset(self, frameset: Frameset):
        self.frames.append(frameset)

    """
    The getFrameSet method returns the frameset at the given index.

    PARAMETERS
    ----------
    index : int 
        Index of the frameset

    RETURNS
    -------
    Frameset
        Frameset at the given index.
    """
    def getFrameset(self, index: int) -> Frameset:
        return self.frames[index]

    """
    The size method returns the size of the frames list.

    RETURNS
    -------
    int
        the size of the frames list.
    """
    def size(self) -> int:
        return len(self.frames)