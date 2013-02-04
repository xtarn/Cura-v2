import wx
import style
import threading
import os
import binascii

from gui.customControls import GenericButton
from util import printerConnect
from util import sliceRun

class PrintPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(style.width*3+1, style.height*7+1))

		heading_font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.LIGHT)
		small_font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.LIGHT)

		head1_panel = wx.Panel(self)
		head1 = Text(head1_panel, 'Setting Summary', heading_font, style.accent1)

		head1_1 = Text(head1_panel, 'Quality', small_font)
		head1_2 = Text(head1_panel, 'Material', small_font)
		head1_3 = Text(head1_panel, 'Special', small_font)

		self.quality = Text(head1_panel, 'Unknown', small_font)
		self.material = Text(head1_panel, 'Unknown', small_font)
		self.special = Text(head1_panel, 'Unknown', small_font)


		slice_panel = wx.Panel(self)
		prepare_button = GenericButton(slice_panel, label='Prepare Print\t')
		prepare_button.Bind(wx.EVT_BUTTON, self.OnSlice)

		self.progress_gauge = wx.Gauge(slice_panel, size=(200,20))
		self.progress_gauge.SetRange(100)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(prepare_button)
		sizer.AddSpacer(20)
		sizer.Add(self.progress_gauge)
		sizer.AddSpacer(10)
		slice_panel.SetSizer(sizer)

		self.send_button = GenericButton(self, label='Send to Printer\t')
		self.send_button.Bind(wx.EVT_BUTTON, self.OnSend)

		sizer = wx.GridBagSizer()
		sizer.Add(head1, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((500,0), (1,3))
		sizer.AddSpacer((150,0), (1,1), span=(1,2))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))

		sizer.Add(head1_1, (2,1))
		sizer.Add(head1_2, (3,1))
		sizer.Add(head1_3, (4,1))

		sizer.Add(self.quality, (2,3))
		sizer.Add(self.material, (3,3))
		sizer.Add(self.special, (4,3))

		head1_panel.SetSizer(sizer)

		sizer = wx.GridBagSizer()
		sizer.AddSpacer((30,20), (0,0))
		sizer.Add(head1_panel, (1,1))
		sizer.AddSpacer((1,20), (2,1))
		sizer.Add(slice_panel, (3,1))
		sizer.AddSpacer((0,20), (4,1))
		sizer.Add(self.send_button, (5,1))

		self.SetSizerAndFit(sizer)

		self.send_button.disable()

		self.printTime = None
		self.filamentLength = None
		self.filamentWeight = None
		self.mat = None
		self.cost = None

	def OnSlice(self, event):
		frame = self.GetParent().GetParent().GetParent()

		thread = WorkerThread(self, frame.filename)

		self.send_button.enable()


	def OnSend(self, event):

		uniqueId = binascii.hexlify(os.urandom(4))

		frame = self.GetParent().GetParent().GetParent()

		info = []
		info.append(frame.filename[frame.filename.rfind('/')+1:-4] + '\n')
		info.append(self.printTime + '\n')
		info.append(self.filamentLength + '\n')
		info.append(self.filamentWeight + '\n')
		info.append(self.mat + '\n')
		info.append(self.cost + '\n')
		info.append(os.uname()[1] + '\n')
		info.append(uniqueId)

		infofile = open(frame.filename[:-4] + ".info", "w")
		infofile.writelines(info)
		infofile.close()

		printserv = printerConnect.printerConnect()
		printserv.connect()

		printserv.sendJob(frame.filename, uniqueId)
		printserv.sendJobInfo(frame.filename, uniqueId)
		printserv.closeConnection()


class WorkerThread(threading.Thread):
	def __init__(self, notifyWindow, filename):
		threading.Thread.__init__(self)

		self.filename = filename
		self.notifyWindow = notifyWindow
		self.cmdList = sliceRun.getSliceCommand(filename)
		self.start()

	def run(self):
		pass
		#p = sliceRun.startSliceCommandProcess(self.cmdList)

class Text(wx.StaticText):
	def __init__(self, parent, label, font, colour=wx.BLACK):
		wx.StaticText.__init__(self, parent, label=label)
		self.SetFont(font)
		self.SetForegroundColour(colour)