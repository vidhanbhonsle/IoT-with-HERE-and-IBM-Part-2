# Build a location aware IoT Ecosystem with HERE and IBM Cloud – Part 2

## Introduction

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

<img width="623" alt="11" src="https://user-images.githubusercontent.com/16270682/89897967-5190b880-dbf9-11ea-844f-ba0084c53599.PNG">

<img width="772" alt="111" src="https://user-images.githubusercontent.com/16270682/89898000-62d9c500-dbf9-11ea-9644-7c3c15f1736f.PNG">

2. Click Add new card. And then from the types of cards available, select Line chart under Devices.

<img width="630" alt="13" src="https://user-images.githubusercontent.com/16270682/89898020-69683c80-dbf9-11ea-80cd-0577ffc21654.PNG">

3. Select the device that will provide the data to be displayed in the card. Some card types provide an option to use another card as a data source for the data set that is displayed. This allows the data displayed on the dependent card to be filtered by selecting values on the other card. For example, the values that are included in a visualization card can be filtered by selecting which devices to display from a device list card.

4. Connect a data set. You’ll need to select the event type (status), and then configure a property by selecting the data type and entering a range of values and then clicking Next.

<img width="520" alt="15" src="https://user-images.githubusercontent.com/16270682/89898030-7127e100-dbf9-11ea-9050-c3ec2cceb13f.PNG">

5. Configure the appearance of the card, by entering size, color, and title for the card, and then click Submit to add the card to the board.

<img width="493" alt="1111111" src="https://user-images.githubusercontent.com/16270682/89898210-bd732100-dbf9-11ea-9454-d5e5997a071a.PNG">

