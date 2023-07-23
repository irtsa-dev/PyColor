# PyColor
A [**python**](https://www.python.org) collection of classes and functions to convert between **rgb**, **hsv**, **hsl**, **xyz**, **cmyk** and **hex** color formats and generate palettes from said colors.
<br />
- **RGB** (*red*, *green*, *blue*)
- **HSV** (*hue*, *saturation*, *value*)
- **HSL** (*hue*, *saturation*, *lightness*)
- **XYZ** (*x*, *y*, *z*)
- **CMYK** (*cyan*, *magenta*, *yellow*, *key*)
- **HEX** (*hexidecimal*)
<br />
<br />
<br />
<br />
<br />

## Usage
To import, simply put:
```py
from PyColor.Colors import *
from PyColor.Palettes import GeneratePalette
```
<br />

Then, later on you may utilize:
```py
rgb = RGB(100, 100, 100)
hsv = HSV(200, 100, 100)
hsl = HSL(200, 100, 100)
xyz = XYZ(10.0, 10.0, 80.0)
cmyk = CMYK(100, 100, 100, 100)
hexidecimal = HEX("#121212")
```
```py
rgb.rgb
# Returns a tuple of the rgb values from rgb.
rgb.hsv
# Returns a tuple of the hsv values from rgb.
rgb.hsl
# Retuns a tuple of the hsl values from rgb.
rgb.xyz
# Returns a tuple of the xyz values from rgb.
rgb.cmyk
# Returns a tuple of the cmyk values from rgb.
rgb.hexidecimal
# Returns a string of the hexidecimal value from rgb.

rgb.percentForm
# Returns a tuple of the rgb values in a decimal percent form (0-1).
```
```py
hsv.rgb
# Returns a tuple of the rgb values from hsv.
hsv.hsv
# Returns a tuple of the hsv values from hsv.
hsv.hsl
# Retuns a tuple of the hsl values from hsv.
hsv.xyz
# Returns a tuple of the xyz values from rgb.
hsv.cmyk
# Returns a tuple of the cmyk values from hsv.
hsv.hexidecimal
# Returns a string of the hexidecimal value from hsv.

hsv.percentForm
# Returns a tuple of the hsv values in a decimal percent form (0-1).
```
```py
hsl.rgb
# Returns a tuple of the rgb values from hsl.
hsl.hsv
# Returns a tuple of the hsv values from hsl.
hsl.hsl
# Retuns a tuple of the hsl values from hsl.
hsl.xyz
# Returns a tuple of the xyz values from rgb.
hsl.cmyk
# Returns a tuple of the cmyk values from hsl.
hsl.hexidecimal
# Returns a string of the hexidecimal value from hsl.

hsl.percentForm
# Returns a tuple of the hsl values in a decimal percent form (0-1).
```
```py
cmyk.rgb
# Returns a tuple of the rgb values from cmyk.
cmyk.hsv
# Returns a tuple of the hsv values from cmyk.
cmyk.hsl
# Retuns a tuple of the hsl values from cmyk.
cmyk.xyz
# Returns a tuple of the xyz values from rgb.
cmyk.cmyk
# Returns a tuple of the cmyk values from cmyk.
cmyk.hexidecimal
# Returns a string of the hexidecimal value from cmyk.

cmyk.percentForm
# Returns a tuple of the cmyk values in a decimal percent form (0-1).
```
```py
hexidecimal.rgb
# Returns a tuple of the rgb values from hexidecimal.
hexidecimal.hsv
# Returns a tuple of the hsv values from hexidecimal.
hexidecimal.hsl
# Retuns a tuple of the hsl values from hexidecimal.
hexidecimal.xyz
# Returns a tuple of the xyz values from rgb.
hexidecimal.cmyk
# Returns a tuple of the cmyk values from hexidecimal.
hexidecimal.hexidecimal
# Returns a string of the hexidecimal value from hexidecimal.

hexidecimal.percentForm
# Returns a decimal percent form (0-1) of the hexidecimal value.
```
```py
print(rgb)
# Will print off a string representation of the rgb values.

print(hsv)
# Will print off a string representation of the hsv values.

print(hsl)
# Will print off a string representation of the hsl values.

print(xyz)
# Will print off a string representation of the xyz values.

print(cmyk)
# Will print off a string representation of the cmyk values.

print(hexidecimal)
# Will print off a string representation of the hexidecimal value
```
<br />

```py
GeneratePalette(RGB(100, 100, 100), 'triad')
# Will generate a palette in the form of a list of colors in the same type of class given using the scheme provided.
```
​
<br />
<br />
### Code Examples
```py
from PyColors.Colors import *

color = RGB(120, 140, 180)

print("The HSV values for the RGB values of " + str(color.rgb) + " are " + str(color.hsv))
```
```py
from PyColors.Colors import *
from PyColors.Palettes import GeneratePalette

mainColor = HSV(320, 50, 100)
Palette = GeneratePalette(mainColor, "splitcomplimentary")

print("Palette: ")
for color in Palette: print(color)
```
```py
from random import randint
from PyColors.Colors import *

Colors = [RGB(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(10)]

print("Random color RGB values:")
for color in Colors: print(color)
```
​
<br />
<br />
<br />
<br />
## Additional Notes
The following are the currently supports schemes for the `GeneratePalette` function:
- monochromatic
- analogous
- complimentary
- splitcomplimentary
- tetrad
- triad
- random

​
<br />
<br />
​<br />
<br />
<br />
## Installation
```sh
git clone https://github.com/IrtsaDevelopment/PyColor.git
```
