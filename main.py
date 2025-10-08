import os
import shutil

path ="The path to the folder you want to organize "
remove_ex = [".log",".tmp"]
move_ex = {".docx":"Documents",".txt":"Documents",".png":"Pictures",".jpeg":"Pictures",
           ".jpg":"Pictures",".pptx":"Powerpoint Files",".xlsx":"Excel Files"}
processed_files_count = 0

def moveFile(filePath,destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    shutil.move(filePath,destination)
  
for file in os.listdir(path):
    filePath = os.path.join(path,file)
    fileName,file_ex = os.path.splitext(file)
    
    if file_ex in move_ex:
        destination_folder_name = move_ex[file_ex] 
        full_destination_path = os.path.join(path, destination_folder_name) 
        moveFile(filePath, full_destination_path) 
        processed_files_count += 1

    elif file_ex in remove_ex:
        try:
            os.remove(os.path.join(path,file))
            processed_files_count += 1
        except Exception as e:
            print(e)

if processed_files_count == 0:
    print("No files found to process.")
else:
    print(f"Total {processed_files_count} files processed.")

