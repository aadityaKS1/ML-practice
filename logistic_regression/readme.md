# Logistic Regression Decision Boundary Visualization

## Overview
This project demonstrates **logistic regression classification** on a synthetic 2D dataset.  
It includes both:  
1. **Scikit-learn LogisticRegression** implementation  
2. **Custom Gradient Descent** implementation  

The goal is to visualize and compare the **decision boundaries** of both approaches.

---

## Libraries Used
- `numpy` – For numerical computations  
- `matplotlib` – For plotting data and decision boundaries  
- `scikit-learn` – For logistic regression and generating synthetic datasets  

---

## Project Steps
1. **Generate Synthetic Data**  
   - Using `make_classification` with 2 features and 2 classes.  
2. **Visualize Data**  
   - Scatter plot of the points colored by class.  
3. **Logistic Regression using sklearn**  
   - Fit the model and extract the coefficients to plot the decision boundary.  
4. **Logistic Regression from Scratch**  
   - Implement gradient descent with the sigmoid function.  
   - Calculate custom coefficients and intercept.  
5. **Compare Decision Boundaries**  
   - Plot sklearn boundary in red  
   - Plot gradient descent boundary in black  
   - Visualize how closely gradient descent matches sklearn results.

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/ML-Practice.git
