from PropBank import Frameset
import os


class FramesetList(object):

    def __init__(self):
        self.frames = []
        for r, d, f in os.walk("Predicates/"):
            for file in f:
                frameset = Frameset.Frameset("")
                frameset.initWithFile(os.path.join(r, file))
                self.frames.append(frameset)

    def readFromXml(self, synSetId: str):
        frameset = {}
        for f in self.frames:
            if f.getId() == synSetId:
                for i in range(len(f.getFramesetArguments())):
                    framesetArgument = f.getFramesetArguments()[i]
                    frameset[framesetArgument.getArgumentType()] = framesetArgument.getDefinition()
        return frameset

    def frameExists(self, synSetId: str) -> bool:
        for f in self.frames:
            if f.getId == synSetId:
                return True
        return False

    def getFrameSet(self, synSetId: str) -> Frameset:
        for f in self.frames:
            if f.getId == synSetId:
                return f
        return None

    def addFrameset(self, frameset: Frameset):
        self.frames.append(frameset)

    def getFrameset(self, index: int) -> Frameset:
        return self.frames[index]

    def size(self) -> int:
        return len(self.frames)