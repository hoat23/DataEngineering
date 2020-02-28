# Jupiter Instalation in Centos7

Upgrade pip and install jupyter

```
sudo yum update -y
sudo pip install --upgrade pip
pip install jupyter
```

If want force installation in a version of python:

```
python3 -m pip install jupyter
```

View packages installed in Jupyter

```
jupyter --version
```

Generate config files by notebook

```
jupyter notebook --generate-config
```

Path by default: /root/.jupyter/jupyter_notebook_config.py

## Configurate user and security in Jupyter Notebook


