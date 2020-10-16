# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ValueMap2Lizmap
                                 A QGIS plugin
 This plugin creates a table layer with all the ValueMap items of the project to be used as input for a js script which shows description instead of code in Lizmap attribute tables
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-10-14
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Gter srl
        email                : assistenzagis@gter.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import *

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .valuemap_2_lizmap_dialog import ValueMap2LizmapDialog
import os.path
import os
import shutil
from shutil import copyfile

class ValueMap2Lizmap:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ValueMap2Lizmap_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&ValueMap to Lizmap')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        #self.first_start = None
        self.pluginIsActive = False
        self.table = ''
        self.proj_dir = ''
        self.path_media_js = ''
        

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ValueMap2Lizmap', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToWebMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/valuemap_2_lizmap/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'ValueMap2Lizmap'),
            callback=self.pressIcon,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True
        self.dlg = ValueMap2LizmapDialog()

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'&ValueMap to Lizmap'),
                action)
            self.iface.removeToolBarIcon(action)
            
    def pressIcon(self):
        print(self.pluginIsActive)
        if not self.pluginIsActive:
            #print(self.data)
            self.pluginIsActive = True
            self.dlg = ValueMap2LizmapDialog()
            
            self.dlg.helpButton.clicked.connect(self.openHelpButton)
            self.dlg.pushButtonOk.clicked.connect(self.run)
            self.dlg.rejected.connect(self.closePlugin)
            
            self.prepRun()
            self.dlg.show()
        else:
            self.dlg.show()
            self.dlg.activateWindow()
            
    def prepRun(self):
        self.proj_dir = QgsProject.instance().homePath()
        proj_name = QgsProject.instance().fileName().split('/')[-1].split('.')[0]
        if not os.path.exists('{}/media'.format(self.proj_dir)):
            os.makedirs('{}/media/js/{}'.format(self.proj_dir, proj_name))
        else:
            if not os.path.exists('{}/media/js'.format(self.proj_dir)):
                os.makedirs('{}/media/js/{}'.format(self.proj_dir, proj_name))
            else:
                if not os.path.exists('{}/media/js/{}'.format(self.proj_dir, proj_name)):
                    os.makedirs('{}/media/js/{}'.format(self.proj_dir, proj_name))

        if QgsProject.instance().mapLayersByName('valuemap'):
            self.table = QgsProject.instance().mapLayersByName('valuemap')[0]
        else:
            path_plg_dbf = os.path.join(self.plugin_dir, 'valuemap.dbf')
            path_media_dbf = os.path.join('{}/media'.format(self.proj_dir), 'valuemap.dbf')
            if not os.path.isfile(path_media_dbf):
                copyfile(path_plg_dbf, path_media_dbf)
            #print(path)
            lyr_table = QgsVectorLayer(path_media_dbf, 'valuemap')
            QgsProject.instance().addMapLayers([lyr_table])
            self.table = QgsProject.instance().mapLayersByName('valuemap')[0]
            
        path_plg_js = os.path.join(self.plugin_dir, 'valueMap_in_attributeTable.js')
        self.path_media_js = os.path.join('{}/media/js/{}'.format(self.proj_dir, proj_name), 'valueMap_in_attributeTable.js')
        if not os.path.isfile(self.path_media_js):
            copyfile(path_plg_js, self.path_media_js)
            
    def openHelpButton(self):
        webbrowser.open('https://manuale-cdu-creator.readthedocs.io/it/latest/')
            
    def closePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        print("** CLOSING Plugin")
        self.dlg.pushButtonOk.clicked.disconnect(self.run)
        self.dlg.rejected.disconnect(self.closePlugin)
        self.dlg.helpButton.clicked.disconnect(self.openHelpButton)
        
        self.pluginIsActive = False
        self.table = ''
        self.proj_dir = ''
        self.path_media_js = ''
        
        from qgis.utils import reloadPlugin
        reloadPlugin("ValueMap2Lizmap")
        
    def endPlugin(self):
        self.closePlugin()
        self.dlg.close()


    def run(self):
        """Run method that performs all the real work"""

        # # Create the dialog with elements (after translation) and keep reference
        # # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        # if self.first_start == True:
            # self.first_start = False
            # self.dlg = ValueMap2LizmapDialog()

        # # show the dialog
        # self.dlg.show()
        # # Run the dialog event loop
        # result = self.dlg.exec_()
        result = True
        # See if OK was pressed
        if result:
            if QgsProject.instance().mapLayersByName('valuemap'):
                #index of field containing code
                idxC = self.table.fields().indexOf('cod')
                #index of field containing label
                idxD = self.table.fields().indexOf('label')
                #index of field containing the field name
                idxF = self.table.fields().indexOf('fieldname')
                pr = self.table.dataProvider()
                projectInstance = QgsProject.instance()
                root = projectInstance.layerTreeRoot()
                lista = []
                layernames = []
                #the txt file in which the name of layers with valuemap widgets will be stored
                txt_file = os.path.join('{}/media'.format(self.proj_dir),'layer.txt')

                for child in root.findLayers():
                    #check if layer is vector with geom
                    if isinstance(child.layer(), QgsVectorLayer) and child.layer().geometryType() != 4:
                        lyr = child.layer()
                        #get the name of layer with valuemap widgets
                        for f in lyr.fields():
                            if f.editorWidgetSetup().type() == 'ValueMap':
                                layernames.append(lyr.name())
                        #iterate over all fields of the layer
                        for idx in lyr.fields().allAttributesList():
                            if lyr.editorWidgetSetup(idx).type() == 'ValueMap':
                                fieldname = lyr.fields().field(idx).name()
                                #iterate over cod/label of valuemap widget
                                for dicts in lyr.editorWidgetSetup(idx).config().values():
                                    for d in dicts:
                                        for k, v in d.items():
                                            lista.append([v, k, fieldname])

                #write values in the table excluding duplicated records
                list_set = set(map(tuple,lista))
                unique = list(map(list,list_set))
                self.table.startEditing()
                for u in unique:
                    feat = QgsFeature(self.table.fields())
                    feat.setAttribute(idxC, u[0])
                    feat.setAttribute(idxD, u[1])
                    feat.setAttribute(idxF, u[2])
                    pr.addFeature(feat)
                self.table.commitChanges()

                #write layers names in the txt file
                name_set = set(layernames)
                unique_name = list(name_set)
                with open(txt_file, "w") as file:
                    for un in unique_name:
                        file.write('\'' + un + '\'' + ',\n')
                file.close()
                
                with open(self.path_media_js,'r') as fjs:
                    lines = fjs.readlines()

                with open(self.path_media_js,'w') as fjs:
                    for line in lines:
                        #print(line)
                        if line.startswith('var layers_to_translate ='):
                            #newline = line.replace('""', ',\n'.join(unique_name))
                            line = 'var layers_to_translate = {};\n'.format(unique_name)
                        fjs.write(line)
                    fjs.close()
            else:
                self.iface.messageBar().pushMessage("ATTENZIONE", "La tabella valuemap non è caricata nel progetto.", level=Qgis.Critical, duration=4)
            print('FINISHED')
            self.endPlugin()
            