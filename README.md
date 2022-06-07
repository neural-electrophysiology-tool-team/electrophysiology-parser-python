README Neural Electrophysiology Data Analyzer
Written By: Eyal Brand and Michael Levi

1.Setup Requirements:
	Must install packages:
		•	H5py 
		•	Numpy 
		•	OS
		•	matplotlib.pyplot
		•	pyopenephys
	GUI additional Packages:  
		•	sys
		•	matplotlib
		•	PyQt5
		•	Easygui
2.How to run: 
	a.	GUI Application:
		i.	Clone the project.
		ii.	Run MainGUIApplication.py or use .exe file.
		iii.	Choose a file type and select a folder for OE recordings or a file for NWB/MCH5 via the ‘File Explorer’ button. 
		iv.	Choose the channels you would like to display. 
		v.	Select start time and a window time (the window time will be used to go forward and backwards in time).
		vi.	Click ‘Plot’ button. 
		vii.	Use the + or – window time to see other time sections of the recording.
		viii.	Channels, Time Window and Start Time, parameters can be changes at any time.
		ix.	You can zoom in and out, save the plot and change the scale of the axis. 
	b.	Console Application: 
		i.	Clone the project.
		ii.	Run main.py
		iii.	Provide a full file/folder path and follow the instructions.

3.Code structure: 
	a.	FormatInterface.py:
		i.	This is the abstract class. All formats inherit from this class.
		ii.	This class includes the basic parameters such as:
			1.	Time duration. 
			2.	Time window. 
			3.	Number of channels
			4.	Indices of the channels according to the format structure. 
			5.	Indices of timestamps according to the format structure. 
			6.	Metadata.
		iii.	This class includes the basic functionalities:
			1.	PlotData- Data is provided from file and is plotted according to the channels selection and time window.
			2.	 GetRelevantChannels- Gets the relevant channels for console application.
			3.	GetRelevantTimestamps- Gets the relevant timestamps for console application.
			4.	GetTimeIndex- Gets  the time indices of the matrix that contains the metadata according to the selected parameters.
			5.	ShowFileInnerSection- Some data formats are built with many folders. This function makes it more convenient to explore in the data structure.
	b.	MCH5Interface.py, NWBInterface.py, OERecordingsInterface.py:
		i.	These classes inherit from FormatInterface.
		ii.	All formats must have the following functions:
			1.	GetData- extracts the data (usually done via python packages).
			it should extract the data according to the selected channels and time window.
			It should also extract the time step (sampling rate), the total time duration and the number of channels for both GUI and Console applications. 
			2.	 GetAndPlotMetaData- Extract the data for GUI application and plots it.  
	c.	FileHandler.Py:
		i.	FileHandler-Gets the input file and creates an object for the provided file according to its format.
		ii.	GetFilePath- Converts the file path to python format.
	d.	Main.py (Console Application):
		i.	Gets the input path of the file/folder. 
		ii.	Creates an instance via file handler
		iii.	The user is asked to provide parameters
		iv.	Data is plotted
		v.	The user is asked whether to continue or halt.
	e.	MainGuiApplication (GUI Application):
		i.	Window- contains all the buttons, canvas and toolbars.
		ii.	ForwardTime- Adds another time window and safely plots the following data.
		iii.	Backward time- Go subtract a window time from the current time and plots is.
		iv.	openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it gives the option to select a folder.
		Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels, time duration and time step.
		v.	SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.
		vi.	chosenChannels- Gets the selected channels from GUI.
		vii.	Ploti- Check that all needed data is provided, extract the metadata and plots it.
 
MainGuiApplication (GUI Application):
		Window- contains all the buttons, canvas and toolbars.
		ForwardTime- Adds another time window and safely plots the following data.
		Backward time- Go subtract a window time from the current time and plots is.
		openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it gives the option to select a folder.
		Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels, time duration and time step.
		SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.
		chosenChannels- Gets the selected channels from GUI.
		Ploti- Check that all needed data is provided, extract the metadata and plots it.
