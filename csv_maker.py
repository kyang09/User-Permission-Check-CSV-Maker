import sys
import json


def process_user_data(user_json_obj):
    pass


def csv_read():
    if len(sys.argv) == 1:
        try:
            with open(sys.argv[0], 'r') as json_file:
                user_json_obj = json.load(json_file)
            process_user_data(user_json_obj)
        except FileNotFoundError as e:
            print("Could not find the input: %s" % e)
        except ValueError as e:
            print("Invalid JSON in the given file: %s" % e)


def main():
    csv_read()

if __name__ == "__main__":
    main()
