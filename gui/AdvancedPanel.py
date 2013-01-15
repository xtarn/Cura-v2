import wx
import style

class AdvancedPanel(wx.ScrolledWindow):
	def __init__(self, parent):
		wx.ScrolledWindow.__init__(self, parent)

		self.SetScrollRate(0,5)


		heading_font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.LIGHT)
		small_font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.LIGHT)

		#---accuracy---
		head1_panel = wx.Panel(self)
		head1 = Text(head1_panel, 'Accuracy', heading_font, style.accent1)

		head1_1 = Text(head1_panel, 'Layer height (mm)', small_font)
		head1_2 = Text(head1_panel, 'Wall thickness (mm)', small_font)
		head1_3 = Text(head1_panel, 'Initial layer thickness (mm)', small_font)
		head1_4 = Text(head1_panel, 'Extra top/bottom wall (mm)', small_font)
		head1_5 = Text(head1_panel, "Enable 'skin'", small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head1, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))
		sizer.AddSpacer((0,25), (5,0))

		sizer.Add(head1_1, (2,1))
		sizer.Add(head1_2, (3,1))
		sizer.Add(head1_3, (4,1))
		sizer.Add(head1_4, (5,1))
		sizer.Add(head1_5, (6,1))
		head1_panel.SetSizer(sizer)

		#---fill---
		head2_panel = wx.Panel(self)
		head2 = Text(head2_panel, 'Fill', heading_font, style.accent1)

		head2_1 = Text(head2_panel, 'Bottom/Top thickness (mm)', small_font)
		head2_2 = Text(head2_panel, 'Fill density (&%)', small_font)
		head2_3 = Text(head2_panel, 'Infill pattern', small_font)
		head2_4 = Text(head2_panel, 'Infill overlap (&%)', small_font)
		head2_5 = Text(head2_panel, 'Solid infill top', small_font)
		head2_6 = Text(head2_panel, 'Print order sequence', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head2, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))
		sizer.AddSpacer((0,25), (5,0))
		sizer.AddSpacer((0,25), (6,0))

		sizer.Add(head2_1, (2,1))
		sizer.Add(head2_2, (3,1))
		sizer.Add(head2_3, (4,1))
		sizer.Add(head2_4, (5,1))
		sizer.Add(head2_5, (6,1))
		sizer.Add(head2_6, (7,1))
		head2_panel.SetSizer(sizer)

		#---speed---
		head3_panel = wx.Panel(self)
		head3 = Text(head3_panel, 'Speed', heading_font, style.accent1)

		head3_1 = Text(head3_panel, 'Print speed (mm/s)', small_font)
		head3_2 = Text(head3_panel, 'Travel speed (mm/s)', small_font)
		head3_3 = Text(head3_panel, 'Max Z speed (mm/s)', small_font)
		head3_4 = Text(head3_panel, 'Bottom layer speed (mm/s)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head3, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))

		sizer.Add(head3_1, (2,1))
		sizer.Add(head3_2, (3,1))
		sizer.Add(head3_3, (4,1))
		sizer.Add(head3_4, (5,1))
		head3_panel.SetSizer(sizer)

		#---support---
		head4_panel = wx.Panel(self)
		head4 = Text(head4_panel, 'Support Structure', heading_font, style.accent1)
		
		head4_1 = Text(head4_panel, 'Support type', small_font)
		head4_2 = Text(head4_panel, 'Material amount (&%)', small_font)
		head4_3 = Text(head4_panel, 'Distance from object (mm)', small_font)


		sizer = wx.GridBagSizer()
		sizer.Add(head4, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))

		sizer.Add(head4_1, (2,1))
		sizer.Add(head4_2, (3,1))
		sizer.Add(head4_3, (4,1))
		head4_panel.SetSizerAndFit(sizer)

		#---skirt---
		head5_panel = wx.Panel(self)
		head5 = Text(head5_panel, 'Skirt', heading_font, style.accent1)

		head5_1 = Text(head5_panel, 'Line count', small_font)
		head5_2 = Text(head5_panel, 'Start distance (mm)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head5, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))

		sizer.Add(head5_1, (2,1))
		sizer.Add(head5_2, (3,1))
		head5_panel.SetSizer(sizer)

		#---fillament---
		head6_panel = wx.Panel(self)
		head6 = Text(head6_panel, 'Fillament', heading_font, style.accent1)

		head6_1 = Text(head6_panel, 'Diameter (mm)', small_font)
		head6_2 = Text(head6_panel, 'Packing density', small_font)
		head6_3 = Text(head6_panel, 'Printing temperature', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head6, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))

		sizer.Add(head6_1, (2,1))
		sizer.Add(head6_2, (3,1))
		sizer.Add(head6_3, (4,1))
		head6_panel.SetSizer(sizer)

		#---machine size---
		head7_panel = wx.Panel(self)
		head7 = Text(head7_panel, 'Machine Size', heading_font, style.accent1)

		head7_1 = Text(head7_panel, 'Nozzle size (mm)', small_font)
		head7_2 = Text(head7_panel, 'Machine center X (mm)', small_font)
		head7_3 = Text(head7_panel, 'Machine center Y (mm)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head7, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))

		sizer.Add(head7_1, (2,1))
		sizer.Add(head7_2, (3,1))
		sizer.Add(head7_3, (4,1))
		head7_panel.SetSizer(sizer)

		#---Retraction---
		head8_panel = wx.Panel(self)
		head8 = Text(head8_panel, 'Retraction', heading_font, style.accent1)

		head8_1 = Text(head8_panel, 'Enable retraction', small_font)
		head8_2 = Text(head8_panel, 'Retract on jumps only', small_font)
		head8_3 = Text(head8_panel, 'Minimal travel (mm)', small_font)
		head8_4 = Text(head8_panel, 'Speed (mm/s)', small_font)
		head8_5 = Text(head8_panel, 'Distance (mm)', small_font)
		head8_6 = Text(head8_panel, 'Extra length on start (mm)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head8, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))
		sizer.AddSpacer((0,25), (5,0))
		sizer.AddSpacer((0,25), (6,0))

		sizer.Add(head8_1, (2,1))
		sizer.Add(head8_2, (3,1))
		sizer.Add(head8_3, (4,1))
		sizer.Add(head8_4, (5,1))
		sizer.Add(head8_5, (6,1))
		sizer.Add(head8_6, (7,1))
		head8_panel.SetSizer(sizer)

		#---cooling---
		head9_panel = wx.Panel(self)
		head9 = Text(head9_panel, 'Cooling', heading_font, style.accent1)

		head9_1 = Text(head9_panel, 'Minimal layer time (s)', small_font)
		head9_2 = Text(head9_panel, 'Enable cooling fan', small_font)
		head9_3 = Text(head9_panel, 'Minimum feedrate (mm/s)', small_font)
		head9_4 = Text(head9_panel, 'Fan on layer number', small_font)
		head9_5 = Text(head9_panel, 'Fan speed min (&%)', small_font)
		head9_6 = Text(head9_panel, 'Fan speed max (&%)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head9, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))
		sizer.AddSpacer((0,25), (5,0))
		sizer.AddSpacer((0,25), (6,0))

		sizer.Add(head9_1, (2,1))
		sizer.Add(head9_2, (3,1))
		sizer.Add(head9_3, (4,1))
		sizer.Add(head9_4, (5,1))
		sizer.Add(head9_5, (6,1))
		sizer.Add(head9_6, (7,1))
		head9_panel.SetSizer(sizer)

		#---raft---
		head10_panel = wx.Panel(self)
		head10 = Text(head10_panel, 'Raft', heading_font, style.accent1)

		head10_1 = Text(head10_panel, 'Add raft', small_font)
		head10_2 = Text(head10_panel, 'Extra margin (mm)', small_font)
		head10_3 = Text(head10_panel, 'Base material amount (&%)', small_font)
		head10_4 = Text(head10_panel, 'Interface amount (&%)', small_font)

		sizer = wx.GridBagSizer()
		sizer.Add(head9, (0,0), span=(1,4))
		sizer.AddSpacer((20,10), (1,0))
		sizer.AddSpacer((0,25), (2,0))
		sizer.AddSpacer((0,25), (3,0))
		sizer.AddSpacer((0,25), (4,0))

		sizer.Add(head10_1, (2,1))
		sizer.Add(head10_2, (3,1))
		sizer.Add(head10_3, (4,1))
		sizer.Add(head10_4, (5,1))
		head10_panel.SetSizer(sizer)		

		# # ---scroll sizer----
		sizer = wx.GridBagSizer()
		sizer.AddSpacer((30,20), (0,0))
		sizer.Add(head1_panel, (1,1))
		sizer.AddSpacer((1,20), (2,1))
		sizer.Add(head2_panel, (3,1))
		sizer.AddSpacer((1,20), (4,1))
		sizer.Add(head3_panel, (5,1))
		sizer.AddSpacer((1,20), (6,1))
		sizer.Add(head4_panel, (7,1))
		sizer.AddSpacer((1,20), (8,1))
		sizer.Add(head5_panel, (9,1))
		sizer.AddSpacer((1,20), (10,1))
		sizer.Add(head6_panel, (11,1))
		sizer.AddSpacer((1,20), (12,1))
		sizer.Add(head7_panel, (13,1))
		sizer.AddSpacer((1,20), (14,1))
		sizer.Add(head8_panel, (15,1))
		sizer.AddSpacer((1,20), (16,1))
		sizer.Add(head9_panel, (17,1))
		sizer.AddSpacer((1,20), (18,1))
		sizer.Add(head10_panel, (19,1))
		sizer.AddSpacer((1,20), (20,1))

		self.SetSizerAndFit(sizer)

class Text(wx.StaticText):
	def __init__(self, parent, label, font, colour=wx.BLACK):
		wx.StaticText.__init__(self, parent, label=label)
		self.SetFont(font)
		self.SetForegroundColour(colour)


