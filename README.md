# IDMan Window Closer

IDMan Window Closer is a Python application designed to automatically close windows of Internet Download Manager (IDMan) that meet specific criteria, such as size and visibility. The application runs in the background as a tray icon, allowing you to pause or resume the window-closing process easily.

## Features

- Automatically detects and closes windows of IDMan (idman.exe) that exceed specific size thresholds.
- Runs in the system tray, offering a simple `Pause` and `Exit` menu for user control.
- Custom tray icon that changes color depending on whether the process is running or paused.
- Lightweight and configurable via PyInstaller for packaging into an executable.

## Requirements

To run the application, you need to have the following Python packages installed:

- `pystray`
- `PIL` (Pillow)
- `psutil`
- `pywin32`

You can install the required packages by running:

```bash
pip install pystray pillow psutil pywin32
```

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/dangkhoa1612/idman-window-closer.git
cd idman-window-closer
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python idm.py
```

## Packaging as an Executable

You can package this Python application into a standalone executable using `PyInstaller`. Below is an example command to generate an `.exe` file:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole idm.py
```
If you want to use a custom icon for the tray, you can include it with:

```bash
pyinstaller --onefile --icon=youricon.ico idm.py
```
## Run program on Startup

1. Open the Startup folder:

Press the Windows key + R to open the Run dialog.
Type shell:startup and press Enter.

```bash
shell:startup
```

2. Create a shortcut for your program:

Locate the executable file (.exe) of the program you want to run at startup.
Right-click on the file and select "Create shortcut".


3. Add the shortcut to the Startup folder:

Drag and drop (or copy and paste) the newly created shortcut into the Startup folder you opened in step 1.


4. Verify:

Restart your computer to check if the program launches automatically.

Note: To stop a program from running at startup, simply delete its shortcut from the Startup folder.
