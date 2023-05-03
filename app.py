from src.data.factories import AnimalFactory

my_chicken = AnimalFactory.create('Chicken', 'caipira', 2.7, 'hen')
print(AnimalFactory.mapping)

print(my_chicken.survival_strategy.action())
print(my_chicken.survival_strategy.competence_param())
