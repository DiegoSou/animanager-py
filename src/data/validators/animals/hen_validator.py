from src.infra.chain_responsability import ValidatorInterface

class HenValidator(ValidatorInterface):

    def validate(self, param: any) -> bool:
        if self.handler == 'food':
            return (
                (param == 'corn') or (param == 'grains') or (param == 'insects')
            )

    def action(self):
        return self.__food_action_handle()

    def __food_action_handle(self):
        """food validate action"""
        print('Hen tasted it')
