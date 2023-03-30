#!/bin/bash

#Wait instances
/usr/local/bin/wait

# Run Migrations
python migrations.py

#Run flask
flask run --host=0.0.0.0