adder in a Mine - Gerald/Wheatley Numerical Analysis

This project solves a classic numerical analysis problem from the book *Applied Numerical Analysis* by Gerald & Wheatley.

## 🔧 Problem Description
Find the shortest ladder that can pass through a mine corner, given two tunnel widths and the angle between them.

## 🧮 Mathematical Model

We minimize the function:

L(c) = w₁ / sin(a + c) + w₂ / sin(c)

## 📊 Output
- Optimal angle: ~26.80°
- Minimum ladder length: ~33.47 ft

## 🚀 How to run
```bash
pip install numpy
python ladder_solver.py
