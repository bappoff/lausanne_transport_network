# Lausanne public transportation network

This GitHub repository presents the results of a university thesis on the Lausanne 2024 transportation network, including a sorted GTFS dataset, modeling illustrations, and identified errors, aiming to enhance transportation simulation and planning.

## Data

The data consist of 10 text files. These files collectively form a GTFS feed that was used for importing into the PTV VISSIM simulation software.

### Sources

The data were sourced from the [opentransportdata platform](https://opentransportdata.swiss/en/group), [OpenStreetMap](https://www.openstreetmap.org/), and [viageo](https://viageo.ch/)

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