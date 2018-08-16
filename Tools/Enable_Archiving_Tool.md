[Back to main menu](../index.md)  

Enable Archiving Tool
=====================

IMSMA Core Documentation -- August 2017

The **Enable Archiving** tool was written to assist with geodatabase
configuration. When run, the tool enables Geodatabase Archiving on every
feature class in a Workspace ( an enterprise geodatabase connection
file). This process completes the following steps for each feature
class:

1.  Check if Archiving is enabled on a feature class

2.  If not, enable Archiving, which:

    a.  Adds the gdb\_archive\_oid, gdb\_from\_date and gdb\_to\_date
        fields to the base table

    b.  Creates a \<table\_name\_evw database view, which only displays
        the latest feature from an archive table

3.  ArcGIS then displays the \<table\_name\> feature class, which is
    actually pointing directly at the \_evw view

This tool should be used early in the process of deploying a
geodatabase, as any further enabling of Archiving will require stopping
all GIS web services that access those datasets.
