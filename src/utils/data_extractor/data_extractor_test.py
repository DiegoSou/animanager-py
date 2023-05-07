from .data_extractor import DataExtractor

class TestDataExtractor(DataExtractor):

    def extractdata(self, func=None) -> callable:
        return super().extractdata(self.__teste_extract_data)

    def __teste_extract_data(self, data, user_id):
        if 'user_id' not in data:
            return { 'success' : False, 'error' : 'No user id key' }

        if data['user_id'] != user_id:
            return { 'success' : False, 'error' : f'Incorrect user id: {user_id}' }

        return {
            'success' : True,
            'data' : data
        }
