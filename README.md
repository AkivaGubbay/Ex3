hello!

Welcome to the project "Robot Arean"

Link to the presentation of the project: https://github.com/AkivaGubbay/Ex3/blob/master/PerformanceComparison/RobotsArena.pdf

Robots scene simulator project, which can not communicate with each other directly, but only by sending messages to each other.
When the robot sends a message, to Robots that close to it are the most likely to get them, Robots that far - not necessarily receive the message.
There Robots non-moving (static) and Robots moving (non-static), static robots know the location of the lot but of moving robots do not know.
The purpose of robots movable discover the location estimated using robots Stats Posts

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
  <img src="https://github.com/AkivaGubbay/Ex3/blob/master/Performance Comparison/graph.jpg?raw=true" width="800"/>
</p>
See the LOG file link: https://github.com/AkivaGubbay/Ex3/tree/master/PerformanceComparison





Daniel Fuchs , Sapir Ankri , Akiva Gubbay and Zvika Binyamin.


