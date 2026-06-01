#!/usr/bin/env bash
ls -l | awk 'NR % 2 == 0'
