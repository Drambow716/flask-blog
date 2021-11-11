
# Flask Blog


<img src="src/static/blog.png">



## How to run project?

Write following terminal commands to run this project.


- Create .env file in root folder 


```
DATABASE_URL=dialect://username:password@host:port/dbname        

DATABASE_URL=postgresql://postgres:123456@localhost:5432/postgres ## <-- create this string with your own values


```


```sh

    git clone https://github.com/ubeytdemirr/flask-blog

    cd flask-blogs

    ## macos 

     python3 -m venv venv

    ## windows

    py -3 -m venv venv

    ## macos 

    . venv/bin/activate

    ## windows


    venv\Scripts\activate

    pip3 install -r requirements.txt

    python app.py


    * Serving Flask app 'app' (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 128-953-685


```


Go to  http://127.0.0.1:5000/  in your browser!
