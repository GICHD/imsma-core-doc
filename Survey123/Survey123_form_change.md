# Survey123 form change

The following guide is to help making changes to Survey123 forms that are configured to submit data to a feature service that is connected to a geodatabase. This would be indicated by a Feature Service item URL stored in the **submission_url** field in the XLSForm's settings worksheet.

For more details on how to connect a survey123 form to a geodatabase structure, check this [documentation](Connecting_a_Survey123_form_to_a_Geodatabase_Structure.md).  



## Changes with No Impact on GDB

First of all, what can be changed in a Survey123 form with no impact to the geodatabase, i.e. no required changes on the data side:

- changes to the following Survey123 Excel file columns:
  - label (Note that the field "aliases" are not updated in the geodatabase automatically but there is no functional requirement to change them)
  - hint
  - constraint
  - constraint_message
  - required
  - required_message
  - appearance
  - default
  - readonly
  - relevant
  - calculation
  - choice_filter
  - repeat_count
  - media::audio
  - media::image
  - body::accuracyThreshold
  - body::esri:inputMask
  - (bind::esri:parameters) TO CHECK
  - bind::saveIncomplete
- changes to the Settings page in Survey123 Connect for ArcGIS
  - Thumbnail, Title, Summary, Description
  - Style
  - Map default settings
  - Image settings
  - Inbox settings
  - Sent Surveys settings
- deleting a field (optional: [deleting a field from geodatabase](#deleting-a-field-from-geodatabase)
- deleting a repeat (optional: [deleting a related table from geodatabase](#deleting-a-related-table-from-geodatabase))



## Changes that must be made in the Geodatabse (GDB)

Now what changes in a Survey123 form have an impact to the geodatabase and involve modifications to the structure or configuration of the geodatabase.  

`Each possible change has a link in this document that provides step by step guidance on what to do to implement the change in the geodatabase `

- changes to the following Survey123 Excel file columns:
  - type
    - [text to integer](#change-of-type---old_type-to-new_type)
    - [integer to decimal](#change-of-type---old_type-to-new_type)
    - [... to ...](#change-of-type---old_type-to-new_type)
    - [text to select_one](#change-of-type---text-to-select_one) - Note that text to select_one can be changed and reflected in the Field App without updating the GDB but the web view of the data will not use drop-downs unless the GDB change is made.
  - [name](#change-of-field-name)
  - [label](#change-of-label) (if the label change needs to be reflected in the geodatabase)
  - [bind::esri:fieldType](#change-of-type---old_type-to-new_type)
  - [bind::esri:fieldLength](#change-of-bindesrifieldlength)

- [adding a new field](#adding-a-new-field)

  - [adding a new geopoint field to a repeat](#adding-a-new-geopoint-field)

- [modifying a choice list](#modifying-a-choice-list) (if the change needs to be reflected in the geodatabase e.g for use in a web app) 

- [adding a new repeat](#adding-a-new-repeat)


## Step by Step Guides

#### Change of type - old_type to new_type

The data between the fields must be compatible, meaning if you are changing from text to integer, all text values must already be integers, for example. 

1. Stop all feature services using the impacted geodatabase table using ArcGIS Server Manager. If in doubt, stop the ArcGIS Server Windows service which will stop all map and feature services temporarily.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Click on and rename the **old_type** field

5. Save changes

6. Add a **new_type** field by clicking on the last line of the table

7. Enter the field name (same name as **old_type** field), the alias (same alias as **old_type** field), and Data Type (See the [Data Type Conversion Table](#data-type-conversion-table) for more information)

8. Click "out" of the field to complete your edit and if desired, change the position of the field (by clicking, holding and dragging up) to the same position as in Survey123

9. Save changes in the ribbon at the top of the window

10. Open the Attribute Table, right click on the column header of the **new_type** field and choose Calculate Field

11. In the Calculate Field geoprocessing window, select the renamed **old_type** field as the new value

12. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

13. Delete the renamed **old_type** field

14. Save changes

15. Restart feature service(s) or the ArcGIS Server service

[top](#impact-on-gdb) 

#### Change of type - text to select_one

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Find the field and click in the domain cell

5. Choose **Add New Coded Value Domain** and enter your domain information

6. Save changes. If Save fails, use the GP tools **Create Domain**, **Add Coded Value To Domain** and **Assign Domain To Field**

7. Restart feature service(s) or the ArcGIS Server service

[top](#impact-on-gdb) 

#### Change of field name

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Rename the **Field Name**

5. Save changes

6. Restart feature service(s) or the ArcGIS Server service


[top](#impact-on-gdb) 

#### Change of label

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Change the field **Alias**

5. Save changes

6. Restart feature service(s) or the ArcGIS Server service


[top](#impact-on-gdb) 

#### Change of bind::esri:fieldLength

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Change the field **Length** - Note that your new length must be longer than any existing data in the table, or longer than your previous length value.

5. Save changes

6. Restart feature service(s) or the ArcGIS Server service


[top](#impact-on-gdb) 

#### Adding a new field

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Add a new field by clicking on the last line of the table

5. Enter the field name (name in Survey123), the alias (label in Survey123), Data Type (type in Survey123) and the Domain information if it is a select_one. See the [Data Type Conversion Table](#data-type-conversion-table) for more information.

6. Change the position of the field (by dragging up) to the same position as in Survey123

7. Save changes

8. Restart feature service(s) or the ArcGIS Server service


[top](#impact-on-gdb) 

#### Adding a new geopoint field

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Rename the standalone table (like !name!_old) and re-add it to the map
  
4. Create new repeat feature class 

  a. Right click on the database connection and select New, Feature Class

  b. Choose Point as the Feature Class Type and use the same name as the previous table

  c. Import fields from the standalone table (remove Global Id from list)

  d. Choose the right Coordinate System (usually WGS 1984)
  
  e. Finalize creation
  
  f. Right click on the new feature class and Add Global Ids, Enable Archiving and Enable Editor Tracking
  
  g. Add the feature class to the map and rename it in the map Layer List by removing the database and schema information, i.e. `imsma.geo.my_table` -> `my_table`

5. Join the original standalone table (containing information without geographic information) to the feature class containing geographic information, in most cases it would be the main feature class of the Survey123 form with a join on uniquerowid/parentroxid.

6. Append information from the feature class with the join to the new empty feature class with the option Use the Field Map to reconcile schema differences (Editor tracking information is lost)

7. Remove the join

8. Delete and re-create relationship class to point to the new feature class

9. Remove standalone table from map

10. Restart feature service(s) or the ArcGIS Server service (need to be done before overwriting the service definition)

11. Change feature service definition by going to Share, Web Layer, Overwrite Web Layer


[top](#impact-on-gdb) 

#### Adding a new repeat

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Following [this procedure](Connecting_a_Survey123_form_to_a_Geodatabase_Structure.md), create a new temporary Survey123 form, export the structure and copy the new repeat structure in the geodatabase (just the repeat table not the other tables, they already exists in the database).

4. Do not forget to create the new relationship class from parent record to your new table, enable archiving and create attachment tables if necessary

5. Add new feature class to the map used to create the feature service, at the bottom of the layer list.

6. Restart feature service(s) or the ArcGIS Server service (need to be done before overwriting the service definition)

7. Update feature service definition by going to Share, Web Layer, Overwrite Web Layer

8. Check all webmaps and webapps using the feature service



[top](#impact-on-gdb) 

#### Modifying a choice list

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on a feature class of the geodatabase where the choice list must be modified and select **Design** then **Domains**

4. Find the domain in the list and select it

5. Do the modifications in the code list

7. Save changes (if Save fails, it is possible to use the **Add Coded Value To Domain** GP tool)

6. Restart feature service(s) or the ArcGIS Server service


[top](#impact-on-gdb) 

#### Deleting a field from geodatabase

1. Ensure that all users have submitted data from their devices (no pending Outbox forms) then stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Right click on the feature class/table on which the field must be added and select **Design** then **Fields**

4. Delete the field by right clicking on the field and select Delete

5. Save changes

6. Restart feature service(s) or the ArcGIS Server service

7. Ensure that your Survey123 form also has the field deleted and users have updated to the new form version or users will be unable to submit data. 


[top](#impact-on-gdb) 

#### Deleting a related table from geodatabase

1. Stop all feature services using the impacted geodatabase table. In doubt, stop the ArcGIS Server service.

2. Open ArcGIS Pro and connect to the geodatabase (the easiest is to open the project that contains the map used to create the feature service)

3. Remove feature class from map

4. (Optional) Delete feature class from geodatabase (Right click, Delete from Database Connection). Another option is to rename the feature class and delete the relationship which retains the data in case there are any issues.

5. Restart feature service(s) or the ArcGIS Server service (need to be done before overwriting the service definition)

6. Change feature service definition by going to Share, Web Layer, Overwrite Web Layer


[top](#impact-on-gdb) 

## Data Type Conversion Table

| Survey123          | ArcGIS Pro |
| ------------------- | ---------- | 
| text                | Text       | 
| integer             | Long       |
| decimal             | Double     |
| date                | Date       |
| time                | Date       |
| dateTime            | Date       |
| select_one          | Text       |
| select_one_external | Text       |
| select_multiple     | Text       |
| esriFieldTypeDate | Date |
| esriFieldTypeSingle | Float |
| esriFIeldTypeDouble | Double |
| esriFieldTypeInteger | Long |
| esriFieldTypeSmallInteger | Short |
| esriFIeldTypeString | Text |


[top](#impact-on-gdb) 


