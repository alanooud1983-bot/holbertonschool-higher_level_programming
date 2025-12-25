#!/usr/bin/python3
"""
Module: task_03_xml
XML serialization and deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): Output XML filename

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not isinstance(dictionary, dict):
            print("Error: First parameter must be a dictionary")
            return False

        if not isinstance(filename, str):
            print("Error: Filename must be a string")
            return False

        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))

            if isinstance(value, (dict, list)):
                child.text = str(value)
                child.set("type", type(value).__name__)
            elif isinstance(value, bool):
                child.text = str(value).lower()
                child.set("type", "bool")
            elif value is None:
                child.text = "null"
                child.set("type", "null")
            else:
                child.text = str(value)
                child.set("type", type(value).__name__)

        tree = ET.ElementTree(root)

        tree.write(filename, encoding='utf-8', xml_declaration=True)

        print(f"Dictionary successfully serialized to '{filename}'")
        return True

    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary

    Args:
        filename (str): Input XML filename

    Returns:
        dict: Deserialized Python dictionary, or empty dict if failed
    """
    try:
        if not isinstance(filename, str):
            print("Error: Filename must be a string")
            return {}

        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            key = child.tag
            text_value = child.text

            data_type = child.get("type", "str")

            if text_value is None:
                value = None
            elif data_type == "int":
                value = int(text_value)
            elif data_type == "float":
                value = float(text_value)
            elif data_type == "bool":
                value = text_value.lower() == "true"
            elif data_type == "null":
                value = None
            elif data_type == "dict":
                try:
                    value = eval(text_value)
                except:
                    value = text_value
            elif data_type == "list":
                try:
                    value = eval(text_value)
                except:
                    value = text_value
            else:
                value = text_value

            result[key] = value

        print(f"XML successfully deserialized from '{filename}'")
        return result

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return {}
    except ET.ParseError:
        print(f"Error: Invalid XML format in '{filename}'")
        return {}
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'")
        return {}
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return {}
