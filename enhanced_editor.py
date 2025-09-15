#!/usr/bin/env python3
"""
Enhanced Requirements Editor with better editing capabilities
"""

import os
import sys
import tempfile
import subprocess
from typing import Optional


class EnhancedEditor:
    """Enhanced text editor for requirements input"""
    
    def __init__(self):
        self.history = []  # For undo functionality
        self.clipboard = ""  # Simple clipboard simulation
    
    def get_enhanced_multiline_input(self, prompt: str, initial_text: str = "") -> str:
        """Enhanced multiline input with better editing capabilities"""
        
        print("╔══ ENHANCED REQUIREMENTS EDITOR ══")
        print("║")
        print(f"║ {prompt}")
        print("║")
        print("║ 📝 EDITING OPTIONS:")
        print("║   • Type normally and press Enter for new lines")
        print("║   • Type 'CLEAR' to clear all text")
        print("║   • Type 'UNDO' to undo last change")
        print("║   • Type 'EDIT' to open in external editor")
        print("║   • Type 'PASTE' to paste from clipboard simulation")
        print("║   • Type 'DONE' when finished")
        print("║")
        print("╚" + "═" * 35)
        print()
        
        if initial_text:
            print("📄 Current content:")
            print("-" * 30)
            print(initial_text)
            print("-" * 30)
            print()
        
        return self._interactive_edit_loop(initial_text)
    
    def _interactive_edit_loop(self, initial_text: str) -> str:
        """Interactive editing loop with commands"""
        
        current_text = initial_text
        self.history = [current_text]  # Initialize history
        
        print("💡 Start typing (or use commands like CLEAR, UNDO, EDIT, DONE):")
        print()
        
        lines = current_text.split('\n') if current_text else []
        
        while True:
            try:
                # Show current content if it exists
                if lines:
                    print("📝 Current content:")
                    for i, line in enumerate(lines, 1):
                        print(f"  {i:2d}: {line}")
                    print()
                
                user_input = input("✏️  Enter text (or command): ").strip()
                
                if user_input.upper() == "DONE":
                    final_text = '\n'.join(lines)
                    print(f"\n✅ Content saved ({len(final_text)} characters)")
                    return final_text
                
                elif user_input.upper() == "CLEAR":
                    if self._confirm_action("Clear all text"):
                        self._save_to_history(lines)
                        lines = []
                        print("🗑️  All text cleared")
                
                elif user_input.upper() == "UNDO":
                    if len(self.history) > 1:
                        self.history.pop()  # Remove current state
                        restored_text = self.history[-1]
                        lines = restored_text.split('\n') if restored_text else []
                        print("↶  Undo successful")
                    else:
                        print("❌ Nothing to undo")
                
                elif user_input.upper() == "EDIT":
                    current_content = '\n'.join(lines)
                    edited_content = self._open_external_editor(current_content)
                    if edited_content is not None:
                        self._save_to_history(lines)
                        lines = edited_content.split('\n')
                        print("📝 External edit complete")
                
                elif user_input.upper() == "PASTE":
                    paste_content = self._simulate_paste()
                    if paste_content:
                        self._save_to_history(lines)
                        lines.extend(paste_content.split('\n'))
                        print(f"📋 Pasted {len(paste_content)} characters")
                
                elif user_input.upper() == "HELP":
                    self._show_help()
                
                elif user_input.upper().startswith("DELETE "):
                    try:
                        line_num = int(user_input.split()[1]) - 1
                        if 0 <= line_num < len(lines):
                            self._save_to_history(lines)
                            deleted = lines.pop(line_num)
                            print(f"🗑️  Deleted line {line_num + 1}: '{deleted}'")
                        else:
                            print(f"❌ Line {line_num + 1} doesn't exist")
                    except (IndexError, ValueError):
                        print("❌ Usage: DELETE <line_number>")
                
                elif user_input.upper().startswith("INSERT "):
                    try:
                        parts = user_input.split(' ', 2)
                        line_num = int(parts[1]) - 1
                        text_to_insert = parts[2] if len(parts) > 2 else ""
                        if 0 <= line_num <= len(lines):
                            self._save_to_history(lines)
                            lines.insert(line_num, text_to_insert)
                            print(f"➕ Inserted at line {line_num + 1}")
                        else:
                            print(f"❌ Invalid line number {line_num + 1}")
                    except (IndexError, ValueError):
                        print("❌ Usage: INSERT <line_number> <text>")
                
                elif user_input:
                    # Regular text input
                    self._save_to_history(lines)
                    lines.append(user_input)
                
                print()  # Add spacing
                
            except KeyboardInterrupt:
                print("\n\n🛑 Editor interrupted")
                if self._confirm_action("Exit without saving"):
                    return ""
                print("Continuing...")
            except EOFError:
                print("\n\n💾 Auto-saving content...")
                return '\n'.join(lines)
    
    def _save_to_history(self, lines: list):
        """Save current state to history for undo"""
        current_content = '\n'.join(lines)
        self.history.append(current_content)
        # Keep only last 10 states
        if len(self.history) > 10:
            self.history.pop(0)
    
    def _confirm_action(self, action: str) -> bool:
        """Confirm destructive actions"""
        response = input(f"❓ {action}? (y/N): ").strip().lower()
        return response in ['y', 'yes']
    
    def _open_external_editor(self, content: str) -> Optional[str]:
        """Open external text editor"""
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write(content)
                temp_path = f.name
            
            # Try to open with system editor
            editor = os.environ.get('EDITOR', 'nano')  # Default to nano
            
            try:
                subprocess.run([editor, temp_path], check=True)
                
                # Read back the edited content
                with open(temp_path, 'r') as f:
                    edited_content = f.read()
                
                return edited_content
                
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"❌ Could not open editor '{editor}'")
                print("💡 Try setting EDITOR environment variable or install nano")
                return None
            
            finally:
                # Clean up temp file
                try:
                    os.unlink(temp_path)
                except:
                    pass
                    
        except Exception as e:
            print(f"❌ External editor error: {e}")
            return None
    
    def _simulate_paste(self) -> str:
        """Simulate paste functionality"""
        print("📋 PASTE SIMULATION:")
        print("(In a real implementation, this would paste from clipboard)")
        print("For now, enter the text you want to 'paste':")
        print("Type 'CANCEL' to cancel pasting")
        print()
        
        paste_lines = []
        while True:
            line = input("Paste> ")
            if line.upper() == "CANCEL":
                return ""
            if line.upper() == "END":
                break
            paste_lines.append(line)
        
        return '\n'.join(paste_lines)
    
    def _show_help(self):
        """Show help for editor commands"""
        help_text = """
╔══ EDITOR HELP ══
║ 
║ COMMANDS:
║   DONE              - Finish editing and save
║   CLEAR             - Clear all text  
║   UNDO              - Undo last change
║   EDIT              - Open in external editor (nano/vim/etc)
║   PASTE             - Paste text (simulated)
║   DELETE <line#>    - Delete specific line
║   INSERT <line#> <text> - Insert text at line
║   HELP              - Show this help
║
║ SHORTCUTS:
║   Ctrl+C            - Exit (with confirmation)
║   Enter             - Add new line
║
╚════════════════════
"""
        print(help_text)


def test_enhanced_editor():
    """Test the enhanced editor"""
    editor = EnhancedEditor()
    
    print("🧪 TESTING ENHANCED EDITOR")
    print("=" * 40)
    
    result = editor.get_enhanced_multiline_input(
        "Enter your requirements (test mode):",
        "Sample initial text\nWith multiple lines"
    )
    
    print("\n" + "=" * 40)
    print("📄 FINAL RESULT:")
    print(result)


if __name__ == "__main__":
    test_enhanced_editor()