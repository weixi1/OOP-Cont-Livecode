from classes.plant import Plant

def test_plant_initalization():
    # Arrange
    name = "Butterfly pea floewr"
    water_level = 6
    sunlight_hours = 7
    is_blooming = True

    # Act
    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    # assert
    assert plant.name == name
    assert plant.is_blooming

    # assert not plant_2.is_blooming




