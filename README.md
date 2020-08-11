#Build a location aware IoT Ecosystem with HERE and IBM Cloud – Part 2

##Introduction

Purpose: To monitor a person's temperate and guide them to reach the nearest hospital in case of emergency. This will be done by tracking their location, sending them the routing instructions and showing the route on map.

This code Pattern is part two of location aware IoT Ecosystem with HERE and IBM Cloud. You will learn how to visualize the data coming from IoT device using Watson IoT platform, 
will get an overview of HERE Location Services and learn how to integrate location technology in the IoT user application to create a dashboard.  

## Pre-requisites

- Part 1 (https://github.com/vidhanbhonsle/IoT-with-HERE-and-IBM-Part-1)
- IBM Cloud account
- HERE Developer accuont
- Python installed (3.8 prefered)
- Any text editor (We are using VS Code)

## Learning outcomes

- Data Visualization 
- Integrate HERE Location Technology with App Dashboard

## Data Visualization 

Different visualizations of data help us provide a clearer picture of the events that have happened. Let’s use the Watson IoT Platform for visualizing the data that is being sent to the cloud.

To create visualizations, we’ll create a new board:

1. Go to your Watson IoT Platform dashboard, and select Create New Board.

2. Click Add new card. And then from the types of cards available, select Line chart under Devices.

3. Select the device that will provide the data to be displayed in the card. Some card types provide an option to use another card as a data source for the data set that is displayed. This allows the data displayed on the dependent card to be filtered by selecting values on the other card. For example, the values that are included in a visualization card can be filtered by selecting which devices to display from a device list card.

4. Connect a data set. You’ll need to select the event type (status), and then configure a property by selecting the data type and entering a range of values and then clicking Next.
