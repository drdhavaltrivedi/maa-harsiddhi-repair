import os
import glob

html_files = glob.glob('*.html')

geo_tags = """
    <!-- GEO Meta Tags -->
    <meta name="geo.region" content="IN-GJ">
    <meta name="geo.placename" content="Ahmedabad">
    <meta name="geo.position" content="23.0338;72.6120">
    <meta name="ICBM" content="23.0338, 72.6120">
"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace links
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')
    content = content.replace('href="contact.html"', 'href="/contact"')
    
    # Insert GEO tags before </head>
    if "<!-- GEO Meta Tags -->" not in content:
        content = content.replace('</head>', f'{geo_tags}</head>')
        
    with open(file, 'w') as f:
        f.write(content)
print("Updated all HTML files with clean URLs and GEO Meta tags!")
