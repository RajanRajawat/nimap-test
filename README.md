
Database Configuration
> Using PostgreSQL on local host
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': '48296',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
2> install from requirements.txt all the dependencies
3>make migrations and migrate
4> create a super user
Run django server

Creator users from admin panel
Home page
http://127.0.0.1:8000/accounts/login/ 
And login users from login page
And do api operations


Links
You have to perform the following tasks :
1. Register a client
http://127.0.0.1:8000/api/clients > Post > Working  

2. Fetch clients info
http://127.0.0.1:8000/api/clients > Get > Working

3. Edit/Delete client info
http://127.0.0.1:8000/api/clients/2 >get, Patch Working
http://127.0.0.1:8000/api/clients/2> delete also working

4. Add new projects for a client and assign users to those projects.
http://127.0.0.1:8000/api/clients/2/projects working
5. Retrieve assigned projects to logged-in users.
http://127.0.0.1:8000/api/projects working

