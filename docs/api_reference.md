# Modules

## Core Module
The core module contains the primary functionality of the Foo Parameterization, including the calculation of volumes based on the sphere radius.

### `calculate_volume(radius, significant_figures=None, custom_pi=None)`
Calculates the volume of a sphere using the Foo et al. parameterization.

#### Parameters:
- `radius` (float): The radius of the sphere for which the volume is to be calculated.
- `significant_figures` (int, optional): The number of significant figures to which the volume should be rounded. Defaults to `None`.
- `custom_pi` (float, optional): A user-defined value of pi to be used in the calculation. Defaults to `None`, in which case `math.pi` is used.

#### Returns:
- `float`: The calculated volume of the sphere.

#### Raises:
- `ValueError`: If the radius is not a positive number.

#### Example:
```python
from foo_param.core import FooParameterization

# Calculate the volume of a sphere with a radius of 5 units, rounded to 2 significant figures
volume = FooParameterization.calculate_volume(5, significant_figures=2)
print(f"Volume: {volume:.2f}")

# Calculate the volume of a sphere with a radius of 5 units using a custom value of pi
volume = FooParameterization.calculate_volume(5, custom_pi=3.14)
print(f"Volume: {volume:.2f}")
```

## Utils Module
The utils module provides additional utility functions that support the primary functionality of the Foo Parameterization.

### validate_radius(radius)
Validates a given radius

#### Parameters:
radius (float): The given radius of a sphere

#### Returns:
none

#### Raises:
ValueError: If the radius is not a positive number.

#### Example: 
```python
from foo_param.utils import validate_radius

# Validate a radius value
try:
    validate_radius(5)
    print("Radius is valid")
except ValueError as e:
    print(f"Invalid radius: {e}")
```