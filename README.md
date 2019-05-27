# Desktop Database App

A simple desktop app for storing book details in an SQLite database. It has all CRUD features using different buttons in the GUI. The app is built in Python but compiled to .exe for Windows in the dist folder

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installing

After cloning the repo, install the required modules using

```
pip install tkinter sqlite3 pyinstaller
```

In the event you have challenges installing pyinstaller, you could downgrade your pip version to 18.1, install pyinstaller then upgrade it after

```
pip install pip==18.1
pip install pyinstaller
pip install --upgrade pip
```


### Building

In order to compile the front end file (which contains the back end file via import) to a single executable file for Windows, use the following command

```
pyinstaller --onefile --windowed *front end file name*.py
```
The --windowed option ensures that there is no command line which opens in the background behind the main window