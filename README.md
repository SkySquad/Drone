<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SkySquad/Drone_Aramco">
    <img src="images/logo.jpg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Uncontrolled Gas Leak Ignition using Drone</h3>

  <p align="center">
    <br />
    <a href="https://github.com/SkySquad/Drone_Aramco/tree/master/Code">View Code</a>    ·
    <a href="https://github.com/SkySquad/Drone_Aramco/tree/master/Gas%20detection">Gas detection</a>
    ·
    <a href="https://github.com/SkySquad/Drone_Aramco/tree/master/Invastigation">Invastigation</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#goal">Goal</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#hardware-and-software-used">Hardware and Software Used</a>
    </li>
    <li><a href="#minimum-viable-product">MVP</a></li>
    <li><a href="#project-highlights">Project Highlights</a></li>
    <li><a href="#simulation">Simulation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Offshore Drilling / Inspection Department
Currently, Saudi Aramco has several offshore platforms and drilling wells. The uncontrolled gas release event is one of the scenarios that requires immediate mitigation. The last resort of mitigation is to use handheld flare gun to ignite gas cloud manually by operator(s) which could impose risks to individual and environment.
### Goal
Develop drone-based ignition system that is controlled remotely to safely and effectively ignite uncontrolled gas leaks: <br> ● Cost effective and efficient drone-based solution that can be launched 5km away from the gas leak zone  <br> ● Remotely controlled using controller or base-station operating at ISM frequency bands  <br> ● The controller should have HD display to view camera feed & telemetry data, control onboard ignition/re-ignition system and manage flights mission.  <br> ● The drone camera should support navigation, aiming and ignition  <br> ● Imbedded/onboard AI/ML to detect proper gas cloud mixture for accurate navigation, aiming and ignition. <br>  ● The solution shall have autonomous navigation and return-home function.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Requirements
To run this project the following are needed for AI . Furthermore, a Dronekit must be installed.Pymavlink to connect with Drone. For shirt detection opencv, cv2  must be installed on the system.

> **Requirements list (+ all dependencies!) (python2.7):**
> - Dronekit (https://github.com/dronekit/Dronekit-python)
> - keras (http://www.keras.io)
> - theano (http://deeplearning.net/software/theano/)
> - opencv (http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Hardware and Software Used -->
## Hardware and Software Used

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Run the project
If you have all requirements as defined above you can simple run the project by entering:
```
$ python drone.py
```
This contains the main file of the drone. Please make sure that you have an active connection to the drone via wifi.


<!-- MVP -->
## Minimum Viable Product

A minimum viable product (MVP) is a version of a product with just enough features to be usable by early customers who can then provide feedback for future.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Project Highlights -->
## Project Highlights


- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Simulation -->
## Simulation

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


<p align="right">(<a href="#readme-top">back to top</a>)</p>



