# 🧩 Sudoku Solver

A Python desktop application that solves Sudoku puzzles using backtracking algorithms with a clean Tkinter GUI interface.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📸 Demo

<img width="657" height="910" alt="Screenshot 2025-08-28 192245" src="https://github.com/user-attachments/assets/2516065e-fb77-4a40-87c9-f011f0918fb1" />



## 📖 About

This Sudoku Solver provides an intuitive graphical interface for entering and solving Sudoku puzzles. The application validates input boards and uses a recursive backtracking algorithm to find solutions efficiently. The solver runs in a background thread to maintain UI responsiveness during computation.

## ✨ Features

- **Interactive 9×9 Grid**: Clean Tkinter interface with input validation
- **Real-time Validation**: Checks for valid Sudoku constraints before solving  
- **Fast Backtracking Solver**: Efficient recursive algorithm with constraint checking
- **Responsive UI**: Background threading prevents interface freezing
- **Clear Visual Feedback**: Status messages and color-coded grid lines
- **One-click Operations**: Simple Solve and Clear buttons

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (included with most Python installations)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/khemchandkumar/sudoku_solver.git
   ```
   ```bash
   cd sudoku-solver
   ```

2. **Run the application**
    ```bash
    python sudoku_solver.py
    ```


No additional dependencies required! The application uses only Python standard library modules.

## 🎮 Usage

1. **Enter Numbers**: Click on any cell and type digits 1-9. Empty cells represent blanks.

2. **Solve Puzzle**: Click the "Solve" button to validate and solve the puzzle automatically.

3. **Clear Board**: Use the "Clear" button to reset all cells and start over.

4. **Status Feedback**: Check the status bar for solver results and error messages.

### Example
```
5 3 _ | _ 7 _ | _ _ _
6 _ _ | 1 9 5 | _ _ _
_ 9 8 | _ _ _ | _ 6 _
------+-------+------
8 _ _ | _ 6 _ | _ _ 3
4 _ _ | 8 _ 3 | _ _ 1
7 _ _ | _ 2 _ | _ _ 6
------+-------+------
_ 6 _ | _ _ _ | 2 8 _
_ _ _ | 4 1 9 | _ _ 5
_ _ _ | _ 8 _ | _ 7 9
```

## ⚙️ How It Works

### Algorithm
- **Validation**: Checks rows, columns, and 3×3 blocks for duplicate numbers
- **Backtracking**: Recursively tries numbers 1-9 in empty cells
- **Constraint Checking**: Ensures Sudoku rules are maintained at each step
- **Efficiency**: Backtracks immediately when constraints are violated

### Architecture
- **GUI Layer**: Tkinter interface handling user input and display
- **Solver Engine**: Core backtracking algorithm with validation
- **Threading**: Background processing to maintain UI responsiveness

## 📁 Project Structure
```
sudoku-solver/
├── sudoku_solver.py # Main GUI application
├── solver.py # Core solving algorithms
├── README.md # Project documentation
└── LICENSE # MIT license file
```

### File Descriptions

- **`sudoku_solver.py`**: Main application file containing the Tkinter GUI, input validation, threading logic, and user interface components
- **`solver.py`**: Core solving engine with validation functions, backtracking algorithm, and safety checks

## 🛠️ Technical Details

### Key Functions

**solver.py:**
- `isSafe()`: Validates number placement in row, column, and 3×3 block
- `solveSudoku()`: Recursive backtracking solver
- `isValidSudoku()`: Pre-solve validation of the entire board
- `solver()`: Main solver wrapper function

**sudoku_solver.py:**
- `drawGrid()`: Creates the 9×9 input grid with visual separators
- `getValues()`: Extracts board state from GUI inputs
- `_solve_worker()`: Background thread function for solving

## 🎨 Customization

You can modify the appearance by changing these variables in `sudoku_solver.py`:
### Colors
root.configure(bg="#dc92eb") # Main window background
entry.configure(bg="#f6c5c5") # Cell background
btn.configure(bg="#ffea00") # Button color

### Grid styling
Frame(frame, bg="#23A8F5") # Grid line color

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Ideas for contributions:
- Import/export puzzle files (CSV, JSON)
- Difficulty level detection
- Step-by-step solution visualization
- Puzzle generator
- Keyboard navigation
- Multiple solver algorithms
- Performance optimizations

## 🐛 Issues

Found a bug? Please [open an issue](https://github.com/yourusername/sudoku_solver/issues) with:
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)
- Your Python version

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as a learning project for Tkinter GUI development
- Inspired by classic constraint satisfaction problems
- Thanks to the Python community for excellent documentation



---

⭐ **Star this repository if you found it helpful!** ⭐

