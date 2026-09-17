import os
import glob
import re

html_files = glob.glob("*.html")

replacements = [
    # Change name
    (r"NEXUS<span>MODS</span>", r"VIIER<span>MODS</span>"),
    (r"Nexus Mods", r"ViierMods"),
    (r"NexusMods", r"ViierMods"),
    (r">N<", r">V<"),
    (r"NEXUSMODS", r"VIIERMODS"),
    
    # Update premium links in top banner and CTA
    (r'href="#"([^>]*)>Get Premium', r'href="/premium"\1>Get Premium'),
    (r'<button class="btn btn-primary">Upgrade Now — \$4.99/mo</button>', r'<a href="/premium" class="btn btn-primary" style="display:inline-block; margin-top:16px;">Upgrade Now — $4.99/mo</a>'),
    
    # Remove .html from local hrefs
    (r'href="(/?\w[a-zA-Z0-9_-]*)\.html(#.*)?"', r'href="/\1\2"'),
    
    # Special case: fix home links to just /
    (r'href="/index"', r'href="/"'),
]

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
        
    original_content = content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
