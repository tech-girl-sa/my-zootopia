import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal_obj):
    """generates one card to display animal info"""
    to_display = {
        "Name": animal_obj.get("name"),
        "Diet": animal_obj['characteristics'].get('diet'),
        "Location": animal_obj.get("locations")[0],
        "Type": animal_obj['characteristics'].get('type'),
        "Skin Type": animal_obj['characteristics'].get('skin_type'),
    }
    animal_card = '<li class="cards__item">\n'
    for key, value in to_display.items():
        if key == "Name":
            animal_card += f''''
            <div class="card__title">{value}</div>
            <p class="card__text">
            <ul class="animal_info">
'''
        elif value:
            animal_card += f"<li><strong>{key}</strong>: {value}</li>\n"
    animal_card += '</ul>\n</p>\n</li>\n'
    return animal_card

def serialize_animals(data):
    """generates list of animal cards in webpage"""
    animals =""
    for animal in data:
        animal_card = serialize_animal(animal)
        animals += animal_card
    return animals

def load_template(html_path):
    """loads the template to use in generating the webpage"""
    with open(html_path, "r") as handle:
        return handle.read()

def regenerate_html(html_path, data):
    """generates the whole webpage"""
    content = load_template("animals_template.html")
    animals_display = serialize_animals(data)
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animals_display)
    with open(html_path,"w") as handle:
        handle.write(new_content)
    print(f"Website generated successfully! please check {html_path}")

if __name__ == "__main__":
    data = load_data('animals_data.json')
    html_path = "animals.html"
    regenerate_html(html_path, data)