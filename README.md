# ToDo

Opportunities:
+ A handy notepad for a to-do list. 
+ You can create, update or delete favorite tasks, specify tags, deadlines and progress status. 
+ The function of changing the task execution status is also implemented.
***
To install via GitHub, run the following commands:
```
git clone https://github.com/NPovashevych/ToDo/tree/develop
git checkout -b develop
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt 
```
***
After installing all the necessary applications, you need to execute the commands to deploy and start the project: 
```
python manage.py migrate
python manage.py runserver
```
