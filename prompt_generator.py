#!/usr/bin/env python3
"""
DOS-Style Intelligent Prompt Generator
Using the Ultimate LLM Prompt Engineering Guide

A retro-style command-line tool that generates high-quality prompts
through an interactive menu system.
"""

import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enhanced_editor import EnhancedEditor

# ===== ADD YOUR OPENAI API KEY HERE =====
# Get your key from: https://platform.openai.com/api-keys
# Replace the text below with your actual key (starts with "sk-")
OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual key
# 
# Example: OPENAI_API_KEY = "sk-proj-abcd1234..."
# 
# Leave as "your-openai-api-key-here" to use basic mode (8.0+ quality)
# Add real key for AI-enhanced mode (9.0+ quality)
# ========================================


# Console styling for DOS-like appearance
class DOSStyle:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def draw_box(text: str, width: int = 60):
        """Draw a DOS-style box around text"""
        top_line = "┌" + "─" * (width - 2) + "┐"
        bottom_line = "└" + "─" * (width - 2) + "┘"
        
        lines = [top_line]
        for line in text.split('\n'):
            padded_line = f"│ {line:<{width - 4}} │"
            lines.append(padded_line)
        lines.append(bottom_line)
        
        return '\n'.join(lines)
    
    @staticmethod
    def progress_bar(current: int, total: int, width: int = 40):
        """Show a progress bar"""
        filled = int(width * current / total)
        bar = "█" * filled + "░" * (width - filled)
        percentage = int(100 * current / total)
        return f"[{bar}] {percentage}%"
    
    @staticmethod
    def pause():
        """DOS-style pause"""
        input("\nPress Enter to continue...")


@dataclass
class UserRequirements:
    """Store collected user requirements"""
    task_type: str = ""
    target_model: str = ""
    domain: str = ""
    complexity: str = ""
    audience: str = ""
    output_format: str = ""
    format_style: str = ""  # New format requirement
    creativity: str = ""
    safety_level: str = ""
    specific_needs: str = ""
    session_id: str = ""


class DOSInterface:
    """Main DOS-style interface handler"""
    
    def __init__(self):
        self.requirements = UserRequirements()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.requirements.session_id = self.session_id
        self.enhanced_editor = EnhancedEditor()
        self.last_requirements = None  # Store for rerun functionality
    
    def show_header(self):
        """Display the main header"""
        header_text = """INTELLIGENT PROMPT GENERATOR v1.0
Powered by Ultimate LLM Guide
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
        
        print(DOSStyle.draw_box(header_text, 65))
        print()
    
    def show_menu(self, title: str, options: List[str], show_back: bool = False) -> int:
        """Display a menu and get user selection"""
        DOSStyle.clear_screen()
        self.show_header()
        
        print(f"╔══ {title.upper()} ══")
        print("║")
        
        for i, option in enumerate(options, 1):
            print(f"║ [{i}] {option}")
        
        if show_back:
            print(f"║ [0] ← Back")
        
        print("║")
        print("╚" + "═" * (len(title) + 6))
        print()
        
        while True:
            try:
                max_choice = len(options)
                min_choice = 0 if show_back else 1
                
                choice = input(f"Enter choice ({min_choice}-{max_choice}): ").strip()
                
                if not choice:
                    continue
                
                choice_num = int(choice)
                if min_choice <= choice_num <= max_choice:
                    return choice_num
                else:
                    print(f"Invalid choice. Please enter {min_choice}-{max_choice}")
            except ValueError:
                print("Please enter a valid number")
    
    def get_multiline_input(self, prompt: str) -> str:
        """Get multiline input with enhanced editor"""
        DOSStyle.clear_screen()
        self.show_header()
        
        return self.enhanced_editor.get_enhanced_multiline_input(prompt)
    
    def show_progress(self, step: str, current: int, total: int):
        """Show progress during generation"""
        DOSStyle.clear_screen()
        self.show_header()
        
        progress_text = f"""GENERATING YOUR PROMPT...

Current Step: {step}

{DOSStyle.progress_bar(current, total)}

Please wait..."""
        
        print(DOSStyle.draw_box(progress_text, 50))
        time.sleep(1)  # Simulate processing time
    
    def show_success(self, filename: str, generated_prompt=None):
        """Show success message with detailed information"""
        DOSStyle.clear_screen()
        self.show_header()
        
        # Basic success info
        success_text = f"""✓ SUCCESS!

Your optimized prompt has been generated!

File saved as: {filename}

The prompt includes:
• Optimized techniques selection
• Model-specific adaptations  
• Usage instructions
• Quality assessment
• Example test cases"""
        
        print(DOSStyle.draw_box(success_text, 55))
        
        # Show detailed information if available
        if generated_prompt:
            self._show_detailed_results(generated_prompt)
        
        # Add rerun options
        return self._show_rerun_options()
    
    def _show_detailed_results(self, generated_prompt):
        """Show detailed generation results"""
        print("\n" + "=" * 70)
        print("📊 GENERATION DETAILS")
        print("=" * 70)
        
        # Quality and techniques
        print(f"Quality Score: {generated_prompt.quality_score:.1f}/10")
        print(f"Techniques Applied: {len(generated_prompt.techniques_used)}")
        print()
        
        # Show techniques used
        print("🔧 Techniques Successfully Integrated:")
        for i, technique in enumerate(generated_prompt.techniques_used, 1):
            print(f"  {i}. {technique.replace('_', ' ').title()}")
        print()
        
        # Show reasoning
        print("🧠 Why These Techniques Were Selected:")
        for tech, reason in list(generated_prompt.reasoning.items())[:3]:  # Show first 3
            print(f"  • {tech.replace('_', ' ').title()}: {reason}")
        if len(generated_prompt.reasoning) > 3:
            print(f"  • ... and {len(generated_prompt.reasoning) - 3} more reasons")
        print()
        
        # Show generated prompt preview
        print("🎯 Generated Prompt Preview:")
        print("-" * 50)
        preview = generated_prompt.prompt_text[:400] + "..." if len(generated_prompt.prompt_text) > 400 else generated_prompt.prompt_text
        print(preview)
        print("-" * 50)
        
        # Show what was sent to OpenAI if AI was used
        if generated_prompt.used_ai_generation and generated_prompt.meta_prompt_sent:
            print()
            print("📤 WHAT WAS SENT TO OPENAI GPT-4:")
            print("=" * 70)
            self._show_meta_prompt_summary(generated_prompt.meta_prompt_sent)
        elif not generated_prompt.used_ai_generation:
            print()
            print("💡 Used Basic Generation Mode (No OpenAI API)")
    
    def _show_meta_prompt_summary(self, meta_prompt: str):
        """Show key parts of what was sent to OpenAI"""
        lines = meta_prompt.split('\n')
        
        # Show requirements section
        in_requirements = False
        in_techniques = False
        requirements_lines = []
        techniques_lines = []
        
        for line in lines:
            if "## User Requirements" in line:
                in_requirements = True
                requirements_lines.append(line)
            elif "## Required Techniques to Integrate" in line:
                in_requirements = False
                in_techniques = True
                techniques_lines.append(line)
            elif line.startswith("## ") and in_techniques:
                in_techniques = False
            elif in_requirements and line.strip():
                requirements_lines.append(line)
            elif in_techniques and line.strip():
                techniques_lines.append(line)
        
        print("📋 Requirements Sent to GPT-4:")
        for line in requirements_lines[:8]:  # Show first 8 lines
            print(f"  {line}")
        print()
        
        print("🔧 Techniques Sent to GPT-4:")
        for line in techniques_lines[:7]:  # Show technique section
            print(f"  {line}")
        print()
        
        print("📝 Full Meta-Prompt Length:", len(meta_prompt), "characters")
        print("🎯 GPT-4 was instructed to integrate all techniques seamlessly")
    
    def _show_rerun_options(self):
        """Show options to rerun or exit after success"""
        print("\n" + "=" * 70)
        print("🎯 WHAT WOULD YOU LIKE TO DO NEXT?")
        print("=" * 70)
        
        rerun_options = [
            "🔄 Generate Another Prompt - Use the same configuration again",
            "✏️ Modify Requirements - Change some settings and regenerate", 
            "🆕 Start Fresh - Completely new prompt requirements",
            "✅ Exit - I'm satisfied with this prompt"
        ]
        
        choice = self.show_menu("Choose Next Action", rerun_options, show_back=False)
        
        return choice  # Return the choice to the main function


class RequirementsCollector:
    """Handle collection of user requirements through DOS menus"""
    
    def __init__(self, dos_interface: DOSInterface):
        self.dos = dos_interface
        self.requirements = dos_interface.requirements
    
    def collect_all_requirements(self) -> UserRequirements:
        """Main collection workflow"""
        
        # Task Type Selection
        task_options = [
            "Classification - Categorize or label inputs",
            "Analysis - Analyze and interpret information",
            "Generation - Create new content or text",
            "Reasoning - Solve problems through logical thinking",
            "Coding - Generate or debug code",
            "Creative - Creative writing, brainstorming, ideation",
            "Question Answering - Answer questions based on context",
            "Summarization - Condense information into summaries",
            "Extraction - Extract specific information from text"
        ]
        
        choice = self.dos.show_menu("Select Task Type", task_options)
        self.requirements.task_type = task_options[choice - 1].split(' - ')[0].lower()
        
        # Target Model Selection
        model_options = [
            "GPT-4 - OpenAI's most capable model",
            "GPT-3.5 Turbo - Fast and cost-effective",
            "Claude-3 - Anthropic's latest with great reasoning",
            "Claude-3 Haiku - Fast and efficient",
            "Llama-2 - Meta's open-source model",
            "Any Model - Optimized for cross-model compatibility"
        ]
        
        choice = self.dos.show_menu("Select Target Model", model_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()  # Go back
        
        self.requirements.target_model = model_options[choice - 1].split(' - ')[0].lower().replace(' ', '-')
        
        # Domain Selection
        domain_options = [
            "Healthcare - Medical, clinical, health analysis",
            "Legal - Law, contracts, compliance",
            "Finance - Banking, investments, analysis",
            "Education - Teaching, learning, academic",
            "Technology - Software, engineering, IT",
            "Business - Management, strategy, operations",
            "Creative - Arts, writing, design",
            "Science - Research, data analysis",
            "General - No specific domain"
        ]
        
        choice = self.dos.show_menu("Select Domain", domain_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.domain = domain_options[choice - 1].split(' - ')[0].lower()
        
        # Complexity Level
        complexity_options = [
            "Simple - Basic tasks, straightforward requirements",
            "Moderate - Multi-step processes, some complexity",
            "Complex - Advanced reasoning, multiple constraints",
            "Expert - Highly sophisticated, domain expertise needed"
        ]
        
        choice = self.dos.show_menu("Select Complexity Level", complexity_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.complexity = complexity_options[choice - 1].split(' - ')[0].lower()
        
        # Target Audience
        audience_options = [
            "Beginner - New to the topic",
            "Intermediate - Some experience",
            "Expert - Domain professional",
            "Mixed - Various skill levels"
        ]
        
        choice = self.dos.show_menu("Select Target Audience", audience_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.audience = audience_options[choice - 1].split(' - ')[0].lower()
        
        # Output Format
        format_options = [
            "Structured - Organized with clear sections",
            "JSON - Machine-readable structured data",
            "Markdown - Formatted text with headers",
            "Code - Programming language output",
            "Prose - Natural flowing text",
            "Creative - Artistic or expressive format"
        ]
        
        choice = self.dos.show_menu("Select Output Format", format_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.output_format = format_options[choice - 1].split(' - ')[0].lower()
        
        # Format Style Selection
        format_style_options = [
            "Table - Organized in rows and columns",
            "Paragraph - Continuous prose format", 
            "Bullet Points - Listed items with bullets",
            "Short Para - Brief paragraphs with headers",
            "Numbered List - Sequential numbered items",
            "Outline - Hierarchical structure with indentation",
            "Q&A Format - Question and answer pairs",
            "Step-by-Step - Sequential instructions",
            "Comparison - Side-by-side format",
            "Summary Points - Key highlights format"
        ]
        
        choice = self.dos.show_menu("Select Format Style", format_style_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.format_style = format_style_options[choice - 1].split(' - ')[0].lower()
        
        # Creativity Level
        creativity_options = [
            "Conservative - Stick to established patterns",
            "Balanced - Mix of standard and creative approaches",
            "Creative - Encourage innovative solutions",
            "Highly Creative - Maximum innovation and originality"
        ]
        
        choice = self.dos.show_menu("Select Creativity Level", creativity_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.creativity = creativity_options[choice - 1].split(' - ')[0].lower()
        
        # Safety Level
        safety_options = [
            "Standard - Basic safety considerations",
            "High - Strict safety and ethical guidelines",
            "Critical - Maximum safety for sensitive domains"
        ]
        
        choice = self.dos.show_menu("Select Safety Level", safety_options, show_back=True)
        if choice == 0:
            return self.collect_all_requirements()
        
        self.requirements.safety_level = safety_options[choice - 1].split(' - ')[0].lower()
        
        # Additional Requirements
        specific_needs = self.dos.get_multiline_input(
            "Describe any specific requirements or constraints:"
        )
        self.requirements.specific_needs = specific_needs
        
        return self.requirements
    
    def show_summary(self) -> bool:
        """Show collected requirements summary and confirm"""
        DOSStyle.clear_screen()
        self.dos.show_header()
        
        summary_text = f"""REQUIREMENTS SUMMARY

Task Type: {self.requirements.task_type.title()}
Target Model: {self.requirements.target_model.title()}
Domain: {self.requirements.domain.title()}
Complexity: {self.requirements.complexity.title()}
Audience: {self.requirements.audience.title()}
Output Format: {self.requirements.output_format.title()}
Creativity: {self.requirements.creativity.title()}
Safety Level: {self.requirements.safety_level.title()}

Additional Requirements:
{self.requirements.specific_needs[:100]}{'...' if len(self.requirements.specific_needs) > 100 else ''}"""
        
        print(DOSStyle.draw_box(summary_text, 70))
        print()
        
        confirm_options = [
            "✓ Generate Prompt - Looks good, let's proceed!",
            "✏️ Edit Additional Requirements - Modify specific requirements",
            "✗ Start Over - I want to change everything"
        ]
        
        choice = self.dos.show_menu("Confirm Requirements", confirm_options)
        
        if choice == 1:
            return True  # Generate prompt
        elif choice == 2:
            # Edit additional requirements
            DOSStyle.clear_screen()
            self.dos.show_header()
            
            current_needs = self.requirements.specific_needs or ""
            edited_needs = self.dos.enhanced_editor.get_enhanced_multiline_input(
                "Edit your additional requirements:",
                current_needs
            )
            self.requirements.specific_needs = edited_needs
            
            # Show updated summary
            return self.show_summary()
        else:
            return False  # Start over


def main():
    """Main application entry point"""
    
    try:
        # Initialize interface
        dos_interface = DOSInterface()
        collector = RequirementsCollector(dos_interface)
        
        # Welcome screen
        DOSStyle.clear_screen()
        dos_interface.show_header()
        
        welcome_text = """Welcome to the Intelligent Prompt Generator!

This tool will guide you through creating optimized
prompts using advanced prompt engineering techniques.

The generator uses the Ultimate LLM Prompt Engineering
Guide to select the best techniques for your specific
needs and target model.

🔹 WITH OpenAI API: Get 9.0+ quality AI-generated prompts
🔹 WITHOUT API: Get 8.0+ quality rule-based prompts

Ready to create an amazing prompt?"""
        
        print(DOSStyle.draw_box(welcome_text, 65))
        DOSStyle.pause()
        
        # Main workflow loop
        while True:
            # Main generation loop with rerun capability
            while True:
                # Collect requirements (or reuse last ones)
                if dos_interface.last_requirements is None:
                    requirements = collector.collect_all_requirements()
                    
                    # Show summary and confirm
                    if not collector.show_summary():
                        continue  # Go back to requirements collection
                    
                    # Store requirements for potential rerun
                    dos_interface.last_requirements = requirements
                else:
                    # Reuse last requirements
                    requirements = dos_interface.last_requirements
                    print("🔄 Using previous configuration...")
                
                # Generate and show prompt
                next_action = generate_and_show_prompt(dos_interface, requirements)
                
                if next_action == 1:  # Generate another with same config
                    # Update session ID for new generation
                    requirements.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
                    continue
                elif next_action == 2:  # Modify requirements
                    dos_interface.last_requirements = None  # Clear stored requirements
                    break  # Break to requirements collection
                elif next_action == 3:  # Start fresh
                    dos_interface.last_requirements = None
                    break
                else:  # Exit
                    return
                    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return
    except Exception as e:
        print(f"\nUnexpected error in main: {e}")
        return


def generate_and_show_prompt(dos_interface, requirements):
    """Generate prompt and show success screen, return next action choice"""
    
    # Show generation progress
    dos_interface.show_progress("Analyzing requirements...", 1, 5)
    dos_interface.show_progress("Selecting techniques...", 2, 5)
    dos_interface.show_progress("Generating prompt...", 3, 5)
    dos_interface.show_progress("Optimizing output...", 4, 5)
    dos_interface.show_progress("Creating documentation...", 5, 5)
    
    # Import here to avoid circular imports
    from llm_generator import LLMPromptGenerator
    from output_generator import PromptPackageGenerator, FileManager
    
    try:
        # Initialize generators with API key
        api_key = OPENAI_API_KEY if OPENAI_API_KEY != "your-openai-api-key-here" else None
        llm_generator = LLMPromptGenerator(api_key=api_key)
        output_generator = PromptPackageGenerator()
        
        # Generate the optimized prompt
        generated_prompt = llm_generator.generate_prompt(requirements)
        
        # Create the comprehensive output package
        filename = FileManager.generate_filename(requirements)
        output_generator.create_package(generated_prompt, requirements, filename)
        
        # Show success with detailed information and return next action
        next_action = dos_interface.show_success(filename, generated_prompt)
        return next_action
        
    except Exception as e:
        # Fallback to basic output if generation fails
        task_clean = requirements.task_type.replace(' ', '-')
        domain_clean = requirements.domain.replace(' ', '-') 
        filename = f"{task_clean}-{domain_clean}-prompt-{requirements.session_id}.md"
        
        with open(filename, 'w') as f:
            f.write(f"""# Generated Prompt - {requirements.task_type.title()}

**Generated**: {datetime.now().isoformat()}
**Session**: {requirements.session_id}
**Status**: Basic generation (full system temporarily unavailable)

## Requirements Summary
- Task: {requirements.task_type}
- Model: {requirements.target_model}
- Domain: {requirements.domain}
- Complexity: {requirements.complexity}

## Basic Prompt
You are a {requirements.domain} expert. Your task is to {requirements.task_type} the provided information with {requirements.complexity} level analysis for a {requirements.audience} audience.

Please provide your response in {requirements.output_format} format.

{requirements.specific_needs}

## Note
This is a basic prompt. For full optimization with advanced techniques, ensure all dependencies are available.

Error details: {str(e)}
""")
            print(f"\nNote: Generated basic prompt due to: {e}")
            # Show basic success for fallback mode and return exit choice
            return dos_interface.show_success(filename)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)