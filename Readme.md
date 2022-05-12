## installation

## Create virtual machine
```bash
python -m venv .env
```

## Activate virtual environment
```bash
source env\scripts\activate
```

## pip install 
```bash
pip install -r requirements.txt
```

## environment variables for database connection
```bash
 set SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://user:password@ip:puerto/db_name
```

## Run
flask run 


## container db
docker run --name pokemon \
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=pokemon \
-e MYSQL_USER=root \
-e MYSQL_PASSWORD=1234 \
-p 3381:3306 \
-d \
mysql/mysql-server:8.0.23

## run script

1.-docker cp  sepomex.sql sepomex:/sepomex.sql

2.-docker exec -it "sepomex" "bash"

## execute 
1.-mysql -u root -p
2.-use sepomex;
3.-source sepomex.sql


## Documentation DB

[Documentation](https://hub.docker.com/r/mysql/mysql-server)



## API Reference

#### POST item

```http
  POST /login
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. |
| `password`| `string` | **Required**. |


#### Get all items

```http
  GET /state/name
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**.|

#### Get item

```http
  GET /suburb_name/suburb
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |


