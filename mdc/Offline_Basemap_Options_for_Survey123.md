Creating offline Tile Packages for Survey123
============================================

Defining Offline Data and Tiles
-------------------------------

Survey123 and other Esri applications generally handle the term
"offline" in the same way. Offline access means that data is available
when a device does not have internet access via WiFi or Cellular Data
Network (3G, 4G, LTE etc.) Esri Mobile apps support various levels of
offline data access, but generally datasets are split into **offline
vector or attribute** data and offline **basemap or tiled** data. On top
of this, some applications support different levels of editing of the
vector or attribute data with differente permissions defining what
layers and features can be edited, added, deleted or modified. Offline
support is therefore a combination of **data,** **tiles** and
**permissions**.

Offline Data
------------

Esri provides access to offline vector data and attributes primarily
through the concept of feature services. Feature services are web
services published to ArcGIS Server or through ArcGIS Online, which
allow an authenticated client (a user that has logged in) to request a
set of features from a service for a specific area. This is the classic
"Collector" workflow, where a user pre-defines their area of interest,
and the app downloads all of the vector features for that area so they
can be viewed and (if appropriate) edited.

Survey123 supports offline data through the Inbox, a simpler method of
taking data offline which allows a user to review existing records and
make edits to them.

Offline Tiles
-------------

Esri supports offline basemaps using the Tile Package data item. Tile
Packages are .tpk files, which are zipfiles that contain a director of
basemap tiles and a few files that provide relevant metadata about the
area of coverage, layers, and other items. A tile package can only
contain one set of basemap tiles. Tile packages are created through
several different processes to be discussed in the next sections.

The ingredients for a tile package are:

1.  Either

    a.  The service URL of the map service with Tile Export Enabled --
        this specifies which service + tiles to request

    or

    b.  The map in ArcMap or Pro to export a TPK from

<!-- -->

2.  An Extent to request (the geographic area to request tiles for) --
    this controls the area of interest

3.  The Levels (zoom scales) to request tiles for (0-20 generally) --
    this controls the level of detail of the tiles

Together, these three parameters define the tile package, which can
range from a few Mb to Gb in size.

Offline Permissions
-------------------

Access to edit and add to datasets is generally controlled at the
feature service permission level. A certain dataset may allow users to
create new features only, or might allow them to edit existing features
but not create or delete, for example. These permissions are inherited
in the offline data, which the app uses to control what a user can and
cannot do with their data once it is available offline.

Creating Tile Packages for Survey123
------------------------------------

Survey123 supports offline basemaps through tile packages. There are
several ways to create a tile package, the best of which is **Tile
Package Kreator**, a desktop stand-alone application which allows a user
to identify a service from their ArcGIS Enterprise or ArcGIS Online
organization, choose an extent and which scale levels to export, and
generate the exported package, which is then downloaded to their
computer.

Help for the Tile Package Kreator is available here:
[https://esri.app.box.com/s/d6xaclvrdu14pqk6t95arxu02zz2mtin](https://esri.app.box.com/s/d6xaclvrdu14pqk6t95arxu02zz2mtin)

Users can also create Tile Packages with ArcMap and ArcGIS Pro. These
tools are helpful for when a user wants to include other layers in their
tile package, or use custom imagery files or other data. Note that when
other layers are included in a tile package they are "flattened" to the
raster format of the TPK, so no attributes can be extracted and
symbology cannot be changed.

ArcMap documentation: [How to create a tile
package](http://desktop.arcgis.com/en/arcmap/latest/map/working-with-arcmap/how-to-create-a-tile-package.htm)

ArcGIS Pro documentation: [Tile Package
Overview](http://pro.arcgis.com/en/pro-app/help/sharing/overview/tile-package.htm)

Tile packages can also be created directly from the ArcGIS REST API by a
developer using the Export Tiles function (when enabled): [Export Tiles
Documentation](http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Export_Tiles/02r30000025t000000/)

Another web-based tool for creating tile packages is available here:
[http://nixta.github.io/tpk-creator/\#](http://nixta.github.io/tpk-creator/)

Methods for making Tile Packages available to users in Survey123
----------------------------------------------------------------

There are four main methods for getting a tile package available to
Survey123 field users:

1.  Load to an SD Card -
    [Documentation](http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm#ESRI_SECTION1_7D8E3F7EB17A457088A9368CB065465B)

2.  Copy your Tile Package Directly to the Device -
    [Documentation](http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm#ESRI_SECTION1_2AE91E3EDB004B61905B1B7E7D0A6431)

3.  Package TPKs in the media folder during Survey publishing -
    [Documentation](http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm#ESRI_SECTION1_7C1C32D5FB2C401DA4F1A547A93891C9)

4.  Upload TPKs to Portal and reference them in the Survey -
    [Documentation](http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm#ESRI_SECTION1_81F988166E0D4CB4BD6823C84AE3186C)

These methods are all covered in detail in the following documentation
from the Survey123 website:
[http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm](http://doc.arcgis.com/en/survey123/desktop/create-surveys/preparebasemaps.htm)

Included below is a brief Pro/Con listing of the options to help decide
which is best for a specific scenario:

[]{#_gjdgxs .anchor}

| **Method**      | **Pros**        | **Cons**        | **Recommended Use Case**      |
| --- | --- | --- | --- |
| Load tile       | -   Easy to     | -   Not         | Areas with very |
| packages to SD  |     share cards |     supported   | limited network |
| Cards           |                 |     on iOS      | connectivity +  |
|                 | -   Quick to    |                 | Android devices |
|                 |     copy and    | -   Only update |                 |
|                 |     load        |     by          |                 |
|                 |                 |     connecting  |                 |
|                 | -   Large TPKs  |     to a        |                 |
|                 |     are         |     computer    |                 |
|                 |     supported   |                 |                 |
|                 |                 |                 |                 |
|                 | -   No Network  |                 |                 |
|                 |     Bandwidth   |                 |                 |
|                 |     Required    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Load to device  | -   Direct load | -   No updates  | Small survey    |
| from            |     via USB     |     over the    | teams           |
| Windows/Mac OS  |                 |     air         |                 |
| using USB       | -   Fast to     |                 | One-off field   |
|                 |     copy        | -   Requires    | exercises       |
|                 |                 |     users to be |                 |
|                 |                 |     at the same |                 |
|                 |                 |     place to    |                 |
|                 |                 |     access data |                 |
|                 |                 |                 |                 |
|                 |                 | -   Difficult   |                 |
|                 |                 |     to send     |                 |
|                 |                 |     updates     |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add to Survey   | -   All in one  | -   Large       | Small Tile      |
| During          |     package     |     download    | Packages or     |
| Publishing      |                 |     size for    | frequently-upda |
|                 | -   Publisher   |     survey      | ted             |
|                 |     can update  |                 | packages,       |
|                 |     survey +    | -   Downloads   | working in      |
|                 |     tile        |     on every    | areas with good |
|                 |     package     |     refresh     | data coverage   |
|                 |     remotely    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add the TPK     | -   Create tile | -   Requires    | Best option     |
| link to the     |     package     |     bandwidth   | across the      |
| MySurvey.info   |     once and    |     for users   | various use     |
| file after      |     host it -\    |     to download | cases           |
| publishing      |     everyone    |                 |                 |
|                 |     can use     | -   Manual      |                 |
|                 |                 |     process to  |                 |
|                 |                 |     add it to   |                 |
|                 |                 |     the file as |                 |
|                 |                 |     a publisher |                 |
|                 |                 |                 |                 |
|                 |                 | -   No method   |                 |
|                 |                 |     for         |                 |
|                 |                 |     updating    |                 |
|                 |                 |     automatical |                 |
|                 |                 | ly              |                 |
+-----------------+-----------------+-----------------+-----------------+

Outstanding TPK topics
----------------------

1.  How to update a TPK that has been published to Portal and have users
    re-download the file?

2.  How to pre-generate TPKs across an area for use in mobile devices,
    so they can be pre-loaded or available for pre-loading as necessary

3.  Generation of a country-scale TPK down to L12 or so which can be
    used for all offline scenarios
