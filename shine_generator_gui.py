##########################################################################
# Copyright 2021 Crispi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###########################################################################
import re
import PySimpleGUI as sg

# A function to get all relevant data out of the focus file
def extract_data(filepath):
    # Create list to store relevant lines in and dictionary to replace unnecessary stuff
    icon_list = []
    to_replace = {'\n': '', ' ': '', 'icon=': ''}

    # Read in focus file
    with open(filepath, 'r') as focus:
        for line in focus:
            # if the line matches the pattern of a relevant icon line do
            if re.search('^\s*icon =.+$', line):
                # replace useless stuff (to_replace)
                for key, value in to_replace.items():
                    line = line.replace(key, value)

                icon_list.append(line)

    return icon_list


def generate_shine_entries(icon_list, switch):
    # Template for a correct shine entry (taken from: https://hoi4.paradoxwikis.com/National_Focus_modding#Focus_icons)
    shine_template = """
    SpriteType = {
        name = "<sprite name>"
        texturefile = "gfx/interface/goals/<filename>"
    }

    SpriteType = {
        name = "<sprite name>_shine"
        texturefile = "gfx/interface/goals/<filename>"
        effectFile = "gfx/FX/buttonstate.lua"
        animation = {
            animationmaskfile = "gfx/interface/goals/<filename>"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = -90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = { x = 0.0 y = 0.0 }
            animationtexturescale = { x = 1.0 y = 1.0 } 
        }

        animation = {
            animationmaskfile = "gfx/interface/goals/<filename>"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = 90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = { x = 0.0 y = 0.0 }
            animationtexturescale = { x = 1.0 y = 1.0 } 
        }
            legacy_lazy_load = no
    }
    
    """

    # Open a new file (output file) and write the replaced shine_template into it
    with open('generated_shine.txt', 'w') as shine:
        for icon in icon_list:
            if switch:
                expected_filename = icon
            else:
                expected_filename = icon.replace('GFX_', '')
            shine_object = shine_template
            shine_object = shine_object.replace('<sprite name>', icon)
            shine_object = shine_object.replace('<filename>', expected_filename + '.dds')
            shine.write(shine_object)


def main():
    # Set theme
    sg.theme('Dark')

    # PySimpleGUI Layout
    layout = [[sg.Text('You must have the line \"icon = GFX_TAG_your_focus_name\" in each focus definition!')],
              [sg.Text('Select the file that contains your focus tree:')],
              [sg.Input(), sg.FileBrowse(key="-IN-"), sg.Checkbox('GFX_filename', key='-SWITCH-')],
              [sg.Button('Add Shines'), sg.Button('Close')]]

    # Building Window
    window = sg.Window('Generate shine entries', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        elif event == "Add Shines":
            try:
                generate_shine_entries(extract_data(values['-IN-']), values['-SWITCH-'])
                num = len(extract_data(values['-IN-']))
                if num == 0:
                    sg.popup_error('Couldn\'t generate any entries!\nMake sure you have your focus tree file with '
                                   'icon definitions selected!', title='Error', text_color='Red')
                else:
                    sg.popup_auto_close('Added ' + str(num) + ' shine entries to the output file')

            except FileNotFoundError:
                sg.popup_error('No file found')


# Run this
if __name__ == '__main__':
    main()
