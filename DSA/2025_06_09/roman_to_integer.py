# Roman to Integer - DSA Solution

def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.
    
    Args:
        s: Roman numeral string (I, V, X, L, C, D, M)
    
    Returns:
        int: Integer value of the Roman numeral
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Process from right to left
    for char in reversed(s):
        current_value = roman_values[char]
        
        # If current value is less than previous, subtract
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

def int_to_roman(num: int) -> str:
    """
    Convert an integer to a Roman numeral string.
    
    Args:
        num: Integer to convert (1-3999)
    
    Returns:
        str: Roman numeral string
    """
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    result = ""
    
    for value, numeral in roman_numerals:
        while num >= value:
            result += numeral
            num -= value
    
    return result

# Example usage
if __name__ == "__main__":
    # Test Roman to Integer
    test_cases = [
        "III",      # 3
        "IV",       # 4
        "IX",       # 9
        "LVIII",    # 58
        "MCMXCIV",  # 1994
        "MMXXIII",  # 2023
        "XL",       # 40
        "XC",       # 90
        "CD",       # 400
        "CM",       # 900
    ]
    
    print("Roman to Integer:")
    for roman in test_cases:
        result = roman_to_int(roman)
        print(f"{roman} -> {result}")
    
    print("\nInteger to Roman:")
    int_test_cases = [3, 4, 9, 58, 1994, 2023, 40, 90, 400, 900]
    for num in int_test_cases:
        result = int_to_roman(num)
        print(f"{num} -> {result}") 