import unittest

from PropBank.FramesetList import FramesetList


class FramesetListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.framesetList = FramesetList("../Predicates/")

    def test_Frames(self):
        self.assertEquals(17691, self.framesetList.size())

    def test_ArgSize(self):
        count = 0
        for i in range(self.framesetList.size()):
            count += len(self.framesetList.getFrameSet(i).getFramesetArguments())
        self.assertEquals(29759, count)

    def test_ArgName(self):
        nameList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getArgumentType() in nameList:
                    nameList[argument.getArgumentType()] = nameList[argument.getArgumentType()] + 1
                else:
                    nameList[argument.getArgumentType()] = 1
        self.assertEquals(14668, nameList["ARG0"])
        self.assertEquals(13126, nameList["ARG1"])
        self.assertEquals(1886, nameList["ARG2"])
        self.assertEquals(78, nameList["ARG3"])
        self.assertEquals(1, nameList["ARG4"])

    def test_ArgFunction(self):
        functionList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getFunction() in functionList:
                    functionList[argument.getFunction()] = functionList[argument.getFunction()] + 1
                else:
                    functionList[argument.getFunction()] = 1
        self.assertEquals(481, functionList["com"])
        self.assertEquals(14, functionList["ext"])
        self.assertEquals(814, functionList["loc"])
        self.assertEquals(198, functionList["rec"])
        self.assertEquals(14, functionList["pat"])
        self.assertEquals(10687, functionList["ppt"])
        self.assertEquals(605, functionList["src"])
        self.assertEquals(801, functionList["gol"])
        self.assertEquals(156, functionList["tmp"])
        self.assertEquals(14557, functionList["pag"])
        self.assertEquals(1432, functionList["dir"])

if __name__ == '__main__':
    unittest.main()
