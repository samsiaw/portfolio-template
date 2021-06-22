# portfolio-template

A version of this app is hosted on 
https://mypyanywhere.pythonanywhere.com/

## Running the Project

1. Make sure python is installed on your pc
2. Run:
    
    `git clone https://github.com/samsiaw/portfolio-template.git`

3. Move to the top level project folder *i.e the folder containing manage.py file*

    `cd portfolio-template`
4. Run  `pip install -r requirements.txt` to install project dependencies
5. `python3 manage.py makemigrations portfolio`

>> NOTE: Run all `python manage.py` cmds in the top-level folder

6. If a `no changes detected` message is printed, delete the files `./db.sqlite3 , myweb/__pycache__, portfolio/migrations ` and `portfolio/__pycache__` files/folders. 

    Repeat step 5
    
6. Run `python3 manage.py migrate`

7. To run the web app, run `python manage.py runserver`

8. Visit `http://localhost:8000` or `http://127.0.0.1:8000/` to view app


## Setting Up A Test User

You should notice an `Internal Server Error` message on first running the app.

You would need to set-up a `superuser` to manage the back-end database. 

>>For the purpose of testing, we would use a generic user with username: `test`

1. Stop the server: `Use ctrl-C or cmd-C` whiles server is running in terminal

2. Run: 
    `python manage.py createsuperuser`

3. Type `test` for username and a password and email of your choice. 

...Highly encouraged to type in something for the email to know what goes where how in the web app

4. Rerun the server with `python manage.py runserver`

>> If you created the superuser with username `test`, you should notice the homepage no longer shows `Internal Server Error`

5. `http://localhost:8000/admin` or `http://127.0.0.1:8000/admin` to access the admin page 

6. Type in the username and password used for  `superuser` in step 3.

You should now have access to the models defined for the project

## Adding Documentation

The app's models are divided into:

* Project
* Tool
* Concept
* Owner


### Owner
Owner defines the owner/user whose projects are going to be added.

Multiple registered owners/users are allowed but projects displayed are those of the current owner only. 


#### Setting an owner

To set the current owner:

set the `USERNAME` in `portfolio/views.py` to your desired username


### Project
The project's only required fields are the name of the project and the owner. 

The `show` field in the project determines whether or not a project is visible on the website or not, even if the project has been created. 

The default website also supports a project being *featured* or not. 
>> You could decide not to set any project as featured at all, and the projects page should adapt accordingly.


*Try setting different values for the current user, (i.e first and last name, email,etc..), add a few projects and notice how things*


### Known Errors
Deleting a project doesn't break the website. 

However, the navigation buttons *(i.e Prev and Next)* on single project pages wouldn't work properly.

*User is expected to clear all items in the portfolio info or simply set `show` to False/Off*