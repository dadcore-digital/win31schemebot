from PIL import Image
import sys

img = Image.open('crazypants.gif')
img = img.convert("RGBA")

color_lookup = {'Desktop': (255, 0, 255, 255),
                'Inactive Border': (170, 0, 85, 255),
                'Inactive Title Bar': (255, 0, 0, 255),
                'Inactive Title Bar Text': (134, 138, 142, 255),
                'Active Border': (255, 255, 0, 255),
                'Active Title Bar': (170, 170, 85, 255),
                'Active Title Bar Text': (170, 85, 170, 255),
                'Menu Bar': (14, 54, 255, 255),
                'Menu Text': (0, 170, 85, 255),
                'Disabled Text': (190, 189, 189, 255),
                'Highlighted Text': (255, 255, 255, 255),
                'Highlight': (0, 170, 85, 255), 
                'Application Workspace': (0, 255, 0, 255),
                'Window Background': (146, 12, 208, 255),
                'Window Text': (0, 0, 0, 255),
                'Button Highlight': (159, 195, 177, 255),
                'Button Face': (134, 138, 142, 255),
                'Button Shadow': (248, 194, 194, 255),
                'Button Text': (0, 0, 0, 255),
                'Scrollbars': (0, 255, 255, 255)
}

pixdata = img.load()

# Clean the background noise, if color != white, then set to black.
# change with your color
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        for k, v in color_lookup.items():
            if pixdata[x, y] == v:
                pixdata[x, y] = (0, 0, 0, 255)
                break

img.show()            