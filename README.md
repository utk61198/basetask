# basetask


#### The following link has the live demo of the task : https://dashboard-bse.herokuapp.com/


### Technologies used

#### Django
 
The backend of the the dashboard is written in python and the code to download the file can be found in dashboard/views.py. The code downloads the latest bhavcopy file from https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx .
In case of the weekends the bhavcopy file from friday is downloaded and the data is parsed.

#### VueJs
 The front dashboard of the application is made using VueJs componenets. The dashboard consist of a table displaying the Name,Code,Open,High,Low,Close for the stock as published by the bhavcopy.
 The searchbar filters the stock on the basis of the name and the export button downloads the table contents in CSV format.
 
 #### Redis
 For hosting the redis database Heroku Redis has been used.
 
 #### Heroku
 The entire application is hosted on heroku.
 
 
 ### Setup Instructions
 
 #### Step 1
 clone the github repository using git clone https://github.com/utk61198/basetask.git
 
 #### Step 2
 Go into the folder and install virtualenv using python -m venv venv and activate it using venv\Scripts\activate
 
 #### Step 3
 ##### install the packages
 pip install requirements.txt
 
 #### Step 4
 Migrate the changes using python manage.py migrate 
 
 #### Step 5
 Start the application using python manage.py runserver
 
 #### The application will start on http://127.0.0.1:8000/
 
 
 #### Video Demo
 
 [![YouTube link](https://youtu.be/qxFJKGqoCeI/0.jpg)](https://youtu.be/iAP55nR5jHc)
