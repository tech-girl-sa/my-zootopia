import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animals_cards(data):
    animals =""
    for animal in data:
        to_display = {
            "Name": animal.get("name"),
            "Diet": animal['characteristics'].get('diet'),
            "Location": animal.get("locations")[0],
            "Type":animal['characteristics'].get('type')
        }
        display_text = '<li class="cards__item">\n'
        for key, value in to_display.items():
            if value:
                display_text += f"{key}: {value}<br/>\n"
        display_text += '</li>\n'
        animals += display_text
    return animals

def load_template(html_path):
    with open(html_path, "r") as handle:
        return handle.read()

def regenerate_html(html_path, data):
    content = load_template(html_path)
    animals_display = serialize_animals_cards(data)
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animals_display)
    with open(html_path,"w") as handle:
        handle.write(new_content)

if __name__ == "__main__":
    data = load_data('animals_data.json')
    html_path = "animals_template.html"
    regenerate_html(html_path, data)