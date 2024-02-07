# Lausanne public transportation network

This GitHub repository presents the results of a university thesis on the Lausanne 2024 transportation network, including a sorted GTFS dataset, modeling illustrations, and identified errors, aiming to enhance transportation simulation and planning.

## Data

Initially, the dataset includes 9 text files. Following processing, it transforms into 9 text files refined as per the methodology outlined in the [Methodology](#Methodology) section, supplemented by an additional text file detailing the precise trajectories of public transport vehicles.
These files collectively form a GTFS feed that was used for importing into the PTV VISSIM simulation software.
All filtered data are available in the folder [filtered_data](/filtered_data).

### Sources

The data were sourced from the [opentransportdata platform](https://opentransportdata.swiss/en/group), [OpenStreetMap](https://www.openstreetmap.org/), and [viageo](https://viageo.ch/).

### Organisation 

The data are structured according to the layout illustrated in the image below.

![](img/GTFS-structure.png)

## Methodology

This section details the approach adopted to filter the nine text files, removing extraneous data and isolating pertinent information. It also describes the process for reordering points within the shapes.txt file to ensure the data accurately represents the transportation network's geometry.

### Filter text files

One proposed approach for filtering the files is to follow the schema outlined below, after having previously filtered the stops.txt file using the _0_filter_stops.py_ script and the transfers.txt file using the _5_filter_transfers.py_ script.

![](img/Workflow.jpg)

### Reorder points in shapes.txt


Two methods were used to reorder the points in the shapes.txt file. Method 1 using _launcher.py_ is highly specific to the errors encountered, whereas Method 2 using _reorder_points.py_ arranges the points based on their proximity from a specified beginning input point.


## Results

In this results section, we present the outputs of our model imported into PTV VISSIM. Additional visualizations are available in the folder [model_results_visualizations](/model_results_visualizations), while a video of the model during simulation can be viewed by following the link below: [results_video](https://youtu.be/fm3Ltio2lVY).

## Authors 

This project was created by Baptiste Poffet as master thesis results presentation.


