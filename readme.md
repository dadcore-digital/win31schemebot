# Infinite Hotdog Stand

[@hotdogstand4eva](https://twitter.com/hotdogstand4eva) is a twitter bot that generates Windows 3.1 color schemes from random color palettes from [Colour Lovers](https://www.colourlovers.com).

## Method

### The Image

I decided on using the actual color scheme picker in Windows 3.1 to display each color scheme, as that show every possible UI element in Windows in a small space. Also it's iconic itself.

I had to identify each separately customizable UI element, and paint each element with a different color. This allows me to unique identify each element, and assign it in a new color in the code.

I ended up with an image like this:

![Color Scheme Template](https://raw.githubusercontent.com/ianfitzpatrick/win31schemebot/master/template.gif)

And here is the dictionary of color lookups that go with that:


```    
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
```

I also apply some logic to make sure for instance, text and background color of an element aren't the same.

### The Palette

This was pretty simple. Colour Lovers has an API that allows you to get a random palette back as JSON. I did have to convert colors from hex to RGB, and reject any one-color palettes (it's a thing).

The one thing I'm not doing is restricting to the original 256 colors, or somehow casting the palettes to the nearest 256 equivalent. So this is an imaginary Windows 3.1 of nostalgic ideal memory.

### The Font

Locking horns with raster fonts again!

I am dynamically generating the text in the color scheme pull-down with the name of the palette, so the palette name becomes the name of this imaginary cololor scheme.

However for it to look right, I had to get the font perfect. And of course, this is using a raster font which I was not able to find. 

It doesn't appear to be `system.fon`, I compared the fonts side by side and while it could be in that family, it seems to be a bold or wide variant of some sort.

So I did the 'ole screenshot every character, create a sprit sheet, and write a function that "prints" the characters as bitmaps on screen.

For more discussion of spritesheet, see my [Win95 Promises Bot](https://github.com/ianfitzpatrick/win95bot) where I first figured out my method for this.

### Attribution

I went back and forth on how to properly attribute the color palette used to generate each color scheme.

First I tried putting the ID in scheme drop-down in the screenshot, but I didn't like the aesthetic break from original Windows 3.1. I wanted these screenshots to look like plausible actual Windows screenshots.

Next I tried putting attribution in the tweet, but it took focus off the images.

I also tried writing an attribution in the footer of an image using Pillow (the image library I'm using) but there is no way to turn off anti-aliasing to get a pixel font feel. It looked terrible and out of place.

Finally I decided just to log attribution to a text file and link it in the twitter bot's bio.







