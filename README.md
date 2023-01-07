# OMEGAPy-Project

## COMING SOON (this README.md is not updated)

<h2 style="box-shadow:-2px 1.5px 3px rgb(68,68,68);padding:4px">This project was created to make Python easy to use</h2>


<h4 style="padding-left:10px;padding:1px;text-shadow:1px 1px rgb(36,100,100);"> You can create your projects in OMEGAPy and use its </h4>
<h4 style="padding-left:10px;padding:1px;text-shadow:1px 1px rgb(36,100,100);"> ready-made libraries as much as possible, as well as </h4>
<h4 style="padding-left:10px;padding:1px;text-shadow:1px 1px rgb(36,100,100);"> install the libraries you need in the virtual environment</h4>
<h4 style="padding-left:10px;padding:1px;text-shadow:1px 1px rgb(36,100,100);"> and get the final of your project. </h4>

<br>
<br>

## Install (not completed)
<pre>
git clone https://github.com/M1778M/OMEGAPy.git
bash OMEGAPy/install.sh
</pre>

<br>
<br>

## Use
### Create New Project
<pre>
omegapy create project NameOfProject_Folder
</pre>
```
OMEGAPy-Project (not updated)
+-- core
|   +-- cfg.ini
|   +-- config.ini
|   +-- controler.py
|   +-- .PROJECTPATHS
+-- omg
|   +-- UI
|   |   +-- cquery.py
|   |   +-- objects.c
|   |   +-- ....
|   +-- etu.py
|   +-- omglib.py
|   +-- p2d.py
|   +-- error_handling.py
|   +-- request.py
|   +-- zbot.py
|   +-- ....
+-- prj
|   +-- project_manager.py
|   +-- package_manager.py
|   +-- ....
+-- venv
|   +-- ....
+-- Project.py
+-- main.py
+-- requirements.txt
```

## How To Use The OMG Library
### In The main.py You can import it or from it import library (For Example)
### main.py
```
# Basic Imports In The Main App
from Project import init
from prj import project_manager,package_manager
#------------------------------------------------
# Import From omg
import omg
from omg import etu,p2d

etu.c_for(int(0),etu.Condition("i<10"),'+',etu.c_for.std_print) # basic simulation of for
```

<br>
<br>

## How To Install Packages We Need (not updated)

```
venv/Scripts/pip install <your_pkg_you_need>
# or
source venv/Scripts/activate # Linux / MacOS
venv/Scripts/activate.bat # Windows
```
<h3 style="padding-left:20px;color:black">-><a href="https://docs.python.org/3/library/venv.html">More About VirtualEnvironment</a><-</h3>

<br>
<br>

## Why OMEGAPy
<h4 style="padding-left:20px;background-color:gray;color:black;border:1px solid black;border-radius:2px;">
Sometimes developers need an environment or software development package for their project.
</h4>
<h4 style="padding-left:20px;background-color:gray;color:black;border:1px solid black;border-radius:2px;">
In addition to the Python development environment and packages, OMEGAPy introduces another environment and considers it part of OMEGAPy
And provides you with packages that you may need in your project by default
You can even use your own OMEGAPy packages, all of which are included in the 'omg' software package.
</h4>
