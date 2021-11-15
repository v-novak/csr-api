#!/usr/bin/env python3

import os

BASE_PORT=8000
DEBUG=False

def server_settings():
    if DEBUG:
        secret_path = 'data/secret.txt'
    else:
        secret_path = '/opt/csr_api/secret.txt'

    return {
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'cookie_secret': open(secret_path, 'r').read(),
        'login_url': '/login',
        'xsrf_cookies': True
    }
