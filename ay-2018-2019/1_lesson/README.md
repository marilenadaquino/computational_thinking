# 1st Lesson
## Table of Contents
 * [Install Python with Anaconda](#install-python-with-anaconda)
 * [Use python in the shell](#use-python-in-the-shell)
 * [Install pip3](#install-pip3)
 * [Install modules with pip3](#install-modules-with-pip3)
 * [Install PyCharm](#install-pycharm)
 * [Links](#links)

First of all, download or clone this repo :)

## Install Python with Anaconda
We'll install Python on our laptop/desktop by using [Anaconda](https://www.anaconda.com/) Distribution. Anaconda comes with many packages for Python and Jupyter Notebook.
The current version of Anaconda is 5.3.1. We install on of the latest versions of Python (3.6)

* Go to [*Download Anaconda*](https://www.anaconda.com/download/) page. 
* Choose the correct installer according to your OS (Windows, macOS or Linux). 


#### Mac
[Instructions](https://docs.anaconda.com/anaconda/install/mac-os)
Mac users should already have Python 2.7 installed, thus we upgrade it to 3.6 with Anaconda.
Once the installer is downloaded, double click to launch and go through the steps. 
 * Agree to the license
 * Select "Install for me only"
 * Click *Install* and then *close*

#### Linux
[Instructions](http://docs.anaconda.com/anaconda/install/linux/)

#### Windows
[Instructions](https://docs.anaconda.com/anaconda/install/windows)
Notice that you might need to disable your anti-virus software during the installation.
Once the installer is downloaded, double click to launch and go through the steps. 
 * Click *Next*
 * Agree to the license
 * Select *Just me*
 * Select a destination folder 
 * Check the box **Register Anaconda as my default Python 3.6**
 * Click Install > Next > Finish.


## Use python in the shell
In computing, a [shell](https://en.wikipedia.org/wiki/Shell_(computing)) is a user interface for accessing services of an operating system. It can be a command-line interface (CLI) or a graphical user interface (GUI). It enables a user to perform several operations, such as file management, run processes, monitor and configure OS. We'll use it as an interpreter for python

#### Mac
 * Go to the folder *Applications/Utility* and open *Terminal* application. 
 * Type `python --version` or `python3 --version` to double-check which version you are using.
 * Type `python` to access python in interactive mode. You'll see in the first line which version of python is installed.*
 * Type `print("Hello world")`.
 * Type `exit()` and press return to exit python.

*If it still shows you `python 2.X`, type `exit()` and press return to exit python and type `python3` to access the latest version of python.


#### Windows
 * Go to *Start/Run*, type *cmd* in the textbox to enter the command prompt.
 * Type `python --version` or `python -V` to double-check which version you are using.
 * Type `python` to access python in interactive mode. You'll see in the first line which version of python is installed.
 * Type `print("Hello world")`.
 * Type `exit()` and press return to exit python.

### Install pip3
`pip` is a package management system used to install and manage software packages written in Python. In other terms, you will use it whenever you want to install a library for Python3. For the latest version of python it has been renamed `pip3`.

#### Mac/Unix
Great you already have `pip` installed! 
* Type `pip --version` to see which version is actually installed. 
* Otherwise type `sudo apt-get install python3-pip` to install the latest version of pip.

#### Windows
Great you already have `pip` installed! 
* Type `pip -V` to see which version is actually installed. 
* Type `pip` to see if it is working. 
* Otherwise follow the [instructions here](https://stackoverflow.com/questions/41501636/how-to-install-pip3-on-windows/41501815) to find where and which version is installed.

### Install modules with pip3
Some packages like `csv` and `collections` are built-in, so you do not need to install them.
[NLTK](http://www.nltk.org/install.html) and other packages, such as [anytree](http://anytree.readthedocs.io/en/latest/index.html), need to be downloaded and installed instead. 

Here is the list of libraries/packages you'll need to install for the labs.
 * [beautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
 * [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
 * [requests](https://pypi.org/project/requests/) 
 * [nltk](https://www.nltk.org/install.html) 
 * [nltk.data](https://www.nltk.org/data.html)

and download the following packages:
 * nltk.download('punkt')
 * nltk.download('gutenberg')
 * nltk.download('genesis')
 * nltk.download('inaugural')
 * nltk.download('popular')

#### Mac/Unix
To install a package, open your shell and type:
 * To install `NLTK` type `pip3 install -U nltk`.

#### Windows 
 * To dowload NLTK use the [installer](https://pypi.python.org/pypi/nltk).
 * To install e.g. `anytree` type `pip3 install anytree` in the bash.

## Install PyCharm
PyCharm is a lightweight IDE (Integrated Development Environment) for Python. It includes an interpreter for python and a way to access the shell.

 * Select `Community` open-source version (NOT professional). 
 * Download the correct version of [PyCharm](https://www.jetbrains.com/pycharm/download) according to your OS. 

#### Mac
 * Double-click the file downloaded. 
 * Drag and drop the icon in `Application` folder. 
 * In the Application folder, double-click the `PyCharm` icon to open the editor.

#### Linux
 * Download the tar.gz folder and unpack it
 * Run pycharm.sh from the bin subdirectory
 
#### Windows
 * Download the tar.gz folder and unpack it
 * Run the pycharm-2018.3.exe file that starts the Installation Wizard
 * Whether during the installation you selected to create a shortcut on your desktop, double-click that shortcut. Otherwise, go to the `\<PyCharm\>\bin folder` (e.g. `C:\Program Files (x86)\JetBrains\PyCharm 2017.1\bin`) and run `pycharm.exe`, `pycharm64.exe`, or `pycharm.bat`.

Once you have opened the editor select `Open` and open `2_lesson_3.py` script that is in the same folder as this readme file. 
Now you need to configure the interpreter so as to run your python code. In the Project Interpreter page, expand the drop-down list of interpreters, and then choose `Show all`. In the list of interpreter types, choose `Configure local interpreter` and choose the one corresponding to your python version.
Then you can run your code. Go to the menu `Run > Run` and select your project/interpreter.

## Links
 * Install [Anaconda](https://www.anaconda.com/download/) 
    * [**Mac** Python Tutorial: Anaconda - Installation using Conda](https://www.youtube.com/watch?v=YJC6ldI3hWk)
    * [**Windows** Install Python (Anaconda) on Windows + Setting Python and Conda Path (2017)](https://www.youtube.com/watch?v=dgjEUcccRwM) follow instructions till 1:55
 * [PyCharm](https://www.jetbrains.com/pycharm/download)
 * [Configure the interpreter in PyCharm](https://www.jetbrains.com/help/pycharm-edu/configuring-python-interpreter-for-a-project.html)