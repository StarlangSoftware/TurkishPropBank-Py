import unittest

from PropBank.FramesetList import FramesetList


class FramesetListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.framesetList = FramesetList()

    def test_Frames(self):
        self.assertEqual(17691, self.framesetList.size())

    def test_ArgSize(self):
        count = 0
        for i in range(self.framesetList.size()):
            count += len(self.framesetList.getFrameSet(i).getFramesetArguments())
        self.assertEqual(29759, count)

    def test_ArgName(self):
        nameList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getArgumentType() in nameList:
                    nameList[argument.getArgumentType()] = nameList[argument.getArgumentType()] + 1
                else:
                    nameList[argument.getArgumentType()] = 1
        self.assertEqual(14668, nameList["ARG0"])
        self.assertEqual(13126, nameList["ARG1"])
        self.assertEqual(1886, nameList["ARG2"])
        self.assertEqual(78, nameList["ARG3"])
        self.assertEqual(1, nameList["ARG4"])

    def test_ArgFunction(self):
        functionList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getFunction() in functionList:
                    functionList[argument.getFunction()] = functionList[argument.getFunction()] + 1
                else:
                    functionList[argument.getFunction()] = 1
        self.assertEqual(481, functionList["com"])
        self.assertEqual(14, functionList["ext"])
        self.assertEqual(814, functionList["loc"])
        self.assertEqual(198, functionList["rec"])
        self.assertEqual(14, functionList["pat"])
        self.assertEqual(10687, functionList["ppt"])
        self.assertEqual(605, functionList["src"])
        self.assertEqual(801, functionList["gol"])
        self.assertEqual(156, functionList["tmp"])
        self.assertEqual(14557, functionList["pag"])
        self.assertEqual(1432, functionList["dir"])

if __name__ == '__main__':
    unittest.main()
