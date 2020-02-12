# Feature Flag Demo

## What it is?

A prototype for showing how we can handle feature change based on feature flag. 

## Tech stack

* Nuxt for frontend, served by Nginx
* FastAPI for backend
* Postgres for database
* Flagr for feature flag
* Docker compose for orchestration

## Architecture

```
Nuxt --(auth)--> FastAPI
                    |
                    # success, check with user id
                    |
                    |------------> Flagr
                    |<------------ 
                    |
                    # receive feature list with enable flag
                    |
Nuxt <---------- FastAPI
# FE save and render
```

## How to run

Make sure you have docker and docker-compose. Run

```bash
$ docker-compose up
```

## Flag

* User Management
    * List User
    * Add User
    * Dashboard (Total and New User)
* Transaction
* Ticketing System
* Server Monitoring