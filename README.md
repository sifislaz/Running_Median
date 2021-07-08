#Running_Median
Given a huge amount of locations in Earth and their temperatures, we want to locate the location with the median temperature.
The temperatures change in a live rate.

The exercise want to:
1. Create 500,000 random locations with (x=[0,..,1000], y=[0,1000]) integer coordinates and their random temperatures as floats with 2 decimal points,
between -50.00 and 50.00.
2. Always keep the median location easily accesible [O(1)].
3. Save the new data in the structures created immediately.
4. Use the coordinates as key. If the same coordinates occur, update the temperature value.

Also, in order to understand the procedure, save externally the first 100 random locations to an array T, in order to do the following operations:
a. Change randomly the temperature of the locations saved in array T, and update the temperature in the general structure.\
b. Print the temperatures and the coordinates of the location, which consist the median element in these 100 changes.
c. Time this procedure and present the result.

Note: The exercise is a product of University of Patras professors.