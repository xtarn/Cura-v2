import wx
import style

class LoadPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(style.width*3+1, style.height*7+1))

		heading_font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.LIGHT)

		load_stl_heading = wx.StaticText(self, label='Load STL')
		load_batch_heading = wx.StaticText(self, label='Load Batch Project')
		load_online_heading = wx.StaticText(self, label='Load From Thingiverse')

		load_stl_heading.SetFont(heading_font)
		load_stl_heading.SetForegroundColour(style.accent1)

		load_batch_heading.SetFont(heading_font)
		load_batch_heading.SetForegroundColour(style.accent1)

		load_online_heading.SetFont(heading_font)
		load_online_heading.SetForegroundColour(style.accent1)


		sizer = wx.GridBagSizer()
		sizer.AddSpacer((30,20), (0,0))
		sizer.Add(load_stl_heading, (1,1))
		sizer.Add(load_batch_heading, (3, 1))
		sizer.Add(load_online_heading, (5,1))

		self.SetSizerAndFit(sizer)
