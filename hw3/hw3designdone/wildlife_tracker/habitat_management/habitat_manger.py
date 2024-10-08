from typing import Optional, List

class HabitatManager:

    habitats: dict[int, Habitat] = {}

    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass
    
    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def get_habitat_details(habitat_id: int) -> dict:
        pass

    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass
    
    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

    def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass
    
    