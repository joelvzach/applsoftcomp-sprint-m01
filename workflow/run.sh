#!/bin/bash
uv sync
uv run python process_mortality.py
uv run python process_gdp.py
uv run python merge.py
uv run python create_visualization.py