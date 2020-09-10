

class FormDataExtractor:
    """This class suppose to extract data for multiple forms"""

    def create_data_packages(self, post_data, number_of_forms):
        processed_data = []
        partial_data = {}
        for f in range(0, number_of_forms):
            for key in post_data.keys():
                try:
                    partial_data[key] = post_data[key][f]
                except IndexError:
                    pass
            processed_data.append(partial_data)
            partial_data = {}
        return processed_data