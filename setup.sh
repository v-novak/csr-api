#!/usr/bin/env bash
set -eux

virtualenv3 pyenv
source pyenv/bin.activate
pip3 install < requirements.txt

mkdir -p /var/csr_api
openssl rand -hex 32 > /var/csr_api/secret.txt
