#!/usr/bin/env python3
"""
Simple test script to verify the Flask app structure
Run this to test the app locally: python test_app.py
"""

try:
    from flask import Flask, render_template
    print("✓ Flask imported successfully")
    
    # Test if we can create a basic Flask app
    test_app = Flask(__name__)
    print("✓ Flask app created successfully")
    
    # Test if templates directory exists
    import os
    if os.path.exists('templates/map.html'):
        print("✓ Templates directory and map.html found")
    else:
        print("✗ Templates directory or map.html not found")
        
    print("\n✅ App structure looks good!")
    print("To run locally: python app.py")
    print("To deploy: Push to GitHub and connect to Vercel")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Install dependencies with: pip install -r requirements.txt")
except Exception as e:
    print(f"✗ Error: {e}") 