import gmplot
gmap = gmplot.GoogleMapPlotter(23.729211164246585, 90.40874895549243,14)
gmap = gmplot.GoogleMapPlotter(23.7708680271343, 90.38098892695923,14)

gmap.marker(23.729211164246585, 90.40874895549243, color='cornflowerblue')
gmap.marker(23.7708680271343, 90.38098892695923, color='red')
gmap.marker(23.7284766533655, 90.40910864263893, color='yellow')
gmap.marker(23.728881264793493, 90.40888399782175, color='yellow')
gmap.marker(23.75363622259384, 90.39417243785537, color='yellow')
gmap.marker(23.780215725696586, 90.40895332665768, color='black')
gmap.marker(23.728917093659554, 90.40956388277749, color='white')


gmap.draw("map1.html")