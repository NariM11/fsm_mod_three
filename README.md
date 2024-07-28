# Mod Three FSM

This project implements a Finite State Machine (FSM) to determine the remainder of a binary number when divided by three.

## Directory Structure

`root folder`

- `src`
  - `mod_three.py`
  - `mod_three_test.py`
- `README.md`
- `run.py`

## Prerequisites

- Python 3.7 or higher
- `git` for cloning the repository
- (Optional) `virtualenv` for creating an isolated Python environment

## Installation

1. Clone the repository:

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. (Optional) Create and activate a virtual environment:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

To run the program and compute the remainder of a binary number divided by three, execute:

```sh
python run.py <binary_string>
```

Replace <binary_string> with the binary number you want to process.

## Testing

To run the tests:

```sh
python -m unittest src.test_mod_three
```

## Files

- src/mod_three.py: Contains the FSM implementation and the main function to compute the remainder.
- src/mod_three_test.py: Contains unit tests for the FSM implementation.
- run.py: Entry point to run the program with command line input.

## Examples

```sh
python run.py 1101  # Output: 1
python run.py 1110  # Output: 2
python run.py 1111  # Output: 0
```
