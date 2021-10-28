# GPIO_Control_Via_Webpage
HTML page setup on raspberry pi to control the GPIO pins of rPi using the HTML page. Authentication of the user registration of user.
We want to control the GPIO of Raspbery Pi using the HTML page. 
So the webserver is running on raspberry pi.
Python flask module is used to create the HTML page to control the GPIO pins of raspberry pi. 
Now we need the authentication page to make sure only allowed user can access the raspberry pi GPIO.

gpio_ctrl.py implements the python flask module with sqlalchemy to register and authenticate and control the gpio pins of raspberry pi.

