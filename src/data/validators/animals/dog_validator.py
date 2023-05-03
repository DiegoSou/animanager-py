from src.infra.chain_responsability import ValidatorInterface

class DogValidator(ValidatorInterface):

    def validate(self, param: any) -> bool:
        if self.handler == 'food':
            return (
                (param == 'dog_food') or (param == 'bone') or (param == 'chicken')
            )

    def action(self):
        return self.__food_action_handle()

    def __food_action_handle(self):
        """food validate action"""
        print('Dog tasted it')
