import wx
import style

from customControls import ToggleSwitch, GenericButton

class TransformPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(style.width*3+1, style.height*7+1))

		heading_font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.LIGHT)
		small_font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.LIGHT)

		swap_heading = wx.StaticText(self, label='Swap')
		mirror_heading = wx.StaticText(self, label='Mirror')
		scale_heading = wx.StaticText(self, label='Scale')

		swap_heading.SetFont(heading_font)
		mirror_heading.SetFont(heading_font)
		scale_heading.SetFont(heading_font)

		swap_heading.SetForegroundColour(style.accent1)
		mirror_heading.SetForegroundColour(style.accent1)
		scale_heading.SetForegroundColour(style.accent1)

		# swap panel
		swap_panel = wx.Panel(self)

		xy_heading = wx.StaticText(swap_panel, label='Swap X and Y')
		yz_heading = wx.StaticText(swap_panel, label='Swap Y and Z')

		xy_heading.SetFont(small_font)
		yz_heading.SetFont(small_font)

		self.xy_button = ToggleSwitch(swap_panel)
		self.yz_button = ToggleSwitch(swap_panel)

		sizer = wx.GridBagSizer()
		sizer.AddSpacer((20,1), (0,0))
		sizer.AddSpacer((100,1), (0,1))
		sizer.AddSpacer((1,25), (1,0))
		sizer.AddSpacer((1,25), (2,0))
		sizer.AddSpacer((20,1), (0,2))

		sizer.Add(xy_heading, (1,1))
		sizer.Add(yz_heading, (2,1))
		sizer.Add(self.xy_button, (1,3))
		sizer.Add(self.yz_button, (2,3))

		swap_panel.SetSizerAndFit(sizer)

		#mirror panel
		mirror_panel = wx.Panel(self)

		x_heading = wx.StaticText(mirror_panel, label='Mirror X')
		y_heading = wx.StaticText(mirror_panel, label='Mirror Y')
		z_heading = wx.StaticText(mirror_panel, label='Mirror Z')

		x_heading.SetFont(small_font)
		y_heading.SetFont(small_font)
		z_heading.SetFont(small_font)

		self.x_button = ToggleSwitch(mirror_panel)
		self.y_button = ToggleSwitch(mirror_panel)
		self.z_button = ToggleSwitch(mirror_panel)

		sizer = wx.GridBagSizer()
		sizer.AddSpacer((20,1), (0,0))
		sizer.AddSpacer((100,1), (0,1))
		sizer.AddSpacer((1,25), (1,0))
		sizer.AddSpacer((1,25), (2,0))
		sizer.AddSpacer((1,25), (3,0))
		sizer.AddSpacer((20,1), (0,2))

		sizer.Add(x_heading, (1,1))
		sizer.Add(y_heading, (2,1))
		sizer.Add(z_heading, (3,1))
		sizer.Add(self.x_button, (1,3))
		sizer.Add(self.y_button, (2,3))
		sizer.Add(self.z_button, (3,3))

		mirror_panel.SetSizerAndFit(sizer)

		#scale panel
		scale_panel = wx.Panel(self)

		self.scale = wx.SpinCtrl(scale_panel)
		self.scale.SetValue(1.0)

		sizer = wx.GridBagSizer()
		sizer.AddSpacer((20,1), (0,0))
		sizer.AddSpacer((1,25), (1,0))

		sizer.Add(self.scale, (1,1))

		scale_panel.SetSizer(sizer)

		#reset button
		reset = GenericButton(self, 'Reset All')
		reset.Bind(wx.EVT_BUTTON, self.onReset)

		# window settings
		sizer = wx.GridBagSizer()
		sizer.AddSpacer((30,20), (0,0))

		sizer.Add(swap_heading, (1,1))
		sizer.AddSpacer((1,10), (2,1))
		sizer.Add(swap_panel, (3,1))
		sizer.AddSpacer((1,10), (4,1))

		sizer.Add(mirror_heading, (5,1))
		sizer.AddSpacer((1,10), (6,1))
		sizer.Add(mirror_panel, (7,1))
		sizer.AddSpacer((1,10), (8,1))

		sizer.Add(scale_heading, (9,1))
		sizer.AddSpacer((1,10), (10,1))
		sizer.Add(scale_panel, (11,1))
		sizer.AddSpacer((1,10), (12,1))

		sizer.AddSpacer((1,30), (13,1))
		sizer.Add(reset, (14,1))

		self.SetSizer(sizer)
		self.Fit()


	def onReset(self, event):
		self.xy_button.clear()
		self.yz_button.clear()
		self.x_button.clear()
		self.y_button.clear()
		self.z_button.clear()
		self.scale.SetValue(1)
