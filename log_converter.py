keymap = {
    1: "ESC", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9", 
    11: "0", 12: "-", 13: "=", 14: "BACKSPACE", 15: "TAB", 16: "q", 17: "w", 18: "e", 
    19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 26: "[", 27: "]", 
    28: "\\", 29: "ALT", 30: "a", 31: "s", 32: "d", 33: "f", 34: "g", 35: "h", 36: "j", 
    37: "k", 38: "l", 39: ";", 40: "'", 41: " ", 42: "print_screen", 44: "z", 
    45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: "m", 51: ",", 52: ".", 53: "/", 
    55: "num_MULTIPLY", 56: "num_0", 57: "num_1", 58: "num_2", 59: "F1", 60: "F2", 
    61: "F3", 62: "F4", 63: "F5", 64: "F6", 65: "F7", 66: "F8", 67: "F9", 68: "F10", 
    69: "Num_Lock", 70: "num_3", 71: "num_4", 72: "num_5", 73: "num_6", 74: "num_7", 
    75: "num_8", 76: "num_9", 87: "F11", 88: "F12", 98: "num_DIVIDE", 102: "Home", 
    103: "up_arrow", 104: "Page_Up", 105: "left_arrow", 106: "right_arrow", 
    107: "down_arrow", 108: "END", 109: "Page_Down", 110: "Insert", 111: "Delete", 
    59: "F13", 60: "F14", 61: "F15", 62: "F16", 63: "F17", 64: "F18", 65: "F19", 
    66: "F20", 67: "F21", 68: "F22", 69: "F23", 70: "F24", 71: "Pause/Break", 
    72: "Menu"
}

def convert_logs(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                keycodes = line.strip().split()
                converted_line = []
                for code in keycodes:
                    if code.isdigit():  
                        keycode = int(code)
                        if keycode in keymap:
                            converted_line.append(keymap[keycode])
                    else:
                        converted_line.append(code)  
                outfile.write(' '.join(converted_line) + '\n')
        print(f"Conversion complete. Converted logs saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except ValueError:
        print("Error: Invalid keycode found in the log file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = 'logs.txt'
output_file = 'logs_converted.txt'
convert_logs(input_file, output_file)

