# lausanne_transport_network
Ce dépôt GitHub présente les résultats d'un mémoire universitaire sur le réseau de transport de Lausanne 2024, incluant un jeu de données GTFS trié, des illustrations de modélisation et les erreurs identifiées, visant à améliorer la simulation et planification des transports.






Acces the site live: [https://melindafemminis.github.io/covid-europa-dataviz/](https://melindafemminis.github.io/covid-europa-dataviz/)

![](img/project_1.png)

## Data 

### Sources

The COVID-19 statistics used in this project comes from [https://github.com/owid/covid-19-data/tree/master/public/data](https://github.com/owid/covid-19-data/tree/master/public/data). It is a publicly available dataset that is updated daily by [Our World Data](https://ourworldindata.org/coronavirus). The provide relevant informations about the pandemic such as *reproduction rate*, *vaccination*, *policy responses* and more. We choose to focus on two of those, **confirmed cases** and **confirmed deaths**. 

The basemap used is [World Terrain Base](https://www.arcgis.com/home/item.html?id=c61ad8ab017d49e1a82f580ee1298931) from ERSI. 

The coutries layer is a [geoJSON file ](https://github.com/leakyMirror/map-of-europe), modified to only keep European countries. 

### Organisation 

All the information is in the geoJSON file. After deleting coutries outside of Europe, the COVID-19 statistics were added directly in the file, so they are directly available when a coutry is selected. 

## Functionnalities

Here are the different ways users can interact with the map: 

- move the map with the mouse by click-and-drag, zoom in and out
- see what coutry the mouse is hovering on in the top right side of the map box
- select a country:
	- either by clicking on it
	- or by search for it with the serach box on the left
- switch between cases and deaths to see the corresponding barplot
- hover on the bars to highlight a particular month
- Reset everything with a button

![](img/project_2.png)

# Tools and librairies

- [Leaflet](https://leafletjs.com) to display the map and navigation functions
- [D3](https://github.com/d3/d3) to build the graph in the right sidebar 
- [www.geojson.io](www.geojson.io). to edit the geojson files

## Authors 

This project was created by Baptiste Poffet and Melinda Femminis for the course "Visualisation de données" given by Isaac Pante at UNIL. 