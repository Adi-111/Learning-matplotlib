import matplotlib.pyplot as plt
import numpy as np

# Write values of x you wanna take as x = np.linspace(val, val, val, val....)
x = np.linspace(0, np.pi)

# Write how y is related with x
y = np.sin(x)/np.cos(x)  # Calculate the sine of each value of x

# Plot the sine function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = np.sin(x)/np.cos(x)')
plt.title('Write Title Here')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
