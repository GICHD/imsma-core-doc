[Back to main menu](../index.md)  

Making Changes to Survey123 Forms
=================================

Survey123 Forms are created through the following process:

1.  Create form in Survey123 Connect

2.  Edit XLSForm spreadsheet to add questions and change parameters

3.  Preview form in Survey123 Connect to test validation, skip logic,
    etc.

4.  Publish the form to your Portal

    a.  This step creates a feature service and data schema to match
        your questions

    b.  **Note: at this point you can no longer change certain aspects
        of the form without recreating the service and losing your
        data**

Types of Changes Allowed
------------------------

Provided your edits don\'t change the schema of the feature service, you
can republish your survey without deleting and re-creating the feature
service. Only the form item will be updated. The following table
describes the changes that can be made to a published survey that would
not cause loss of data. 


|  Changes                                                        | Done without republishing? |
| --- | --- |
|  Reorder questions                                              | Yes |
|  Delete questions                                               | Yes |
|  Update labels in questions                                     | Yes |
|  Update labels in groups                                        | Yes |
|  Add, update, or delete choices in lists\*                      | Yes |
|  Update constraints, defaults, hints, required question status  | Yes |
|  Update calculations, choice filters                            | Yes |
|  Delete questions or repeats                                    | Yes |
|  Change question types                                          | No |
|  Add new questions                                              | No |
|  Add repeats                                                    | No |
|  Add new notes                                                  | Yes |
|  Update repeat name                                             | No |
|  Add groups                                                     | Yes |


\*If a field has a domain the choices in the choice list can only be
deleted to limit the options. If you would like to add choices for a
text field you can do so but it will not create a domain in the feature
service.

See
[http://doc.arcgis.com/en/survey123/desktop/create-surveys/publishsurvey.htm\#ESRI\_SECTION1\_97A01E11C37D401EB95C7D22EF251F66](http://doc.arcgis.com/en/survey123/desktop/create-surveys/publishsurvey.htm#ESRI_SECTION1_97A01E11C37D401EB95C7D22EF251F66)
for more information.

Survey Sheet:
-------------


|  Survey123 XLSForm Column   | Can be updated without feature service updates?  | Comments |
| --- | --- | --- |
|  type                       | Yes                                              | Change of type must be compatible with field type (ex: text to select\_one, date to dateTime) |
|  name                       | No                                                |  |
|  label::en                  | Yes                                              | |
|  hint                       | Yes                                              | |
|  constraint                 | Yes                                              | |
|  constraint\_message        | Yes                                              | |
|  required                   | Yes                                              | |
|  required\_message          | Yes                                              | |
|  appearance                 | Yes                                              | |
|  default                    | Yes                                              | Must be compatible with any domain values |
|  readonly                   | Yes                                              | |
|  relevant                   | Yes                                              | |
|  calculation                | Yes                                              | |
|  choice\_filter             | Yes                                              | |
|  repeat\_count              | Yes                                              | |
|  label::language(..)        | Yes                                              | |
|  hint::language(..)         | Yes                                              | |
|  media::audio               | Yes                                              | |
|  media::image               | Yes                                              | |
|  body::accuracyThreshold    | Yes                                              | |
|  bind::esri:fieldType       | No                                               | |
|  bind::esri:fieldLength     | Yes                                              | Can only shorten, cannot lengthen |
|  bind::esri:fieldAlias      |                                                  | |
|  body::esri:inputMask       | Yes                                              | |
|  bind::esri:parameters      | Yes                                              | |
|  bind::esri:saveIncomplete  | Yes                                              | |

Choices Sheet:
--------------

 | Column              |  Can this be updated? |  Comments |
 | --- | --- | --- |
 | list\_name          |  No                   |  |
 | name                |  No                   |  |
 | label               |  Yes                  | |
 | image               |  Yes                  |  |
 | label::language(..) |  Yes                  |  |

Notes:

-   If you add a new list for a given field this will not cause a domain
    to be applied to a field in the feature service.

-   You can delete choices but you cannot add them to a list that has
    been applied to a field with a domain.

Settings Sheet:
---------------

 | Column              |  Can this be updated? |  Comments |
 | --- | --- | --- |
 | form\_title        | Yes   |                 |
 | form\_id           | No   |                 |
 | instance\_name     | Yes   |                | 
 | submission\_url    | No    |                 |
 | default\_language  | Yes   |                 |
 | version            | Yes   |                 |
 | style              | Yes   |                 |

Workarounds
===========

If you need to add questions to your survey or change the choices of a
question that points to a field with a domain you must modify the
feature service before modifying the survey to avoid the feature service
being republished.

Adding questions:

-   Add the feature service to a new map with full editing control or
    add the feature service to a map in ArcGIS Pro.

-   Add fields to your feature service that correspond with the question
    types you would like to create.

-   Add questions to your survey form that correspond to the field names
    you just added to your feature service.

Changing question choices:

-   Use the Solution Deployment Add-In in ArcGIS Pro to modify the
    values of the feature service domain.

-   Modify the choices sheet making sure the values in the name column
    match the new values in the domain.

There are certain types of questions that can be added without affecting
the existing schema of the feature service.

-   Groups -- can be used to break down questions in your survey into
    logical sections

-   Notes -- can be used to provide users with critical information or
    feedback to help capture data more efficiently

All other types of questions can be added without affecting the existing
schema by using the bind::esri:fieldType of null. This could prove
useful for questions that are used to drive the relevant logic of the
survey or to gather information used in a calculation.

[Back to main menu](../index.md)  
