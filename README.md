# Drone Engineering Ecosystem   
![DEE_software_architecture](https://user-images.githubusercontent.com/100842082/209946685-f3dc19d6-f781-4703-a0da-52a5e6a85fe6.png)

## 1. General description

The Drone Engineering Ecosystem is a software tool that allows controlling the operation a drone platform in different ways and using different types of devices and applications. Look at the figure to see the software architecture and the technologies and tools involved.   

Some of the modules run on board (the red box in the figure). These modules control the different devices of the drone platform (the autopilot, camera, LEDs, servo, etc.). Some others are front-end applications that allow the user to control the drone (specifying flight plans, showing the images send by the drone, etc.). Finally, some modules are the back-end for data storage and recovery. These modules communicate through MQTT brokers (one internal running on board, and one external running in internet).   

The modules of the ecosystem are in development. Each of them a repo in GitHub with the code and detailed information. This is a brief description of each module:   

* *Dashboard*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-dashboard-brightgreen.svg)](https://github.com/dronsEETAC/DashboardDEE) a desktop application that a desktop application (Python + tkinter) that allows the global control of the system (define flight plans, process data comming from the drone, arm, take-off, etc.).
   
* *DashApp*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-dashboard-brightgreen.svg)](https://github.com/dronsEETAC/DashboardDEE) a web app (Vue) with similar functionalities that the Dashboard, but that can be operated from a laptop connected to internet.
   
* *Drone Circus*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-dashboard-brightgreen.svg)](https://github.com/dronsEETAC/DashboardDEE) a desktop application (Python + tkinter) that allows the user to interact with the drone platform in a fun way (for instance, guide the drone with body poses or with the voice).


* *Mobile app*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-mobileapp-brightgreen.svg)](https://github.com/dronsEETAC/DroneMobileAppDEE) a web app (Vue + Ionic) with a reduced set of functionalities that can be operated from a mobile phone or Tablet connected to internet. 
 
* *Autopilot service*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-autopilot-brightgreen.svg)](https://github.com/dronsEETAC/DroneAutopilotDEE) an on-board module that controls the autopilot to execute the commands coming from other modules (arm, takeoff, go to position, etc.).    

* *Camera service*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-cameracontroller-brightgreen.svg)](https://github.com/dronsEETAC/CameraControllerDEE) an on-board module that controls the on-board camera to execute the commands coming from other modules (take a picture, get the video stream, etc.)       
   
* *LEDs service*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-ledscontroller-brightgreen.svg)](https://github.com/dronsEETAC/LEDsControllerDEE) an on-board module that controls the LEDs of the drone platform to inform of the status of the drone platform, or a servo installed in the platform, as required by other modules.        
* *Monitor*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-gate-brightgreen.svg)](https://github.com/dronsEETAC/GateDEE) records on board data for future analysis (for instance, all the messages send through the brokers.    

* *API REST*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-apirest-brightgreen.svg)](https://github.com/dronsEETAC/RESTAPIDEE) a server that provides data storage and retrieval through HTTP basic operations (GET, POST, PUT, DELETE).      

* *Data service*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-dataservice-brightgreen.svg)](https://github.com/dronsEETAC/DataServiceDEE) controls the data storage and retrieval in the API REST, as required by the rest of modules.

In addition to these modules, the ecosystem uses:
1. An internal broker (Mosquitto) running on-board to facilitate the communication among on-board services.
2. An external broker (Mosquitto) running in internet to facilitate the communication between front-end and back-end modules and the drone platform.
3. The Mission Planner, that is used for development purposes, since it provides an autopilot simulator, so that the ecosystem can be developed and tested without requiring a real drone platform. 
   
## 2. A case example
The best way to understand how the Drone Engineering Ecosystem works is through an example.
Let's imagine a user who wants the drone to scan a certain surface and take photos at certain points. Using the Dashboard the user can prepare the mission by indicating the waypoints to visit and the points where a photo should be taken. From the Dashboard it will send the flight plant to the Autopilot service instructions to the Camera service on when to take the photos. Then, already at the site where the mission must be carried out, the user can use the mobile application to give the order to start the flight plan. From this application the user can also make decisions in an emergency (stop, land, return home, etc.). In addition, on the mobile phone the user can see the photos that the drone is taking. Those photos are also sent to the data service which stores them in the database for further analysis.   
    
Now imagine that the user does not want to receive all the photos, but only those in which a certain object appears (for example, a car). Also, the user wants the selected photos to be stored on-board and download and process them once the drone has landed. These additional functionalities may require the development of additional modules, such as an image processing service and a data storage and retrieval service, both on board.

## 3. The drone platform
The drone platform can be seen in the figure. It uses a HexSoon kit for the frame and motors, an Orange Cube Pixhawk as flight controller and a Raspberry Pi as on board computer (the red box). The platform includes also a camera, a servo, a button and a collection of LEDs.   

![dron](https://user-images.githubusercontent.com/100842082/209948305-c1f2e4dc-2606-4259-bf78-930cb6b44510.jpg)

    
A detailed guide on how to assemble, configure and tune up the drone platform can be found here:
[TransversalProjectGuide.pdf](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/files/10319359/TransversalProjectGuide.pdf)

 
## Demo   
[Drone Engineering Ecosystem demo](https://www.youtube.com/playlist?list=PL64O0POFYjHpXyP-T063RdKRJXuhqgaXY)    
      
## Dasboard   
The dashboard is implemented in Python using Tkinter, that is a library to develop graphic user interfaces (GUI).   
A nice course on Tkinter can be found here:   
[Tkinter](https://www.youtube.com/watch?v=YXPyB4XeYLA)   

## Mobile app   
The mobile app is implemented in Python using Kivy, that is another library to develop GUI,
but more suitable for mobile devices. A nice course on Kivy can be found here:   
[Kivy](https://www.youtube.com/watch?v=l8Imtec4ReQ)   
 

## Brokers   
Both the local and the global brokers use the MQTT protocol based on publication-subscription mechanism. 
These are implemented using Mosquitto, that automatically generates the broker.    
In the development environment, both the local and the global broker are run in the localhost, 
the global broker in port 1884 and the local broker in port 1883. The basics of MQTT can be found here:   
[MQTT](https://www.youtube.com/watch?v=EIxdz-2rhLs)   
More information about Mosquitto and how to install it in Windows and in Linux can be found here:
[Mosquitto](https://www.youtube.com/watch?v=DH-VSAACtBk)      
This is a good example to start using MQTT (using a public broker):    
[Example](https://www.youtube.com/watch?v=kuyCd53AOtg)   

## API Rest   
The API Rest module has been build using the Flask framework. A very simple and clear example on how to use Flask
(in Spanish) can be found here:    
[Flask](https://youtu.be/Esdj9wlBOaI)

## Supporting materials   
[Transversal project guide](https://github.com/miguelvalero/DroneEngineeringEcosystem/blob/main/TransversalProjectGuide.pdf)   
[Deploy the APP in an Android Mobile Phone](https://youtu.be/0-c6p1GblVc)     


## Tools required   
### Git and GitHub   
We use Git and GitHub to have the software available to everybody in the cloud, to manage different versions
of the software and to organize the integration of the contributions of different participants in the project.   
Create a GitHub account if you do not have one.    
[GitHub](https://github.com/)      
Install git in your computer.     
[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)      
It is not recommended to install Gui Client because most of the time, if you are a developer,
you may want to work with command lines instead of GUI programs.      
Run these commands in a terminal, for some initial configurations:
```
git config --global user.name "Your name"
git config --global user.email youremail@domain.com
```

### Mosquitto     
Download Mosquitto broker:      
[Mosquitto](https://mosquitto.org/download/)    

In the folder where mosquitto has been downloaded, create two configuration files named "mosquitto1883.conf"
and "mosquitto1884.conf". Include the following lines in these files:
In "mosquitto1883.conf", that will be the local broker:   
```
listener 1883
allow_anonymous true
```
In "mosquitto1884.conf", that will be the global broker:
```
listener 1884
allow_anonymous true
```
You can start running the local broker with this command (from a terminal opened in the mosquitto folder):
```
 .\mosquitto -c mosquitto1883.conf
```
     
Do the same to start the global broker, from another terminal.

### Mission Planner     
Download and install the latest Mission Planner installer:      
[Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)     


### Python
You will need two versions of Python: python2.7 for the autopilot module and python3.7 for the rest:       
[python3.7](https://www.python.org/downloads/release/python-370/)    
[python2.7](https://www.python.org/downloads/release/python-2718/)    


### PyCharm 
PyCharm is the recommended IDE for development in Python.   
[PyCharm](https://www.jetbrains.com/pycharm/)   

Configure the system interpreter (the versions of python to be used). See this guide:   
[Configure interpreter](https://www.jetbrains.com/help/pycharm/configuring-local-python-interpreters.html)   
      
You will have to install some packages during development. Look at this guide for this:        
[Installing packages](https://www.youtube.com/watch?v=zCO3KxV2zPI&ab_channel=PhilParisi)     

## Drone Engineering Ecosystem installation   
Follow these steps:     
     
Log-in in your GitHub account. Then make a fork from the Drone Engineering Ecosystem repository. 
Now you have a copy of the original repository in your account. We will refer to this repository as "forked".     
[How to fork](https://user-images.githubusercontent.com/99663441/154680663-996139d2-17c7-4630-b338-9a1f53b1ff8d.gif)    



Clone the forked repository in your computer:   
```
   git clone (URL of forked)
```
      
Now you have created the "local" repository. The system has created a connector between the local repository
and the original. The connector is named "origin". See this with this command:
```
   git remote -v
```
      
Now change the name of the connector:
```
   git remote rename origin forked
```
     
Create a new connector between the local repository and the original:
```
    git remote add origin https://github.com/miguelvalero/DroneEngineeringEcosystem
```
     
Check that now you have two connectors: "forked" connects your local repository with the forked one, 
and "origin" connects the local with the original:
```
   git remote -v
```

## Procedure for contributions 
Contributions must be integrated in the original repo only after exhaustive test of correctness.     

These are the steps for contributing, assuming that you have cloned the projects, as indicated in the previous section.     

1. Create a branch for your developments:
```
  git checkout –b dev
```
          
2. Develop whatever you want to develop, and test until you are sure that everything is correct.
          
3. Commit the changes:
```
  git add .
  git commit –m “Description of your development”
```
                   
4. Push the changes to your forked repo:
```
  git push forked dev
```
           
5. From the dev branch of forked repo, make a pull request to integrate the changes into origin. 
It is important to make sure that the changes are integrated into the main branch of origin. 
Clearly describe the developments made. When making the pull request, 
it will be indicated if there are conflicts or not. If there are no conflicts accept the pull request. 
If there is a conflict then try to resolve the conflicts or contact one of the responsible teachers 
if you have difficulties to do so.
           
6. Download in your local repo the result of the integration:
```
  git checkout main
  git pull origin main
```
         
7. Check that everything is running ok in the new version (which may contain recent developments from other contributors).
             
8. Unload the new version to your forked repo:
```
  git push forked main
```
9. Remove development branches:
```
   git branch -d dev
   git push forked --delete dev
 ```
