# Author   : Martin Užák <martin.uzak@gmail.com>
# Creation : 2020-06-15 13:07

import csv
import json
from text_unidecode import unidecode

result = []

with open("./mesta_cz.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[2]
        population = row[3]
        if not name:
            continue
        city = dict(
            name = name,
            name_ascii = unidecode(name),
            population = int(population)
        )
        result.append(city)

print(json.dumps(result))
