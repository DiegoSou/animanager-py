# pylint:disable=E1101

import os
import json

from typing import Type, Dict, List
from pandas import read_json, DataFrame

from src.domain.models import Animals
from src.domain.usecases import IFindAnimalUseCase
from src.data.animals.interface import AnimalsRepositoryInterface

class FindAnimalUseCase(IFindAnimalUseCase):

    def __init__(self, repo: Type[AnimalsRepositoryInterface]):
        self.repo = repo

    def find(
            self,
            animal_id: str = None,
            animal_name: str = None,
            animal_type: str = None,
            export: str = None,
            convert_to_model: bool = True
        ) -> Dict[bool, List[Animals]]:

        try:
            response = self.repo.animals_select(animal_id, animal_name, animal_type, convert_to_model)

            if export in ('csv', 'excel'):
                prefix = 'animal' + '_' + str(animal_name or '') + '_' + str(animal_type or '')
                self.__generate_export(prefix.lower(), export, response)


            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}


    def __generate_export(self, prefix: str, extension: str, data: List[Animals]):
        """exporta dados como um arquivo"""
        result_dir = str(os.environ.get('EXPORTS_DIR')) + '/' + prefix

        data_dict = [a._asdict() for a in data]
        data_df = read_json(json.dumps(data_dict))

        if extension == 'csv':
            data_df.to_csv(str(result_dir) + '.csv', index=False)
        elif extension == 'excel':
            data_df.to_excel(str(result_dir) + '.xlsx', index=False)
