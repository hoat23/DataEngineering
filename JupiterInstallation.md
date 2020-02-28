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

```
#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Allow password to be changed at login for the notebook server.
#
#  While loggin in with a token, the notebook server UI will give the opportunity
#  to the user to enter a new password at the same time that will replace the
#  token login mechanism.
#
#  This can be set to false to prevent changing password from the UI/API.
c.NotebookApp.allow_password_change = True

## Allow requests where the Host header doesn't point to a local server
#
#  By default, requests get a 403 forbidden response if the 'Host' header shows
#  that the browser thinks it's on a non-local domain. Setting this option to
#  True disables this check.
#
#  This protects against 'DNS rebinding' attacks, where a remote web server
#  serves you a page and then changes its DNS to send later requests to a local
#  IP, bypassing same-origin checks.
#
#  Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local, along
#  with hostnames configured in local_hostnames.
#c.NotebookApp.allow_remote_access = False

## Whether to allow the user to run the notebook as root.
c.NotebookApp.allow_root = False

## The IP address the notebook server will listen on.
c.NotebookApp.ip = 'localhost'


## Hostnames to allow as local when allow_remote_access is False.
#
#  Local IP addresses (such as 127.0.0.1 and ::1) are automatically accepted as
#  local as well.
c.NotebookApp.local_hostnames = ['localhost']


## Forces users to use a password for the Notebook server. This is useful in a
#  multi user environment, for instance when everybody in the LAN can access each
#  other's machine through ssh.
#
#  In such a case, server the notebook server on localhost is not secure since
#  any user can connect to the notebook server via ssh.
#c.NotebookApp.password_required = False

## The port the notebook server will listen on.
c.NotebookApp.port = 8888

## The number of additional ports to try if the specified port is not available.
c.NotebookApp.port_retries = 9999

## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
#c.NotebookApp.pylab = 'disabled'

## If True, display a button in the dashboard to quit (shutdown the notebook
#  server).
c.NotebookApp.quit_button = True

```

Documentation: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
