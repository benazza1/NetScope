#!/bin/bash

clear

echo "🔥 Installing NetScope..."

pkg update -y >/dev/null 2>&1
pkg install python -y >/dev/null 2>&1

chmod +x netscope.py

echo ""
echo "✅ Installation Complete!"
echo ""
echo "▶ Run Tool:"
echo "python3 netscope.py"
