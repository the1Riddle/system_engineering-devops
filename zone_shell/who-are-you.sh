curl -s https://learn.zone01kisumu.ke/assets/superhero/all.json | jq ".[] | select(.id == 70) | .name"
