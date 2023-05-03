from src.data.factories import AnimalFactory

animal_food_chain_responsability = AnimalFactory.create_validation_chain('food')
animal_food_chain_responsability.process('corn')
