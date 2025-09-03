# Collatz Stopping Constant Estimation

This project computes and estimates the Collatz stopping constant \(C\) by calculating the cumulative average of the ratio of stopping time \(s(n)\) to the natural logarithm of \(n\) for \(n\) from 2 to a large \(N\).

## Introduction

The Collatz conjecture states that for any positive integer \(n\), the sequence defined by repeatedly applying \(n = n/2\) if even or \(n = 3n + 1\) if odd will eventually reach 1. The stopping time \(s(n)\) is the number of steps to reach 1.

The Collatz stopping constant \(C\) is defined as:
\[
C = \lim_{N \to \infty} \frac{1}{N} \sum_{n=2}^{N} \frac{s(n)}{\log n}
\]

This code uses memoization to efficiently compute \(s(n)\) and plots the cumulative average to visualize convergence.

## Prerequisites

- Python 3.x
- matplotlib

Install dependencies:
```bash
pip install matplotlib
```

## Usage

Run the script:
```bash
python collatz_constant.py
```

The script will compute for \(N = 1,000,000\) and display a plot of the cumulative average.

## Expected Results

The cumulative average converges to approximately 10.0, suggesting \(C \approx 10\).

## Further Work

- Increase \(N\) for better accuracy.
- Analyze different subsequences.
- Study the distribution of \(s(n) / \log n\).
