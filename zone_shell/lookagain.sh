#!/usr/bin/env bash
find . -name "*.sh" -exec basename {} .sh \; | sort -r
