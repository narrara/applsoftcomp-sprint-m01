#!/bin/bash
uv sync
uv run python workflow/process_mortality.py
uv run python workflow/process_gdp.py
uv run python workflow/merge_data.py
uv run python workflow/create_visualization.py