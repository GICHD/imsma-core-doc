[Back to main menu](../index.md)  

Working with Geodatabase Attachments
====================================

What are attachments?
---------------------

Attachments are files, of any type, that a user would like to "connect"
to an existing record or a newly-submitted record in a database. This
allows you to effectively staple an attachment to a record, such as a
PDF version of a report attached to the database row that represents it.

In IMSMAng, attachments were managed as a simple One to Many
relationship from any feature in the database, a user could attach one
or more files, and references to those files would be saved in a table,
with the file saved on disk in a single folder on the IMSMAng host
server.

Attachments are often used to store photographs of objects, evidence,
devices or hazards in the field

What are Geodatabase Attachments?
---------------------------------

In an ArcGIS Geodatabase, Attachments refer to "geodatabase
attachments," which are files that are stored inside the database,
related to specific rows in a feature class or table in the geodatabase.
This is different from the IMSMAng method of storing attachments on disk
and simply storing a link to the feature in the database itself.
Geodatabase attachments are stored as binary objects in a column in the
database, also known as BLOBs (Binary Large Objects).

Attachments provide a flexible way to manage additional information that
is related to your features. Attachments allow you to add files to
individual features and can be images, PDFs, text documents, or any
other type of file. For example, if you have a feature representing a
building, you could use attachments to add multiple photographs of the
building taken from several angles, along with PDF files containing the
building\'s deed and tax information.

To add file attachments, you first need to enable attachments on the
feature class or table. When you enable attachments, ArcGIS creates a
new table to contain the attachment files and a new relationship class
to relate the features to the attached files. You add attachments to the
features during an edit session or by using the Add Attachments
geoprocessing tool.

Attachments are similar to hyperlinks but allow you to associate
multiple files to a feature, store the attached files in the
geodatabase, and access the files in more ways. You can view attachments
from the Identify window, from the Attributes window (when editing), in
the attribute table window, and through HTML pop-up windows.

How are Geodatabase Attachments used in IMSMA Core?
---------------------------------------------------

One of the primary ways that IMSMA core differs from IMSMAng is that it
allows users to submit photographs from the field using Survey123. These
features are stored as geodatabase attachments when they are first
submitted, allowing a full web service based submission and query
process for these files.

In order to access these attachments for future use, a user must view
the feature class through a web service or directly from ArcGIS Desktop.
