#!/usr/bin/env bash
flask db upgrade
python3 -u socket_server.py