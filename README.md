
Project "Robot Areana"

Project presentation: https://github.com/AkivaGubbay/Ex3/blob/master/PerformanceComparison/RobotsArena.pdf

General description of the Areana:

Suppose there is a set of "robots" in a defined environment. Each robot has a unique identifier and ability at any point in time to listen to the environment. When a message is transmitted, the transmitting robot does not receive information from the environment. 

Communication model: A robot can only receive one message at a time. If a message is transmitted from a greater distance, the probability of it being received is lower.

Robot attributes:

Some robots are static, others have "voluntary" movement ability or random movement capability.

Each robot has a battery. When battery consumption is linearly dependent on: Quantity, The duration of the movement (assuming a constant speed), and the robot's operating time.
Each robot has a solar panel that allows it to charge itself when there is a sun around it That the battery is fully charged after 4 hours of sunshine.

The basic operation of each robot is: to listen, to think where to go ahead, to transmit information Relevant to the rest of the robots. A robot knows only position and direction relative to its starting point! (No GPS)
The areana consists of three colored parts:
1) White  - It has a "light" for charging, and you can move inside it. 
2) Gray  - has no light, but allows movement Inside.
3) Black - an obstacle that can not be entered.

How to run:

When you run the file Main() via python parallel to the next screen:
<p align="center">
  <img src="https://github.com/AkivaGubbay/Ex3/blob/master/pictures/Image1.jpg?raw=true" width="600"/>
</p>


By clicking on one of the buttons, the robots would send each other messages and will move to the location:
<p align="center">
  <img src="https://github.com/AkivaGubbay/Ex3/blob/master/pictures/Image2.jpg?raw=true" width="600"/>
</p>

Of course everything is documented action of Hrobtim blog will open at the exit from the program:
<p align="center">
  <img src="https://github.com/AkivaGubbay/Ex3/blob/master/pictures/Image3.jpg?raw=true" width="600"/>
</p>


As can be seen in comparing performance we did, over time the robot correctly guess the location from deviation of 500 meters to a deviation of 65 meters:
<p align="center">
  <img src="https://github.com/AkivaGubbay/Ex3/blob/master/pictures/Image4.jpg?raw=true" width="800"/>
</p>
See the LOG file link: https://github.com/AkivaGubbay/Ex3/tree/master/PerformanceComparison





Daniel Fuchs , Sapir Ankri , Akiva Gubbay and Zvika Binyamin.


