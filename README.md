# pip-mockup-kit

```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt

cd packages/jit-ai-hello-world
#generate a .tar.gz and .whl file in the `dist` directory 
python3 setup.py sdist bdist_wheel

cd ../../
python3 generate_index.py

#install
pip install jit-ai-hello-world --extra-index-url https://juniorit-ai.github.io/pip-mockup-kit/packages
```

requirements.txt file
```
# requirements.txt 
--extra-index-url https://juniorit-ai.github.io/pip-mockup-kit/packages
```

```bash
pip3 install -r requirements.txt 
```

Using pip.conf or pip.ini

Create or edit the pip.conf file, which is usually located at ~/.config/pip/pip.conf or /etc/pip.conf

```
[global]
extra-index-url = https://juniorit-ai.github.io/pip-mockup-kit/packages
```
 
or

```bash
export PIP_EXTRA_INDEX_URL=https://juniorit-ai.github.io/pip-mockup-kit/packages

pip install jit-ai-hello-world
```



