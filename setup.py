#!/usr/bin/env python3
"""
Enhanced MIA Setup Script
Automates the setup process for the Enhanced Mechanic Ideation Assistant
"""

import os
import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_environment():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        print("📝 Creating .env file from template...")
        try:
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created successfully")
            print("⚠️  Please edit .env file and add your API keys")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    else:
        print("❌ .env.example file not found")
        return False

def check_api_keys():
    """Check if API keys are configured"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        return False
    
    try:
        with open(env_file, 'r') as f:
            content = f.read()
        
        required_keys = ['IGDB_CLIENT_ID', 'IGDB_CLIENT_SECRET', 'ANTHROPIC_API_KEY']
        missing_keys = []
        
        for key in required_keys:
            if f"{key}=your_" in content or f"{key}=" in content and f"{key}=your_" not in content:
                # Check if it's still the default template value
                if f"{key}=your_" in content:
                    missing_keys.append(key)
        
        if missing_keys:
            print(f"⚠️  Please configure these API keys in .env file: {', '.join(missing_keys)}")
            return False
        else:
            print("✅ API keys appear to be configured")
            return True
    except Exception as e:
        print(f"❌ Error checking API keys: {e}")
        return False

def print_api_instructions():
    """Print instructions for obtaining API keys"""
    print("\n🔑 API KEY SETUP INSTRUCTIONS:")
    print("=" * 50)
    
    print("\n1. IGDB API (Required for game data):")
    print("   • Go to: https://api.igdb.com/")
    print("   • Create an account and register your application")
    print("   • Get your Client ID and Client Secret")
    print("   • Add them to your .env file")
    
    print("\n2. Anthropic Claude API (Required for AI analysis):")
    print("   • Go to: https://www.anthropic.com/")
    print("   • Create an account and get your API key")
    print("   • Add it to your .env file")
    
    print("\n3. Edit your .env file:")
    print("   IGDB_CLIENT_ID=your_actual_client_id")
    print("   IGDB_CLIENT_SECRET=your_actual_client_secret")
    print("   ANTHROPIC_API_KEY=your_actual_api_key")

def main():
    """Main setup function"""
    print("🎮 Enhanced MIA Setup")
    print("=" * 30)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup environment file
    if not setup_environment():
        sys.exit(1)
    
    # Check API keys
    api_keys_configured = check_api_keys()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    
    if not api_keys_configured:
        print_api_instructions()
        print("\n⚠️  Please configure your API keys before running the application")
    
    print("\n🚀 To start the application:")
    print("   streamlit run app.py")
    print("\n📖 For more information, see README.md")

if __name__ == "__main__":
    main()
