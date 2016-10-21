# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Analyst Toolbar
                                 A QGIS plugin
 View Analyst Toolbar Files
                             -------------------
        begin                : 2016-07-12
        copyright            : (C) 2016 by NorthArrowResearch
        email                : info@northarrowresearch.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

######################### REMOTE DEBUG #########################
# To activate remote debugging set ENVIRONMENT=DEBUG as a QGIS
# Environment variable in Preferences -> System -> Environment
import os
if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] == "DEBUG":
    import pydevd
    pydevd.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)
######################### /REMOTE DEBUG #########################

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ToolbarViewer class from file ToolbarViewer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .toolbar_viewer import ToolbarViewer
    return ToolbarViewer(iface)
