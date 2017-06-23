#!/bin/bash

# Down Load the web theme
THEME="readthedocs"
GITHUBIO="bigdl-project.github.io"
if [ ! -d "$THEME" ]
then
  if [ ! -d "$GITHUBIO" ]
  then
    git clone https://github.com/bigdl-project/bigdl-project.github.io.git
  else
  	cd bigdl-project.github.io
    git pull
    cd ..
  fi
fi
cp -r bigdl-project.github.io/readthedocs readthedocs

# Generate mkdocs.yml
python generate_md.py

# Build the website
mkdocs build

# DownLoad Scala Python api docs
rm -r site/APIdocs/python-api-doc
rm -r site/APIdocs/scaladoc
cp -r bigdl-project.github.io/APIdocs/python-api-doc/ site/APIdocs/
cp -r bigdl-project.github.io/APIdocs/scaladoc/ site/APIdocs/

# Open the web site
sysOS=`uname -s`
if [ $sysOS == "Linux" ]
then
  xdg-open site/index.html
else
  open site/index.html
fi




