#!/usr/bin/env bash
set -eux

cd -- "$( dirname -- "${BASH_SOURCE[0]}" )"

virtualenv pyenv
source ./pyenv/bin/activate
pip3 install -r requirements.txt
deactivate

openssl rand -hex 32 > secret.txt
chmod 600 secret.txt

cd -
