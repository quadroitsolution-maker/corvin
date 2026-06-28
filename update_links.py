import re

html_file = 'regular.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

products = [
    ('Indian Army Soft Cotton T-Shirt', 'product-indian-army.html'),
    ('Indian Air Force Soft Cotton T-Shirt', 'product-indian-air-force.html'),
    ('?Flying Rafael Soft Cotton T-Shirt', 'product-flying-rafael.html'),
    ('?Nautical Miles Soft Cotton T-Shirt', 'product-nautical-miles.html'),
    ('Land Warfare Soft Cotton T-Shirt', 'product-land-warfare.html'),
    ('Indian Navy Soft Cotton T-Shirt', 'product-indian-navy.html')
]

for name, link in products:
    content = content.replace(f'<h4>{name}</h4>', f'<h4><a href="{link}" style="color: inherit; text-decoration: none;">{name}</a></h4>')
    content = content.replace(f'<h3 class="product-title">{name}</h3>', f'<h3 class="product-title"><a href="{link}" style="color: inherit; text-decoration: none;">{name}</a></h3>')
    
    # Let's also wrap the product images.
    # We can do this by regex or by specific image file.
    # It's easier just to wrap the whole image div or the image tag.

# Actually, the quickest way to make the whole card clickable or the image clickable is:
content = content.replace('<div class="product-image">', '<div class="product-image" onclick="const link = this.nextElementSibling.querySelector(\'a\'); if(link) window.location.href=link.href;" style="cursor:pointer;">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
