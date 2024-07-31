import os


def generate_index(directory):
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w') as f:
        f.write('<html><body>\n')
        for filename in os.listdir(os.path.join(directory, 'dist')):
            if filename != 'index.html':
                f.write(f'<a href="dist/{filename}">{filename}</a><br>\n')
        f.write('</body></html>\n')

def process_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if we are in a 'dist' directory
        if os.path.basename(dirpath) == 'dist':
            generate_index( os.path.join(dirpath, '..'))


# Root directory where packages are stored
root_dir = 'packages'

# Process each subdirectory to generate index.html in each 'dist' directory
process_directory(root_dir)
