# 0x1A. Application server

## TASKS

1. __0. Set up development with Python__

***Requirements***

- Install the net-tools package on your server: sudo apt install -y net-tools
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named app

2. __1. Set up production with Gunicorn__

***Requirements***

- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called app.

3. __2. Serve a page with Nginx__

configuring Nginx to serve your page from the route /airbnb-onepage/

File: 2-app_server-nginx_config

***Requirements:***

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as 2-app_server-nginx_config.

4. __3. Add a route with query parameters__

 configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports.

File: 3-app_server-nginx_config

___Requirements:___

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) the process listening on port 5001.
- Include your Nginx config file as 3-app_server-nginx_config.


5. __4. Let's do this for your API__

serve what you built for AirBnB clone v3 - RESTful API on web-01.

___Requirements:___

- Git clone your AirBnB_clone_v3
- Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002
- Nginx must serve this page both locally and on its public IP on port 80
- To test your setup you should bind Gunicorn to api/v1/app.py
- It may be helpful to import your data (and environment variables) from this project
- Upload your Nginx config file as 4-app_server-nginx_config

6. __5. Serve your AirBnB clone__

 serve what you built for AirBnB clone - Web dynamic on web-01.

___Requirements:___

- Git clone your AirBnB_clone_v4
- Your Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003
- Setup Nginx so that the route / points to your Gunicorn instance
- Setup Nginx so that it properly serves the static assets found in web_dynamic/static/ (this is essential for your page to render properly)
- For your website to be fully functional, you will need to reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP
- Nginx must serve this page both locally and on its public IP and port 5003
- Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
- Upload your Nginx config as 5-app_server-nginx_config

