curl -s https://learn.zone01kisumu.ke/assets/superhero/all.json | jq -r ".[] | select(.id == 170) | .name, .powerstats.power, .appearance.gender"
