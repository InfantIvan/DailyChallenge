#!/usr/bin/env python3
"""
Vowel Balance Problem Solution

Problem: Given a string, determine whether the number of vowels in the first half 
of the string is equal to the number of vowels in the second half.

Rules:
- The string can contain any characters
- The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels
- If there's an odd number of characters in the string, ignore the center character

Author: Technical Architect Solution
Compatible with: VS Code Python environment
"""

def vowel_balance(s):
    """
    Simple vowel balance checker.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if vowel counts in both halves are equal, False otherwise
    """
    # Define vowels (both uppercase and lowercase)
    vowels = set('aeiouAEIOU')
    
    # Get the length of the string
    length = len(s)
    
    # Calculate the midpoint (ignore center character if odd length)
    mid = length // 2
    
    # Split the string into two halves
    first_half = s[:mid]
    second_half = s[mid + (length % 2):]  # Skip center character if odd length
    
    # Count vowels in each half
    first_half_vowels = sum(1 for char in first_half if char in vowels)
    second_half_vowels = sum(1 for char in second_half if char in vowels)
    
    # Return True if vowel counts are equal
    return first_half_vowels == second_half_vowels


def vowel_balance_detailed(s):
    """
    Enhanced vowel balance checker with detailed analysis.
    
    Args:
        s (str): Input string to check
        
    Returns:
        dict: Dictionary containing result and analysis details
    """
    vowels = set('aeiouAEIOU')
    length = len(s)
    mid = length // 2
    
    # Handle edge cases
    if length == 0:
        return {
            'result': True,
            'input': s,
            'length': length,
            'first_half': '',
            'second_half': '',
            'first_vowels': 0,
            'second_vowels': 0,
            'center_char': None,
            'analysis': 'Empty string - balanced by default'
        }
    
    first_half = s[:mid]
    second_half = s[mid + (length % 2):]
    center_char = s[mid] if length % 2 == 1 else None
    
    first_vowels = sum(1 for char in first_half if char in vowels)
    second_vowels = sum(1 for char in second_half if char in vowels)
    
    result = first_vowels == second_vowels
    
    return {
        'result': result,
        'input': s,
        'length': length,
        'first_half': first_half,
        'second_half': second_half,
        'first_vowels': first_vowels,
        'second_vowels': second_vowels,
        'center_char': center_char,
        'analysis': f"{'Balanced' if result else 'Not balanced'} - {first_vowels} vs {second_vowels} vowels"
    }


def print_analysis(analysis):
    """
    Pretty print the analysis results.
    
    Args:
        analysis (dict): Analysis dictionary from vowel_balance_detailed()
    """
    print(f"Input: '{analysis['input']}'")
    print(f"Length: {analysis['length']}")
    print(f"First half: '{analysis['first_half']}' ({analysis['first_vowels']} vowels)")
    print(f"Second half: '{analysis['second_half']}' ({analysis['second_vowels']} vowels)")
    if analysis['center_char']:
        print(f"Center character (ignored): '{analysis['center_char']}'")
    print(f"Result: {analysis['result']} - {analysis['analysis']}")
    print("-" * 50)


def interactive_checker():
    """
    Interactive vowel balance checker for testing multiple strings.
    Perfect for VS Code terminal usage.
    """
    print("🎯 Vowel Balance Checker")
    print("=" * 50)
    print("Enter strings to check vowel balance.")
    print("Press Enter with empty string to quit.")
    print()
    
    while True:
        user_input = input("Enter string: ").strip()
        if not user_input:
            print("👋 Goodbye!")
            break
        
        analysis = vowel_balance_detailed(user_input)
        print_analysis(analysis)


def run_tests():
    """
    Run comprehensive tests to validate the solution.
    """
    test_cases = [
        ("abcdef", True),      # Even: "abc"(1) vs "def"(1)
        ("abcdefg", True),     # Odd: "abc"(1) vs "efg"(1), ignore 'd'
        ("hello", True),       # Odd: "he"(1) vs "lo"(1), ignore 'l'
        ("world", False),      # Odd: "wo"(1) vs "ld"(0), ignore 'r'
        ("programming", True), # Odd: "progr"(1) vs "mming"(1), ignore 'a'
        ("aeiou", True),       # Odd: "ae"(2) vs "ou"(2), ignore 'i'
        ("bcdfg", True),       # Odd: "bc"(0) vs "fg"(0), ignore 'd'
        ("AeIoU", True),       # Odd: "Ae"(2) vs "oU"(2), ignore 'I'
        ("bookkeeper", False), # Even: "bookk"(2) vs "eeper"(3)
        ("", True),            # Empty string
        ("a", True),           # Single character (ignored)
        ("ab", False),         # Even: "a"(1) vs "b"(0)
        ("ae", True),          # Even: "a"(1) vs "e"(1)
    ]
    
    print("🧪 Running Test Cases")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, (test_string, expected) in enumerate(test_cases, 1):
        result = vowel_balance(test_string)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i:2d}: '{test_string}' → {result} (expected: {expected}) {status}")
        
        if result == expected:
            passed += 1
    
    print("-" * 50)
    print(f"Results: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 All tests passed! Solution is working correctly.")
    else:
        print("⚠️  Some tests failed. Please review the implementation.")


if __name__ == "__main__":
    # Choose what to run when script is executed
    print("Vowel Balance Problem - Solution Menu")
    print("1. Run tests")
    print("2. Interactive checker")
    print("3. Quick examples")
    
    choice = input("\nSelect option (1/2/3) or press Enter for tests: ").strip()
    
    if choice == "2":
        interactive_checker()
    elif choice == "3":
        print("\n🔍 Quick Examples:")
        examples = ['hello', 'world', 'programming', 'aeiou']
        for example in examples:
            result = vowel_balance(example)
            print(f"vowel_balance('{example}') = {result}")
    else:
        run_tests()