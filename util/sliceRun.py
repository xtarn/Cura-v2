from __future__ import absolute_import

import platform, os, subprocess, sys

if not hasattr(sys, 'frozen'):
	cura_sf_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../cura_sf/"))
	if cura_sf_path not in sys.path:
		sys.path.append(cura_sf_path)
	from skeinforge_application.skeinforge_utilities import skeinforge_craft


def getSliceCommand(filename):
	pass