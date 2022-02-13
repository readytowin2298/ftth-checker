Hi Team!!!

The main home for this project is, of course, app.py.
In app.py you'll find two very helpful functions, ftth_checker and conversion. 

Conversion accepts a standard coordinate as a string, i.e. 32°26'44.95"N, and converts it
to a decimal value, returning a float.


ftth_checker accepts to parameters, and returns a boolean indicating whether or not the second param is in the object made from the first

The first parameter used with ftth_checker exists a list of coordinate dicts with keys of lattitude and longitude. You
can find an example of this in test_coords.py, name test_neighborhood.

The second parameter should be a coordinate dict matching the format outlined above, see test_home and test_not_home in 
test_coords.py for examples

If you want to see a visual representation of what the program is finding from the coordinates, you can open app.py with a text editor and uncomment the following lines: 2, 43, 44, 47, 48, 51, and 54. Then run the below commands:
    python
    from app import ftth_checker
    neighborhood = [list of coordinate objects]
    home = {single coordinate dict}
    ftth_checker(neighborhood, home)

FOR WINDOWS USERS ONLY: I have included a file called setup.bat. Assuming you've already got python and pip installed and
accessible from the command line, this file will generate the virtual environment needed to house dependancies, activate
sai virtual envirnment, install aforementioned dependancies, and leave you with a terminal open to the correct directory
to interact with the code. It can be used anytime you want to play with the code, it only generates the virtual envirnment if one is not already present. You can run test_app.py to ensure that the code is functioning properly, or play with node directly
by entering the command "python" and then use imports to gain access to code in the files. Commands to do this look like:
    from some_file_name import some_named_vairable

If you have any questions or concerns, please reach out to David Ames either on teams, or at 
dames@team.nxlink.com.

Happy Hacking!!

