# Mirror-to-do-list

Mirror Todo List

## Run app
```bash
mysql -u root -p # in one terminal
python manage.py runserver # in another terminal
```
http://127.0.0.1:8000/todos/

## Run test
```bash
coverage run manage.py test
```

## Sync database
```bash
python manage.py syncdb
```

## Migrate the database changes
```bash
python manage.py migrate todos
```

## API
### todos/
List all todos

### todos/add  
Add new todo

### todos/details/{id}
Display todo details

### admin/
Login to database admin
username: admin1
email: admin1@gmail
password: admin123
