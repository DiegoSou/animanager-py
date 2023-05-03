from src.infra.chain_responsability import ValidatorInterface

class PigValidator(ValidatorInterface):

    def validate(self, param: any) -> bool:
        if self.handler == 'food':
            return (
                (param == 'soybean') or (param == 'corn') or (param == 'barley')
            )

    def action(self):
        return self.food_action_handle()

    def food_action_handle(self):
        """food validate action"""
        print('Pig tasted it')
