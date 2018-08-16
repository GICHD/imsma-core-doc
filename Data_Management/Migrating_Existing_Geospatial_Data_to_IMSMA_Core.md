[Back to main menu](../index.md)  

Migrating Existing Geospatial Data to IMSMA Core
================================================

Migrating Geospatial data to IMSMA Core
---------------------------------------

When migrating from an earlier version of IMSMA to IMSMA Core, there are
several considerations in relation to the geospatial coordinate storage
for point, line and polygon data.

IMSMAng currently supports data entry in any Datum, with coordinates
stored in the database as WGS1984 from a pure geometry perspective. This
process of supporting data entry using other coordinate systems is still
important, and IMSMA Core will attempt to follow the same patterns.

The GICHD recommends *projecting* all existing geospatial data from
projected coordinate systems into WGS 1984 coordinates to provide
central storage and a single geospatial coordinate format for all data.
This one-time process is described in this document.

GICHD is aware of the long history and reasoning behind the use of local
projections for data in IMSMA Core, but the following statement
represents the decision to focus on WGS1984:

*While there are important and historic reasons for using local datums,
local projections or other reference systems, WGS 1984 provides a
precise and functionally-equivalent representation of these features for
the purposes of Mine Action.*

For example -- a difference in datum may lead to a coordinate being
shown a few meters distant from another coordinate when establishing the
boundary of an SHA. In reality, the boundary of the SHA should be marked
on the ground and any technical survey team will likely cover the entire
area, including the discrepancy in boundary. In this case is important
to capture the relatively-precise size and location of the SHA, not
capture SHA boundaries using DGPS which will then become irrelevant
during the Technical Survey process.

Projecting Existing Geospatial Data
-----------------------------------

Any existing shapefiles, feature classes or other geospatial layers that
are used in IMSMAng or are used by the Information Management team for
other purposes should be consolidated as part of IMSMA Core development.
WGS 1984 coordinate storage provides a precise and usable format for
coordinates while ensuring that coordinate conversion, interoperability
between applications and submission of data from the field are all kept
in sync.

When projecting existing geospatial data, use the **Project** tool in
ArcGIS Pro, and be sure to specify an appropriate translation for your
data. For more guidance on selecting a translation for projecting data,
see this page:
<https://blogs.esri.com/esri/arcgis/2009/05/06/about-geographic-transformations-and-how-to-choose-the-right-one/>

It is recommended to project all data sources into a file geodatabase
initially, and re-add the data to the map to ensure that boundaries line
up and are equivalent to the pre-projection data. This review process
will help to build confidence with the GIS and IM teams before loading
the data to IMSMA Core's PostgreSQL database.

Changing GPS Data Collection Procedures
---------------------------------------

The majority of Mine Action programs use advanced GPS data collection
methods in the field to establish geospatial locations for devices,
boundaries of hazardous areas, or EOD spot tasks. In many programs,
these DGPS devices are set to record coordinates using a local datum and
local projection. GICHD recommends that programs moving to IMSMA Core
consider changing this data collection to use a pure WGS1984-based datum
and decimal Latitude/Longitude coordinates. Digital storage systems for
geospatial data already use decimal degrees WGS 1984, and setting field
devices to use this datum will result in clean data collection and data
storage workflows, while still retaining the necessary and useful level
of precision that a Mine Action program may need.
