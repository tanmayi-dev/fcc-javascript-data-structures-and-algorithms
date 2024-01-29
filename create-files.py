import os

def process_string(input_str, index):
    # Append numbers to the string
    output_str = f'{index + 1:02d} ' + input_str

    # Convert all letters to lowercase
    output_str = output_str.lower()

    # Replace spaces with hyphens and remove other non-alphanumeric characters
    output_str = '-'.join(filter(str.isalnum, output_str.split()))

    return output_str

def generate_js_file(folder_path, strings):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path) # create dirs if they dont exist

    js_content = ''
    for i, string in enumerate(strings):
        processed_str = process_string(string, i)
        js_file_path = os.path.join(folder_path, f'{processed_str}.js')
        with open(js_file_path, 'w') as js_file:
          js_file.write(js_content)

    print(f'JavaScript file created at: {folder_path}')

# Example usage
input_strings = ["Palindrome Checker","Roman Numeral Converter","Caesars Cipher","Telephone Number Validator","Cash Register"]

folder_path = "./10-js-projects"
generate_js_file(folder_path, input_strings)
