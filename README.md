# pip-mockup-kit

```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt

# after add new packages, ref: packages/jit_ai_hello_world-1.0.0/README.md
python3 python3 generate_index.py

cd packages
python -m http.server 8000

pip install jit_ai_hello_world --extra-index-url http://localhost:8000
```

requirements.txt file
```
# requirements.txt 
--extra-index-url http://localhost:8000
```

```bash
pip3 install -r requirements.txt 
```

Using pip.conf or pip.ini

Create or edit the pip.conf file, which is usually located at ~/.config/pip/pip.conf or /etc/pip.conf

```
[global]
extra-index-url = http://localhost:8000
```
 
or

```bash
export PIP_EXTRA_INDEX_URL=http://localhost:8000

pip install jit_ai_hello_world
```



