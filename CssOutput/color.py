
def RGBtoColorcode(R, G, B, A=None):
    R16 = "{0:02x}".format(R)
    G16 = "{0:02x}".format(G)
    B16 = "{0:02x}".format(B)

    color_code = "#" + R16 + G16 + B16

    if not A is None:  # RGB
        A16 = "{0:02x}".format(A)
        print(A16)
        color_code += A16

    return color_code


# RGBtoColorcode(100, 200, 250, 100)
