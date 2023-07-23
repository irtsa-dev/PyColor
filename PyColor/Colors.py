# PythonColor | Color






#Imports
from math import degrees, acos, sqrt






#Classes
class RGB:
    """
    RGB color class object. 
    Takes in a red, green, and blue value between 0-255

    Attributes:
        red (int): An integer value between 0-255.
        green (int): An integer value between 0-255.
        blue (int): An integer value between 0-255.

    Valid Examples:
     - RGB(100, 100, 100)
     - RGB(30, 30, 30)
     - RGB(50, 34, 200)

    Invalid Examples:
     - RGB(234, 300, 100)
     - RGB(249, 29, 290)
     - RGB(365, 265, 100)
    """
    
    @staticmethod
    def __checkIfRGB(value):
        if any([True for i in value if type(i) != int]): return False
        if len([i for i in value if i > 0 and i < 255]) != 3: return False
        
        return True



    def __init__(self, red: int, green: int, blue: int):
        if self.__checkIfRGB((red, green, blue)):
            self.red = red
            self.green = green
            self.blue = blue
            self.__valid = True
        
        else: self.__valid = False
    

    @property
    def rgb(self) -> tuple:
        if not self.__valid: return None
        return (self.red, self.green, self.blue)


    @property
    def hexidecimal(self) -> str:
        if not self.__valid: return None

        r = hex(self.red)[2:].upper()
        g = hex(self.green)[2:].upper()
        b = hex(self.blue)[2:].upper()

        return '#' + ''.join([r, g, b])


    @property
    def hsv(self) -> tuple:
        if not self.__valid: return None

        M = max(self.red, self.green, self.blue)
        m = min(self.red, self.green, self.blue)

        V = (M / 255) * 100

        S = 0
        if M > 0: S = 100 - ((m / M) * 100)

        try:
            H = degrees(acos((self.red - (self.green / 2) - (self.blue / 2)) / sqrt((self.red ** 2) + (self.green ** 2) + (self.blue ** 2) - (self.red * self.green) - (self.red * self.blue) - (self.green * self.blue))))
            if self.blue > self.green: H = 360 - H
        except: H = 0

        H = int(round(H))
        S = int(round(S))
        V = int(round(V))

        return (H, S, V)


    @property 
    def hsl(self) -> tuple:
        if not self.__valid: return None

        M = max([self.red, self.green, self.blue])
        m = min([self.red, self.green, self.blue])

        M = max([(self.red / 255.0), (self.green / 255.0), (self.blue / 255.0)])
        m = min([(self.red / 255.0), (self.green / 255.0), (self.blue / 255.0)])

        C = M - m
        L = (M + m) / 2.0

        S = 0
        if C != 0: S = ((C / (1.0 - abs((2.0 * L) - 1.0))) * 100.0)
		
        try:
            H = degrees(acos((self.red - (self.green / 2) - (self.blue / 2)) / sqrt((self.red ** 2) + (self.green ** 2) + (self.blue ** 2) - (self.red * self.green) - (self.red * self.blue) - (self.green * self.blue))))
            if self.blue > self.green: H = 360 - H
        except: H = 0

        H = int(round(H))
        S = int(round(S))
        L = int(round(L * 100.0))
			
        return (H, S, L)


    @property
    def cmyk(self) -> str:
        if not self.__valid: return None

        nr = self.red / 255.0
        ng = self.green / 255.0
        nb = self.blue / 255.0

        K = 1.0 - max(nr, ng, nb)

        C = int(round(((1 - nr - K) / (1 - K) * 100)))
        M = int(round(((1 - ng - K) / (1 - K) * 100)))
        Y = int(round(((1 - nb - K) / (1 - K) * 100)))
        K = int(round(K * 100))

        return (C, M, Y, K)
    

    @property
    def percentForm(self) -> tuple:
        if not self.__valid: return None

        r = round((self.red / 255.0), 2)
        g = round((self.green / 255.0), 2)
        b = round((self.blue / 255.0), 2)

        return (r, g, b)
        


    def __repr__(self):
        if not self.__valid: return 'Invalid RGB'
        return str(self.red) + ' ' + str(self.green) + ' ' + str(self.blue)




class HEX:
    """
    HEX color class object. 
    Takes in a hexidecimal representation of a color as a string that includes the #.

    Attributes:
        hexicode (str): A hexidecimal form of a color.

    Valid Examples:
     - HEX("#121212")
     - HEX("#A32B12")
     - HEX("#FEFF73")

    Invalid Examples:
     - HEX(121212)
     - HEX("A3312")
     - HEX("311252")
    """

    @staticmethod
    def __checkIfHEX(value):
        if type(value) != str: return False
        value = [value[1:][i:i+2] for i in range(0, len(value[1:]), 2)]

        if any([True for i in value if len(i) != 2]): return False

        try: value = [int(i, 16) for i in value]
        except: return False

        if any([True for i in value if i > 255]) or any([True for i in value if i < 0]): return False

        return True



    def __init__(self, hexicode: str):
        if self.__checkIfHEX(hexicode):
            self.hexicode = hexicode
            self.__valid = True
        
        else: self.__valid = False
    

    @property
    def rgb(self) -> tuple:
        if not self.__valid: return None

        Values = [self.Values[1:][i:i+2] for i in range(0, len(self.Values[1:]), 2)]
        Values = [int(i, 16) for i in Values]

        return tuple(Values)


    @property
    def hexidecimal(self) -> str:
        if not self.__valid: return None
        return self.hexicode
    

    @property
    def hsv(self) -> tuple:
        if not self.__valid: return None

        M = max(self.rgb[0], self.rgb[1], self.rgb[2])
        m = min(self.rgb[0], self.rgb[1], self.rgb[2])

        V = (M / 255) * 100

        S = 0
        if M > 0: S = 100 - ((m / M) * 100)

        try:
            H = degrees(acos((self.rgb[0] - (self.rgb[1] / 2) - (self.rgb[2] / 2)) / sqrt((self.rgb[0] ** 2) + (self.rgb[1] ** 2) + (self.rgb[2] ** 2) - (self.rgb[0] * self.rgb[1]) - (self.red * self.rgb[2]) - (self.rgb[1] * self.rgb[2]))))
            if self.rgb[2] > self.rgb[1]: H = 360 - H
        except: H = 0

        H = int(round(H))
        S = int(round(S))
        V = int(round(V))

        return (H, S, V)
    

    @property 
    def hsl(self) -> tuple:
        if not self.__valid: return None

        M = max([self.rgb[0], self.rgb[1], self.rgb[2]])
        m = min([self.rgb[0], self.rgb[1], self.rgb[2]])

        M = max([(self.rgb[0] / 255.0), (self.rgb[1] / 255.0), (self.rgb[2] / 255.0)])
        m = min([(self.rgb[0] / 255.0), (self.rgb[1] / 255.0), (self.rgb[2] / 255.0)])

        C = M - m
        L = (M + m) / 2.0

        S = 0
        if C != 0: S = ((C / (1.0 - abs((2.0 * L) - 1.0))) * 100.0)
		
        try:
            H = degrees(acos((self.rgb[0] - (self.rgb[1] / 2) - (self.rgb[2] / 2)) / sqrt((self.rgb[0] ** 2) + (self.rgb[1] ** 2) + (self.rgb[2] ** 2) - (self.rgb[0] * self.rgb[1]) - (self.rgb[0] * self.rgb[2]) - (self.rgb[1] * self.rgb[2]))))
            if self.rgb[2] > self.rgb[1]: H = 360 - H
        except: H = 0

        H = int(round(H))
        S = int(round(S))
        L = int(round(L * 100.0))
			
        return (H, S, L)
    

    @property
    def cmyk(self):
        if not self.__valid: return None

        nr = self.rgb[0] / 255.0
        ng = self.rgb[1] / 255.0
        nb = self.rgb[2] / 255.0

        K = 1.0 - max(nr, ng, nb)

        C = int(round(((1 - nr - K) / (1 - K) * 100)))
        M = int(round(((1 - ng - K) / (1 - K) * 100)))
        Y = int(round(((1 - nb - K) / (1 - K) * 100)))
        K = int(round(K * 100))

        return (C, M, Y, K)



    @property
    def percentForm(self) -> float:
        Numbers = [int(i, 16) for i in self.hexicode[1:]][::-1]
        Numbers = [((16 ** i) * Numbers[i]) for i in range(len(Numbers))]

        number = sum(Numbers)

        return round((number / 16777215.0), 3)
    


    def __repr__(self):
        if not self.__valid: return 'Invalid HEX'
        return self.hexicode




class HSV:
    """
    HSV color class object. 
    Takes in hue, saturation, and value values.

    Attributes:
        hue (int): An integer value between 0-360.
        saturation (int): An integer value between 0-100.
        value (int): An integer value between 0-100.

        
    Valid Examples:
     - HSV(342, 100, 100)
     - HSV(100, 30, 80)
     - HSV(50, 30, 100)

    Invalid Examples:
     - HSV(2, 101, 50)
     - HSV(-3, 29, 290)
     - HSV(365, 123, 100)
    """
    
    @staticmethod
    def __checkIfHSV(value):
        if any([True for i in value if type(i) != int]): return False

        if value[0] < 0 or value[0] > 360: return False
        if value[1] < 0 or value[1] > 100: return False
        if value[2] < 0 or value[2] > 100: return False

        return True



    def __init__(self, hue: int, saturation: int, value: int):
        if self.__checkIfHSV((hue, saturation, value)):
            self.hue = hue
            self.saturation = saturation
            self.value = value
            self.__valid = True
        
        else: self.__valid = False
    

    @property
    def rgb(self) -> tuple:
        if not self.__valid: return None

        value = self.value / 100.0
        saturation = self.saturation / 100.0
		
        C = value * saturation
        X = C * (1.0 - abs(((self.hue / 60.0) % 2.0) - 1.0))
        m = value - C
		
        match int(self.hue / 60.0):
            case 0: rgb = [C, X, 0]
            case 1: rgb = [X, C, 0]
            case 2: rgb = [0, C, X]
            case 3: rgb = [0, X, C]
            case 4: rgb = [X, 0, C]
            case 5 | 6: rgb = [C, 0, X]
        
        rgb = [((rgb[0] + m) * 255.0), ((rgb[1] + m) * 255.0), ((rgb[2] + m) * 255.0)]
        rgb = [int(round(i)) for i in rgb]

        return (rgb[0], rgb[1], rgb[2])
    

    @property
    def hexidecimal(self) -> str:
        if not self.__valid: return None

        r = hex(self.rgb[0])[2:].upper()
        g = hex(self.rgb[1])[2:].upper()
        b = hex(self.rgb[2])[2:].upper()

        return '#' + ''.join([r, g, b])
    

    @property
    def hsv(self) -> tuple:
        return (self.hue, self.saturation, self.value)
        

    @property
    def hsl(self) -> tuple:
        if not self.__valid: return None

        s = self.saturation / 100.0
        v = self.value / 100.0

        L = (2 - s) * v / 2.0

        if L != 0:
            if L == 1: S = 0
            elif L < 0.5: S = int(round(s * v / (L * 2.0)))
            else: S = int(round(s * v / (2.0 - L * 2.0)))
        
        S = int(round(S * 100.0))
        L = int(round(L * 100.0))

        return (self.hue, S, L)
    

    @property
    def cmyk(self) -> tuple:
        if not self.__valid: return None

        nr = self.rgb[0] / 255.0
        ng = self.rgb[1] / 255.0
        nb = self.rgb[2] / 255.0

        K = 1.0 - max(nr, ng, nb)

        C = int(round(((1 - nr - K) / (1 - K) * 100)))
        M = int(round(((1 - ng - K) / (1 - K) * 100)))
        Y = int(round(((1 - nb - K) / (1 - K) * 100)))
        K = int(round(K * 100))

        return (C, M, Y, K)
    

    @property
    def percentForm(self) -> tuple:
        if not self.__valid: return None

        h = round((self.hue / 360.0), 2)
        s = round((self.saturation / 100.0), 2)
        v = round((self.value / 100.0), 2)

        return (h, s, v)
    


    def __repr__(self):
        if not self.__valid: return 'Invalid HSV'
        return str(self.hue) + '° ' + str(self.saturation) + '% ' + str(self.value) + '%'




class HSL:
    """
    HSL color class object. 
    Takes in hue, saturation, and lightness values.

    Attributes:
        hue (int): An integer value between 0-360.
        saturation (int): An integer value between 0-100.
        lightness (int): An integer value between 0-100.

        
    Valid Examples:
     - HSL(342, 100, 100)
     - HSL(100, 30, 80)
     - HSL(50, 30, 100)

    Invalid Examples:
     - HSL(2, 101, 50)
     - HSL(-3, 29, 290)
     - HSL(365, 123, 100)
    """

    @staticmethod
    def __checkIfHSL(value):
        if any([True for i in value if type(i) != int]): return False

        if value[0] < 0 or value[0] > 360: return False
        if value[1] < 0 or value[1] > 100: return False
        if value[2] < 0 or value[2] > 100: return False

        return True



    def __init__(self, hue: int, saturation: int, lightness: int):
        if self.__checkIfHSL((hue, saturation, lightness)):
            self.hue = hue
            self.saturation = saturation
            self.lightness = lightness
            self.__valid = True
        
        else: self.__valid = False
    

    @property
    def rgb(self) -> tuple:
        if not self.__valid: return None

        saturation = self.saturation / 100
        lightness = self.lightness / 100
		
        C = (1 - abs((2 * lightness) - 1)) * saturation
		
        X = C * (1 - abs(((self.hue / 60) % 2) - 1))
		
        m = lightness - (C / 2)

        match int(self.hue / 60.0):
            case 0: rgb = [C, X, 0]
            case 1: rgb = [X, C, 0]
            case 2: rgb = [0, C, X]
            case 3: rgb = [0, X, C]
            case 4: rgb = [X, 0, C]
            case 5 | 6: rgb = [C, 0, X]
		
		
        rgb = [((rgb[0] + m) * 255), ((rgb[1] + m) * 255), ((rgb[2] + m) * 255)]
        rgb = [int(round(i)) for i in rgb]
			
        return (rgb[0], rgb[1], rgb[2])


    @property
    def hexidecimal(self) -> str:
        if not self.__valid: return None

        r = hex(self.rgb[0])[2:].upper()
        g = hex(self.rgb[1])[2:].upper()
        b = hex(self.rgb[2])[2:].upper()

        return '#' + ''.join([r, g, b])
    

    @property
    def hsv(self) -> tuple:
        if not self.__valid: return None

        L = (self.lightness / 100.0) * 2

        if L <= 1: S = (self.saturation / 100.0) * L
        else: S = 2 - L

        S = int(round((2.0 * S) / (L + S)))
        V = int(round((L + S) / 2.0))

        return (self.hue, S, V)


    @property
    def hsl(self) -> tuple:
        if not self.__valid: return None
        return (self.hue, self.saturation, self.lightness)
    

    @property
    def cmyk(self) -> tuple:
        if not self.__valid: return None

        nr = self.rgb[0] / 255.0
        ng = self.rgb[1] / 255.0
        nb = self.rgb[2] / 255.0

        K = 1.0 - max(nr, ng, nb)

        C = int(round(((1 - nr - K) / (1 - K) * 100)))
        M = int(round(((1 - ng - K) / (1 - K) * 100)))
        Y = int(round(((1 - nb - K) / (1 - K) * 100)))
        K = int(round(K * 100))

        return (C, M, Y, K)
    

    @property
    def percentForm(self) -> tuple:
        if not self.__valid: return None

        h = round((self.hue / 360.0), 2)
        s = round((self.saturation / 100.0), 2)
        l = round((self.lightness / 100.0), 2)

        return (h, s, l)
    


    def __repr__(self):
        if not self.__valid: return 'Invalid HSL'
        return str(self.hue) + '° ' + str(self.saturation) + '% ' + str(self.lightness) + '%'




class CMYK:
    """
    CMYK color class object. 
    Takes in cyan, magenta, yellow, and key values.

    Attributes:
        cyan (int): An integer value between 0-100.
        magenta (int): An integer value between 0-100.
        yellow (int): An integer value between 0-100.
        key (int): An integer value between 0-100.

        
    Valid Examples:
     - CMYK(100, 100, 100, 100)
     - CMYK(100, 30, 80, 30)
     - CMYK(50, 30, 100, 0)

    Invalid Examples:
     - CMYK(2, 101, 50, 101)
     - CMYK(-3, 29, 290, 0)
     - CMYK(365, 123, 100, -100)
    """

    @staticmethod
    def __checkIfCMYK(value):
        if any([True for i in value if type(i) != int]): return False
        return len([i for i in list(value) if i >= 0 and i <= 100]) == 4



    def __init__(self, cyan: int, magenta: int, yellow: int, key: int):
        if self.__checkIfCMYK((cyan, magenta, yellow, key)):
            self.cyan = cyan
            self.magenta = magenta
            self.yellow = yellow
            self.key = key
            self.__valid = True
        
        else: self.__valid = False
    

    @property
    def rgb(self) -> tuple:
        if not self.__valid: return None

        K = self.key / 100.0
        red = int(round(-255 * (((self.cyan / 100.0) * (1 - K)) - 1 + K)))
        green = int(round(-255 * (((self.magenta / 100.0) * (1 - K)) - 1 + K)))
        blue = int(round(-255 * (((self.yellow / 100.0) * (1 - K)) - 1 + K)))

        return (red, green, blue)


    @property
    def hexidecimal(self) -> str:
        if not self.__valid: return None

        r = hex(self.rgb[0])[2:].upper()
        g = hex(self.rgb[1])[2:].upper()
        b = hex(self.rgb[2])[2:].upper()

        return '#' + ''.join([r, g, b])
    

    @property
    def hsv(self) -> tuple:
        if not self.__valid: return None

        red = self.rgb[0]
        green = self.rgb[1]
        blue = self.rgb[2]

        M = max(red, green, blue)
        m = min(red, green, blue)

        V = (M / 255) * 100

        S = 0
        if M > 0: S = 100 - ((m / M) * 100)

        try:
            H = degrees(acos((red - (green / 2) - (blue / 2)) / sqrt((red ** 2) + (green ** 2) + (blue ** 2) - (red * green) - (red * blue) - (green * blue))))
            if blue > green: H = 360 - H
        except: H = 0
        if H != 0: H -= 1

        H = int(round(H))
        S = int(round(S))
        V = int(round(V))

        return (H, S, V)


    @property 
    def hsl(self) -> tuple:
        if not self.__valid: return None

        red = self.rgb[0]
        green = self.rgb[1]
        blue = self.rgb[2]

        M = max([red, green, blue])
        m = min([red, green, blue])

        M = max([(red / 255.0), (green / 255.0), (blue / 255.0)])
        m = min([(red / 255.0), (green / 255.0), (blue / 255.0)])

        C = M - m
        L = (M + m) / 2.0

        S = 0
        if C != 0: S = ((C / (1.0 - abs((2.0 * L) - 1.0))) * 100.0)
		
        try:
            H = degrees(acos((red - (green / 2) - (blue / 2)) / sqrt((red ** 2) + (green ** 2) + (blue ** 2) - (red * green) - (red * blue) - (green * blue))))
            if blue > green: H = 360 - H
        except: H = 0
        if H != 0: H -= 1

        H = int(round(H))
        S = int(round(S))
        L = int(round(L * 100.0))
			
        return (H, S, L)
    

    @property
    def cmyk(self) -> tuple:
        if not self.__valid: return None
        return (self.cyan, self.magenta, self.yellow, self.key)
    

    @property
    def percentForm(self) -> tuple:
        if not self.__valid: return None

        c = round((self.cyan / 100.0), 2)
        m = round((self.magenta / 100.0), 2)
        y = round((self.yellow / 100.0), 2)
        k = round((self.key / 100.0), 2)

        return (c, m, y, k)


    
    def __repr__(self):
        if not self.__valid: return 'Invalid CMYK'
        return str(self.cyan) + '% ' + str(self.magenta) + '% ' + str(self.yellow) + '% ' + str(self.key) + '% '
