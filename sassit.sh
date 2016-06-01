#!/bin/bash
cd $(dirname $0)
mkdir -p gameapp/static/css/
sass gameapp/static/sass/main.scss > gameapp/static/css/main.css
