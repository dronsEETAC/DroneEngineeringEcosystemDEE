# Drone Engineering Ecosystem     

<img width="1991" height="1094" alt="Image" src="https://github.com/user-attachments/assets/d91ff2e1-0878-46ee-ad8b-3faa3c06ecb6" />


## 1. General description
  
The Drone Engineering Ecosystem is a software tool that allows controlling the operation of a drone platform (or several drons simultaneously) in different ways and using different types of devices and applications. Look at the figure to see the software architecture and the technologies and tools involved.    

Some of the modules run on board (the red box in the figure). These modules control the different devices of the drone platform (the autopilot, camera, LEDs, servo, etc.). The software onboard is packaged in a Docker container to facilitate installation.   
    
Some others modules are front-end applications that allow the user to control the drone (specifying flight plans, showing the images send by the drone, etc.). There are three types of front-end applications. Desktop applications must be installed in the laptop that is used as ground station. Desktop applications control the drone directly or through the software on board. Some of the application allow to define and execute flight plans, process the video stream from the drone or guide the drone with body poses. Desktop applications are developed in Python of in C#.   
   
Web app allow controlling the drone from any mobile device (phones or tablets). No installation in the device is required. Only internet connection to access the web server. This is ideal to allow visitors to our Drone Lab interact with the drone using their mobile phones, guiding the drone with a set of buttons or with their voice. Usually a web app communicates with a Desktop application through a broker or a web sockect, since it is the laptop that is connected to the drone to send it the commands (or receive telemetry info) as required by the web apps. Web apps are develped in Flask or in Vue.    

Native applications are developed specifically for mobile devices so that they can leverage device-specific features and offer optimal performance. Native applications are developed using Android Studio, Java, Kotlin and Flutter.    
    
Finally, some modules are the back-end for data storage and recovery.  

In addition to these modules, the ecosystem uses:
1. An internal broker (Mosquitto) running on-board to facilitate the communication among on-board services.
2. An external broker (any public broker or a specific UPC broker) running in internet to facilitate the communication between front-end and back-end modules and the drone platform.
3. The Mission Planner, that is used for development purposes, since it provides an autopilot simulator (SITL), so that the ecosystem can be developed and tested without requiring a real drone platform. 

The modules are organized into blocks, depending on the technologies used for their development. For each block there is a GitHub repo where the code of the different modules belonging to the block can be found together with information about the technologies used (installation instructions, tutorials, demos, etc.). These are the repos of the different blocks:

* *On board*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-OnBoard-orange.svg)](https://github.com/dronsEETAC/DEE_OnBoard) Modules that run on board (shown in the red box of the figure).


* *Desktop applications*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Desktop-orange.svg)](https://github.com/dronsEETAC/DEE_DesktopApplications) Front-end modules developed using Python and Tkinter (or CustomTkinter) or in C# as GUI.

* *WebApps*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-WebApps-orange.svg)](https://github.com/dronsEETAC/DEE_WebApps) Front-end modules in the form of WebApp, developed using Vue and Ionic or Flask.

* *Android Apps*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Android-orange.svg)](https://github.com/dronsEETAC/DEE_Android) Front-end modules developed for Android native using Java or Kotlin.

* *Flutter Apps*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Flutter-orange.svg)](https://github.com/dronsEETAC/DEE_Flutter) Front-end modules developed using Flutter.

* *Back End*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-BackEnd-orange.svg)](https://github.com/dronsEETAC/DEE_BackEnd) Modules that serve as on hearth back end for computation and data storage and retrieval.

Fnnally, the following is a list of complementary modules that can be usefull for different developments. For each of these complementary modules there is a repo with detailed explanations, examples, codes, and demos.       
    
* *Object recognition with neural network*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Object_recognition-blue.svg)](https://github.com/dronsEETAC/ObjectRecognitionWithNN) Tutorials and demos on how to use Yolov5 to train a neural network for object recognition and integrate it into the ecosystem
* *Flying Indoor*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Flying_Indoor-blue.svg)](https://github.com/dronsEETAC/DashIndoor.git) How to configure the dron to fly indoor with stability and navegability. Includes an dashboar application to control the dron.
* *DronLink library*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-DronLink-blue.svg)](https://github.com/dronsEETAC/DronLink.git) Our own library to control the drons aimed at replacing DroneKit.
* *CameraLink library and webSockets*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-CameraLink-blue.svg)](https://github.com/dronsEETAC/CameraLink.git) Our own library to control the camera. Includes material to learn how to communicate videostream via websockets.
* *Joystick*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Joystick-blue.svg)](https://github.com/dronsEETAC/Joystick.git) How to control the drone with a joystick (a real one or a virtual one in the form of web app).
* *csDronLink*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-csDronLink-blue.svg)](https://github.com/dronsEETAC/csDronLink.git) A version of dronLink in C#.
* *Phone sensors*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Sensors-blue.svg)](https://github.com/dronsEETAC/Sensors.git) How to get information from the mobile phone sensors (giroscope, GPS, accelerometer) using a Flask web app and use this information to control the drone.
* *Unity*:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Unity-blue.svg)](https://github.com/dronsEETAC/Unity.git) How to use Unity in the context of the ecosystem (includes a demo application with some augmented reality).
   
## 2. A case example
The best way to understand how the Drone Engineering Ecosystem works is through an example.
Let's imagine a user who wants the drone to scan a certain surface and take photos at certain points. Using the Dashboard the user can prepare the mission by indicating the waypoints to visit and the points where a photo should be taken. From the Dashboard the flight plan will be sent to the Autopilot service and instructions to the Camera service on when to take the photos. Then, already at the site where the mission must be carried out, the user can use the mobile application to give the order to start the flight plan. From this application the user can also make decisions in an emergency (stop, land, return home, etc.). In addition, on the mobile phone the user can see the photos that the drone is taking. Those photos are also sent to the data service which stores them in the database for further analysis.   
    
Now imagine that the user does not want to receive all the photos, but only those in which a certain object appears (for example, a car). Also, the user wants the selected photos to be stored on-board and download and process them once the drone has landed. These additional functionalities may require the development of additional modules, such as an image processing service and a data storage and retrieval service, both on board.

## 3. The drone platform
The drone platform can be seen in the figure. It uses a HexSoon kit for the frame and motors, an Orange Cube Pixhawk as flight controller and a Raspberry Pi as on board computer (the red box). The platform includes also a camera, a servo, a button and a collection of LEDs.   

![dron](https://user-images.githubusercontent.com/100842082/209948305-c1f2e4dc-2606-4259-bf78-930cb6b44510.jpg)

A detailed guide on how to assemble, configure and tune up the drone platform can be found here:
[TransversalProjectGuide.pdf](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/files/10319359/TransversalProjectGuide.pdf)

## 4. Demos   
This is a tutorial with and introduction to the ecosystem organization and an example on how to install and run some of the modules.
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-Introduction_tutorial-pink.svg)](https://www.youtube.com/playlist?list=PLyAtSQhMsD4o6s7OSD32KVOksonKDSRJ-)     

Go to the repos of the different front-end applications (Drone Circus, Dashboard or Mobile App) for other nice demos.

## 5. Communication modes
In relation to communication system, the Drone Engineering Ecosystem can work in three modes.    
      
![global](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/a6ab5a73-8448-4023-bb1e-1127afd8e195)
      
In global communication mode it is assumed that the drone platform, the front-end and back-end modules are all connected to the internet and communicate through an external broker. Any public access broker can be used as external broker, or the  private broker that runs on a server at the Campus facilities (which requires access credentials).   
      
![local](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/9a9aa1e1-9f9f-4b2a-9b17-1a3800665d2a)
      
When there is no internet coverage, then local mode can be used. In this case, the front-end module (for example, the Dashboard) must connect to the WIFI access point provided by the on-board computer. In this case, the external broker is also executed on-board. On-board modules connect to this broker at localhost:8000 but external modules should connect to 10.10.10.1:8000. Naturally, in local mode it is not possible to use the back-end services that are only operational when there is an internet connection.   

![direct](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/7cd7b2de-eccf-4fae-904b-3f41ae4bd3bf)
      
Finally, it is also possible to work in direct mode, which is the only possibility if there is not on-board computer. In direct mode, the autopilot service (am also the external broker) in run as a part of the front-end application and connects directly to the autopilot via the telemetry radio.     

A detailed description of commuinication modes and how to configure the modules in each case can be found here:
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-communication_modes-pink.svg)](https://www.youtube.com/playlist?list=PLyAtSQhMsD4qeEJ6uV70C_faX7WYyW5_R)
    
More details on the brokers required to support the communication modes in the Drone Engineering Ecosystem can be found in section 8.
      
## 6. Operation modes
The system can be run in production mode and in simulation mode. The production mode corresponds to the actual execution of the missions. Naturally, in that case the on-board services must be run on the on-board computer. Section 7 provides some important details on how to start the on-board services.   
    
In simulation mode all modules (including brokers) run on the same computer (for example, a laptop). In this case, Mission Planner is needed, which incorporates a simulator that will be controlled by the Autopilot service exactly as it would be in production mode. Simulation mode is ideal to develop and test the applicacions before moving to production mode.    

Review the videos on communication modes for details on how to configure also the operation mode:    
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-communication_modes-pink.svg)](https://www.youtube.com/playlist?list=PLyAtSQhMsD4qeEJ6uV70C_faX7WYyW5_R)

## 7. Swarm mode
Some of the front-end applications can work with a swarm of drones. For instance, a swarm of drones can complete in less time the scanning of a certain area.   

A swarm of drones can also work in different communication and operation modes.    

![global_swarm](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/ada86b73-2daf-4b39-8d38-2bdc8df88f93)   
    
In global communication mode all drones are connected via internet to the external broker. The front-end application will specify in the topic of its publications which drone is the destination of the command.    

![local_swarm](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/0c8fad74-938e-479d-84f1-3c0892221207)

In local communication, all drones and also the front-end device (laptop or mobile phone) are connected to a router. Then the autopilot of every drone connects to the external broker running in the front-end device. Again, the front-end application will specify in the topic of its publications which drone is the destination of the command.    

![direct_swarm](https://github.com/dronsEETAC/DroneEngineeringEcosystemDEE/assets/100842082/d24c1315-58ed-4c37-8c34-685f36fcf11a)

In case of direct communication, we must connect to the front-end device the telemetry radios of every drone in the swarm. The front-end application must run one instance of the autopilot services per dron, all of them connected to the external broker, that will also run in the front-end device.  

A swarm can also be operated in simulation mode. Watch this video for some key points regarding this issue.       
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-swarm_simulation-pink.svg)](https://www.youtube.com/watch?v=nUItdJ4_QTA)

## 7. The MQTT communication protocol
The Drone Engineering Ecosystem uses Mosquitto brokers to facilitate the communication among the different modules. Mosquitto brokers implement the MQTT (Message Queuing Telemetry Transport) communication protocol. You can learn more about MQTT here: 
[MQTT protocol](http://www.steves-internet-guide.com/mqtt/)
 
MQTT is based on a simple publication/subscription mechanism. Let's see how this protocol is used in the Drone Engineering Ecosystem. Assume that all the modules are connected to a Mosquitto broker. The Autopilot Service may subscribe to the following topic:
```
dashboard/autopilotService/takeOff
```
If the Dashboard publishes a message in the broker with exactly this topic, the Autopilot Service will run a function where (presumably) it will send the command to the drone to take off. In some case, the published message will include additional information requited by the subscriptor. For instance, the Autopilot Service may require a value indicating the altitude to be reached in the take off operation. The additional information is included in the payload of the message.   
The Autopilot Service may want to inform the Dashboard that the drone has reached the required altitude. In this case, it will publish a message with the following topic:
```
autopilotService/dashboard/takenOff
```
Obviously, the Dashboard must have subscribed this topic in order to receive the message.  

Note that our convention for the topic format is: 
```
name_of_the_origin_module/name_of_the_destination_module/command
```

We can imagine that the Autopilot Service must be ready to accept commands from any of the modules of the ecosystem (not only from the Dashboard) and not only the takeOff command. So the Autopilot Service must subscribe this topic: 
```
+/autopilotService/+
```
indicating the it can accept any command from any module. Obviously, the function that runs when a message is received must analyze the topic to identify the origin module and the command required (and possibly extract the payload it the message is coming with additional data).
  
In the repo of echo of the service modules of the ecosystem you will find detailed information on the topic format for each of the services provided by the module.


## 8. Tools requiredregardless of the type of contribution to be made
You will requiere quite a few tools in order to contribute to the Drone Engineering Ecosystem. In this section you will find information about general tools requiered, regardless of the type of contribution to be made. Other tools will be required depending on the type of contribution. The information on these tools can be found in the corresponding repos.

### Git and GitHub
We use Git and GitHub to have the software available to everybody in the cloud, to manage different versions of the software and to organize the integration of the contributions of different participants in the project. So create your owno account in GitHub and install Git in your computer.

### Mosquitto
As you can see in the figure showing the communication modes, two brokers are needed: the internal and the external broker.   
The internal broker will be always run in localhome, port 1884, in your laptop when working in simulation mode and in the on board computer when working in production mode.  Use this configuration to start the internal broker:
User this configuration file to start the internal broker:
```
listener 1884
allow_anonymous true
```
The external broker must use the websocket protocol. Moreover, when running secure WebApps, the communication with the external broker must use secure websockets.   
When internet is available (for instance, when using global communication mode) we can use as external broker one of the brokers shown in the table:


Name | port | protocol | notes 
--- | --- | --- | --- 
broker.hivemq.com | 8000 | websockets| 
broker.hivemq.com | 8883 | secure websockets| In case of using secure WebAppsSeconds 
classpip.upc.edu | 8000 |  websockets| Requiere credentials provided by the DEE academic responsible 
classpip.upc.edu | 8884 |  secure websockets|  In case of using secure WebApps. Requiere credentials provided by the DEE academic responsible 


When internet is not available (for instance, when using local or direct communication modes) a mosquitto broker must be running on board or in localhost. The required configuration for this mosquitto broker is that:
```
listener 1883
listener 8000
protocol websockets
socket_domain ipv4
allow_anonymous true
```

Note that in this case we do not need secure websockets since WepApp (which require secure websockets) will allways operate with internet available and any of the brokers in the table above can be used in this case.
   
There are many tutorial in internet on how to install and configure Mosquitto in Ubuntu and in Windows. See below for tutorial materials on MQTT and Mosquitto.    

Communication via Mosquitto brokers use the MQTT protocol, based on publications and subscriptions, as described in section 7.

### Mission Planner
Download and install the latest version of Mission Planner.
We have recently encountered a problem starting the simulator included in Mission Planner. The system indicates that it cannot find the dll file *cyggcc_s-seh-1.dll*.
The problem is easily solved by downloading that dll from here (https://www.dll-files.com/cyggcc_s-seh-1.dll.html) and placing the file in the folder:
```
D:\Users\usuario\Documents\Mission Planner\sitl
```
     
## 9. Contributions
Students contribute to the development of the Drone Engineering Ecosystem by doing their TFG/TFM. There are three modalities of work: individual, in small group or in a larger group with SCRUM methodology.   
   
The individual modality is the usual one. The student develops the work individually according to the objectives established with the tutors. In the small group mode, students form groups of 2 or 3, work as a team, organizing the tasks to their liking, although presenting individual reports at the end (which probably have a good part in common). The oral presentation will also be joint. This modality is ideal for working with colleagues with whom there is a good understanding.   
   
In the SCRUM modality, students are grouped into larger groups (4 or more), even if they have not worked together before (or even know each other). The work is carried out according to the guidelines of the agile SCRUM methodology, advancing by sprints. Finally, each student presents the report that describes their contribution to the group's work. The final presentation can be individual or in small groups of students who have worked more closely in the different sprints.

## 10. Contribution protocol
Contributions must follow the protocol described in this section. Two cases are considered: individual contribution and team contribution.    

### Individual contribution
The figure shows the sequence of steps involved in an individual contribution.   
![individualContribution (1)](https://user-images.githubusercontent.com/100842082/215315504-4077ce55-8ab7-41d4-81af-c6f703c14e16.png)     

These two videos show an example.   
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-contributions(1)-pink.svg)](https://youtu.be/MWoIC6T-5m4) 
[![DroneEngineeringEcosystem Badge](https://img.shields.io/badge/DEE-contributions(2)-pink.svg)](https://youtu.be/jSS6Q2iIurU)


In the first video the individual contribution does not have any conflict. In the second video some conflicts arise. In the following every step shown is these videos is described. While watching the videos you must have in mind the figure.    

*Demo part 1: Contribution without conflicts*
1. Miguel forks the original repo for the CameraController into his own github account (personal repo)
2. Clones his personal repo into a folder in his laptop (local repo)
3. Opens PyCharm and creates a new project with the cloned code (build project with existing resources)
4. The project requires the installation of several libraries, identified in the file requierements.txt. These libraries
are installed.
5. When running the code, a library is missing. It was not in requirements.txt. This library must also be installed. During
the development new libraries may be also needed and installed.
6. After the missing library is installed, the code runs well.
7. A new branch dev is created for the new development.
8. The pre-commit is installed. This tool will verify that the code satisfies a few code quality rules.
9. The development is very simple: just change the text of a topic in a subscription and include a line of text in the README.md file
10. When trying to commit the changes an error occurs. This is because the pre-commit has not be run before the commit.
11. Among other verifications, pre-commit checks that there are not trailing spaces at the end of lines and checks
that there is a single blank line at the end of every file. Note that this is not the case for the README.md file. The pre-commit corrects this.
12. After pre-commit, the commit is successful and the code is pushed into the personal repo. In the case of more elaborated developments, pre-commits and commits must be done frequently, before pushing the code to the personal repo.
13. A new branch dev is automatically created in the personal repo containing the development. It is time to do a pull request from this dev branch
into the main branch of the original repo. There are not conflicts and the pull request can be confirmed.
14. Note that the pre-commit checks are done again to assure that the merged code fulfils the code quality rules.
15. The owner of the original repo finds a pull request from Miguel. Since there are not conflicts the code can be merged into the main branch.
16. Miguel deletes the dev branch from both the local and the personal repos.
17. The personal repo is synchronized with the original repo and local repo is synchronized with the personal repo. Everything is ready for a new contribution.

*Demo part 2: Contribution with conflicts*
1. Miguel realizes that the requirements.txt file was not updated with the reference to the new library that was installed. A new dev branch is created
for the new development.
2. The requirements file is updated and a new line of text is included in the README.md file to clarify the nature of the new contribution.
3. A new pull request is created from the dev branch of the personal repo into the main of the original one. However, in this case a conflict appears.
4. The conflict appears because other people has contributed to the same code while Miguel was preparing his new contribution.
5. Miguel has the option to resolve the conflict, that appears in the README.md file. Note that github shows the differences between the codes to be merged.
In some cases, the author of the contribution may not have all the information to solve the conflict (or may have doubts). In this case the conflict will be resolved by the owner of the original repo.
6. Note that after marking the conflict has solved Miguel forgets to push the commit merge green button. This is the reason he has to repeat the operation of rearranging the README.md file to solve the conflict.
7. The owner of the original repo finds the new pull request by Miguel. In this case the pre-commit checks are not fulfilled. When rearranging the README.md file Miguel did not take into account
the rules (no trailing spaces and only one blank line at the end of the file).
8. After correcting this the owner can merge the code. 
9. The end of the history is the same as in part 1: Miguel deleted dev branches and synchronizes repos.
 
Note that in the case of long developments, the contributor may want to push frequently his local repo into his personal repo, just to have an updated copy of the development safe in the cloud.

### Team contribution
The protocol in case of a team contribution is similar, as shown in this figure (no demo videos are needed in this case).    
![teamContribution (1)](https://user-images.githubusercontent.com/100842082/215315553-b54a43ca-fd3f-4436-93f1-a18b47848fdd.png)    

Just note that:
1. The original repo is forked into the personal repo of one member of the team (personal #1 in the figure).
2. All members of the team clone the personal #1 repo into their laptop and creates a development branch. ATTENTION: they must use different names for the development branches.
3. Team members develop with frequent pre-commit, commit and pushed into the personal #1 repo (only shown for member #3 in the figure).
4. Push of different members creates different dev branches in the personal #1 repo. The team should merge all these branches into a single one before contributing to the original repo.
5. Merging development branches into a single one may cause conflicts that must be solved by the team in order to merge all the developments into a single branch. In the figure, all developments are merged into branch dev1. Then a pull request from dev1 into main in the original repo is generated.
This pull request may generate conflicts that must be resolved (maybe with the help of the original repo owner).
6. Finally, all repos are synchronized.



## 11. Supporting materials   
     
Mosquitto installation and configuration:      
[Installing Mosquitto in Ubuntu](http://codigoelectronica.com/blog/instalar-mosquitto-ubuntu)      
[Mosquitto configuration](http://www.steves-internet-guide.com/mossquitto-conf-file)
   
The basics of MQTT can be found here:   
[MQTT](https://www.youtube.com/watch?v=EIxdz-2rhLs)   
More information about Mosquitto and how to install it in Windows and in Linux can be found here:    
[Mosquitto](https://www.youtube.com/watch?v=DH-VSAACtBk)      
This is a good example to start using MQTT (using a public broker):    
[Example](https://www.youtube.com/watch?v=kuyCd53AOtg)   

You can find here more information about public Access brokers.       
[Public access brokers](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping)

The API Rest module has been build using the Flask framework. A very simple and clear example on how to use Flask (in Spanish) can be found here:    
[Flask](https://youtu.be/Esdj9wlBOaI)

## 12.Compilation of TFG and TFM projects   


Title (with link)  | Author | Year 
--- | --- | --- 
[Puesta en marcha de un sistema conversacional con IA para el control de drones mediante voz con cámara integrada](https://upcommons.upc.edu/entities/publication/X)| PASTOR DOMENECH, MARINA| 2025
[Development of a Drone Control Application for Object Detection and Image Stitching](https://upcommons.upc.edu/entities/publication/X)| QUINTILLA CASTELLÓN, BERNAT| 2025
[Augmented Reality through Unity in the Drone Engineering Ecosystem](https://upcommons.upc.edu/entities/publication/X)| DOMENECH FONS, ARNAU| 2025
[WebApp en Flask para controlar un dron](https://upcommons.upc.edu/entities/publication/X)| FERNÁNDEZ MERINO, ERIK| 2025
[Estudi de les possibilitats de la eina Flask pel desenvolupament de web apps per controlar drons](https://upcommons.upc.edu/entities/publication/X)| DEL HIERRO MOSTEIRO, SANTIAGO| 2025
[Implementació d'un joc de combat de drons amb Flutter, Node.js i Python](https://upcommons.upc.edu/entities/publication/X)| SABATER NUALART, ANNA| 2025
[DroneQuest PX: Desarrollo de un videojuego multijugador para drones en el Drone Engineering Ecosystem](https://upcommons.upc.edu/entities/publication/X)| SANCHEZ BRIZ, SERGIO| 2025
[Desarrollo de un sistema conversacional con IA para el control de drones mediante voz](https://upcommons.upc.edu/entities/publication/156d2867-2b57-4cb6-9476-b885bda6bc76)| SOROYA BAYOD, VICTOR| 2024
[Control de un dron mediante la voz](https://upcommons.upc.edu/entities/publication/5fb3d265-0f74-454e-9e86-355cb01d1944)| TAPOUNET DOMENE, MARC| 2024
[Innovaciones en el DEE: Mejoras en FlutterApp y Desarrollo de Tecnología para Vuelos Interiores](https://upcommons.upc.edu/entities/publication/39290a13-4629-4ef9-b04b-d0780c025c2a)| MONCHO ROIG, ELOI| 2024
[Desenvolupament d'un dron de seguiment hibrid per al Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/417766)| CARRASCO CASTRO, CARLES| 2024
[Reconocimiento de objetos para el control de drones en el Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/414365)| MARCOS PAYA, POL| 2024
[AeroVox: A Web App Developed for Voice Controlled Drone Operations with 3D Spatial Constraints](https://upcommons.upc.edu/handle/2117/417756)| LÓPEZ AMOR VENDER, MATEO| 2024
[Contribució al Drone Engineering Ecosystem: Implementació d'un gestor de base de dades](https://upcommons.upc.edu/entities/publication/97f67b75-25bb-4304-8884-60d9768d4bff)| FERRER FALLOUK, OMAR| 2024
[MultiDronBoard: una aplicación para la gestión de múltiples drones](https://upcommons.upc.edu/handle/2117/417135)| SANDU LEFCU, TOMI RICCARDO| 2024
[Contribución al Drone Engineering Ecosystem: implementación de obstáculos](https://upcommons.upc.edu/handle/2117/412419)| ÁLVAREZ FERNÁNDEZ, MIGUEL| 2024
[Flutter en el Drone Engineering Ecosystem: Desarrollo de tutorial y estudio sobre videostreaming](https://upcommons.upc.edu/handle/2117/403655)| IBRAHIM GUARDIA, RUBEN| 2024
[Control de múltiples drones en el Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/403650)| SANMARTÍN ARÉVALO, ADOLFO| 2024
[Sistema anticolisión cooperativo 3D entre tráficos UAVs](https://upcommons.upc.edu/handle/2117/403395)| GARCÍA FÉLIX, HÉCTOR-ANDRÉS| 2024
[Reconocimiento de objetos en tiempo real mediante Deep Learning aplicado en Drones](https://upcommons.upc.edu/handle/2117/403398)| ALONSO SUÁREZ, IKER| 2024
[DroneLink EETAC: Nuevas librerías para el Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/412545)| CARNEROS MATEU, DANIEL| 2024
[Dockerización de los servicios de a bordo y mejora en la planificación y ejecución de planes de vuelo en el Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/403790)| LLAVERÍA NÚÑEZ, JORDI| 2024
[Contribució al ecosistema dels drons: DroneLab](https://upcommons.upc.edu/handle/2117/395745)| EL OUARIK CHEMLAL, YASSINNE| 2023
[Disseny i Implementació del Mode Cursa en el Drone Circus, del Drone Engineering Ecosystem (DEE)](https://upcommons.upc.edu/handle/2117/395234)| GARCIA MEDIAVILLA, PABLO | 2023
[Operaciones de enjambre en DEE](https://upcommons.upc.edu/handle/2117/395270) | SÁNCHEZ ERASO, SERGIO | 2023
[Drone control and monitoring by means of a web application](https://upcommons.upc.edu/handle/2117/395271) | SINGH ATWAL, JASKIRAT |  2023
[From Backend to DashMobile: Expanding the Horizons of the Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/394931)| PINTO MORENO, ALEJANDRO SAMUEL |  2023 
[Contribución al Drone Engineering Ecosystem con Android Nativo](https://upcommons.upc.edu/handle/2117/393653) | NUEZ ZARAGOZA, LAURA |  2023
[Desenvolupament i integració de jocs i aplicacions web al Drone Engineering Ecosystem](https://upcommons.upc.edu/handle/2117/393331) |  ORPELLA PALOMAR, JOANA |  2023
[Diseño e implementación de una estación de control de drones en Android nativo](https://upcommons.upc.edu/handle/2117/392005)| CASAÑA CABRERIZO, POL |  2023
[Study of drone synchronization](https://upcommons.upc.edu/handle/2117/383486) | JOHERA IZQUIERDO, JOEL |  2023
[Design, development, and validation of a web-based control application for drones](https://upcommons.upc.edu/handle/2117/392647) | LE GALL, THÉO EVAN |  2023  
[Drone-Based Panorama Stitching: A Study of SIFT, FLANN, and RANSAC Techniques](https://upcommons.upc.edu/handle/2117/392245) | CHANG, YICHENG |  2023
[Autonomous transmission tower inspection using UAV](https://upcommons.upc.edu/handle/2117/390947) | COLOMÉ SANZ, FERRAN |  2023
[Estandardització i posada en marxa de l¿ecosistema anomenat Drone Engineering Ecosystem]( https://upcommons.upc.edu/handle/2117/385113) | AGUILA I PALLEJÀ, GUILLEM |  2023
[Contribution to the development of a drone engineering station](https://upcommons.upc.edu/handle/2117/376354) | YILAKEQI |  2022
[Estudi sobre la viabilitat de diferents tecnologies per un ecosistema de drons](https://upcommons.upc.edu/handle/2117/376632) | LLOVERAS ORTEGA, GUILLEM |  2022
[Arquitectura software per a la monitorització i control de drons mitjançant una aplicació web](https://upcommons.upc.edu/handle/2117/375394) |CÁRDENAS MÁRQUEZ, JUAN ANTONIO|  2022


