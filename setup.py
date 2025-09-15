#!/usr/bin/env python3
"""
Quick setup script for the Intelligent Prompt Generator
"""

import os
import sys
import subprocess


def check_python():
    """Check Python version"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.7+")
        return False


def install_openai():
    """Install OpenAI package"""
    print("\n📦 Installing OpenAI package...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "openai"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ OpenAI package installed successfully")
            return True
        else:
            print("❌ Failed to install OpenAI package")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error installing OpenAI: {e}")
        return False


def check_api_key():
    """Check for OpenAI API key"""
    print("\n🔑 Checking for OpenAI API key...")
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        print("✓ OpenAI API key found")
        print("🔥 System will use AI-enhanced generation (9.0+ quality)")
        return True
    else:
        print("⚠️  No OpenAI API key found")
        print("💡 System will use basic generation (8.0+ quality)")
        print("\nTo enable AI-enhanced generation:")
        print("1. Get API key from: https://platform.openai.com/api-keys")
        print("2. Run: export OPENAI_API_KEY='your-key-here'")
        return False


def test_system():
    """Test the system"""
    print("\n🧪 Testing system...")
    try:
        result = subprocess.run([
            sys.executable, "test_generator.py"
        ], capture_output=True, text=True, timeout=30)
        
        if "All tests passed" in result.stdout:
            print("✓ All tests passed")
            return True
        else:
            print("❌ Some tests failed")
            print("Output:", result.stdout[-500:])  # Last 500 chars
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def main():
    """Main setup function"""
    print("🚀 Intelligent Prompt Generator - Setup")
    print("=" * 50)
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Install OpenAI
    if not install_openai():
        print("\n⚠️  OpenAI installation failed, but system will work in basic mode")
    
    # Check API key
    has_api_key = check_api_key()
    
    # Test system
    if test_system():
        print("\n🎉 Setup Complete!")
        print("=" * 50)
        
        if has_api_key:
            print("✅ AI-Enhanced Mode: Ready (9.0+ quality prompts)")
        else:
            print("✅ Basic Mode: Ready (8.0+ quality prompts)")
        
        print("\nNext steps:")
        print("• Run: python3 prompt_generator.py")
        print("• Or try: python3 demo.py")
        
        if not has_api_key:
            print("\n💡 For AI-enhanced mode:")
            print("• Get API key: https://platform.openai.com/api-keys")
            print("• Set key: export OPENAI_API_KEY='your-key'")
    else:
        print("\n❌ Setup encountered issues")
        print("Check the error messages above and try running tests manually:")
        print("python3 test_generator.py")


if __name__ == "__main__":
    main()