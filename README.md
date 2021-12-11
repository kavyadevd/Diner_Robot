[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Diner_Robot
This project is a CoppeliaSim based serving robot in a diner scene. The main objective is to model a 6 degree of freedom robotic arm
fixed on a 2 degree of freedom four-wheeled moving cart. Followed by the implementation of a four-wheeled differential drive, and forward-inverse kinematics and
program the model to simulate the task for autonomously navigating and completing a pre-defined job. All the calculations are verified using an independent [python
script](https://github.com/kavyadevd/Diner_Robot/blob/main/UR5Transformation.ipynb)

### Steps to run simulation
##### Clone this repository
```bash
git clone --recursive https://github.com/kavyadevd/Diner_Robot.git
```

##### Coppeliasim
  [Download Coppeliasim](https://www.coppeliarobotics.com/files/CoppeliaSim_Player_V4_2_0_Ubuntu20_04.tar.xz) unpack the compressed file.
  Run the simulator script by running the following command on cmd:
  ```bash
  $<CoppeliaSim-folder-path>/coppeliaSim.sh <Diner-Robot-Folder>/Diner4.ttt
  ```
  
  In separate terminal run the following command:
  ```bash
  cd Diner_Robot
  python3 robot_control.py
  ```

The robot moel in custom scene is as follows
![intermediate](https://user-images.githubusercontent.com/13993518/145513812-4a3c9ef3-e8cc-48ab-84c4-1d96de64186e.png)

![final](https://user-images.githubusercontent.com/13993518/145513835-c8abd826-e80f-4018-a123-2bc286bc4fcf.png)


The complete demo can be seen [here](https://www.youtube.com/watch?v=pwTl2Ah0ebo&feature=youtu.be)
