# Modules

## Core Module
The core module contains the primary functionality of the Foo Parameterization, including the calculation of volumes based on the sphere radius.

### calculate_volume(radius)
Calculates the volume of a sphere using the Foo et al. parameterization.

#### Parameters:
radius (float): The radius of the sphere for which the volume is to be calculated.

#### Returns:
float: The calculated volume of the sphere.

#### Example:
```
from foo.core import calculate_volume

# Calculate the volume of a sphere with a radius of 5 units
volume = calculate_volume(5)
print(f"Volume: {volume:.2f}")
```

## Utils Module
The utils module provides additional utility functions that support the primary functionality of the Foo Parameterization.

### validate_radius(radius)
Validates a given radius

#### Parameters:
radius (float): The given radius of a sphere

#### Returns:
boolean: if the given radius is true or not

#### Example: 
```
from foo_param.utils import validate_radius

# Validate a radius value
try:
    validate_radius(5)
    print("Radius is valid")
except ValueError as e:
    print(f"Invalid radius: {e}")
```