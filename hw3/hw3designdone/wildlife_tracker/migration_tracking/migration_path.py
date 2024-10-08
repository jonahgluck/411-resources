from typing import Optional

class MigrationPath:

    path_id: int
    species: str
    start_location: Habitat 
    destination: Habitat
    duration: Optional[int] = None
    
