#!/usr/bin/env bash
exec gunicorn -b :5000 segmental_app:app