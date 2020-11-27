<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="it" sourcelanguage="en">
<context>
    <name>ValueMap2Lizmap</name>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="189"/>
        <source>&amp;ValueMap to Lizmap</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="374"/>
        <source>ValueMap2Lizmap</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="378"/>
        <source>Error</source>
        <translation>Errore</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="378"/>
        <source>The valuemap table is not loaded in the project.</source>
        <translation>La tabella valuemap non è caricata nel progetto.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="332"/>
        <source>Warning</source>
        <translation>Attenzione</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="328"/>
        <source>The valuemap widget of field {} in layer {} is empty.</source>
        <translation type="obsolete">Il widget Value Map del campo {} nel layer {} è vuoto.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="374"/>
        <source>The process is succesfully completed</source>
        <translation>Il processo è terminato con successo</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="376"/>
        <source>Info</source>
        <translation>Info</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="372"/>
        <source>No layer with valuemap widget found</source>
        <translation type="obsolete">Non è stato trovato alcun layer con widget Value Map</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="332"/>
        <source>The Value Map widget of field {} in layer {} is empty.</source>
        <translation>Il widget Value Map del campo {} nel layer {} è vuoto.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="376"/>
        <source>No layer with Value Map widget found</source>
        <translation>Non è stato trovato alcun layer con widget Value Map</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="214"/>
        <source>The project must be saved before running the plugin.</source>
        <translation>Il progetto deve essere salvato prima di utilizzare il plugin.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap.py" line="220"/>
        <source>The Lizmap configuration file does not exist. Run Lizmap plugin to publish the project</source>
        <translation>Il file di configurazione Lizmap non esiste. Lanciare il plugin Lizmap per pubblicare il progetto</translation>
    </message>
</context>
<context>
    <name>ValueMap2LizmapDialogBase</name>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="14"/>
        <source>ValueMap to Lizmap</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="67"/>
        <source>ValueMap2Lizmap</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="97"/>
        <source>This plugin retrieves all codes and labels from  columns with
ValueMap widget and compiles a table layer. The table layer
has three text columns named: fieldname, cod and label and
it is automatically created and added to the QGIS project.
This table is then used by the valueMap_in_attributeTable.js
file in order to show descriptions instead of lables in  Lizmap
attribute tables.  The resulting table layer must be added  to
lizmap web client.  Moreover the script automatically put the
valueMap_in_attributeTable.js  in the  proper  folder.  If this
folder does not exist, it is automatically created.</source>
        <translation type="obsolete">Il  plugin  recupera tutti i codici e le descrizioni dalle colonne
con widget ValueMap e compila una tabella composta da tre
colonne testuali nominate : fieldname, cod and label e viene
automaticamente  creata  e  caricata nel progetto  QGIS.  La
tabella è poi utilizzata dal file  valueMap_in_attributeTable.js
per  mostrare  la descrizione invece del  codice nella  tabella
attributi di Lizamp.  La  tabella  deve essere  aggiunta  come
layer a lizmap web client. Inoltre lo script salva direttamente
il file valueMap_in_attributeTable.js nella cartella appropriata
Se questa cartella non esiste, viene automaticamente creata.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="143"/>
        <source>Help</source>
        <translation>Guida</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="163"/>
        <source>Ok</source>
        <translation>Ok</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="97"/>
        <source>This plugin retrieves all codes and labels from  columns with
ValueMap widget and compiles a table layer. The table layer
has three text columns named: fieldname, cod and label and
it is automatically created and added to the QGIS project.
This table is then used by the valueMap_in_attributeTable.js
file in order to show descriptions instead of lables in  Lizmap
attribute tables.  The resulting table layer must be added  to
lizmap web client as WFS.  Moreover the script automatically
put   the  valueMap_in_attributeTable.js   file  in  the  proper
folder. If the folder does not exist, it is automatically created.</source>
        <translation type="obsolete">Il  plugin  recupera  tutti i codici  e le  descrizioni dalle colonne
con widget ValueMap e  compila  una tabella  composta da tre
colonne  testuali  nominate :  fieldname, cod and label e viene
automaticamente  creata  e  caricata  nel  progetto   QGIS.  La
tabella è  poi  utilizzata dal  file  valueMap_in_attributeTable.js
per  mostrare  la  descrizione  invece del  codice  nella  tabella
attributi di Lizamp. La tabella deve essere aggiunta come WFS
layer a lizmap web client.  Inoltre lo script  salva  direttamente
il file valueMap_in_attributeTable.js  nella cartella  appropriata
Se questa cartella non esiste, viene automaticamente creata.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="109"/>
        <source>This plugin retrieves all codes and labels from columns with ValueMap widget and compiles a table layer. The table layer has three text columns named: fieldname, cod and label and it is automatically created and added to the QGIS project. This table is then used by the valueMap_in_attributeTable.js file in order to show descriptions instead of codes in Lizmap attribute tables. The resulting table layer must be added to lizmap web client as WFS. Moreover the script automatically puts the valueMap_in_attributeTable.js file in the proper folder. If the folder does not exist, it is automatically created.</source>
        <translation type="obsolete">Il plugin recupera tutti i codici e le descrizioni dalle colonne con widget ValueMap e compila una tabella composta da tre colonne testuali nominate: fieldname, cod and label e viene automaticamente creata e caricata nel progetto QGIS. La tabella è poi utilizzata dal file valueMap_in_attributeTable.js per mostrare la descrizione invece del codice nelle tabelle attributi di Lizamp. La tabella deve essere aggiunta come layer WFS a lizmap web client. Inoltre lo script salva direttamente il file valueMap_in_attributeTable.js nella cartella appropriata. Se questa cartella non esiste, viene automaticamente creata.</translation>
    </message>
    <message>
        <location filename="../valuemap_2_lizmap_dialog_base.ui" line="109"/>
        <source>This plugin retrieves all codes and labels from columns with ValueMap widget and compiles a table layer. The table layer has four text columns named: fieldname, cod, label and layer and it is automatically created and added to the QGIS project. This table is then used by the valueMap_in_attributeTable.js file in order to show descriptions instead of codes in Lizmap attribute tables. The resulting table layer must be added to lizmap web client as WFS. Moreover the script automatically puts the valueMap_in_attributeTable.js file in the proper folder. If the folder does not exist, it is automatically created.</source>
        <translation>Il plugin recupera tutti i codici e le descrizioni dalle colonne con widget ValueMap e compila una tabella composta da quattro colonne testuali nominate: fieldname, cod, label e layer e viene automaticamente creata e caricata nel progetto QGIS. La tabella è poi utilizzata dal file valueMap_in_attributeTable.js per mostrare la descrizione invece del codice nelle tabelle attributi di Lizamp. La tabella deve essere aggiunta come layer WFS a lizmap web client. Inoltre lo script salva direttamente il file valueMap_in_attributeTable.js nella cartella appropriata. Se questa cartella non esiste, viene automaticamente creata.</translation>
    </message>
</context>
</TS>
