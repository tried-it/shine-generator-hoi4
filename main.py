import re


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


def generate_shine_entries(icon_list):
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
            modifiable_thingy = shine_template
            modifiable_thingy = modifiable_thingy.replace('<sprite name>', icon)
            modifiable_thingy = modifiable_thingy.replace('<filename>', icon + '.dds')
            shine.write(modifiable_thingy)


# Run this
if __name__ == '__main__':
    generate_shine_entries(extract_data('files/ITA_focus.txt'))
