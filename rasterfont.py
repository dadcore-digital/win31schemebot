from PIL import Image


sprite_map_rows = [ ('W', 0, 22, 24), # Characters, top, bottom, width
                    ('@', 22, 44, 22),
                    ('AMVXYZmw%', 44, 66, 16),
                    ('CDGHKNOPQRU#_', 66, 88, 14),
                    ('BEFLSTabcdeghknopquvy234567890?$^&+', 88, 110, 12),
                    ('sxz<>"', 110, 132, 10),
                    ('J1={}', 132, 154, 8),
                    ('frt-();,', 154, 176, 6),
                    ("Iijl!':. ", 176, 198, 4)
                    ] 


def build_sprite_map(chars, top, bottom, width):
    """
    Automatically build a sprite map dictionary.

    Takes:
    
        chars: String of characters like 'abcde'
        top: X of top row of sprites
        bottom: X of bottom of row of sprites
        width: the width of each sprite
    """

    sprite_map = {}
    
    for idx, char in enumerate(chars):
        sprite_map[char] = (idx * width,  top, (idx * width) + width, bottom)

    return sprite_map

def build_sprite_dict(sprite_map, sprite_img):
    """
    Build a dictionary of the actual sprites

    Takes:

        sprite_map: a dictionary of charcters/crop positions
        sprite_img: a PIL image object of the sprite sheet to process

    """

    sprite_dict = {}

    for char, pos in sprite_map.items():
        img = sprite_img.copy()
        img = img.crop(box=pos)
        sprite_dict[char] = img

    return sprite_dict


def composite(text, bg_img, x, y, sprite_dict, kerning=2):
    """
    Composites a list of of messages to a background image, returning a new copy of
    the composite.

    Takes:

        Required
        - text: Text to composite
        - bg_img: The background image to composite text onto
        - x, y: Upper left corner starting coordinates
        - sprite_dict: A dictioanry of sprite PIL image objects (the hacked together win 3.1 font)
    
        Optional
        - char_height: height of characters in font
        - kerning: Amount of space between characters
    """

    new_bg_img = bg_img.copy()
    x_pos, y_pos = x, y
        
    for char in text:
        try:
            new_bg_img.paste(sprite_dict[char], (x_pos, y_pos))
            x_pos = x_pos + sprite_dict[char].width + kerning
        except KeyError:
            # We don't have a sprite for this special character
            pass


    return new_bg_img

def init_chars(spritesheet_path):
    """
    Build sprite dict and store in memory on program run
    """
    sprite_img = Image.open(spritesheet_path).convert('RGBA')

    sprite_map = {}
    for row in sprite_map_rows:
        result = build_sprite_map(row[0], row[1], row[2], row[3])
        sprite_map = dict( sprite_map.items() + result.items() )

    sprite_dict = build_sprite_dict(sprite_map, sprite_img)
    return sprite_dict


def print_to_image(image_obj, text, x, y, spritesheet_path):
    sprite_dict = init_chars(spritesheet_path)
    result = composite(text, image_obj, x, y, sprite_dict)
    return result




