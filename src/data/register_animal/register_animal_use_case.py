from typing import Dict, List, Type
from pandas import read_csv, read_excel
from src.domain.models import Animals
from src.data.interface import AnimalsRepositoryInterface
from src.domain.usecases import IRegisterAnimalUseCase

class RegisterAnimalUseCase(IRegisterAnimalUseCase):

    def __init__(self, repo: Type[AnimalsRepositoryInterface]):
        self.repo = repo

    def register_animal(
            self,
            name: str,
            sex: str,
            animal_type: str,
            weight: float = None,
            specie: str = None
        ) -> Dict[bool, Animals]:

        try:
            response = self.repo.animals_register(name, sex, weight, specie, animal_type)

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}


    def upload_animals(self, file_data: any) -> Dict[bool, List[Animals]]:

        try:
            extension = file_data.filename.replace(' ', '_')[-4:]

            if extension == '.csv':
                animals_df = read_csv(file_data)
            elif (
                extension == '.xls' or
                extension == 'xlsx' or
                extension == '.odf' or
                extension == '.odt' or
                extension == '.ods'
            ): animals_df = read_excel(file_data)

            self.__format_df_to_lowercase_columns(animals_df)

            if (
                'name' not in animals_df.columns or 
                'sex' not in animals_df.columns or 
                'animal_type' not in animals_df.columns
            ): raise AssertionError('Required columns are missing (name, sex, animal_type)')

            # se a planilha tiver colunas a mais, funcionará normalmente
            response = self.repo.animals_bulk_register(animals_df)

            return {"success": True, "data": response}
        except Exception as exc:
            return {"success": False, "error": str(exc)}


    def __format_df_to_lowercase_columns(self, df):
        lowercase_columns = []

        for col in df.columns:
            lowercase_columns.append(col.lower())

        df.columns = lowercase_columns
