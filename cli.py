import re
import argparse


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
    parser = argparse.ArgumentParser(description='Create shines from a focus file')
    parser.add_argument('filepath', metavar='f', type=str, nargs='+',
                        help='the filepath to the focus file (e.g. \mod\common\\national_focus)')
    parser.add_argument('--file_name_catch', action='store_true', help='adds \"GFX_\"d in front of the filenames')

    args = parser.parse_args()
    generate_shine_entries(extract_data(args.filepath[0]), args.file_name_catch)


# Run this
if __name__ == '__main__':
    main()
