# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ValueMap2Lizmap
                                 A QGIS plugin
 This plugin creates a table layer with all the ValueMap items of the project to be used as input for a js script which shows description instead of code in Lizmap attribute tables
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-10-14
        copyright            : (C) 2020 by Gter srl
        email                : assistenzagis@gter.it
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ValueMap2Lizmap class from file ValueMap2Lizmap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .valuemap_2_lizmap import ValueMap2Lizmap
    return ValueMap2Lizmap(iface)
