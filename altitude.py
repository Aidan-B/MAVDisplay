import tkinter as tk


class AltitudeWidget:
    
    def __init__(self, root, text):
        self._event = "<<update_attitude>>"
        
        self.text = text
        self.root = root
        self.label = tk.Label(root, text=text)
        self.label.place(x=0, y=0, relwidth=1, relheight=.5)

        self.root.bind(self._event, self.event_handler)  # event triggered by background thread

    def update_attitude_widget(self, text):
        # update text
        self.text = text

        # generate event
        self.root.event_generate(self._event, when="tail", state=123) # trigger event in main thread
    
    def event_handler(self, evt):
        self.label.config(text=self.text)  # update widget


        