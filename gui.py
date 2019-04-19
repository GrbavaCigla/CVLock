import gi
import cv2
import getpass
import os
import numpy
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
OUTPUT_FOLDER = "/usr/local/CVLock/"

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
class ListTile(Gtk.Box):
    def __init__(self,text,action_wdiget):
        Gtk.Box.__init__(self)
        self.label=Gtk.Label()
        self.label.set_text(text)
        self.space = Gtk.Box()
        
        self.space.set_hexpand(True)
        self.pack_start(self.label,False,False,10)
        self.pack_start(self.space, True, True, 0)
        self.pack_end(action_wdiget,False,False,10)


class MainWindow(Gtk.Window):
    def scan(self,*args):
        cv2.imwrite(("/usr/local/CVLock/" + getpass.getuser() + "/crop{}.jpg").format(self.counter),self.roi_gray)
        self.counter += 1
        
    def show_frame(self,*args):
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channels = frame.shape
        # TODO: Resize before cropping. IMPORTANT!
        fitsize = (600,400)
        xmargin = int((width-fitsize[0])/2)
        ymargin = int((height-fitsize[1])/2)
        frame = frame[ymargin:ymargin+fitsize[1], xmargin:xmargin+fitsize[0]]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 4)
            self.roi_gray = gray[y:y+h, x:x+w].copy()
            roi_color = frame[y:y+h, x:x+w].copy()
        pb = GdkPixbuf.Pixbuf.new_from_data(frame.tostring(),GdkPixbuf.Colorspace.RGB,False,8,fitsize[0],fitsize[1],fitsize[0]*channels)
        self.image.set_from_pixbuf(pb.copy())
        return True
    def __init__(self):
        Gtk.Window.__init__(self, title="CVLock - "+getpass.getuser())
        self.set_default_size(900, 400)
        self.set_resizable(False)
        self.counter = 0
        self.set_border_width(0)
        self.grid = Gtk.Grid()
        # self.grid.set_column_homogeneous(True)
        self.add(self.grid)
        self.image = Gtk.Image()
        self.grid.attach(self.image, 0, 0, 1, 1)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.grid.attach_next_to(self.box,self.image,Gtk.PositionType.RIGHT,1,1)
        
        self.listview = Gtk.ListBox()
        self.listview.set_selection_mode(Gtk.SelectionMode(0))
        self.listview.set_vexpand(True)
        self.box.pack_start(self.listview,True,True,0)

        self.user_info = Gtk.Label(label=getpass.getuser())
        self.listview.add(ListTile("Username", self.user_info))

        self.output_info = Gtk.Label(label=OUTPUT_FOLDER)
        self.listview.add(ListTile("Output Folder", self.output_info))

        self.scan_btn = Gtk.Button(label="Scan")
        self.scan_btn.connect("pressed",self.scan)
        self.box.pack_start(self.scan_btn,False,True,0)
window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
GLib.idle_add(window.show_frame)
Gtk.main()
