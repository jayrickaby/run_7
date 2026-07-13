# Config

## General
- On Windows: `\HKEY_CURRENT_USER\Software\JayRickaby\Run-7`<sub>(I am aware this sucks as you need to use RegEdit.)</sup>
- On Linux: `~/.config/JayRickaby/Run-7.conf`

## KDE Plasma
You can make the Window more accurate by applying a Window Rule, such as:
![kde_winrules](assets/screenshots/kde_winrules.png)

I calculate the y-position based off my screen height, window height and taskbar height.
e.g. `1200` - `~216` - `~48` respectively = `936`. However, this is buggy and currently affects all windows!

It is highly recommended you use this alongside [AeroThemePlasma](https://gitgud.io/aeroshell/atp/aerothemeplasma).


## Settings
### [Appearance]
#### icon
*Acceptable Values: `Any valid local file`*

This will prefer to use your icon of choice.

![icon](assets/screenshots/icon.png)

#### osOverride
*Acceptable Values: `Any valid string`*

This will prefer to use a name of your choice for all instances of the OS.

![osOverride](assets/screenshots/osOverride.png)

*Note: This will override `prettyOsName`!*

#### prettyOsName
*Acceptable Values: `true`, `false`*

This will prefer to use the more elaborate version of your system. 
e.g. 
- Linux → EndeavorOS (whatever distribution you are using)
- Windows → Windows 11

![prettyOsNames](assets/screenshots/prettyOsNames.png)

*Note: This will be overridden by `osOverride`!*

#### title
*Acceptable Values: `Any valid string`*

This will prefer to use a name of your choice for all instances of the application title.

![title](assets/screenshots/title.png)

### [History]
#### limitHistorySize
*Acceptable Values: `Any valid unsigned integer`, `-1`*

- This will cause the URL History to become a queue (follows FILO). It will have a size of whatever has been designated.
- A size of `-1` means that there is no limit to the history.
- History will be shrunk on application open/close.
