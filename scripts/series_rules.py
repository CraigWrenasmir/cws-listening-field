"""Series boundaries and score limits shared by composition and publishing."""
import json
from pathlib import Path
SERIES=json.loads((Path(__file__).resolve().parents[1]/'data/series.json').read_text())
def series_for(opus):
    matches=[s for s in SERIES if s['first_opus']<=opus<=s['last_opus']]
    if len(matches)!=1:raise ValueError(f'No unique study series for opus {opus}')
    return matches[0]
