#!/usr/bin/python3
"""
Module: task_02_csv
Convert CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format

    Args:
        csv_filename (str): Path to the CSV file

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        if not isinstance(csv_filename, str):
            print("Error: CSV filename must be a string")
            return False

        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            data = [row for row in csv_reader]

        if not data:
            print("Warning: CSV file is empty or contains no data")

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Successfully converted '{csv_filename}' to 'data.json'")
        print(f"Number of records converted: {len(data)}")

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found")
        return False
    except PermissionError:
        print(f"Error: Permission denied for file '{csv_filename}'")
        return False
    except csv.Error as e:
        print(f"Error: CSV parsing error - {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: JSON encoding error - {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return False
