"""
Runs app.py
"""

from app import app

app.run(debug=True, port=8001, host='localhost')
