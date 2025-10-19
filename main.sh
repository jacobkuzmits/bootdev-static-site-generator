#!/bin/bash
# Run with local basepath (from config.json)
python3 src/main.py local
cd docs && python3 -m http.server 8888