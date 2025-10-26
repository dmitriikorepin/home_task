import os

current_directory = os.getcwd()

print("Your operating system is Windows" if os.name == "nt" else "Linux")
print("You are currently in", current_directory)

def my_files_sorter():
    txt_count = 0
    csv_count = 0
    py_count = 0
    txt_total_size = 0
    csv_total_size = 0
    py_total_size = 0
    moved_txt_files = 0
    moved_csv_files = 0
    moved_py_files = 0

    excluded_dirs = {
    'Sorted directory for txt files',
    'Sorted directory for csv files',
    'Sorted directory for py files'
    }

    for my_filename in os.listdir(current_directory): #Loop for counting and directory creation
        if os.path.isdir(os.path.join(current_directory, my_filename)) or my_filename in excluded_dirs:
            continue
        match my_filename.split('.')[-1]:
            case "txt":
                txt_count += 1
            case "csv":
                csv_count += 1
            case "py":
                py_count += 1

    if txt_count != 0 and not os.path.exists('Sorted directory for txt files'):
        os.mkdir('Sorted directory for txt files')
    if csv_count != 0 and not os.path.exists('Sorted directory for csv files'):
        os.mkdir('Sorted directory for csv files')
    if py_count != 0 and not os.path.exists('Sorted directory for py files'):
        os.mkdir('Sorted directory for py files')

    print(f"In current directory there are {txt_count} txt files, {csv_count} csv files, and {py_count} py files")

    for my_filename in os.listdir(current_directory): #Loop for moving files in recently created directories
        extension = my_filename.split('.')[-1]
        source_path = os.path.join(current_directory, my_filename)

        if os.path.isdir(source_path) or my_filename in excluded_dirs:
            continue

        if extension == "txt":
            new_filename = f"renamed_{my_filename}"
            new_source_path = os.path.join(current_directory, new_filename)
            os.rename(source_path, new_source_path)
            source_path = new_source_path

            destination_path = os.path.join(current_directory, 'Sorted directory for txt files', new_filename)
            if not os.path.exists(destination_path):
                os.rename(source_path, destination_path)
                moved_txt_files += 1
                txt_total_size += os.path.getsize(destination_path)
                print(f"Moved {my_filename} to {destination_path}")
            else:
                print(f"File {my_filename} already exists in {destination_path}")

        elif extension == "csv":
            new_filename = f"renamed_{my_filename}"
            new_source_path = os.path.join(current_directory, new_filename)
            os.rename(source_path, new_source_path)
            source_path = new_source_path

            destination_path = os.path.join(current_directory, 'Sorted directory for csv files', new_filename)
            if not os.path.exists(destination_path):
                os.rename(source_path, destination_path)
                moved_csv_files += 1
                csv_total_size += os.path.getsize(destination_path)
                print(f"Moved {my_filename} to {destination_path}")
            else:
                print(f"File {my_filename} already exists in {destination_path}")

        elif extension == "py":
            new_filename = f"renamed_{my_filename}"
            new_source_path = os.path.join(current_directory, new_filename)
            os.rename(source_path, new_source_path)
            source_path = new_source_path
            
            destination_path = os.path.join(current_directory, 'Sorted directory for py files', new_filename)
            if not os.path.exists(destination_path):
                os.rename(source_path, destination_path)
                moved_py_files += 1
                py_total_size += os.path.getsize(destination_path)
                print(f"Moved {my_filename} to {destination_path}")
            else:
                print(f"File {my_filename} already exists in {destination_path}")

    # Convert sizes to kilobytes
    txt_total_size_kb = round(txt_total_size / 1024, 2)
    csv_total_size_kb = round(csv_total_size / 1024, 2)
    py_total_size_kb = round(py_total_size / 1024, 2)

    print(f"\nIn the folder for text files, {moved_txt_files} files were moved with a total size of {txt_total_size_kb} KB")
    print(f"In the folder for CSV files, {moved_csv_files} files were moved with a total size of {csv_total_size_kb} KB")
    print(f"In the folder for Python files, {moved_py_files} files were moved with a total size of {py_total_size_kb} KB")

my_files_sorter()