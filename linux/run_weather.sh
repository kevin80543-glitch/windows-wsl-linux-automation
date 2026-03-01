#!/bin/bash

cd "$(dirname "$0")"

# 使用 venv 內的 python 直接執行
./venv/bin/python test_weather_api.py

