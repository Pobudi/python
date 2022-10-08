testy = (218, 112, 214)
hex_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for rgb_value in rgb_color:
        print(rgb_value)
        first_value = hex_values[rgb_value // 16]
        hex_color += first_value
        second_value = hex_values[int((rgb_value / 16 - rgb_value // 16)*16)]
        hex_color += second_value
    return hex_color

hex = rgb_to_hex(testy)
print(hex)