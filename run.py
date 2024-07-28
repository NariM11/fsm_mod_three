import sys
from src.mod_three import mod_three

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <binary_string>")
        sys.exit(1)
    
    binary_string = sys.argv[1]
    
    try:
        remainder = mod_three(binary_string)
        print(f"The remainder of the binary number {binary_string} when divided by 3 is: {remainder}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
