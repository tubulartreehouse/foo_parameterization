import math

class FooParameterization:
    @staticmethod
    def calculate_volume(radius):
        """
        Calculate the volume of a sphere using the Foo et al. parameterization.
        
        Parameters:
        radius (float): Radius of the sphere
        
        Returns:
        float: Volume of the sphere
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        
        # Placeholder for complex Foo et al. parameterization
        volume = (4/3) * math.pi * radius ** 3
        return volume