# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision G, 12/31/2025

Verified working on: Python 3.12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm (no Mac testing yet, but might work while not in GUI-mode).
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

###########################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
###########################################################

###########################################################
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
from PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import traceback
import keyboard
###########################################################

###########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
###########################################################

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global PhidgetsCurrentSensor30ampDConlyVCP1100_Object
    global PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG
    global SHOW_IN_GUI_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:

        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG == 1 and SHOW_IN_GUI_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG == 1:
                PhidgetsCurrentSensor30ampDConlyVCP1100_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global PhidgetsCurrentSensor30ampDConlyVCP1100_Object
    global PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsCurrentSensor30ampDConlyVCP1100
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_PhidgetsCurrentSensor30ampDConlyVCP1100 = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_PhidgetsCurrentSensor30ampDConlyVCP1100, text='   PhidgetsCurrentSensor30ampDConlyVCP1100   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_PhidgetsCurrentSensor30ampDConlyVCP1100 = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    if PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG == 1:
        PhidgetsCurrentSensor30ampDConlyVCP1100_Object.CreateGUIobjects(TkinterParent=Tab_PhidgetsCurrentSensor30ampDConlyVCP1100)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG
    USE_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG
    SHOW_IN_GUI_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_PhidgetsCurrentSensor30ampDConlyVCP1100
    global GUI_COLUMN_PhidgetsCurrentSensor30ampDConlyVCP1100
    global GUI_PADX_PhidgetsCurrentSensor30ampDConlyVCP1100
    global GUI_PADY_PhidgetsCurrentSensor30ampDConlyVCP1100
    global GUI_ROWSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100
    global GUI_COLUMNSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100
    GUI_ROW_PhidgetsCurrentSensor30ampDConlyVCP1100 = 1

    GUI_COLUMN_PhidgetsCurrentSensor30ampDConlyVCP1100 = 0
    GUI_PADX_PhidgetsCurrentSensor30ampDConlyVCP1100 = 1
    GUI_PADY_PhidgetsCurrentSensor30ampDConlyVCP1100 = 1
    GUI_ROWSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100 = 1
    GUI_COLUMNSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100 = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_PhidgetsCurrentSensor30ampDConlyVCP1100
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsCurrentSensor30ampDConlyVCP1100_Object

    global PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG
    PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG = -1

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict = dict()

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Raw
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Raw = [-11111.0]*1

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Filtered
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Filtered = [-11111.0]*1

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_CurrentDerivative_AmpsPerSec
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_CurrentDerivative_AmpsPerSec = [-11111.0]*1

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag = [-1]*1

    global PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_Time
    PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_Object

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global PhidgetsCurrentSensor30ampDConlyVCP1100_GUIparametersDict
    PhidgetsCurrentSensor30ampDConlyVCP1100_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG),
                                                                    ("EnableInternal_MyPrint_Flag", 0),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                    ("GUI_ROW", GUI_ROW_PhidgetsCurrentSensor30ampDConlyVCP1100),
                                                                    ("GUI_COLUMN", GUI_COLUMN_PhidgetsCurrentSensor30ampDConlyVCP1100),
                                                                    ("GUI_PADX", GUI_PADX_PhidgetsCurrentSensor30ampDConlyVCP1100),
                                                                    ("GUI_PADY", GUI_PADY_PhidgetsCurrentSensor30ampDConlyVCP1100),
                                                                    ("GUI_ROWSPAN", GUI_ROWSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100),
                                                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_PhidgetsCurrentSensor30ampDConlyVCP1100)])

    global PhidgetsCurrentSensor30ampDConlyVCP1100_SetupDict
    PhidgetsCurrentSensor30ampDConlyVCP1100_SetupDict = dict([("GUIparametersDict", PhidgetsCurrentSensor30ampDConlyVCP1100_GUIparametersDict),
                                                                ("VINT_DesiredSerialNumber", -1), #-1 MEANS ANY SN, CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                                ("VINT_DesiredPortNumber", 1), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                                                ("DesiredDeviceID", 105),
                                                                ("WaitForAttached_TimeoutDuration_Milliseconds", 1000),
                                                                ("NameToDisplay_UserSet", "Reuben's Test VCP1100 Current Sensor Board"),
                                                                ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                                                ("DataCallbackUpdateDeltaT_ms", 20),
                                                                ("CurrentSensorList_Current_Amps_ExponentialFilterLambda", [0.95]),
                                                                ("CurrentSensorList_CurrentDerivative_AmpsPerSec_ExponentialFilterLambda", [0.5])]) #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

    if USE_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            PhidgetsCurrentSensor30ampDConlyVCP1100_Object = PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class(PhidgetsCurrentSensor30ampDConlyVCP1100_SetupDict)
            PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG = PhidgetsCurrentSensor30ampDConlyVCP1100_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsCurrentSensor30ampDConlyVCP1100_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PhidgetsCurrentSensor30ampDConlyVCP1100_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG != 1:
                print("Failed to open PhidgetsCurrentSensor30ampDConlyVCP1100_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_GUIparametersDict
    MyPrint_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_SetupDict
    MyPrint_SetupDict = dict([("NumberOfPrintLines", 10),
                            ("WidthOfPrintingLabel", 200),
                            ("PrintToConsoleFlag", 1),
                            ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                            ("GUIparametersDict", MyPrint_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("GraphCanvasWidth", 900),
                                                                    ("GraphCanvasHeight", 700),
                                                                    ("GraphCanvasWindowStartingX", 0),
                                                                    ("GraphCanvasWindowStartingY", 0),
                                                                    ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                    ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 30)])


    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_GUIparametersDict),
                                                            ("ParentPID", os.getpid()),
                                                            ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 5.0),
                                                            ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Raw", "Filtered", "Derivative"]),
                                                                                                        ("MarkerSizeList", [3, 2, 1]),
                                                                                                        ("LineWidthList", [2, 1, 0]),
                                                                                                        ("IncludeInXaxisAutoscaleCalculationList", [1, 1, 1]),
                                                                                                        ("IncludeInYaxisAutoscaleCalculationList", [1, 1, 1]),
                                                                                                        ("ColorList", ["Red", "Blue", "Green"])])),
                                                            ("SmallTextSize", 7),
                                                            ("LargeTextSize", 12),
                                                            ("NumberOfDataPointToPlot", 100),
                                                            ("XaxisNumberOfTickMarks", 10),
                                                            ("YaxisNumberOfTickMarks", 10),
                                                            ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("XaxisAutoscaleFlag", 1),
                                                            ("YaxisAutoscaleFlag", 1),
                                                            ("X_min", 0.0),
                                                            ("X_max", 5.0),
                                                            ("Y_min", -5.0),
                                                            ("Y_max", 5.0),
                                                            ("XaxisDrawnAtBottomOfGraph", 0),
                                                            ("XaxisLabelString", "Time (sec)"),
                                                            ("YaxisLabelString", "Y-units (units)"),
                                                            ("ShowLegendFlag", 1),
                                                            ("GraphNumberOfLeadingZeros", 0),
                                                            ("GraphNumberOfDecimalPlaces", 3),
                                                            ("SavePlot_DirectoryPath", os.path.join(os.getcwd(), "SavedImagesFolder")),
                                                            ("KeepPlotterWindowAlwaysOnTopFlag", 0),
                                                            ("RemoveTitleBorderCloseButtonAndDisallowWindowMoveFlag", 0),
                                                            ("AllowResizingOfWindowFlag", 1)])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_Object = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_Object, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_PhidgetsCurrentSensor30ampDConlyVCP1100 = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    print("Starting main loop 'test_program_for_PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ####################################################
        ####################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ####################################################
        ####################################################

        #################################################### GET's
        ####################################################
        if PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG == 1:

            PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict = PhidgetsCurrentSensor30ampDConlyVCP1100_Object.GetMostRecentDataDict()

            if "Time" in PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict:
                PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Raw = PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict["CurrentSensorList_Current_Amps_Raw"]
                PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Filtered = PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict["CurrentSensorList_Current_Amps_Filtered"]
                PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_CurrentDerivative_AmpsPerSec = PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict["CurrentSensorList_CurrentDerivative_AmpsPerSec"]
                PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag = PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict["CurrentSensorList_ErrorCallbackFiredFlag"]
                PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_Time = PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict["Time"]

                #print("PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_Time: " + str(PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_Time))
        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_Object.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess >= MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents"]/1000.0 + 0.001:
                        
                        MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["Raw", "Filtered", "Derivative"], [CurrentTime_MainLoopThread]*3, [PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Raw, PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_Current_Amps_Filtered, PhidgetsCurrentSensor30ampDConlyVCP1100_MostRecentDict_CurrentSensorList_CurrentDerivative_AmpsPerSec])
                        
                        LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_MainLoopThread
            ####################################################

        ####################################################
        ####################################################

        time.sleep(0.002)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting main program 'test_program_for_PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class.")

    #################################################
    if PhidgetsCurrentSensor30ampDConlyVCP1100_OPEN_FLAG == 1:
        PhidgetsCurrentSensor30ampDConlyVCP1100_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_Object.ExitProgram_Callback()
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################