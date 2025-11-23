import sys
import pyfiglet # Import the library for the banner

# Define ANSI color codes for a dashing look
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
def print_fancy_header(title):
    """Prints a styled section header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}>>> {title} <<< {Colors.ENDC}")
    print(f"{Colors.HEADER}---" * 10 + Colors.ENDC)

def handle_exit_choice(choice):
    """Checks if the user chose the exit option."""
    if choice.upper() == 'X':
        print(f"\n{Colors.RED}👋 Program terminated by user. Goodbye!{Colors.ENDC}")
        sys.exit()

def print_banner(text):
    """Prints the text as a large ASCII art banner."""
    # Generate the ASCII art
    banner = pyfiglet.figlet_format(text, font="slant")
    # Print the banner in a striking color
    print(f"{Colors.BLUE}{Colors.BOLD}")
    print("=" * 70)
    print(banner.strip())
    print("=" * 70)
    print(f"{Colors.ENDC}")


def get_user_preferences_dashing():
    # ... [Rest of the get_user_preferences_dashing function remains the same] ...
    
    # --- 1. Color Choice: Simple vs. Gradient ---
    print_fancy_header("🎨 Step 1: CHOOSE YOUR COLOR STYLE")
    
    print(f"{Colors.CYAN}1. Simple Color{Colors.ENDC} (A solid, single hue)")
    print(f"{Colors.CYAN}2. Gradient Color{Colors.ENDC} (A smooth fade between two colors)")
    print(f"{Colors.RED}X. Exit Program{Colors.ENDC}") 

    color_choice = input(f"{Colors.YELLOW}{Colors.BOLD}Enter 1, 2, or X (Color): {Colors.ENDC}").strip()
    handle_exit_choice(color_choice)

    final_color_data = None
    
    if color_choice == '1':
        color_value = input(f"   {Colors.GREEN}Enter Simple Color (e.g., 'Teal' or #008080): {Colors.ENDC}").strip()
        final_color_data = {"type": "Simple", "value": color_value}
        print(f"\n✨ {Colors.BLUE}You selected: Simple Color ({color_value}){Colors.ENDC}")
        
    elif color_choice == '2':
        color_start = input(f"   {Colors.GREEN}Enter Gradient START color (e.g., 'Purple'): {Colors.ENDC}").strip()
        color_end = input(f"   {Colors.GREEN}Enter Gradient END color (e.g., 'Pink'): {Colors.ENDC}").strip()
        final_color_data = {"type": "Gradient", "start": color_start, "end": color_end}
        print(f"\n✨ {Colors.BLUE}You selected: Gradient from {color_start} ➡️ {color_end}{Colors.ENDC}")
        
    else:
        print(f"\n🚨 {Colors.RED}Invalid choice. Defaulting to Simple Color: Gray.{Colors.ENDC}")
        final_color_data = {"type": "Simple", "value": "Gray"}
        
    
    # --- 2. Size Choice: Predefined vs. Custom ---
    print_fancy_header("📏 Step 2: DEFINE THE SIZE")
    
    print(f"{Colors.CYAN}1. Small{Colors.ENDC} (Compact, discreet)")
    print(f"{Colors.CYAN}2. Medium{Colors.ENDC} (Standard, balanced)")
    print(f"{Colors.CYAN}3. Large{Colors.ENDC} (Prominent, spacious)")
    print(f"{Colors.CYAN}4. Custom Size{Colors.ENDC} (Your specific dimensions)")
    print(f"{Colors.RED}X. Exit Program{Colors.ENDC}") 

    size_choice = input(f"{Colors.YELLOW}{Colors.BOLD}Enter 1, 2, 3, 4, or X (Size): {Colors.ENDC}").strip()
    handle_exit_choice(size_choice) 

    final_size_data = None
    
    if size_choice == '1':
        final_size_data = {"type": "Predefined", "value": "Small"}
    elif size_choice == '2':
        final_size_data = {"type": "Predefined", "value": "Medium"}
    elif size_choice == '3':
        final_size_data = {"type": "Predefined", "value": "Large"}
    elif size_choice == '4':
        custom_size = input(f"   {Colors.GREEN}Enter Custom Size (e.g., '800px x 600px'): {Colors.ENDC}").strip()
        final_size_data = {"type": "Custom", "value": custom_size}
    else:
        print(f"\n🚨 {Colors.RED}Invalid choice. Defaulting to Medium.{Colors.ENDC}")
        final_size_data = {"type": "Predefined", "value": "Medium"}
        
    print(f"\n✨ {Colors.BLUE}You selected: {final_size_data['value']}{Colors.ENDC}")

    # --- Summary ---
    return {
        "Color": final_color_data,
        "Size": final_size_data
    }

# --- Execution ---
if __name__ == "__main__":
    # --- BANNER CODE ADDED HERE ---
    print_banner("HACKITON")
    # ------------------------------
    
    preferences = get_user_preferences_dashing()

    print_fancy_header("✅ FINAL SELECTION SUMMARY")

    print(f"{Colors.BOLD}COLOR PREFERENCE:{Colors.ENDC}")
    if preferences['Color']['type'] == 'Simple':
        print(f"  Type: {Colors.GREEN}Simple{Colors.ENDC}")
        print(f"  Value: {Colors.GREEN}{preferences['Color']['value']}{Colors.ENDC} 🎨")
    else:
        print(f"  Type: {Colors.GREEN}Gradient{Colors.ENDC}")
        print(f"  Start: {Colors.GREEN}{preferences['Color']['start']}{Colors.ENDC}")
        print(f"  End: {Colors.GREEN}{preferences['Color']['end']}{Colors.ENDC} 💫")
        
    print(f"\n{Colors.BOLD}SIZE PREFERENCE:{Colors.ENDC}")
    print(f"  Type: {Colors.GREEN}{preferences['Size']['type']}{Colors.ENDC}")
    print(f"  Value: {Colors.GREEN}{preferences['Size']['value']}{Colors.ENDC} 📐")
    print(f"\n{Colors.BOLD}{Colors.HEADER}Configuration Complete!{Colors.ENDC}")

