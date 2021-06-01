# Lesson 2, 3

## Start flask app
```
python wsgi.py
```


## Working with sqlite database

### Creation migrations folder
```
flask db init
```

### Create migration
(this command does not make any changes to the DB, it just generates the migration script)
```
flask db migrate -m "some message"
```

### Apply migrations to the database
```
flask db upgrade
```

### Insert data in database
```
python src/database/inserts.py
```

### Connect to the sqlite3 database
```
sqlite3 data/db.sqlite3
```
