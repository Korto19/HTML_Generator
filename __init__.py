# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HTML_Generator
                                 A QGIS plugin
 HTML single or multi page generator
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-11-18
        copyright            : (C) 2020 by Giulio
        email                : giulio.fattori@tin.it
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

__author__ = 'Giulio Fattori'
__date__ = '2020-11-18'
__copyright__ = '(C) 2020 by Korto19'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HTML_MultiPages class from file HTML_MultiPages.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .HTML_Generator import HTML_GeneratorPlugin
    return HTML_GeneratorPlugin()
