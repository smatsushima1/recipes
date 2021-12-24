
import os


# Remove/create directories
def reset_dir(dir_path):
    try:
        for i in os.scandir(dir_path):
            os.remove(i.path)
        os.rmdir(dir_path)
        os.makedirs(dir_path)
        print("'%s' directory was created." % (dir_path))
    except:
        os.makedirs(dir_path)
        print("'%s' directory was not there, so was created instead." % (dir_path))


# Convert to individual text files
def convert_file(file_name, dir_name):
    # Read file
    with open(file_name, encoding = 'utf8') as mr:
        lines = mr.readlines()
        mr.close()
    # Read lines
    for i in lines:
        # Reset, then start saving the file name of the new text file
        fname = ""
        if i.isupper():
            close_ind = 0
            fname = i.rstrip()
            # Update file name
            fname_dir = fname.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '').replace("'", '').replace('’', '').replace('.', '').lower() + '.txt'
            wf = open(dir_name + '/' + fname_dir, 'w', encoding = 'utf8')
            wf.writelines(i)
            continue
        # Skip blank spaces
        elif len(i.strip()) == 0:
            close_ind += 1
            if close_ind == 1:
                wf.close()
                continue
            else:
                close_ind = 0
                continue
        # Append text
        else:
            wf.writelines(i.rstrip())


# Combine all operations on each file
def convert_all():
    for i in os.scandir():
        if i.name.endswith('.txt'):
            dname = i.name.replace('.txt', '')
            reset_dir(dname)
            convert_file(i.name, dname)


# Check for dupes
def dupe_check():
    for i in os.listdir():
        if os.path.isdir(i) and i != '__pycache__':
            print(i)
    
    
