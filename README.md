# python-file-sharing
File sharing app

To run the server locally python must be installed.
The development version of choice was 3.5

by running the following command:
    python manage.py runserver 8000


The server will start and you access the app through the following URL:
http://127.0.0.1:8000/upload/

There you will have 2 options:
1-"Click here to upload a file"   -->  from here you can upload any file and give it a name
MAX FILE SIZE IS 4GB

2-"Click here to recieve files"  ---> from here you can download the files,
the list of available files is refreshed every 30 seconds
Click any file to immediately download it


------------- OPTIONAL --------------------------
sometimes when migrating to a different enviroment,
database migrations may be required to run the server.
if the above command threw an exception then the following commands should fix it
    python manage.py makemigrations
    python manage.py migrate


------------- OPTIONAL --------------------------
if you desire to delete records,
you can access the django admin via

http://127.0.0.1:8000/admin/


admin credentials:
admin@example.com
naraninc
-----------------------------------------------------

