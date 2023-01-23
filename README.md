# microblog
This is a small web blogging application built using the Python web microframework Flask following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) also available on [archive.org](https://web.archive.org/web/20230118004110/https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Stack
* Web - Flask
* Templating - Jinja2
* Database - SQLite
* ORM - SQLAlchemy
* Testing - pytest

Debug SMTP server set up with new instance and command 
```Python
python -m smtpd -n -c DebuggingServer localhost:8025
```