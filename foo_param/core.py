import math

class FooParameterization:
    """
    Calculate the volume of a sphere using the Foo et al. parameterization.
    
    Parameters:
    radius (float): Radius of the sphere
    
    Optional Parameters:
    significant_figures (int, optional): The number of significant figures to which the volume should be rounded.
                                         Defaults to None, meaning no rounding is applied.

    custom_pi (float, optional): A user-defined value of pi to be used in the calculation. 
                                 Defaults to None, in which case math.pi is used.
    
    Returns:
    float: Volume of the sphere
    """
    @staticmethod
    def calculate_volume(radius, significant_figures=None, custom_pi=None):
        from foo_param.utils import validate_radius
        
        validate_radius(radius)
        pi_value = custom_pi if custom_pi is not None else math.pi
        volume = (4/3) * pi_value * (radius ** 3)
        
        if significant_figures is not None:
            volume = round(volume, significant_figures)
        
        return volume