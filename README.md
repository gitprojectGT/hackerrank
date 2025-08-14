# HackerRank Python Solutions

A collection of Python solutions for various HackerRank programming challenges, covering fundamental algorithms, data structures, and Python-specific concepts.

## 🚀 Quick Start

```bash
# Run any solution
python <filename>.py

# Run tests (where available)
python test_<filename>.py
```

## 📁 Problem Categories

### Collections Module
- **py-collections-deque.py** - Double-ended queue operations
- **py-collections-namedtuple.py** - Named tuple usage
- **py-collections-ordereddict.py** - Ordered dictionary implementation

### Set Operations
- **py-set-add.py** - Adding elements to sets
- **py-set-difference-operation.py** - Set difference operations
- **py-set-discard-remove-pop.py** - Set element removal methods
- **py-set-intersection-operation.py** - Set intersection operations
- **py-set-mutations.py** - Set mutation operations
- **py-set-symmetric-difference-operation.py** - Symmetric difference operations
- **py-set-union.py** - Set union operations

### String Manipulation
- **py-ginorts.py** - Custom string sorting with specific rules
- **py-word-order.py** - Word ordering and frequency analysis
- **py-most-commons.py** - Finding most common characters

### Basic Python
- **python-arithmetic-operators.py** - Basic arithmetic operations
- **python-division.py** - Division operations
- **python-loops.py** - Loop constructs
- **python-print.py** - Print statement variations
- **write-a-function.py** - Function definition and leap year logic

### Logic & Algorithms
- **py-if-else.py** - Conditional logic
- **py-piling-up.py** - Stack-based problem solving
- **py-the-captains-room.py** - Finding unique elements

## 🧪 Testing

Some solutions include comprehensive unit tests:

- **test_py_ginorts.py** - Complete test suite for the ginorts string sorting problem

Tests cover:
- Basic functionality
- Edge cases (empty inputs, single characters)
- Error handling
- Performance with large inputs

## 🛠️ Development

### Code Structure
- Each file is a standalone solution
- Input/output handled via `input()` and `print()`
- Main execution in `if __name__ == '__main__':` blocks
- Modular functions for complex problems

### Testing Framework
- Uses Python's built-in `unittest` module
- Comprehensive test coverage including edge cases
- Performance testing for larger inputs

## 📝 Solution Highlights

### Advanced String Sorting (py-ginorts.py)
Implements custom sorting with specific rules:
1. Lowercase letters (alphabetically)
2. Uppercase letters (alphabetically)  
3. Odd digits (numerically)
4. Even digits (numerically)

### Collections Mastery
Demonstrates proper usage of Python's collections module:
- `deque` for efficient append/pop operations
- `Counter` for frequency analysis
- `OrderedDict` for maintaining insertion order

## 🎯 Problem-Solving Approach

1. **Input Processing** - Robust input handling and validation
2. **Algorithm Implementation** - Clean, readable solution logic
3. **Edge Case Handling** - Comprehensive coverage of boundary conditions
4. **Testing** - Unit tests where complexity warrants verification

## 🔧 Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## 📚 Learning Resources

These solutions demonstrate key Python concepts:
- Lambda functions and custom sorting
- Collections module usage
- String manipulation techniques
- Set operations and mathematical concepts
- Error handling and input validation