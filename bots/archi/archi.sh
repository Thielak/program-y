#!/bin/bash
set -eu

export PYTHONPATH=../../src

cd "$(dirname "$(readlink -f "$0")")"
python3 ../../src/programy/clients/rest.py --bot_root . --config config.yaml --cformat yaml --logging logging.yaml
