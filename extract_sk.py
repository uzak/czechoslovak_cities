# Author   : Martin Užák <martin.uzak@gmail.com>
# Creation : 2020-06-15 13:07

import csv
import json
from text_unidecode import unidecode

result = []

with open("./mesta_sk.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[1].strip()
        city = dict(
            name = name,
            name_ascii = unidecode(name),
            name_de = row[2].strip(),
            name_hu = row[3].strip(),
            population = int(row[4].replace(' ', '')),
        )
        result.append(city)

print(json.dumps(result))
