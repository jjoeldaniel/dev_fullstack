#!/usr/bin/env bash

if ! [ -d ./venv/ ]; then
	echo "no venv :("
	python3 -m venv venv
	echo "pls activate the venv and run \"pip install -r requirements.txt\""
fi

echo "lets run your app :)"

uvicorn main:app
