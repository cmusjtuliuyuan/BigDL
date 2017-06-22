#!/bin/bash
DIR="readthedocs"
if [ ! -d "$DIR" ]
then
  git clone https://github.com/bigdl-project/bigdl-project.github.io.git
  mv bigdl-project.github.io/readthedocs readthedocs
  rm -rf bigdl-project.github.io/ 
fi

python generate_md.py

mkdocs serve