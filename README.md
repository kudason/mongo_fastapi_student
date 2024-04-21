> This is a project show how to use [`fastapi`](https://fastapi.tiangolo.com/) framework to create apis for connect to students which is store in a mongo database.
___
### Table of content

1. [Tech stack](https://github.com/kudason/mongo_fastapi_student#Tech-Stack)
2. [Install](https://github.com/kudason/mongo_fastapi_student#Install)
3. [Usage](https://github.com/kudason/mongo_fastapi_student#Usage)
4. [Reference](https://github.com/kudason/mongo_fastapi_student#Reference)
___

## Tech Stack
<div>
  <a href="https://fastapi.tiangolo.com/">
    <img height="32" align="left" alt="fastapi" src="https://github.com/kudason/mongo_fastapi_student/assets/143707562/21b78bfc-f7f2-4591-bcdb-792b26958f5b" />
  </a>
  
  <a href="https://www.mongodb.com/">
    <img height="32" align="left" alt="mongo" src="https://github.com/kudason/mongo_fastapi_student/assets/143707562/6af4cd9f-6dd9-48e1-b879-71e061cfcc86" />
  </a>
  
  <a href="https://www.python.org/">
    <img height="32" align="left" alt="python" src="https://github.com/kudason/mongo_fastapi_student/assets/143707562/3ffff6ff-c146-4bbb-a36c-9b37b1b7773e" />
  </a>
  
  <a href="https://code.visualstudio.com/">
    <img height="32" align="left" alt="vscode" src="https://github.com/kudason/mongo_fastapi_student/assets/143707562/551b34d9-1731-472f-a2c8-ccd15c66b9a8" />
  </a>
</div>

<br>

## Install

`Step 1`: Install python with this link [python download](https://www.python.org/downloads/)

`Step 2`: Install virtualenv with command 
```
pip install virtualenv
```

`Step 3`: Create and activate virtual environment
- Create env:
```
virtualenv your_env_name_here
```
- Activate env:
On windows run:
```
your_env_name\Scripts\activate
```
On Unix/Mac run:
```
source your_env_name/bin/activate
```

`Step 4`: Install necessary dependencies 
```
pip install -r requirements.txt
```

## Usage
1. **Swagger UI**:
- First use command to run `main.py` file:
```
python main.py
```
and this is the result:
![image](https://github.com/kudason/mongo_fastapi_student/assets/143707562/d0817c96-dea5-4a1e-a42f-fc3fda1a1622)

After that access  http://127.0.0.1:5000/docs to open swagger UI which provide by fastapi framework
![image](https://github.com/kudason/mongo_fastapi_student/assets/143707562/b96baa4f-a425-42a2-bb2c-41962c392672)
You can test api by edit each method provide by above UI such as (GET, POST, PUT)

2. **PostMan**
![image](https://github.com/kudason/mongo_fastapi_student/assets/143707562/6b85b604-6a6e-4db6-91e5-c3da068ae323)

## Reference
- [Python FastAPI and PyMongo Tutorials - FunTechs](https://www.youtube.com/playlist?list=PLjBZiVgQGi_1fAuZNSZuVHyl_az_OkWw1)
- [Getting Started with MongoDB and FastAPI](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
