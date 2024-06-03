def validate_radius(radius):
    """
    Validate the radius value.
    
    Parameters:
    radius (float): Radius of the sphere
    
    Returns:
    none

    Raises:
    ValueError: If the radius is not a positive number.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")