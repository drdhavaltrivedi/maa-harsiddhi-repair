import os
import glob

html_files = glob.glob('*.html')

favicon_tags = """
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/android-chrome-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="/images/android-chrome-512x512.png">
    <link rel="apple-touch-icon" href="/images/android-chrome-192x192.png">
"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Insert Favicon tags before </head> if not present
    if "<!-- Favicon -->" not in content:
        content = content.replace('</head>', f'{favicon_tags}</head>')
        
    with open(file, 'w') as f:
        f.write(content)
print("Updated all HTML files with Favicons!")
