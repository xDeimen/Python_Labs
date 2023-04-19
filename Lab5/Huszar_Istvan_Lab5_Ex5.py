def rgb_to_hex(r, g, b):
    """Conversia din RGB în Hexadecimal"""
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex_code):
    """Conversia din Hexadecimal în RGB"""
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


while True:
    print("Select conversion option:")
    print("1. RGB to HEX")
    print("2. HEX to RGB")
    option = input("Enter option number: ")
    if option not in ("1", "2"):
        print("Invalid option. Please enter 1 or 2.")
        continue
    value = input("Enter value: ")
    if option == "1":
        a=[0, 0, 0]
        a[0], a[1], a[2]= value.split()
        a[0] = int(a[0])
        a[1] = int(a[1])
        a[2] = int(a[2])
        if(len(a) != 3 or a[0]>255 or a[1]>255 or a[2]>255 or a[0]<0 or a[1]<0 or a[2]<0):
            print("Invalid Format please introduce 3 integer numbers for rgb, which are smaller than 256 and bigger than -1")
            continue
        print(rgb_to_hex(a[0], a[1], a[2]))
    elif option == "2":
        if(len(value)!=7 or len(value) !=6):
            print("Invalid format, please introduce a proper hexadecimal value")
            continue
        print(hex_to_rgb(value))
    break
