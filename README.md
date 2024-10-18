# Exercism Exercises

This repository contains my solutions to exercises from [Exercism](https://exercism.org/). 
Exercism is a platform that provides coding exercises in various programming languages, 
allowing learners to improve their skills through practice and feedback.

## System Requirements

These instructions are specifically for **Debian 12 Linux**. 
Adjust commands accordingly if you're using another system.

## Getting Started

1. **Install the Exercism CLI** following the [installation guide](https://exercism.org/docs/using/solving-exercises/working-locally).  
   On Debian 12, you can download the CLI and install it by running:
    ```bash
    curl -O https://exercism.org/install
    chmod +x exercism
    sudo mv exercism /usr/local/bin/exercism
    ```
2. **Configure your workspace**:
    ```bash
    exercism configure --workspace=/path/to/your/workspace
    ```
3. **Download an exercise** using the CLI:
    ```bash
    exercism download --track=python --exercise=exercise-name
    ```
4. **Set up a virtual environment** (recommended):
   To avoid conflicts with system packages, it's recommended to use a virtual environment. You can create and activate one by running:
    ```bash
    python3 -m venv ./venv
    source ./venv/bin/activate
    ```
5. **Install project dependencies**:
   If the exercises require specific libraries, install them using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
6. **Solve the exercise** and run your tests locally:
    ```bash
    pytest
    ```

## Progress Overview

### Python Track
- Total exercises: 140
- Completed: 1/140

  [X] [X] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]

### C++ Track
- Total exercises: 95
- Completed: 1/95

  [X] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
  [ ] [ ] [ ] [ ] [ ] [ ]


## Notes

- The exercises are written in Python and C++.
- Each exercise directory contains the original problem statement and my solution.

## How to Contribute

Feel free to open issues or submit pull requests if you'd like to suggest improvements or new solutions.
