"""
Basic Config Manager Class for python

Author - Joshua Barrass

Contact - Joshuabarrass010203@gmail.com
Github - @JoshuaBarrass

For Basic Use - 

1. Change the file path if different one is required

2. Change the default `_default_config` var to reflect your needs

3. To get an attributes value, use : `get_attribute(attribute_name: str)`

4. to set an attributes value, use : `set_attribute(attribute_name: str, value: any)` - Note: this can store any type as the value but in the end it'll be parsed by json into a file

- the `get_keys()` function will return all the 'attributes' currently being stored
"""

import os
import json

class ConfigManager():
    """ConfigManager - Singleton Based  

    """

    _instance = None

    _filepath = f"{os.getenv('APPDATA')}/ConfigManager/"
    _filename = "config.json"

    _default_config = { 'email' : 'UPDATE EMAIL IN SETTINGS',
                    'name' : 'UPDATE NAME IN SETTINGS',
                    'max_thread' : '5'}

    def __check_dir_exists(self):
        print(f"Checking dir -  {self._filepath}")
        if not os.path.exists(self._filepath):
            print("mkdir XEMU")
            os.mkdir(self._filepath)

    def __new__(cls):
        if cls._instance is None:
            print('Logger singleton Init')
            cls._instance = super(ConfigManager, cls).__new__(cls)
            # Init Method
            cls.__check_dir_exists(cls)
            cls._get_config(cls)

        return cls._instance

    def get_attribute(self, att: str) -> any:
        """gets the attribute from the config

        Args:
            att (str): attribute name to get

        Returns:
            any: Returns The Value OR None if it doesn't exist
        """

        try:
            return self._default_config[att]
        except:
            self.set_attribute(att, None)
            return None

    def set_attribute(self, att: str, value: any):
        """Set the value of a given attribute

        Args:
            att (str): name of the attribute to set
            value (any): Value to set attribute to
        """
        try:
            self._default_config[att] = value
        except:
            pass
        finally:
            self._save_config_to_file()

    def _save_config_to_file(self):
        with open(f"{self._filepath}{self._filename}", "w", encoding="UTF-8") as config_file:
            config_file.write(json.dumps(self._default_config))

    def _get_config(self) -> dict:
        try:
            with open(f"{self._filepath}{self._filename}", "r", encoding="UTF-8") as config_file:
                filedata = json.loads(config_file.read())
                self._default_config = filedata.copy()
        except Exception as e:
            print("Error Getting Config, no config found - using default")
            self._save_config_to_file(self) # pylint: disable=too-many-function-args # will run when file doesnt exist

    def get_keys(self) -> list:
        """returns a list of keys thats in the current config

        Returns:
            list: List of Current Keys
        """
        return list(self._default_config.keys())
