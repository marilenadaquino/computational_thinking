# 1st Lesson
## Table of Contents
 * [What to download before to start](#What-to-download-before-to-start)
 * [Install Python](#install-python)
 * [Install Python libraries](#install-python-libraries)
 * [Install PyCharm](#install-PyCharm)


Remember to download or clone this repo!

## What to download before to start
#### Python 
1. Go to [*Python Downloads*](https://www.python.org/downloads/). It will show *Download the latest version of Python* according to the OS you are using to access the browser.
2. Click on the download button to get the latest version of **Python (3.8)**.

##### Windows
You will be redirected to another web page. From the spreadsheet press *Windows x86-64 executable installer file* to start the download.

##### Mac
The download should start without any redirection.

#### PyCharm
1. Go to [*PyCharm home page*](https://www.jetbrains.com/pycharm/?fromMenu)
2. Press the *Download* button in the up-right corner, which redirects you to the download page, according to the OS you are using to access the browser.
3. Under the label *Community*, press *Download*.

## Install Python

### 1. Open the terminal / command prompt
We'll install the latest version of Python (3.7.5) for your OS by using a shell (also called terminal (Mac) / command prompt (Windows).

> > In computing, a [shell](https://en.wikipedia.org/wiki/Shell_(computing)) is a user interface for accessing services of an operating system. It can be a command-line interface (CLI) or a graphical user interface (GUI). It enables a user to perform several operations, such as file management, installations, run processes, monitor and configure OS. We'll use it to install packages and as an interpreter for python.

#### Windows
1.  Open the Windows menu 
2.  Type *command* in the search bar
3.  Select Command Prompt from the search results
  
#### Mac
1. Open the Spotlight search box in the upper right-hand corner.
2. Type *terminal* in the search bar
3. Click on Terminal or just hit return if it's the first result.

Alternatively, go to the folder *Applications/Utility* and open *Terminal* application. 

### 2. Check if you have Python already installed in your laptop.
[Instructions](https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html)

1. Type `python --version` (also `python -V` on Windows) in the command line and press return to see whether you have a default version of Python (2.7) already installed. If you don't have python installed, you should get an error message. Mac comes usually with Python 2.7 installed, hence the shell will show the current installed version. For instance:

~~~~
python --version
Python 2.7.3
~~~~

2. Type `python3 --version` (also `python3 -V` on Windows) in the command line and press return to check whether you have Python 3 installed, and eventually which version.

### 3. Install python package

#### Windows
1. Open the downloaded file (.exe) to start the installation wizard.
2. Select the first option to install Python on your path (you will need admin rights on your computer to do that, meaning it will ask you your password).
3. Close the wizard.
4. Either select the .exe file in your *Downloads* folder or, in the windows menu search for python.exe and click on it to reopen the wizard.
5. Select Modify, press next without modifying anything. 
6. In the window *Advanced options* click on the checkbox called *Add Python to environment variables* and press Install.
7. Close and reopen the wizard. 
8. Select Repair to apply the changes.
9. Finally, go to the command line and try to type `python --version` (also `python3 -V`) and press return to check whether you correctly installed Python.

#### Mac
1. Double-click on the downloaded .pkg file to start the wizard.
2. Follow the instructions.
2. Finally, go to the command line and try to type `python --version` (also `python3 --version` in case you have installed also Python 2) and press return to check whether you correctly installed Python.

### 4. Play with Python in the shell
Both Windows and Mac users can use the shell as a Python interpreter.

> > The interpreter is the program you’ll need to run Python code and scripts. Technically, the interpreter is a layer of software that works between your program and your computer hardware to get your code running.

 * Type `python` (or `python3`) in the shell. You'll see in the first line which version of python is installed. If it still shows you `python 2.X`, type `exit()` and press return to exit python, and type `python3` to access the latest version of python installed on your computer.
 * In the second line you will see `>>>`. This means you accessed python in *interactive mode* and you can now type your commands to be executed by the shell.
 * Type `print("Hello world")` and press enter.
 
~~~~
>>> print("Hello world")
Hello World
~~~~ 

 * Type `exit()` and press return to exit python interactive mode.

## Install Python libraries

> > A text file containing Python code that is intended to be directly executed by the user is called **script**. A text file that contains Python code that is designed to be imported and used from another Python file, is called **module/library**. 

Some libraries/modules (e.g. `csv` and `collections`) are built-ins, meaning you do not need to install them, while others, developed by the larger community, must be downloaded and installed.

We can install python libraries by using `pip` in the shell.

> > `pip` is a package management system used to install and manage software packages written in Python. You will use it whenever you want to install a Python library. If you also have Python 2 on your laptop, pip it has been renamed `pip3`.

#### Mac/Unix

Great you already have `pip` installed! 

* Type `pip --version` in the terminal to see which version is installed. 
* If not installed, type `sudo apt-get install python3-pip` to install the latest version of pip.

#### Windows

Great you already have `pip` installed! 

* Type `pip --version` in the command line to see which version is actually installed. 
* If not installed, follow the [instructions here](https://stackoverflow.com/questions/41501636/how-to-install-pip3-on-windows/41501815) to find where and which version is installed.

### Install modules with pip3
We will see how to install [NLTK](http://www.nltk.org/install.html) and [anytree](http://anytree.readthedocs.io/en/latest/index.html). 

#### Mac/Unix

 * To install `NLTK` type `pip3 install -U nltk` in the shell.
 * To install `anytree` type `pip3 install -U anytree` in the shell.

#### Windows 
 * To dowload NLTK use the [installer](https://pypi.python.org/pypi/nltk).
 * To install e.g. `anytree` type `pip3 install anytree` in the shell.

Whenever you want to install a library, look for the documentation page and the official name of the package to be used in the shell. Here is the list of libraries/packages you'll need to install for the hands-on classes.
 * [beautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
 * [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
 * [requests](https://pypi.org/project/requests/) 
 * [nltk](https://www.nltk.org/install.html) 
 * [nltk.data](https://www.nltk.org/data.html)

## Install PyCharm
> > PyCharm is a lightweight IDE (Integrated Development Environment) for Python. It includes a rich text editor, an interpreter for python, a way to access the shell, and allows you to save your scripts (as .py files).

### 1. Install and setup the editor

Follow the instructions according to your OS.

#### Windows
 1. Download the tar.gz folder and unpack it.
 2. Run the `pycharm-xxxxxx.exe` file that starts the Installation Wizard.
 3. In the window *Choose Installation location* press *Next*.
 4. In the window *Installation Options* select the checkboxes **Create Desktop Shourtcut** and **Update PATH variable (restart needed)** and press Next.
 5. In the next window press *Install*.
 6. Select *Rebooth now* and press *Finish*. Your laptop will restart.
 7. If during the installation you selected to create a shortcut on your desktop, double-click that shortcut. Otherwise, go to the `\<PyCharm\>\bin folder` (e.g. `C:\Program Files (x86)\JetBrains\PyCharm 2017.1\bin`) and run `pycharm.exe`, `pycharm64.exe`, or `pycharm.bat`. 
 8. If it prompts to import settings select *do not import settings*.
 9. Agree and sign the license, press *Continue*.
 10. Install the plugins you may want to have (e.g. Markdown support) 

#### Mac
 1. Double-click the downloaded .dmg file. 
 2. Drag and drop the icon in `Application` folder. 
 3. In the Application folder, double-click the `PyCharm` icon to open the editor.
 4. If it prompts to import settings select *do not import settings*. 
 5. Agree and sign the license, press *Continue*. 
 6. Install the plugins you may want to have (e.g. Markdown support) 

### 2. Create a project and configure your Python interpreter

For both Windows and Mac users.

 1. Select *Create a new project*
 2. Change the location and the name of the project folder as you wish
 3. Click on the Dropdown menu *Project interpreter: existing interpreter*
 4. Select the checkbox *Existing interpreter* and 
 5. Double-click on the `...` icon on the right to open a new window
 6. On the left column select *System interpreter*. In the up right bar you will see the path to your interpreter (i.e. the `..\python.exe` file for windows users)
 7. Press OK, and when you are back in the prior window finally press *Create*

[Instructions to configure the interpreter in PyCharm](https://www.jetbrains.com/help/pycharm-edu/configuring-python-interpreter-for-a-project.html)

### 3. Create your first python script

For both Windows and Mac users.

 1. From the menu select File > New > Python file. 
 2. Input `hello_world` as a name of your file. It will create hello_world.py in your project folder (see the left column)
 3. In the editor type your command `print("hello world")` and press Cmd+S (on Mac) or CTRL+s (on Windows) to save changes to the file.
 4. From the menu select Run > Run. In the interactive window select the name of your file `hello_world`. In the bottom part of the editor will appear the result.
