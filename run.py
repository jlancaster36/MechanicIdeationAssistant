#!/usr/bin/env python3
"""
Enhanced MIA Run Script
Convenient launcher for the Enhanced Mechanic Ideation Assistant
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'requests', 'anthropic', 'python-dotenv']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: python setup.py")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has API keys"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        print("Run: python setup.py")
        return False
    
    try:
        with open(env_file, 'r') as f:
            content = f.read()
        
        if 'your_igdb_client_id_here' in content or 'your_anthropic_api_key_here' in content:
            print("⚠️  Please configure your API keys in .env file")
            print("See README.md for instructions")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Error reading .env file: {e}")
        return False

def launch_app():
    """Launch the Streamlit application"""
    print("🚀 Launching Enhanced MIA...")
    print("The app will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch application: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
        return True
    
    return True

def main():
    """Main run function"""
    print("🎮 Enhanced MIA Launcher")
    print("=" * 30)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment configuration
    if not check_env_file():
        sys.exit(1)
    
    # Launch the application
    launch_app()

if __name__ == "__main__":
    main()
