from typing import Type, Sequence
from src.infra.interface import ValidatorInterface

class ValidationChain:

    @classmethod
    def __init__(cls, chain: Sequence[Type[ValidatorInterface]]):
        cls.validators = chain

    @classmethod
    def process(cls, param: any, all_or_none: bool = False):
        """Process param for each validator of the class
        - params
            - param: The agument to validate
            - all_or_none: If needs to pass through all validators
        """
        for vldt in cls.validators:
            valid = vldt.validate(param)

            if valid:
                vldt.action()

            if not valid and all_or_none:
                raise AssertionError(f"Assertion error: {vldt.__class__.__name__} failed.")
