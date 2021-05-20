# IMPORTS |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from tkinter import *
import front.InitialScreen




# MAIN |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
root = Tk()
st = front.InitialScreen( root, "gui", "1080x720")
st.setInitialOptions()
st.start()