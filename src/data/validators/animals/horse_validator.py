from src.infra.chain_responsability import ValidatorInterface

class HorseValidator(ValidatorInterface):

    def validate(self, param: any) -> bool:
        if self.handler == 'food':
            return (
                (param == 'pasture') or (param == 'hay') or (param == 'fruits')
            )

    def action(self):
        return self.__food_action_handle()

    def __food_action_handle(self):
        """food validate action"""
        print('Horse tasted it')
