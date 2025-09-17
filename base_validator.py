"""
Base Number Validator
A Python program to validate whether a string represents a valid number in a given base (2-36).

Compatible with VS Code and can be run directly.
"""

def is_valid_base_number(number_string, base):
    """
    Determine whether a string representing a number is valid in the given base.
    
    Args:
        number_string (str): The string representing the number to validate
        base (int): The base to validate against (2-36)
    
    Returns:
        bool: True if the number is valid in the given base, False otherwise
    
    Raises:
        ValueError: If base is not between 2 and 36
    """
    # Validate base range
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    # Handle empty string
    if not number_string:
        return False
    
    # Convert to uppercase for case-insensitive comparison
    number_string = number_string.upper()
    
    # Check each character in the string
    for char in number_string:
        # Get the digit value of the character
        if char.isdigit():
            digit_value = int(char)
        elif char.isalpha() and 'A' <= char <= 'Z':
            # A=10, B=11, ..., Z=35
            digit_value = ord(char) - ord('A') + 10
        else:
            # Invalid character (not alphanumeric)
            return False
        
        # Check if digit value is valid for the given base
        if digit_value >= base:
            return False
    
    return True


def show_valid_digits(base):
    """Show what digits are valid for a given base"""
    if base < 2 or base > 36:
        return "Invalid base: must be between 2 and 36"
    
    valid_digits = []
    
    # Add numeric digits (0-9)
    for i in range(min(10, base)):
        valid_digits.append(str(i))
    
    # Add letter digits (A-Z) if base > 10
    if base > 10:
        for i in range(10, base):
            valid_digits.append(chr(ord('A') + i - 10))
    
    return ', '.join(valid_digits)


def main():
    """Main function for interactive usage"""
    print("Base Number Validator")
    print("=" * 30)
    
    while True:
        try:
            # Get user input
            number_input = input("\nEnter a number string (or 'quit' to exit): ").strip()
            
            if number_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            base_input = input("Enter the base (2-36): ").strip()
            base = int(base_input)
            
            # Validate and show result
            is_valid = is_valid_base_number(number_input, base)
            valid_digits = show_valid_digits(base)
            
            print(f"\nResult:")
            print(f"Number: '{number_input}'")
            print(f"Base: {base}")
            print(f"Valid digits for base {base}: {valid_digits}")
            print(f"Is valid: {'Yes' if is_valid else 'No'}")
            
            if not is_valid and number_input:
                # Show which characters are invalid
                invalid_chars = []
                number_upper = number_input.upper()
                for char in number_upper:
                    if char.isdigit():
                        if int(char) >= base:
                            invalid_chars.append(f"'{char}' (value {int(char)})")
                    elif char.isalpha() and 'A' <= char <= 'Z':
                        char_value = ord(char) - ord('A') + 10
                        if char_value >= base:
                            invalid_chars.append(f"'{char}' (value {char_value})")
                    else:
                        invalid_chars.append(f"'{char}' (invalid character)")
                
                if invalid_chars:
                    print(f"Invalid characters/digits: {', '.join(invalid_chars)}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Run some quick tests to verify the function works
    test_cases = [
        ("101", 2, True),
        ("102", 2, False),
        ("ABC", 16, True),
        ("GHI", 16, False),
        ("zZ", 36, True),
    ]
    
    print("Running quick validation tests...")
    all_passed = True
    for number_str, base, expected in test_cases:
        result = is_valid_base_number(number_str, base)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{number_str}' in base {base} -> {result}")
        if result != expected:
            all_passed = False
    
    if all_passed:
        print("All tests passed! ✓")
        print()
        # Start interactive mode
        main()
    else:
        print("Some tests failed! ✗")