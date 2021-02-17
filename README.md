# AgroFides Bare Bones API

This repository contains the minimum necessary code to create a web server, update it using a python script, and retrieve information with a GET request.

## Dev Setup

### Clone Repo and build Docker containers
1. Clone repo `git clone git@gitlab.com:agrofides/bare-bones-api.git` and cd into the project
2. Run `docker-compose build` to build the docker containers
3. Run `docker-compose up` to launch the containers

### Initialize DB and import schema
1. In a new terminal run `docker-compose exec api flask db init` to create a new database migration repository

2. Run `docker-compose exec api flask db migrate` to create a new revision

3. Run `docker-compose exec api flask db upgrade` to persist the newly created revision

### Create Roles

1. Run `docker-compose exec api python -m app.bin.setup_roles`.
2. Also change the `enabled` fields on line 24 and do 1 again to show update functionality 

### Get Roles

1. Go to http://localhost:5000/roles to see the created roles

	![Created Roles](images\Created Roles.PNG)
	
	## Other Operations
	
	### Close Server
	
	​	Ctrl+c in flask window
	
	### Delete Database
	
		1. Build docker containers
	 	2. `docker-compose exec api python -m app.bin.nukedb`
	 	3. Initialize DB and import schema
	
	## Key Files
	
	### 	app/models.py 
	
	​	Defined schema for database entry, in this case user accounts
	
	###     app/bin/setuproles.py
	
	​		Script to populate database with user  roles entries
	
	###    app/routes/main_routes.py
	
	​		contains welcome page, error page, and get user roles pages (all and by role id)		


## Links / Reference
* http://www.fao.org/waicent/faostat/agricult/pr_ele-e.htm
