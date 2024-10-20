keymap = {
    1: "",
    2: "1",
    3: "2",
    4: "3",
    5: "4",
    6: "5",
    7: "6",
    8: "7",
    9: "8",
    10: "9",
    11: "0",
    14: "",
    15: "",
    16: "q",
    17: "w",
    18: "e",
    19: "r",
    20: "t",
    21: "y",
    22: "u",
    23: "i",
    24: "o",
    25: "p",
    28: "",
    30: "a",
    31: "s",
    32: "d",
    33: "f",
    34: "g",
    35: "h",
    36: "j",
    37: "k",
    38: "l",
    44: "z",
    45: "x",
    46: "c",
    47: "v",
    48: "b",
    49: "n",
    50: "m",
    55: "KP_Multiply",
    56: "",
    57: "",
    58: "",
    59: "F1",
    60: "F2",
    61: "F3",
    62: "F4",
    63: "F5",
    64: "F6",
    65: "F7",
    66: "F8",
    67: "F9",
    68: "F10",
    69: "Num_Lock",
    87: "F11",
    88: "F12",
    98: "KP_Divide",
    102: "Home",
    103: "",
    104: "Page_Up",
    105: "",
    106: "",
    107: "",
    108: "",
    109: "Page_Down",
    110: "Insert",
    111: "Delete",
    42: ""
}

def convert_logs(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                keycodes = line.strip().split()
                converted_line = ''.join(keymap.get(int(code), '') for code in keycodes)
                outfile.write(converted_line + '\n')
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
