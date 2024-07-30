# pip-mockup-kit


```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt

# after add new packages
python3 python3 generate_index.py
```


export PIP_EXTRA_INDEX_URL=https://example.com/repository
pip install mypackage

python setup.py sdist bdist_wheel

Generate an Index
```
/my-repository
    /mypackage
        /1.0.0
            mypackage-1.0.0-py3-none-any.whl
            mypackage-1.0.0.tar.gz
        /1.1.0
            mypackage-1.1.0-py3-none-any.whl
            mypackage-1.1.0.tar.gz
```

```
import os

def generate_index(directory):
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write('<html><body>\n')
        for filename in os.listdir(directory):
            if filename != 'index.html':
                f.write(f'<a href="{filename}">{filename}</a><br>\n')
        f.write('</body></html>\n')

for root, dirs, files in os.walk('my-repository'):
    generate_index(root)
```
cd my-repository
python -m http.server 8000

pip install mypackage --extra-index-url http://localhost:8000

```
# requirements.txt 
--extra-index-url https://pypi.mysite.com/pypi

aiofiles==0.8.0
    # via gcloud-aio-storage
aiohttp==3.9.3
    # via
    #   -r requirements.in
```

```
example/
├── example/
│   ├── __init__.py
│   └── your_module.py
├── setup.py
└── README.md
```

Create the setup.py File
```
from setuptools import setup, find_packages

setup(
    name='example',
    version='2.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/example',  # Replace with your package's URL
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
```

python setup.py sdist bdist_wheel
This will generate .tar.gz and .whl files in the dist directory.
```
example/
├── dist/
│   ├── example-2.0.0-py3-none-any.whl
│   └── example-2.0.0.tar.gz
├── example/
│   ├── __init__.py
│   └── your_module.py
├── setup.py
└── README.md
```

Upload to a Repository (optional)

pip install twine
twine upload dist/*

```
local-repo/
├── example-1.0.0/
│   ├── example-1.0.0-py3-none-any.whl
│   └── example-1.0.0.tar.gz
└── example-2.0.0/
    ├── example-2.0.0-py3-none-any.whl
    └── example-2.0.0.tar.gz
```

Generate Index Files
```
import os

def generate_index(directory):
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write('<html><body>\n')
        for filename in os.listdir(directory):
            if filename != 'index.html':
                f.write(f'<a href="{filename}">{filename}</a><br>\n')
        f.write('</body></html>\n')

root_dir = 'local-repo'
generate_index(root_dir)
for version_dir in ['example-1.0.0', 'example-2.0.0']:
    generate_index(os.path.join(root_dir, version_dir))
```

cd local-repo
python -m http.server 8000

export PIP_EXTRA_INDEX_URL=http://localhost:8000
pip install example==1.0.0

Verify Installation
pip show example


Using pip.conf or pip.ini

Create or edit the pip.conf file, which is usually located at ~/.config/pip/pip.conf or /etc/pip.conf

```
[global]
extra-index-url = https://your.extra.index.url/simple
```


Using setup.py

Modify setup.py:
```
from setuptools import setup

setup(
    name='your-package',
    version='0.1',
    install_requires=[
        'some-package @ https://your.extra.index.url/simple/some-package'
    ],
)
```
python setup.py install




If `PIP_INDEX_URL` and `PIP_EXTRA_INDEX_URL` are being ignored during the dependency scan when using `setup.py`, you can use a custom `get_requires_for_build_wheel` in your `setup.py` to ensure these URLs are used.

### Using a Custom `get_requires_for_build_wheel`

Here’s how you can use a custom function in your `setup.py` to set the `PIP_EXTRA_INDEX_URL` during the build process:

1. **Modify `setup.py`**:

   You need to add a custom hook in your `setup.py` to ensure that `pip` uses the extra index URL when installing dependencies.

   ```python
   import os
   from setuptools import setup
   from setuptools.command.build_py import build_py as _build_py

   class build_py(_build_py):
       def run(self):
           # Set the PIP_EXTRA_INDEX_URL environment variable
           os.environ['PIP_EXTRA_INDEX_URL'] = 'https://your.extra.index.url/simple'
           super().run()

   setup(
       name='your-package',
       version='0.1',
       cmdclass={'build_py': build_py},
       install_requires=[
           'some-package',
           'another-package',
       ],
   )
   ```

### Explanation:

- **Custom Command Class**: By creating a custom `build_py` class that inherits from `setuptools.command.build_py`, you can set environment variables or perform other actions before running the default build process.
- **Environment Variable**: The `PIP_EXTRA_INDEX_URL` environment variable is set inside the `run` method of the custom command class.
- **cmdclass**: The `cmdclass` argument in `setup` is used to replace the standard `build_py` command with the custom one.

### Using `pip` Configuration

If modifying `setup.py` is not desired, using `pip` configuration files can be an alternative:

1. **Create/Edit `pip.conf` (Linux/macOS)**:

   ```ini
   [global]
   extra-index-url = https://your.extra.index.url/simple
   ```

2. **Create/Edit `pip.ini` (Windows)**:

   ```ini
   [global]
   extra-index-url = https://your.extra.index.url/simple
   ```

### Summary

By incorporating a custom command class in your `setup.py`, you can ensure that the `PIP_EXTRA_INDEX_URL` is used during the build process. This method allows you to set environment variables or perform other preparatory steps before the actual build command runs, ensuring all dependencies are fetched from the desired indexes. Alternatively, using `pip` configuration files provides a global or user-specific way to always include the extra index URL.