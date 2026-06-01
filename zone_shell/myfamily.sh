#!/usr/bin/env bash
curl -s https://learn.zone01kisumu.ke/assets/superhero/all.json | jq -r '.[] | select(.id == '$HERO_ID') | (.connections.relatives | gsub("\n"; "\\n"))'
