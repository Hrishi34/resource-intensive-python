import time
import os

file_size = 50000000  # 50 MB

# Writing to a large file
with open('large_file.txt', 'w') as file:
    for _ in range(file_size):
        file.write('A')

file_path="large_file.txt"

# Reading from a large file
with open('large_file.txt', 'r') as file:
    data = file.read()

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
else:
    print(f"File '{file_path}' does not exist.")
    
time.sleep(20)  # To simulate a 2-minute execution time
