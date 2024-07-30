import os

def generate_index(directory):
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w') as f:
        f.write('<html><body>\n')
        for filename in os.listdir(directory):
            if filename != 'index.html':
                f.write(f'<a href="{filename}">{filename}</a><br>\n')
        f.write('</body></html>\n')
    print(f"Index generated at {index_path}")

def process_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if we are in a 'dist' directory
        if os.path.basename(dirpath) == 'dist':
            generate_index(dirpath)

# Root directory where packages are stored
root_dir = 'packages'

# Generate the main index for the root directory
generate_index(root_dir)

# Process each subdirectory to generate index.html in each 'dist' directory
process_directory(root_dir)
