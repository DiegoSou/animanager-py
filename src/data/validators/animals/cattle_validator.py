from src.infra.chain_responsability import ValidatorInterface

class CattleValidator(ValidatorInterface):

    def validate(self, param: any) -> bool:
        if self.handler == 'food':
            return (
                (param == 'hay') or (param == 'grasses') or (param == 'clover')
            )

    def action(self):
        return self.__food_action_handle()

    def __food_action_handle(self):
        """food validate action"""
        print('Cattle tasted it')
