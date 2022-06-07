#electrophysiology-parser-python<br/>
README Neural Electrophysiology Data Analyzer<br/>
Written By: Eyal Brand and Michael Levi<br/>

1.	Setup Requirements:<br/>
  Must install packages:<br/>
    >•	H5py -3.6.0<br/>
    >•	Numpy -1.22.2<br/>
    •	OS -8.6<br/>
    •	matplotlib.pyplot -3.5.1<br/>
    •	pyopenephys - 1.1.5<br/>
  GUI additional Packages:  <br/>
    •	sys -8.6<br/>
    •	matplotlib- 3.5.1<br/>
    •	PyQt5 -5.15.6<br/>
    •	Easygui - 0.98.2<br/>
    
2.	How to run: <br/>
  a.	GUI Application:<br/>
    i. Clone the project.<br/>
    ii. Run MainGUIApplication.py or use .exe file.<br/>
    iii. Choose a file type and select a folder for OE recordings or a file for NWB/MCH5 via the ‘File Explorer’ button. <br/>
    iv. Choose the channels you would like to display. <br/>
     v. Select start time and a window time (the window time will be used to go forward and backwards in time).<br/>
    vi. Click ‘Plot’ button. <br/>
    vii.Use the + or – window time to see other time sections of the recording.<br/>
    viii.	Channels, Time Window and Start Time, parameters can be changes at any time.<br/>
    ix.	You can zoom in and out, save the plot and change the scale of the axis. <br/>
  b.	Console Application: <br/>
    i.	Clone the project.<br/>
    ii.	Run main.py<br/>
    iii.	Provide a full file/folder path and follow the instructions.<br/>

3.	Code structure: <br/>
  a.	FormatInterface.py:<br/>
    i.	This is the abstract class. All formats inherit from this class.<br/>
    ii.	This class includes the basic parameters such as:<br/>
      1.	Time duration. <br/>
      2.	Time window. <br/>
      3.	Number of channels<br/>
      4.	Indices of the channels according to the format structure. <br/>
      5.	Indices of timestamps according to the format structure. <br/>
      6.	Metadata.<br/>
    iii.	This class includes the basic functionalities:<br/>
      1.	PlotData- Data is provided from file and is plotted according to the channels selection and time window.<br/>
      2.	 GetRelevantChannels- Gets the relevant channels for console application.<br/>
      3.	GetRelevantTimestamps- Gets the relevant timestamps for console application.<br/>
      4.	GetTimeIndex- Gets  the time indices of the matrix that contains the metadata according to the selected parameters.<br/>
      5.	ShowFileInnerSection- Some data formats are built with many folders. This function makes it more convenient to explore in the data structure.<br/>
  b.	MCH5Interface.py, NWBInterface.py, OERecordingsInterface.py:<br/>
    i.	These classes inherit from FormatInterface.<br/>
    ii.	All formats must have the following functions:<br/>
      1.	GetData- extracts the data (usually done via python packages).<br/>
      it should extract the data according to the selected channels and time window.<br/>
      It should also extract the time step (sampling rate), the total time duration and the number of channels for both GUI and Console applications. <br/>
      2.	 GetAndPlotMetaData- Extract the data for GUI application and plots it.  <br/>
  c.	FileHandler.Py:<br/>
    i.	FileHandler-Gets the input file and creates an object for the provided file according to its format.<br/>
    ii.	GetFilePath- Converts the file path to python format.<br/>
  d.	Main.py (Console Application):<br/>
    i.	Gets the input path of the file/folder. <br/>
    ii.	Creates an instance via file handler<br/>
    iii.	The user is asked to provide parameters<br/>
    iv.	Data is plotted<br/>
    v.	The user is asked whether to continue or halt.<br/>
    e.	MainGuiApplication (GUI Application):<br/>
    i.	Window- contains all the buttons, canvas and toolbars.<br/>
    ii.	ForwardTime- Adds another time window and safely plots the following data.<br/>
    iii.	Backward time- Go subtract a window time from the current time and plots is.<br/>
    iv.	openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it gives the       option to select a folder.<br/>
    Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels, time             duration and time step.<br/>
    v.	SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.<br/>
    vi.	chosenChannels- Gets the selected channels from GUI.<br/>
    vii.	Ploti- Check that all needed data is provided, extract the metadata and plots it.<br/>

	MainGuiApplication (GUI Application):<br/>
  	Window- contains all the buttons, canvas and toolbars.<br/>
  	ForwardTime- Adds another time window and safely plots the following data.<br/>
  	Backward time- Go subtract a window time from the current time and plots is.<br/>
  	openFileNameDialog- Opens a dialog according to the data format. If MCH5 or NWB, it gives the option to select a file. If OE format is selected it gives the option   to select a folder.<br/>
  Afterwards it uses the FileHandler to create an instance of the file format and extracts the basic data of the recording, such as: number of channels, time duration   and time step.<br/>
  	SelectTime- Gets the selected start time and time window from the GUI and coverts it to the accurate indices of the recording.<br/>
  	chosenChannels- Gets the selected channels from GUI.<br/>
  	Ploti- Check that all needed data is provided, extract the metadata and plots it.<br/>
