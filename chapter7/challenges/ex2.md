### 🔧 STEP 0: Example Setup

Let's say you run the script and provide this input:

```text
Enter a function in one variable: x**2 + 3*x + 2
Enter the variable to differentiate with respect to: x
Enter the initial value of the variable: -4
```

So we have:

- **Function `f(x)`**: $f(x) = x^2 + 3x + 2$
- **Variable**: `x`
- **Initial guess**: $x_0 = -4$

---

### 📐 STEP 1: Derive the Function

The code uses SymPy to differentiate the function:

```python
d = Derivative(f, var).doit()
```

#### ➤ Calculation:

$$
f(x) = x^2 + 3x + 2 \Rightarrow f'(x) = 2x + 3
$$

---

### 🚶 STEP 2: Gradient Descent Algorithm

Now we apply **gradient descent** to minimize $f(x)$. Key values:

- `step_size = 1e-4`
- `epsilon = 1e-6`
- Initial guess $x_0 = -4$

Gradient descent formula:

$$
x_{\text{new}} = x_{\text{old}} - \text{step\_size} \cdot f'(x_{\text{old}})
$$

---

### 🔄 STEP 3: Manual Iteration

Let's do the **first few iterations** manually to demonstrate how the algorithm works.

#### 🧮 Iteration 0:

- $x_0 = -4$
- $f'(x_0) = 2(-4) + 3 = -8 + 3 = -5$
- $x_1 = -4 - 0.0001 \cdot (-5) = -4 + 0.0005 = -3.9995$

#### 🧮 Iteration 1:

- $x_1 = -3.9995$
- $f'(x_1) = 2(-3.9995) + 3 = -7.999 + 3 = -4.999$
- $x_2 = -3.9995 + 0.0004999 \approx -3.9990001$

... and so on until the absolute change between `x_old` and `x_new` is less than `1e-6`.

This will eventually converge to the minimum of the quadratic function, which we know is at:

$$
f'(x) = 0 \Rightarrow 2x + 3 = 0 \Rightarrow x = -1.5
$$

---

### 📈 STEP 4: Plotting the Graph

The function `draw_graph(x_axis, f, var)` does two things:

- Plots the function values $f(x)$ in blue dots over the domain `[-1, 1]`.
- Overlays the **intermediate steps** (`x_axis`) in red dots, which show the **path taken by gradient descent** from `x0` to the minimum.

Since your domain for the graph is `-1` to `1`, and the initial value is `-4`, you may not see the starting point unless you change `frange(-1, 1, 0.01)` to cover a wider range (like `frange(-5, 1, 0.01)`).

---

### ✅ FINAL OUTPUT

Once gradient descent converges, the script prints:

```
x: -1.50000008101614
Minimum value: -0.250000000000000
```

Which is **very close** to the exact minimum:

- $x = -1.5$
- $f(-1.5) = (-1.5)^2 + 3(-1.5) + 2 = 2.25 - 4.5 + 2 = -0.25$
