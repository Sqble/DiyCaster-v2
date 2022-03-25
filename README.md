# DiyCaster-v2
  dependencies: python3, pygame
  
  Raycasting engine implemented in pygame

  
  ![3D View](readme_images/3d.png)

  
  ##How it works:
  
  Raycasting is a Sudo-3D projection technique used in the early days of 3D games. It works by "casting rays"(below image) outward from a point on a top-down map and drawing lines on the user's window (above image) based on how long a ray travelled before hitting a wall. this technique allows you to create a 3D world using only a 2D map.
  ![2D View](readme_images/2d.png)

  ###Rays
  The way these rays are "casted" is actually by casting 2 different rays. one of them checks for horizontal collisions with walls and the other vertical. Each one works by calculating 2 offsets, dx and dy, that can be added to a ray's position to check for collisions with a wall.

  every time dx and dy are added the ray's position is in a new cell of the 2D map which can be used to check for the collision.

  in the image below a ray is checking for collisions with horizontal walls. dy is the size of 1 cell in the 2D world and dx is calculated based on the function 1/tan(angle).
  ![dx Explained](readme_images/dx.jpg)
  for vertical walls it's the same thing except swapping y and x and using -tan(angle) instead.

  ###3D Viewport

  ![viewport](readme_images/viewport.jpg)

  After casting 60-90 rays depending on the player FOV the next part is to display them on the screen. the Width of the screen is divided evenly by the amount of rays casted so each column is a different ray. 
  
  here's how you calculate how much sky, wall, and floor to put on each ray:
  1. multiply the ray's distance by cosine of the difference between the player and ray's angle to remove the fisheye effect
  2. find the wall length. (scale * screenHeight) / newDistance. Scale is a constant used without the program that represents the scale of the 2D map. lower scale means each cell takes up less space
  3. to find the length to fill with sky and air split the remaining space in the column left evenly between the floor and sky.

Lastly some clever modulo's can be used to make walls into textures instead of just a solid color.