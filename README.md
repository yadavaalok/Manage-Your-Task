Manage Your Tasks

Build the Project

-->docker-compose build

Run the Application

-->docker-compose up

Run Test cases

-->docker-compose run --rm app sh -c "python manage.py test"


Steps to setup github actions:

-->login to docker hub and create a new access token

![Screenshot from 2023-08-01 16-52-01](https://github.com/yadavaalok/Manage-Your-Task/assets/40895847/aa9c6e5b-e3a4-40c0-a94d-6107577bc50f)


--> Go to your repo settings and create secrets for dockerhub user and token

Click on the New repository secret

For user , enter your username
For token, paste the access token which you have created in docker hub.

![Screenshot from 2023-08-01 16-56-22](https://github.com/yadavaalok/Manage-Your-Task/assets/40895847/a335a833-f244-473d-abff-6e890b070d21)

