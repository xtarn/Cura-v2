import wx
import style

class StatusPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(style.width*3+1, style.height*7+1))
