import tkinter as tk
import tkinter.font as tkFont
from tkinter.constants import DISABLED, NORMAL
import asyncio

WordleFrames = []
Map = [
{},
{},
{},
{},
{}
]

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=350
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_791=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_791["font"] = ft
        GLabel_791["fg"] = "#333333"
        GLabel_791["justify"] = "center"
        GLabel_791["text"] = "Wordle"
        GLabel_791["relief"] = "flat"
        GLabel_791.place(x=0,y=0,width=350,height=70)

        GLineEdit_890=tk.Entry(root)
        GLineEdit_890["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_890["font"] = ft
        GLineEdit_890["fg"] = "#333333"
        GLineEdit_890["justify"] = "center"
        GLineEdit_890["text"] = "1,1"
        GLineEdit_890.place(x=10,y=80,width=50,height=50)
        WordleFrames.append(GLineEdit_890)
        
        GLineEdit_918=tk.Entry(root)
        GLineEdit_918["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_918["font"] = ft
        GLineEdit_918["fg"] = "#333333"
        GLineEdit_918["justify"] = "center"
        GLineEdit_918["text"] = "1,2"
        GLineEdit_918.place(x=80,y=80,width=50,height=50)
        WordleFrames.append(GLineEdit_918)

        GLineEdit_240=tk.Entry(root)
        GLineEdit_240["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_240["font"] = ft
        GLineEdit_240["fg"] = "#333333"
        GLineEdit_240["justify"] = "center"
        GLineEdit_240["text"] = "1,3"
        GLineEdit_240.place(x=150,y=80,width=50,height=50)
        WordleFrames.append(GLineEdit_240)

        GLineEdit_507=tk.Entry(root)
        GLineEdit_507["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_507["font"] = ft
        GLineEdit_507["fg"] = "#333333"
        GLineEdit_507["justify"] = "center"
        GLineEdit_507["text"] = "1,4"
        GLineEdit_507.place(x=220,y=80,width=50,height=50)
        WordleFrames.append(GLineEdit_507)

        GLineEdit_436=tk.Entry(root)
        GLineEdit_436["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_436["font"] = ft
        GLineEdit_436["fg"] = "#333333"
        GLineEdit_436["justify"] = "center"
        GLineEdit_436["text"] = "1,5"
        GLineEdit_436.place(x=290,y=80,width=50,height=50)
        WordleFrames.append(GLineEdit_436)

        GLineEdit_362=tk.Entry(root)
        GLineEdit_362["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_362["font"] = ft
        GLineEdit_362["fg"] = "#333333"
        GLineEdit_362["justify"] = "center"
        GLineEdit_362["text"] = "2,1"
        GLineEdit_362.place(x=10,y=150,width=50,height=50)
        WordleFrames.append(GLineEdit_362)

        GLineEdit_856=tk.Entry(root)
        GLineEdit_856["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_856["font"] = ft
        GLineEdit_856["fg"] = "#333333"
        GLineEdit_856["justify"] = "center"
        GLineEdit_856["text"] = "2,3"
        GLineEdit_856.place(x=150,y=150,width=50,height=50)
        WordleFrames.append(GLineEdit_856)

        GLineEdit_822=tk.Entry(root)
        GLineEdit_822["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_822["font"] = ft
        GLineEdit_822["fg"] = "#333333"
        GLineEdit_822["justify"] = "center"
        GLineEdit_822["text"] = "2,4"
        GLineEdit_822.place(x=220,y=150,width=50,height=50)
        WordleFrames.append(GLineEdit_822)

        GLineEdit_471=tk.Entry(root)
        GLineEdit_471["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_471["font"] = ft
        GLineEdit_471["fg"] = "#333333"
        GLineEdit_471["justify"] = "center"
        GLineEdit_471["text"] = "2,5"
        GLineEdit_471.place(x=290,y=150,width=50,height=50)
        WordleFrames.append(GLineEdit_471)

        GLineEdit_545=tk.Entry(root)
        GLineEdit_545["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_545["font"] = ft
        GLineEdit_545["fg"] = "#333333"
        GLineEdit_545["justify"] = "center"
        GLineEdit_545["text"] = "3,1"
        GLineEdit_545.place(x=10,y=220,width=50,height=50)
        WordleFrames.append(GLineEdit_545)

        GLineEdit_209=tk.Entry(root)
        GLineEdit_209["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_209["font"] = ft
        GLineEdit_209["fg"] = "#333333"
        GLineEdit_209["justify"] = "center"
        GLineEdit_209["text"] = "3,2"
        GLineEdit_209.place(x=80,y=220,width=50,height=50)
        WordleFrames.append(GLineEdit_209)

        GLineEdit_275=tk.Entry(root)
        GLineEdit_275["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_275["font"] = ft
        GLineEdit_275["fg"] = "#333333"
        GLineEdit_275["justify"] = "center"
        GLineEdit_275["text"] = "3,3"
        GLineEdit_275.place(x=150,y=220,width=50,height=50)
        WordleFrames.append(GLineEdit_275)


        GLineEdit_252=tk.Entry(root)
        GLineEdit_252["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_252["font"] = ft
        GLineEdit_252["fg"] = "#333333"
        GLineEdit_252["justify"] = "center"
        GLineEdit_252["text"] = "3,4"
        GLineEdit_252.place(x=220,y=220,width=50,height=50)
        WordleFrames.append(GLineEdit_252)

        GLineEdit_264=tk.Entry(root)
        GLineEdit_264["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_264["font"] = ft
        GLineEdit_264["fg"] = "#333333"
        GLineEdit_264["justify"] = "center"
        GLineEdit_264["text"] = "3,5"
        GLineEdit_264.place(x=290,y=220,width=50,height=50)
        WordleFrames.append(GLineEdit_264)

        GLineEdit_105=tk.Entry(root)
        GLineEdit_105["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_105["font"] = ft
        GLineEdit_105["fg"] = "#333333"
        GLineEdit_105["justify"] = "center"
        GLineEdit_105["text"] = "4,1"
        GLineEdit_105.place(x=10,y=290,width=50,height=50)
        WordleFrames.append(GLineEdit_105)

        GLineEdit_186=tk.Entry(root)
        GLineEdit_186["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_186["font"] = ft
        GLineEdit_186["fg"] = "#333333"
        GLineEdit_186["justify"] = "center"
        GLineEdit_186["text"] = "4,2"
        GLineEdit_186.place(x=80,y=290,width=50,height=50)
        WordleFrames.append(GLineEdit_186)

        GLineEdit_604=tk.Entry(root)
        GLineEdit_604["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_604["font"] = ft
        GLineEdit_604["fg"] = "#333333"
        GLineEdit_604["justify"] = "center"
        GLineEdit_604["text"] = "5,1"
        GLineEdit_604.place(x=10,y=360,width=50,height=50)
        WordleFrames.append(GLineEdit_604)

        GLineEdit_925=tk.Entry(root)
        GLineEdit_925["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_925["font"] = ft
        GLineEdit_925["fg"] = "#333333"
        GLineEdit_925["justify"] = "center"
        GLineEdit_925["text"] = "4,3"
        GLineEdit_925.place(x=150,y=290,width=50,height=50)
        WordleFrames.append(GLineEdit_925)

        GLineEdit_426=tk.Entry(root)
        GLineEdit_426["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_426["font"] = ft
        GLineEdit_426["fg"] = "#333333"
        GLineEdit_426["justify"] = "center"
        GLineEdit_426["text"] = "4,4"
        GLineEdit_426.place(x=220,y=290,width=50,height=50)
        WordleFrames.append(GLineEdit_426)

        GLineEdit_763=tk.Entry(root)
        GLineEdit_763["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_763["font"] = ft
        GLineEdit_763["fg"] = "#333333"
        GLineEdit_763["justify"] = "center"
        GLineEdit_763["text"] = "4,5"
        GLineEdit_763.place(x=290,y=290,width=50,height=50)
        WordleFrames.append(GLineEdit_763)

        GLineEdit_451=tk.Entry(root)
        GLineEdit_451["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_451["font"] = ft
        GLineEdit_451["fg"] = "#333333"
        GLineEdit_451["justify"] = "center"
        GLineEdit_451["text"] = "5,2"
        GLineEdit_451.place(x=80,y=360,width=50,height=50)
        WordleFrames.append(GLineEdit_451)

        GLineEdit_741=tk.Entry(root)
        GLineEdit_741["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_741["font"] = ft
        GLineEdit_741["fg"] = "#333333"
        GLineEdit_741["justify"] = "center"
        GLineEdit_741["text"] = "5,3"
        GLineEdit_741.place(x=150,y=360,width=50,height=50)
        WordleFrames.append(GLineEdit_741)

        GLineEdit_963=tk.Entry(root)
        GLineEdit_963["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_963["font"] = ft
        GLineEdit_963["fg"] = "#333333"
        GLineEdit_963["justify"] = "center"
        GLineEdit_963["text"] = "5,4"
        GLineEdit_963.place(x=220,y=360,width=50,height=50)
        WordleFrames.append(GLineEdit_963)

        GLineEdit_198=tk.Entry(root)
        GLineEdit_198["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_198["font"] = ft
        GLineEdit_198["fg"] = "#333333"
        GLineEdit_198["justify"] = "center"
        GLineEdit_198["text"] = "5,5"
        GLineEdit_198.place(x=290,y=360,width=50,height=50)
        WordleFrames.append(GLineEdit_198)

        GLineEdit_60=tk.Entry(root)
        GLineEdit_60["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_60["font"] = ft
        GLineEdit_60["fg"] = "#333333"
        GLineEdit_60["justify"] = "center"
        GLineEdit_60["text"] = "2,2"
        GLineEdit_60.place(x=80,y=150,width=50,height=50)
        WordleFrames.append(GLineEdit_60)

        GLabel_716=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_716["font"] = ft
        GLabel_716["fg"] = "#333333"
        GLabel_716["justify"] = "center"
        GLabel_716["text"] = "@Baileyac20"
        GLabel_716.place(x=270,y=470,width=70,height=25)

        GLabel_513=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_513["font"] = ft
        GLabel_513["fg"] = "#cc0000"
        GLabel_513["justify"] = "center"
        GLabel_513["text"] = "Notification"
        GLabel_513.place(x=0,y=420,width=350,height=50)

# Main Code
async def Game():
    # Game Loop
    while True:
        # Reset Elements
        for v in WordleFrames:
            v["state"] = NORMAL
            print("hi")
        # Select Word
        word = "12345"

        await asyncio.sleep(0.01)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    
    for v in WordleFrames:
        x = v["text"].split(",")
        y = int(x[1])
        x = int(x[0])-1
        Map[x][y] = v
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(Game())
    loop.run_forever()
   
    root.mainloop()
