README Neural Electrophysiology Data Analyzer
Written By: Eyal Brand and Michael Levi

1.Setup Requirements:
  -	Must install packages:
	-		H5py -3.6.0
	-		Numpy -1.22.2
	-		OS -8.6
	-		matplotlib.pyplot -3.5.1
	-		pyopenephys -1.1.5
  -	GUI additional Packages:  
	-		sys -8.6
	-		matplotlib -3.5.1
	-		PyQt5 -5.15.6
	-		Easygui -0.98.2
2.How to run: 
  -		GUI Application:
	-		Clone the project.
	-		Run MainGUIApplication.py or use .exe file.
	-		Choose a file type and select a folder for OE recordings or a file for NWB/MCH5 via the ‘File Explorer’ button. 
	-		Choose the channels you would like to display. 
	-		Select start time and a window time (the window time will be used to go forward and backwards in time).
	-	Click ‘Plot’ button. 
	-		Use the + or – window time to see other time sections of the recording.
	-		Channels, Time Window and Start Time, parameters can be changes at any time.
	-	You can zoom in and out, save the plot and change the scale of the axis. 
 -		Console Application: 
	-		Clone the project.
	-		Run main.py
	-		Provide a full file/folder path and follow the instructions.

3.Code structure: 
-		FormatInterface.py:
	-		This is the abstract class. All formats inherit from this class.
	-		This class includes the basic parameters such as:
		-		Time duration. 
		-		Time window. 
		-		Number of channels
		-		Indices of the channels according to the format structure. 
		-		Indices of timestamps according to the format structure. 
		-		Metadata.
	-		This class includes the basic functionalities:
		-		PlotData- Data is provided from file and is plotted according to the channels selection and time window.
		-		 GetRelevantChannels- Gets the relevant channels for console application.
		-		GetRelevantTimestamps- Gets the relevant timestamps for console application.
		-		GetTimeIndex- Gets  the time indices of the matrix that contains the metadata according to the selected parameters.
		-		ShowFileInnerSection- Some data formats are built with many folders. This function makes it more convenient to explore in the data		  -	 structure.
-		MCH5Interface.py, NWBInterface.py, OERecordingsInterface.py:
	-		These classes inherit from FormatInterface.
	-		All formats must have the following functions:
		-		GetData- extracts the data (usually done via python packages).it should extract the data according to the selected channels and time window.It should also extract the time step (sampling rate), the total time duration and the number of channels for both GUI and Console applications. 
		-		 GetAndPlotMetaData- Extract the data for GUI application and plots it.  
-		FileHandler.Py:
	-		FileHandler-Gets the input file and creates an object for the provided file according to its format.
	-		GetFilePath- Converts the file path to python format.
-		Main.py (Console Application):
	-	Gets the input path of the file/folder. 
	-		Creates an instance via file handler
	-		The user is asked to provide parameters
	-		Data is plotted
	-		The user is asked whether to continue or halt.
-		MainGuiApplication (GUI Application):
	-		Window- contains all the buttons, canvas and toolbars.
	-		ForwardTime- Adds another time window and safely plots the following data.
	-		Backward time- Go subtract a window time from the current time and plots is.
	-		openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it gives the option to select a folder.Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels, 	       - time duration and time step.
	-		SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.
	-		chosenChannels- Gets the selected channels from GUI.
	-		Ploti- Check that all needed data is provided, extract the metadata and plots it.
 
MainGuiApplication (GUI Application):
-		Window- contains all the buttons, canvas and toolbars.
-		ForwardTime- Adds another time window and safely plots the following data.
-		Backward time- Go subtract a window time from the current time and plots is.
-		openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it  -- -  gives the option to select a folder.
-		Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels,- - time duration and time step.
-		SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.
-		chosenChannels- Gets the selected channels from GUI.
-		Ploti- Check that all needed data is provided, extract the metadata and plots it.
