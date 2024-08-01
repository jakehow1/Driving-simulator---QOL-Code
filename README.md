# Driving-simulator---QOL-Code
Quality of life code, to make data wrangling / data analysis easier and quicker when using a driving simulator using the software 'City Car Driving' which is otherwise difficult to work with.
This code enables extraction of driving statistics from the simulator sessions by firstly creating .txt files of the mistakes made in each session, then the provided code can be used to create a .csv file.
This .csv file can be used alongside programming language 'R' to further wrangle the data as needed.

Step 1: Creating .txt files of driving errors per driving session
1. Open City Car Driving
2. From the Main Menu, select "statistics"
3. Select the driving session that you wish to export
4. Using the 'snipping tool' or 'fn > prt sc', select an area that includes the text highlighting driving errors.
5. Open the screen capture that you just made and select the text from this picture.
6. Copy and paste the text into a new .txt file (note, you MUST change the name of the files that the code will search for as the code is tailored towards investigating a 2-condition effect and is therefore specific to the names of my conditions)
7. Repeat this process until all sessions have a .txt file

Step 2: Running code
1: ensure WD is the same as the location of your .txt files
2: Change the names of required .txt files that the code should search the WD for.
3: Change the condition mapping as required, so that the correct sessions are attributed to the correct conditions.
4: Change output name to preference.

NOTE: This code is clunky, and was designed specifically for usage in a MRes Psychology Thesis. Therefore, it was designed to meet the requirements of this project, NOT to be used for all projects. However, the instructions above may help others to alter this code or design their own to meet their specific needs.
