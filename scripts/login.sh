#!/bin/sh -x
curl -X 'POST' \
  'http://localhost:8068/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "scriptuser",
  "password": "password",
  "email": "scriptuser@email.com"
}'
