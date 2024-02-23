import csv

def load_data_from_file(filename: str):
     with open(filename, mode='r') as file:
          reader = csv.DictReader(file)
          result = []
          for row in reader:
               result.append(row)
          return result
     
def save_data_to_file(filename: str, data):
     with open(filename, mode='w') as file:
          writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
          writer.writeheader()
          for row in data:
               writer.writerow(row)
