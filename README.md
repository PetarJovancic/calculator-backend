## Calculator

<img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png"
     alt="Markdown Python icon"
     height="50px"
/>&nbsp;&nbsp;&nbsp;
<img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg"
     alt="Markdown FastAPI icon"
     height="50px"
/>&nbsp;&nbsp;&nbsp;
<img src="https://img.icons8.com/fluency/48/000000/docker.png"
     height="50px"/></span>
&nbsp;&nbsp;&nbsp;

### Introduction

This is a backend app for basic calculator.

### Usage

The app requires an `.env` file with the following variables:

```
ALLOW_ORIGINS=*
ALLOW_CREDENTIALS=True
ALLOW_METHODS=*
ALLOW_HEADERS=*
HOST=0.0.0.0
PORT=8000
RELOAD=True
```

It is advised to work in a virtual environment. Create one using the following command:

```
python3 -m venv venv
```

Activating **venv**:

- Windows OS: `./venv/Scripts/activate`
- Unix/Mac OS: `source venv/bin/activate`

Install the required packages into the newly created venv:

```
pip install -r requirements.txt
```

To start the server run:

```
python run.py
```

To start the tests:

```
pytest -v .
```

### Using Docker

To build Docker container use the following command:

```

docker build -t calculator-backend-app .

```

To run Docker container use the following command:

```

docker run -p 8000:8000 calculator-backend-app

```
