import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def display_animals(data):
    for animal in data:
        to_display = {
            "Name": animal.get("name"),
            "Diet": animal['characteristics'].get('diet'),
            "Location": animal.get("locations")[0],
            "Type":animal['characteristics'].get('type')
        }
        display_text = ""
        for key, value in to_display.items():
            if value:
                display_text = display_text + f"\n{key}: {value}"
        print(display_text)


if __name__ == "__main__":
    data = load_data('animals_data.json')
    display_animals(data)