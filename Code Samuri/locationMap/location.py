import gmplot

# Create the map plotter:
apikey = '' # (your API key here)
gmap = gmplot.GoogleMapPlotter(23.729211164246585, 90.40874895549243, 14, apikey=apikey)

# Mark a hidden gem:
gmap.marker(23.729211164246585, 90.40874895549243, color='cornflowerblue')

# Highlight some attractions:
attractions_lats, attractions_lngs = zip(*[
    (23.729211164246585, 90.40874895549243),
    (23.801862310944188, 90.35700996898726),
    
])
gmap.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=False)

# Outline the Golden Gate Park:
golden_gate_park = zip(*[
    (23.729211164246585, 90.40874895549243),
    (23.801862310944188, 90.35700996898726),
    (23.768773179764562, 90.37269632665758),
    (23.733211657612223, 90.40993638432778),
    (23.728881264793493, 90.40888399782175),
    (23.728881264793493, 90.40888399782175),
    (23.75363622259384, 90.39417243785537),
    (23.780215725696586, 90.40895332665768),
    (23.728407931193587, 90.40787482665709),
    (23.7284766533655, 90.40910864263893),
    (23.7284766533655, 90.40910864263893)
])
gmap.polygon(*golden_gate_park, color='cornflowerblue', edge_width=10)

# Draw the map to an HTML file:
gmap.draw('map.html')