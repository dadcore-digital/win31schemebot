import sys
import requests
from PIL import Image
import random

DEBUG = True

color_lookup = {'Desktop': (255, 0, 255, 255),
                'Inactive Border': (170, 0, 85, 255),
                'Inactive Title Bar': (255, 0, 0, 255),
                'Inactive Title Bar Text': (43, 94, 145, 255),
                'Active Border': (255, 255, 0, 255),
                'Active Title Bar': (124, 123, 39, 255),
                'Active Title Bar Text': (170, 85, 170, 255),
                'Menu Bar': (14, 54, 255, 255),
                'Menu Text': (0, 170, 85, 255),
                'Disabled Text': (190, 189, 189, 255),
                'Highlighted Text': (255, 255, 255, 255),
                'Highlight': (159, 195, 177, 255), 
                'Application Workspace': (0, 255, 0, 255),
                'Window Background': (146, 12, 208, 255),
                'Window Text': (165, 242, 255, 255),
                'Button Highlight': (170, 170, 85, 255),
                'Button Face': (134, 138, 142, 255),
                'Button Shadow': (248, 194, 194, 255),
                'Button Text': (0, 0, 0, 255),
                'Scrollbars': (0, 255, 255, 255)
}


def hex_to_rgb(hexcolor):
    """
    Given a hex color, return its RGB value equivalent as a tuple
    """
    hexcolor = hexcolor.strip('#')
    rgb = tuple(int(hexcolor[i:i+2], 16) for i in (0, 2 ,4))
    return rgb

def rgb_to_hsb(r, g, b):
    """
    Given a rgb color as a tuple, return its hsv value equivalent as a tuple
    """

    r, g, b = r/255.0, g/255.0, b/255.0  
    mx = max(r, g, b)  
    mn = min(r, g, b)  
    df = mx-mn  
    if mx == mn:  
        h = 0  
    elif mx == r:  
        h = (60 * ((g-b)/df) + 360) % 360  
    elif mx == g:  
        h = (60 * ((b-r)/df) + 120) % 360  
    elif mx == b:  
        h = (60 * ((r-g)/df) + 240) % 360  
    if mx == 0:  
        s = 0  
    else:  
        s = (df/mx)*100  
    v = mx*100  
    return h, s, v 


def get_color_palette(palette_id=None):
    """
    Get a random color palette using the Colour Lovers API. 
    Simplify the result a bit, and convert hex to rgb.
    """
    if palette_id:
        url ='https://www.colourlovers.com/api/palette/%s?format=json' % palette_id
    else:
        url = 'https://www.colourlovers.com/api/palettes/random?format=json'
    
    r = requests.get(url).json()
    

    palette_dict = {
                    'title': r[0]['title'], 
                    'count': len(r[0]['colors']),
                    'id': r[0]['id'],
                    }

    colors = []
    for hex_color in r[0]['colors']:
        
        rgb = hex_to_rgb(hex_color)        
        hsb = rgb_to_hsb(*rgb)

        color_dict = { 'hex': hex_color, 'rgb': rgb, 'hsb': hsb }
        colors.append(color_dict)
    
    palette_dict['colors'] = colors


    # Re-sort colors based on saturation
    palette_dict['colors'] = sorted(palette_dict['colors'], key=lambda x: x['hsb'][1], reverse=True) 

    # Create a filename safe version of title
    palette_dict['filename'] = "".join([c for c in palette_dict['title'] if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    palette_dict['filename'] = palette_dict['filename'].replace(' ', '_')
    palette_dict['filename'] = palette_dict['filename'].lower()

    if DEBUG:
        print palette_dict['id']

    return palette_dict


def make_theme(palette):
    """
    Given a dictionary of a color palette, return a dicitonary
    of theme color settings. 
    """

    fields = ['Desktop', 'Inactive Border', 'Inactive Title Bar', 'Inactive Title Bar Text', 'Active Border', 'Active Title Bar', 'Active Title Bar Text', 'Menu Bar', 'Menu Text', 'Disabled Text', 'Highlighted Text', 'Highlight', 'Application Workspace', 'Window Background', 'Window Text', 'Button Highlight', 'Button Face', 'Button Shadow', 'Button Text', 'Scrollbars']

    theme_dict = {}

    for field in fields:
        color_choice = random.choice(palette['colors'])
        theme_dict[field] = color_choice['rgb']

    while theme_dict['Active Title Bar'] == theme_dict['Active Title Bar Text']:
        theme_dict['Active Title Bar Text'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Inactive Title Bar'] == theme_dict['Inactive Title Bar Text']:
        theme_dict['Inactive Title Bar Text'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Menu Bar'] == theme_dict['Menu Text']:
        theme_dict['Menu Text'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Desktop'] == theme_dict['Highlight']:
        theme_dict['Highlight'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Highlight'] == theme_dict['Highlighted Text']:
        theme_dict['Highlighted Text'] = random.choice(palette['colors'])['rgb']


    while theme_dict['Button Face'] == theme_dict['Button Text']:
        theme_dict['Button Text'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Window Background'] == theme_dict['Window Text']:
        theme_dict['Window Text'] = random.choice(palette['colors'])['rgb']

    while theme_dict['Desktop'] == theme_dict['Disabled Text']:
        theme_dict['Disabled Text'] = random.choice(palette['colors'])['rgb']

    filename = palette['filename']

    return theme_dict, filename

def theme_screenshot(theme_dict, filename):

    img = Image.open('crazypants.gif')
    img = img.convert("RGBA")

    pixdata = img.load()

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            for k, v in color_lookup.items():
                if pixdata[x, y] == v:
                    pixdata[x, y] = theme_dict[k]
                    break

    img.save("generated/%s.png" % filename, "PNG")

    if DEBUG:
        img.show()

def generate_image(palette_id=None):

    pal = get_color_palette(palette_id)
    theme_dict, filename = make_theme(pal)
    theme_screenshot(theme_dict, filename)

