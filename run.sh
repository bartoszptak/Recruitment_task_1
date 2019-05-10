#!/bin/bash
docker build -t app .
docker run --rm --name pearson.com -p 5000:5000 -e DARK_SKY_KEY=pearson.com app