![💻YOGA_CLASS_ADMISSION](https://user-images.githubusercontent.com/94188124/207295322-ef4a2622-abd3-475f-8961-16a04f1ff7aa.png)
<h1> Django Based Admission Form </h1><br>
<b> 
<li><a href="#about"> About</a> </li>

 <li><a href="#hosted-solution-link">HostedSolutinLink</a> </li>
 
<li><a href="#technology-used">Technology Used</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#-er-diagram">ER-Diagram</a></li>
<li><a href="#-api-endpoints">API Endpoints</a></li> </b>
<br>
<hr>
<h1>ABOUT</h1>
It is a user registration project. It takes the user's data from the frontend and calls the dajngo REST API in backend which performs basic validation and saves the data in the database.
<br> 
<hr> 
<h1>Hosted Solution Link</h1>
https://amangaur6515.pythonanywhere.com/
<br>
<hr>
<h1>Technology Used</h1>

* Python 
 
* Django 
* Django-rest-framework
* API
* HTML  CSS  JS
* Database: SQLite3

<h1>FEATURES</h1> 
<hr>

* Homepage is a form developed using HTML, CSS, JS. New user can register themself or already registered member can go to log in page.<br>

 ![regForm](https://user-images.githubusercontent.com/94188124/207298030-4b61ba8b-a6e6-4d8f-baea-4e51be282a2a.jpg) <br>
 
 * On clicking register, if user is a new one '/registerapi' is called to save the data to database and then success page is diplayed , from there user can complete the payment of registration. But if user is not new then automatically login page is displayed. <br>
 
![registrationSuccess](https://user-images.githubusercontent.com/94188124/207299591-b24a6717-c8a3-4ffa-8032-583164ae48dc.jpg)
![login](https://user-images.githubusercontent.com/94188124/207299610-86854564-2b66-48e2-8185-70a0d3c7001e.jpg)
<br> 
* User can login with the mobile number provided at the time of registration, if mobile matches with the database then the corresponding member instance is displayed via '/member/<id>/' API endpoint. <br>
  ![getMemberById](https://user-images.githubusercontent.com/94188124/207300711-e2f8b4bf-1eeb-4123-86bc-37785bb81049.jpg)
<br>

  <h1>INSTALLATION</h1> 
    <hr>
    Python, Django , django-rest-framework need to be installed <br>
    From the terminal enter the command: py manage.py runserver <br>
    App will be started at port 8000 
  
  <h1> ER-DIAGRAM</h1>
  
![ER_yogaClass](https://user-images.githubusercontent.com/94188124/207302217-fe2306dd-df35-4433-86b1-9ef5b8596578.jpg)
<br>
<hr>

  <h1> API ENDPOINTS</h1>
  
Action       |        URL          | Usage                                  |
------------ | ------------------- | -------------------------------------|
GET           |      /member/         | To List all the members registered| 
GET           |    /member/id/       | To get a member with ID |
POST         |   /regsiterapi/        | To register a new member |

<br> 
<hr>


