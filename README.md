For Developers
============

You can also see [Java](https://github.com/starlangsoftware/TurkishPropBank), [C++](https://github.com/starlangsoftware/TurkishPropBank-CPP), [Swift](https://github.com/starlangsoftware/TurkishPropBank-Swift), or [C#](https://github.com/starlangsoftware/TurkishPropBank-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called PropBank will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishPropBank-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `TurkishPropBank-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [FramesetList](#framesetlist)
+ [Frameset](#frameset)

## FramesetList

Frame listesini okumak ve tüm Frameleri hafızada tutmak için

	a = FramesetList()

Framesetleri tek tek gezmek için

	for i in range(a.size()):
		frameset = a.getFrameset(i)

Bir fiile ait olan Frameseti bulmak için

	frameset = a.getFrameSet("TUR10-1234560")

## Frameset

Bir framesetin tüm argümanlarını bulmak için

	getFramesetArguments(self) -> list
