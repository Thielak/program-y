#!/bin/bash
set -eu

export PYTHONPATH=../../src

cd "$(dirname "$(readlink -f "$0")")"

exec python3 ../../src/programy/clients/console.py --bot_root . --config config.yaml --cformat yaml --logging logging.yaml --debug
