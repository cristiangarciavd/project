"""Provides a JSON files reader class"""
import json


class JsonReader:
    """JSON reader Class
    """
    @staticmethod
    def get_json(file):
        """get JSON method

        Args:
            file (str): file path

        Raises:
            Exception: "Error trying to load JSON file"

        Returns:
            dict: dictionary object with configuration options
        """

        with open(file, encoding="utf-8") as file_to_json:

            try:
                data = json.load(file_to_json)

            except Exception as exc:
                raise Exception('Error trying to load JSON file') from exc

            finally:
                file_to_json.close()

        return data

    @staticmethod
    def edit_json(file, to_add):
        """edit JSON method

        Args:
            file (str): file path
            to_add (dict): dictionary with information to add

        Raises:
            Exception: "Error trying to edit JSON file"
        """

        with open(file, 'w', encoding="utf-8") as json_file:

            try:
                json.dump(to_add, json_file)

            except Exception as exc:
                raise Exception('Error trying to edit JSON file') from exc

            finally:
                json_file.close()
