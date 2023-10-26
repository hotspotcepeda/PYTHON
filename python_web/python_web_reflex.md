# Wake up the [Reflex](https://reflex.dev/docs/getting-started/installation/) beast in Windows 10

**1. For `Python` assuming we have the latest stable version Python 3.12.0 - Oct. 2, 2023 [Python download source](https://www.python.org/downloads/source/)**
```
PS C:\Windows\system32> python --version
Python 3.12.0
```
**2. Creating virtual environment [`venv`](https://docs.python.org/3/library/venv.html) by PowerShell admin .**
```
PS C:\PYTHON\python_web\link_bio> python -m venv venvi
PS C:\PYTHON\python_web\link_bio> ls


    Directorio: C:\PYTHON\python_web\link_bio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26/10/2023     16:03                venvi


PS C:\PYTHON\python_web\link_bio>
```
**3. At this point you must have privileges to execute scripts under the Windows PowerShell.**
```
PS C:\PYTHON\python_web\link_bio> Set-ExecutionPolicy Unrestricted -Force
```
**4. Activated virtual environment**
```
PS C:\PYTHON\python_web\link_bio> .\\venvi\Scripts\Activate.ps1
(venvi) PS C:\PYTHON\python_web\link_bio>
```
**5. `Reflex` install by pip**
```
(venvi) PS C:\PYTHON\python_web\link_bio> pip install reflex
Collecting reflex
...

...
Successfully built python-multipart websockets SQLAlchemy
Installing collected packages: wrapt, websockets, watchdog, typing-extensions, sniffio, six, setuptools, redis, pygments, psutil, platformdirs, packaging, mdurl, MarkupSafe, idna, h11, greenlet, colorama, cloudpickle, certifi, bidict, wsproto, sqlalchemy2-stubs, SQLAlchemy, python-multipart, pydantic, markdown-it-py, Mako, jinja2, gunicorn, click, anyio, watchfiles, uvicorn, typer, starlette, sqlmodel, simple-websocket, rich, httpcore, alembic, starlette-admin, python-engineio, httpx, fastapi, python-socketio, reflex
Successfully installed Mako-1.2.4 MarkupSafe-2.1.3 SQLAlchemy-1.4.41 alembic-1.12.0 anyio-4.0.0 bidict-0.22.1 certifi-2023.7.22 click-8.1.7 cloudpickle-2.2.1 colorama-0.4.6 fastapi-0.96.1 greenlet-3.0.1 gunicorn-20.1.0 h11-0.14.0 httpcore-0.17.3 httpx-0.24.1 idna-3.4 jinja2-3.1.2 markdown-it-py-3.0.0 mdurl-0.1.2 packaging-23.2 platformdirs-3.11.0 psutil-5.9.6 pydantic-1.10.13 pygments-2.16.1 python-engineio-4.8.0 python-multipart-0.0.5 python-socketio-5.10.0 redis-4.6.0 reflex-0.2.9 rich-13.6.0 setuptools-68.2.2 simple-websocket-1.0.0 six-1.16.0 sniffio-1.3.0 sqlalchemy2-stubs-0.0.2a35 sqlmodel-0.0.8 starlette-0.27.0 starlette-admin-0.9.0 typer-0.4.2 typing-extensions-4.8.0 uvicorn-0.20.0 watchdog-2.3.1 watchfiles-0.19.0 websockets-10.4 wrapt-1.15.0 wsproto-1.2.0

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(venvi) PS C:\PYTHON\python_web\link_bio>´
```
**6. Update pip by recommendation of notice**
```
(venvi) PS C:\PYTHON\python_web\link_bio> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\python\python_web\link_bio\venvi\lib\site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/47/6a/453160888fab7c6a432a6e25f8afe6256d0d9f2cbd25971021da6491d899/pip-23.3.1-py3-none-any.whl.metadata
  Downloading pip-23.3.1-py3-none-any.whl.metadata (3.5 kB)
Downloading pip-23.3.1-py3-none-any.whl (2.1 MB)
   ---------------------------------------- 2.1/2.1 MB 13.4 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1
Successfully installed pip-23.3.1
(venvi) PS C:\PYTHON\python_web\link_bio>
```

**7. Initializing `Reflex` Project**
```
(venvi) PS C:\PYTHON\python_web\link_bio> reflex init
Info: Overriding config value username with env var USERNAME=YourUser
────────────────────────────────────────────────────────────────────────────────────── Initializing link_bio ───────────────────────────────────────────────────────────────────────────────────────
Warning: The path to the Node binary could not be found. Please ensure that Node is properly installed and added to your system's PATH environment variable.
[16:33:14] Initializing the web directory.                                                                                                                                             console.py:81
Info: Overriding config value username with env var USERNAME=YourUser
           Initializing the app directory.                                                                                                                                             console.py:81
Info: Overriding config value username with env var USERNAME=YourUser
Success: Initialized link_bio
(venvi) PS C:\PYTHON\python_web\link_bio>ls


    Directorio: C:\PYTHON\python_web\link_bio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26/10/2023     16:33                .web
d-----        26/10/2023     16:17                assets
d-----        26/10/2023     16:33                link_bio
d-----        26/10/2023     16:03                venvi
d-----        26/10/2023     16:33                __pycache__
-a----        26/10/2023     16:33             38 .gitignore
-a----        26/10/2023     16:33             71 rxconfig.py


(venvi) PS C:\PYTHON\python_web\link_bio>
```
