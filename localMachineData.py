import os 
import shutil
import socket

specific_file_size =  "Insert specific file path"
drives = ["C:\\", "D:\\", "U:\\"]
host_name = "".join(["Toolset Name",socket.gethostname()[6:9]])
divisor = 1024 ** 3

#Function to grab host name from the host pc
def write_host_name():
   file.write(f'{host_name},')

#Converts bytes to GB
def byte_to_GB(size):
   GB = round((size / divisor), 2)
   file.write(f'{GB},')

#Utilize the tuple to write out percentages from selected drives on the pc.
def byte_to_GB_tuple(i,total, used):
   GB =  round((total / divisor), 2)
   GB2 = round((used / divisor), 2)
   percentage = round(((GB2 / GB)* 100), 2) 
   print(i)
   if i >= 3:
      file.write(f'{percentage}%')
   else:
      file.write(f'{percentage}%,')

#Takes a file path, utilizes helper function to convert bytes to GB    
def file_size_grab(path):
   file_size = os.path.getsize(path)
   byte_to_GB(file_size)

#Takes the tuple from a drive letter, of total, used and free utilization.
def disk_size_grab(i, drive):
   total, used, free = shutil.disk_usage(drive)
   byte_to_GB_tuple(i, total, used)

#iterates through drives calling helper function
def grab_drive_data():
   i = 0
   for x in drives:
      i += 1
      disk_size_grab(i, x)

#Main code 
file_name =    (f'{host_name} Drive Usage.txt')
file = open(file_name, "a")
if file.closed:
   print("Failed to open file")
write_host_name()
file_size_grab(specific_file_size)
grab_drive_data()
file.close()
exit()
