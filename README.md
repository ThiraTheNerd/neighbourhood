# Community Management System
#### A platform to help you stay informed, connected, and empowered in your community

##  Overview
Stay connected to your community with our innovative web portal. Get the latest news and updates from your neighborhood, discover local businesses, and connect with their owners. Our platform simplifies various manual processes, making it easier for you to stay informed and engaged with your community.

## Core Features

![admin](https://img.shields.io/badge/admin-login-teal.svg?style=flat-square) 
![search](https://img.shields.io/badge/seacrh-books-yellowgreen.svg?style=flat-square)
![issue](https://img.shields.io/badge/issue-books-ff69b4.svg?style=flat-square)
![member](https://img.shields.io/badge/add-member-dodgerblue.svg?style=flat-square) 
![add](https://img.shields.io/badge/add-books-orange.svg?style=flat-square) 

- **Searching** of books
- **Issuing** and **returning** books
- Check fines(if any)
- Librarian can read information about any member
- Librarian can track the books issued by a particular student
- Librarian can **add/remove any member**(student).
- Librarian can **add/delete books**
- Librarian can update the availability status of the books

## Additional Features

**Admin Dashboard** deal with the following : 

- Displaying all members records.

- Displaying all books records.

- Update Book Records.

- Delete Book Records

- Add Book Records

- Add Member/Student Records

- Delete Member/Student Records

- Update Member/Student Records.

## Modules

- Admin login
- Search Books
- Add and Update Books
- Add and Remove Members
- Issue Books

## Technology Stack Used

![HTML](https://img.shields.io/badge/frontend-html-orange.svg?logo=html5&style=flat-square) 
![CSS](https://img.shields.io/badge/frontend-css-yellowgreen.svg?logo=css3&style=flat-square)
![JavaScript](https://img.shields.io/badge/frontend-js-ff69b4.svg?logo=javascript&style=flat-square)
![PHP](https://img.shields.io/badge/backend-php-blue.svg?logo=php&style=flat-square) 
![MYSQL](https://img.shields.io/badge/database-mysql-lightgray.svg?logo=mysql&logoColor=white&style=flat-square) 

- Front End - **HTML**, **CSS**, **JavaScript**
- Back End - **PHP**
- Database - **MySql**

## Requirements

[![PHP](https://img.shields.io/static/v1.svg?label=Source%20Code&message=php&logo=php&style=social)](https://vinitshahdeo.github.io/Library-Management-System/)

The source code of this project is written in **PHP**. So, you'll require **WAMP/XAMPP/MAMP** to run this project.

## Installing 

[![wamp](https://img.shields.io/badge/wamp-server-red.svg?style=flat-square)](http://www.wampserver.com/en/) [![xampp](https://img.shields.io/badge/xampp-server-blue.svg?style=flat-square)](https://www.apachefriends.org/download.html) [![mamp](https://img.shields.io/badge/mamp-server-lightgrey.svg?style=flat-square)](https://www.mamp.info/en/)

- Download [WAMP](http://www.wampserver.com/en/)
- Download [XAMPP](https://www.apachefriends.org/download.html)
- Download [MAMP](https://www.mamp.info/en/)

## How to run?
## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation  
To get the project follow these steps:

##### Cloning the repository:  
 ```bash 
https://github.com/ThiraTheNerd/neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighbourhood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
``` 
 ##### Setup Database
 Create a .env file and fill in the configurations for your database and application.
 python manage.py makemigrations hoodapp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug
## Contact Information   
If you have any question or contributions, please email me at [thiragithinji@gmail.com] 

## License 
* Copyright (c) 2021 **ThiraTheNerd**
