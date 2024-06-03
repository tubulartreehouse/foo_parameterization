## Modules

# Core Module
The core module contains the primary functionality of the Foo Parameterization, including the calculation of volumes based on the sphere radius.

calculate_volume(radius)
Calculates the volume of a sphere using the Foo et al. parameterization.

Parameters:

radius (float): The radius of the sphere for which the volume is to be calculated.
Returns:

float: The calculated volume of the sphere.
Example:
```
from foo.core import calculate_volume

# Calculate the volume of a sphere with a radius of 5 units
volume = calculate_volume(5)
print(f"Volume: {volume:.2f}")
```