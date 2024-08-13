#!/usr/bin/env bash

rm -rf ./secr
mkdir ./secr
if [ "$VIRTUAL_ENV" == "" ]
then
    echo "No venv found, we activate it !"
    source $HOME/.pyenv/versions/venv_quart/bin/activate
else
    echo "(venv) already activated, just fine !"
fi

# sudo rm -fr dist build *egg*
echo y | pip uninstall my-quart-api
$VIRTUAL_ENV/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
pyb
WHL=$(find -type f -name "*.whl")
pip install ${WHL}  --force-reinstall

{
  echo "ENV=dev"
  echo "PYTHONUNBUFFERED=1"
  echo "SERVER_PORT=10002"
} >> secr/.env




