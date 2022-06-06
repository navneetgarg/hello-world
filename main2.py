import math
import sys
import os


import requests

r = requests.get("https://coreyms.com")
# go to definition: F12
print(r.status_code)
# format the code : shft alt F


# linitng: to avoid mistakes
print(sys.version)


def fun(one):
    t = 2
    return one


print(fun(2))


print(fun(2))

    """{
    "python.condaPath": "C:\\ProgramData\\Anaconda3\\Scripts\\conda-script.py",
    "python.terminal.activateEnvironment": true,
    "kite.showWelcomeNotificationOnStartup": false,
    "files.autoSave": "afterDelay",
    "workbench.startupEditor": "newUntitledFile",
    "workbench.colorTheme": "Predawn",
    "workbench.iconTheme": "ayu",
    "workbench.settings.editor": "json",
    "workbench.settings.openDefaultSettings": true,
    "workbench.editor.splitInGroupLayout": "vertical",
    //"python.defaultInterpreterPath": "C:\\ProgramData\\Anaconda3\\python.exe",
    "python.pythonPath": "C:\\ProgramData\\Anaconda3\\python.exe", //
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.suggestFontSize": 14,
    "editor.fontWeight": "500",
    "editor.fontFamily": "Consolas, 'Courier New', monospace", //"Source Code Pro"
    "debug.console.fontFamily": "default",
    "debug.console.fontSize": 14,
    "terminal.integrated.fontSize": 14,
    "terminal.integrated.fontWeight": "400",
    //"code-runner.executorMap": {
    //"python": "$pythonPath -u $FileName",    },
    "code-runner.clearPreviousOutput": true,
    "code-runner.showExecutionMessage": true, //he choose false
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "terminal.integrated.shell"
}
    """