# HoI4 shine generator

HoI4 shine generator is a Python script to automate the creation of shines in Hearts of Iron IV modding.

## Important
```lua
focus = {
	id = TAG_focus_id
	icon = GFX_TAG_focus_id
	cost = 10
	x = 4
	y = 20
	relative_position_id = TAG_previous_focus
}
```
**The tool utilizes the second line of the focus file to generate the shines! Without `icon = GFX_TAG_example` it will NOT work.**

## Installation and Usage

**1.** Download you prefered version of the tool. The `shine_adder_gui.py` provides a graphical interface, while the `cli.py` can be used in the command line.

**2.** Make sure to have Python installed on your machine. Download it [here](https://www.python.org/downloads/).

### For the CLI file:
- Open CMD by pressing <kbd>Windows</kbd> + <kbd>R</kbd>
- Navigate to the download location of the `cli.py` file
- Run `python cli.py --help` for more information on how to use the tool.

### For the GUI file:
- Open CMD by pressing <kbd>Windows</kbd> + <kbd>R</kbd>
- Run this command
```
pip install PySimpleGUI
```
- Now just run `shine_adder_gui.py` via double-clicking


## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
