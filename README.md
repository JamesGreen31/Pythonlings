# Pythonlings

Pythonlings is a learning-by-doing Python exercise suite inspired by projects like Rustlings.  
Learners work through small, self-contained exercises that introduce Python concepts step by step.

---

## Repository Structure

```
.
├── 00_navigation
│   ├── exercise files
├── 01_basics
│   ├── exercise files
├── 02_control_flow
│   ├── exercise files
├── 03_data_structures
│   ├── exercise files
├── 04_classes_and_methods
│   ├── exercise files
├── tests
│   ├── test_*.py
├── driver.py
└── README.md
```

- **driver.py** — orchestrates running all exercises and their corresponding tests.  
- **00_navigation ... 04_classes_and_methods** — directories containing exercises organized by topic.  
- **tests/** — test files that validate each exercise.  

---

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/JamesGreen31/Pythonlings.git
   cd Pythonlings
   ```

   ALTERNATIVE: Download the ZIP archive for the latest release

2. Run the driver:

   ```bash
   python driver.py
   ```

This will run each exercise in order and report whether it passed or failed.

---

## How It Works

- The driver dynamically loads each exercise and its corresponding test.  
- Tests are named following the pattern `test_<module>_<exercise>.py` and must contain a `run(module)` function.  
- Exercises often include a placeholder comment such as:

  ```python
  # REMOVE THIS TO MOVE ON
  ```

  The driver will stop progressing until the learner removes this line.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch.  
3. Add or update exercises and tests.  
4. Submit a pull request.  

Contributions can include new exercises, improved test coverage, documentation, or driver enhancements.

## Reporting Bugs

Please use the issue template in the issues tab to open / report an issue with Pythonlings.
---

## Future Improvements

- New modules / Python Items.

## AI Notice

While these tests were derived by human thought, much of the language, formatting, and test implementations were performed by AI to have a consistent and well presented experience. 

Each exercise has been manually solved by a human and tested by a human. If you feel there is confusion or a bug, please report the issue 
through the issue template so that it can be reviewed by a human).

---

## License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project in accordance with the terms of the license.
