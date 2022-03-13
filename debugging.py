"""
********
*      *
*      *
********
prints a box with given dimensions and symbols
"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of len 1.')
    if (width < 2) or (height < 2):
        raise Exception('width and length must be greater than  or equal to 2')
    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('**', 15, 5)
boxPrint('O', 5, 16)