"""
Acest program definește două funcții, rgb_to_hex și hex_to_rgb, care realizează
conversia din RGB în Hexadecimal și invers, respectiv.
Funcțiile primesc fiecare un singur argument - o tuplă cu valorile R, G și B în cazul rgb_to_hex,
sau o valoare Hexadecimală sub formă de string în cazul hex_to_rgb. Funcțiile returnează valoarea convertită sub forma
unei valori Hexadecimale sau a unei tuple cu valorile R, G și B, în funcție de conversia realizată.
"""

def rgb_to_hex(rgb):
    """Conversia din RGB în Hexadecimal"""
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex_code):
    """Conversia din Hexadecimal în RGB"""
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

# Exemple de utilizare

rgb = (255, 0, 127)
hex_code = rgb_to_hex(rgb)
print(f"RGB: {rgb}, Hexadecimal: {hex_code}")

hex_code = "#ff007f"
rgb = hex_to_rgb(hex_code)
print(f"Hexadecimal: {hex_code}, RGB: {rgb}")