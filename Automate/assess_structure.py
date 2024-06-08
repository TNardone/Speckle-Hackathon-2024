"""
Need to:
Take building model as input
Assess shape
Assess number of columns
Apply rule for spacing/number of columns in the model that is passed in
Return either sound or not sound
"""

from specklepy.objects import Base

def infer_geometry(building: Base):
    """
    Input: Building object (instance of specklepy Base class)
    Output: Building geometry in 
    """
    if hasattr(building, 'geometry'):
        geometry = building.geometry
        # ...
        print(f'Geometry: {geometry}')
    else:
        print('No geometry found.')

    return geometry
