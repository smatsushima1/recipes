
import os, time


# Start timer for functinos
def start_function(func_name):
    start_time = time.time()
    print('\n' + ('#' * 80))
    print('Function: %s\nStarting...' % (func_name))
    return start_time


# End timer for functions
def end_function(start_time):
    end_time = time.time() - start_time
    if end_time > 60:
        res = end_time / 60
        res_spl = str(res).split('.')
        mins = res_spl[0]
        secs = round(float('.' + res_spl[1]) * 60, 3)
        print('''Function finished in %s' %s"''' % (mins, secs))
    else:
        print('Function finished in %s"' % round(time.time() - start_time, 3))


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
        # Append text - line breaks need to be preserved, so no stripping
        else:
            wf.writelines(i)


# Combine all operations on each file
def convert_all():
    start_time = start_function('convert_all')
    for i in os.scandir():
        # Only search for main recipe text files
        if i.name.endswith('.txt'):
            dname = i.name.replace('.txt', '')
            reset_dir(dname)
            convert_file(i.name, dname)
    end_function(start_time)


# Check for dupes
def dupe_check():
    start_time = start_function('dupe_check')
    dlist = []
    # First get list of subdirectories to search through
    for i in os.listdir():
        if os.path.isdir(i) and i != '__pycache__':
            dlist.append(i)
    # Loop through each subdirectory listed and check for any dupes
    for x1, i in enumerate(dlist):
        for j in os.scandir(i):
            for x2, k in enumerate(dlist):
                # Don't run if in the same subdirectory, or if already ran previously
                if x1 >= x2:
                    continue
                else:
                    for l in os.scandir(k):
                        # Show where dupes are
                        if j.name == l.name:
                            print('DIRECTORY 1: %s; FILE 1: %s' % (i, j.name))
                            print('DIRECTORY 2: %s; FILE 2: %s' % (k, l.name))
                            print()
    end_function(start_time)

    
