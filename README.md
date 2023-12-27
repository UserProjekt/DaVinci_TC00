# DaVinci_TC00
A simple solution to the Sony FX3/FX30 Camera timecode reading error caused by Adobe Premiere Pro.

For unknown reasons, Adobe Premiere Pro is unable to read the original timecode from FX3 footage. Instead, it defaults to a timecode of 00:00:00:00, both in the Premiere interface and in the exported XML. This creates a serious problem when attempting to rebuild the editing timeline from this XML.

One solution is install [catalyst prepare plugin](https://support.d-imaging.sony.co.jp/app/cpplugin/en/index.php) for Premiere.(However, based on my experience and tests, this solution didn't work.) 

As an alternative, modify the original timecode to 00:00:00:00. let Resolve to match with Premiere, and rebuilding the timeline correctly.

## Prerequisites and Usage
Excerpted from:

Mac OS:
 /Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/README.txt

Windows:
 C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\README.txt

    


### Prerequisites
DaVinci Resolve scripting requires one of the following to be installed (for all users):

    Lua 5.1
    Python 2.7 64-bit
    Python >= 3.6 64-bit


### Using a script
DaVinci Resolve needs to be running for a script to be invoked.

For a Resolve script to be executed from an external folder, the script needs to know of the API location. 
You may need to set the these environment variables to allow for your Python installation to pick up the appropriate dependencies as shown below:

    Mac OS X:
    RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

    Windows:
    RESOLVE_SCRIPT_API="%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
    RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
    PYTHONPATH="%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\"

    Linux:
    RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
    (Note: For standard ISO Linux installations, the path above may need to be modified to refer to /home/resolve instead of /opt/resolve)

## Example
First, import the FX3 Clips into the DaVinci Resolve media pool root folder. 
Then, run this script. It will automatically modify the timecode to 00:00:00:00 for every Clip in the root folder.
![example](https://github.com/UserProjekt/DaVinci_TC00/assets/78477492/907c6219-c220-4ee8-a771-e1f21df2a44f)



