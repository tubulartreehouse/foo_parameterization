def validate_radius(radius):
    """
    Validate the radius value.
    
    Parameters:
    radius (float): Radius of the sphere
    
    Returns:
    bool: True if radius is valid, else False
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")