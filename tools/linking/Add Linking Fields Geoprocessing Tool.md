Add Linking Fields Geoprocessing Tool
=====================================

GICHD IMSMA Core Documentation -- August 2017

The **Add Linking Fields** geoprocessing tool is designed to be run
against a geodatabase workspace, and is used to add the **imsma\_id**
and **imsma\_links** fields, which are used to track linkages between
different feature types in IMSMA Core. This tool should be run early in
the IMSMA design process, before data loading or further geodatabase
configuration. If the IMSMA Linking fields already exist or a schema
lock is detected, the tool will report the error and continue to the
next feature class.
