#!/usr/bin/env bash
cd "${0%/*}"
tr -d '[:space:]' < seed_factory_data.json > seed_factory_data_no_lines.json
tr -d '[:space:]' < seed_sprocket_types.json > seed_sprocket_types_no_lines.json