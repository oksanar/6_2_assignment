from data_converter import ENGLISH_FORMAT, convert_data
from storage import load_data_from_file, save_data_to_file


def main():
     data = load_data_from_file('data.csv')
     command = int(input('''Which measurement system you use?
1. International metric system (celsius, meter)
2. English (fahrenheit, foot)
'''))
     output_data = []
     if command == 1:
          output_data = convert_data(data)
     if command == 2:
          output_data = convert_data(data, ENGLISH_FORMAT)
     output_filename = 'out/output.csv'
     save_data_to_file(output_filename, output_data)
     print(f'Converted data saved to {output_filename}')

if __name__ == '__main__':
     main()
