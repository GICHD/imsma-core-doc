[Back to main menu](../index.md)  

IMSMA Core Solution Components 
====================

This document lays out the software components and installations that
are part of the IMSMA Core System, whether required or optional. This is
intended to clearly list the different installed software components and
their purpose, as well as other core components like geodatabase
schemas, deployment tools and automation scripts that may be used at
certain NMACs or Operator locations. The goal is to answer the question
of "what do you get" with IMSMA Core, and use this layout as a guideline
for completion.

IMSMA Core is an information management system for mine action,
consisting

-   Several pieces of software, some provided by Esri and other based on
    open-source technology

-   A collection of building blocks to provide functionality to support
    known mine action workflows

    -   Inspiration data collection forms and already-built mobile
        applications

    -   Workflow management tasks and data editing tools and guidelines

    -   Map documents, web mapping applications and information products
        providing a detailed view of mine action data along with summary
        information

-   A full suite of documentation that will allow programs, operators or
    other involved parties to make use of IMSMA Core components in
    configurations that fit their organizational needs

At the center of IMSMA Core is ArcGIS Enterprise -- Esri's on-premises
GIS Platform. This suite of installed software components supports
dynamic web-based mapping, desktop data management, GIS analysis, mobile
apps for viewing and data collection, and reporting and visualization of
Mine Action information. This functionality is provided through the
installation and configuration of several Esri Commercial Off-The-Shelf
(COTS) components, described in detail in the *Esri Software* section of
this document.

Along with the installation of these components, IMSMA Core includes
configurations of data schemas, web maps, applications and
visualizations based on the requirements identified by GICHD and the
current IMSMAng usage across National Mine Action Centers (NMACs) and
Mine Action Operators.

Deployment Options
==================

IMSMA Core can be deployed to support National Mine Action Programs,
operating partners, INGOs or local NGOs working in countries, or any
other group supporting Mine Action. There is no one-size-fits-all
deployment of IMSMA Core, and the components can be installed on a
variety of different hardware options. There are three general
deployment patterns that the GICHD and Esri have prepared and recommend
for most situations.

Cloud-Hosted IMSMA Core
-----------------------

IMSMA Core can be installed on a cloud-hosted virtual server, such as an
Amazon EC2 instance, which will contain all the relevant ArcGIS Software
and configurations required for a country or a program's deployment of
IMSMA Core. This approach can provide multiple benefits:

-   GICHD staff will be able to access the server to perform upgrades,
    change database configurations, and deploy new tools

-   Automated backups of the server can be taken with Amazon's cloud
    tools and functionality

-   Hosting stability is maintained by Amazon (security, data center
    access, etc.)

-   Speed of access is maintained by Amazon's substantial internet
    access speeds

-   Multiple operators in a country or region can contribute to a single
    shared database on this shared server

-   Mobile users can access data and information from IMSMA Core from
    any location with cellular data service or Wi-Fi connectivity

Locally-Hosted IMSMA Core
-------------------------

IMSMA Core may also be deployed on a local server, running in a small
data center configuration at a National Mine Action Center, as part of a
national agency, or in the offices of an operator or other involved
party. This option allows all mine action data to be stored locally to
the organization hosting the deployment, and supports countries with
better in-country network connectivity than internet connectivity. Local
servers do not have a simple backup strategy, require system
admininstrator resources to manage local network connectivity, and
require users to be on the local network to synchronize mobile devices,
submit data, etc. if the server is not exposed to the Internet. This
option would also require increased GICHD involvement for software
deployment, troubleshooting and potential upgrades.

Local Deployment with ArcGIS Online
-----------------------------------

IMSMA Core, or a subset of functionality requested by a program or
operator, may be installed on a single local desktop or laptop machine,
for small programs, field deployments or low-bandwidth environments.
Installing the full stack of IMSMA Core platform components on a single
consumer-grade machine is possible but not recommended. In this
deployment configuration, mobile users and a data manager with a desktop
interface can still follow IMSMA Core workflows and use associated
tools, with data submitted to web services hosted by the GICHD in ArcGIS
Online or through an ArcGIS Online organization provided to the country
program through GICHD's negotiated ArcGIS Licensing. This provides a
country with the benefits of cloud data storage but does not require
investment in a server or local hardware. This configuration is best
suited for a Mine Action Programme that is involved in limited
activities within the Mine Action or focused on a few specific
activities.

Examples of IMSMA Core Deployments
----------------------------------

### Handicap International -- Jordan Program

The HI Jordan deployment of IMSMA Core follows a **Cloud-hosted IMSMA
Core** model. A single ArcGIS Enterprise deployment is hosted in Amazon
Web Services by Esri Managed Cloud Services, which provides the ArcGIS
tools and a dedicated URL for all HI Jordan users. HI was not previously
an IMSMAng user, and migrated their data collection methods from paper
forms to digital forms using Survey123. HI is currently operating in
Jordan and collecting the following 5 types of surveys:

-   RE -- Risk Education

-   AC-VA -- Accidents & Victims

-   HA -- Hazardous Areas

-   CS -- Community Survey

-   EO -- EO Spot Tasks

HI's work is split into 4 primary Hubs -- roughly geographic areas of
interest within their working area. These hubs are restricted from
viewing data from other Hubs, so the security model allows for four
different levels of access:

1.  Collectors -- Partner-employed in the field that submit records for
    a specific activity type for a specific Hub

2.  National Partner PMs -- overseeing project managers or team leads
    who review data submitted by their teams

3.  Hub DBM/PM -- International staff or HI staff that review all data
    submitted within a specific hub for accuracy and completion. Also
    responsible for Donor allocation

4.  Coordination -- HI Main Jordan office and International Staff, who
    create reports, organize resources and plan strategy across the
    hubs.

The data collection pattern in HI follows these rough steps:

1.  Users submit forms (of any of the 5 types) from the field using
    personal Android devices. Forms are automatically marked for certain
    "QA notes" that should be reviewed by a higher-level staffperson.
    The forms themselves are set up so that most data quality issues are
    addressed through verification

2.  Partner PMs or Hub DBMs have access to the submitted forms, review
    them for consistency and make any necessary edits, then mark the
    forms as reviewed

3.  Hub PMs or Coordination PMs review completed data at the end of the
    month and assign Donors to each record based on existing donor
    relationships. This completes the data submission, review and
    verification process. Records are visible in various web application
    dashboards for review.

### UNMAS -- Gaza Risk Assessment Deployment

UNMAS Gaza requested GICHD assistance with executing Risk Assessment
tasks in urban areas of Gaza, a process which was previously handled
with spreadsheets and paper forms. GICHD developed an IMSMA Core "light"
version that takes advantage of the IMSMA Core patterns and allows the
UNMAS team to effectively complete their operations with the benefits of
mobile data submission and smart form logic.

1.  UNMAS receives phone-in requests for Risk Assessments to a central
    office location, and records the details of these requests using a
    Windows-based Survey123 form.

2.  These requests are then assigned using a Web AppBuilder app, to
    provide a responsible user and show only those locations needing
    assignment

3.  Users in the field can open Collector (when connected to WiFi or
    Cellular Network) and review their assignments, take the map
    offline, etc.

    a.  From the Collector map of assignments, the users can launch a
        Survey123 form for the actual Risk Assessment and collect
        evidence/attributes that remain related to the assignment point

4.  After the RA activities are submitted, staff can view results from a
    dashboard built with Web AppBuilder

This system is deployed entirely within the GICHD ArcGIS Online
environment -- with a selected set of users from UNMAS. This pattern
will be used for a trial of similar functionality for UNMAS in Iraq in
November 2017.

### MAG -- Global IM deployment

To be described

Operating System Components
===========================

Windows Operating System
------------------------

The main ArcGIS software components of IMSMA Core is supported on
Windows-based operating environments only. System Requirements for IMSMA
Core are not yet defined but are expected to be Windows 7+, Windows 8+,
Windows 10+ or Windows Server 2012+. The majority of the Operating
System requirements will be defined by the ArcGIS System Requirements
provided by Esri, the most current version of which is available here:
[http://server.arcgis.com/en/server/latest/install/windows/arcgis-for-server-system-requirements.htm](http://server.arcgis.com/en/server/latest/install/windows/arcgis-for-server-system-requirements.htm)

For some component applications, especially mobile applications, support
for Mac OS X operating systems and Android or iOS operating systems is
available.

Internet Information Services (IIS) Web Server
----------------------------------------------

IMSMA Core is a web-based solution, with many user workflows occurring
through a web browser and web services along with traditional desktop
application workflows. This requires the IMSMA Core system to include a
dedicated web server, in this case the Internet Information Services
(IIS) web server that is available with each supported version of
Microsoft Windows. IIS is used to host the ArcGIS Web Adaptor, and more
detailed system requirements are available here:
[http://server.arcgis.com/en/web-adaptor/latest/install/iis/arcgis-web-adaptor-system-requirements.htm](http://server.arcgis.com/en/web-adaptor/latest/install/iis/arcgis-web-adaptor-system-requirements.htm)

Mobile Devices
--------------

Data collection with mobile devices (smartphones or tablets) is a key
workflow for IMSMA Core, building on the increased availability of these
devices and the existing apps that Esri provides for working with data
offline using a mobile device. In general, IMSMA Core has the following
mobile device system requirements:

1.  Android version 4.1 or later

2.  iOS version 9 or later

3.  Cellular data connectivity (3G or better) or Wi-Fi connectivity for
    syncing data and submitting surveys (not required while collecting
    data).

Additional Software Components
------------------------------

### PostgreSQL

PostgreSQL is an enterprise-class open source and freely available
relational database system. PostgreSQL has many different functions,
tools and features that can support mine action information management,
but in the context of IMSMA Core it serves the following purposes:

-   Storing geodatabase tables that contain IMSMA Core Data -- both
    geospatial and tabular features

-   Storing the "sde" schema which contains the enterprise geodatabase
    system table, geospatial functions and stored procedures

-   Storing archival versions of relevant IMSMA Core features (IMSMA
    Core's version of the 'infoversions' in IMSMAng)

-   Storing additional tables created by NMACs or identified as
    ancillary to IMSMA Core

-   Setting privileges and controlling user access to data and editing
    privileges

-   Providing import/export functionality to back up the database,
    provide it as a data export, or importing features from another
    database

Versions of PostgreSQL are also embedded within the ArcGIS Data Store
and Portal for ArcGIS installations. These embedded versions are not
accessible to users and do not conflict with the primary PostgreSQL
installation used for the enterprise geodatabase and IMSMA Core
features. IMSMA Core supports using an existing PostgreSQL installation
or deploying a new PostgreSQL system using the most recent versions of
major releases 9.4, 6.5 or 9.6.

Esri Software
=============

Below is a list of the Esri software components used in IMSMA Core along
with a description of their use as part of IMSMA Core

ArcGIS Server
-------------

ArcGIS Server is Esri's mapping web server, which provides access to
geospatial data through open web services that allow for cartographic
rendering, query and filtering of geospatial data, geocoding, accessing
imagery and raster data, and many other workflows. ArcGIS Server is a
mature product from Esri, used in thousands of organizations to expose
geospatial data to users in desktop, mobile and web-based applications.
The ArcGIS REST API is an
[openly-documented](http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#/Overview/02r3000001zz000000/)
API that supports interactions with ArcGIS Server from each of these
types of application.

In IMSMA Core, ArcGIS Server exposes geospatial and tabular data and
objects from within a PostgreSQL database to users via web services.
ArcGIS Server can also show data from local filesystems or from
satellite imagery and elevation products or data gathered from drones.
The most common type of web service published to ArcGIS Server is a map
service, which supports rendering an image of geospatial data for a
user, or returning a JSON collection of features and attributes.

ArcGIS Data Store
-----------------

The ArcGIS Data Store is an installable configuration of the PostgreSQL
relational database software, designed to work closely with Portal for
ArcGIS and ArcGIS for Server to allow Portal users to publish data from
their own machines or data stores into the Web GIS architecture. As an
example use case, a Portal user could take a zipped shapefile provided
by a partner, open it in ArcGIS Pro and publish it as a feature layer in
their Portal. Behind the scenes, the data is loaded into the ArcGIS Data
Store as a PostgreSQL table with spatial geometry, where it is then
exposed by ArcGIS Server as a feature service and registered in Portal
as an item that can be searched for and found by Portal users. A user
could also upload the same zipped shapefile directly to Portal to create
services and web maps.

The Data Store is configured to support publishing and consuming
hundreds of these ad-hoc feature services by hundreds of users, without
data being created or extracted into the organization's official system
of record database. While this may create confusion in some cases for
database administrators, the functionality to allow for ad-hoc service
creation is a worthwhile reason to install the Data Store.

ArcGIS Enterprise Geodatabase
-----------------------------

The ArcGIS Enterprise Database is a set of tables, procedures and schema
elements that supports the storage and manipulation of geodata inside of
a traditional relational database. Esri supports "creating" an
enterprise geodatabase inside of several different RDBMS platforms, most
commonly Oracle, SQL Server and PostgreSQL. For IMSMA Core, PostgreSQL
is the defined RDBMS of choice. The Enterprise Geodatabase schema is
described in more detail at the following link:
[http://desktop.arcgis.com/en/arcmap/latest/manage-data/using-sql-with-gdbs/overview-geodatabase-system-tables.htm](http://desktop.arcgis.com/en/arcmap/latest/manage-data/using-sql-with-gdbs/overview-geodatabase-system-tables.htm)

The Enterprise Geodatabase tables are created during the initial setup
of IMSMA in a database called *imsma\_core*, but it is also important to
note that additional enterprise geodatabases can easily be created on
the same PostgreSQL host as the IMSMA Core geodatabase and used for
other purposes. Additional non-geospatial PostgreSQL databases can also
be created or maintained on the same database instance and viewed
through ArcGIS. The Create Enterprise Geodatabase tool requires an
ArcGIS for Server license file to run, which will be provided as part of
IMSMA Core and deployed as part of the IMSMA Core setup process.

ArcGIS Web Adaptor
------------------

The ArcGIS Web Adaptor is an installable .NET web application provided
by Esri which serves two main purposes:

-   Reverse-proxy traffic from web browsers and other client apps from
    ports 80 and 443 (HTTP + HTTPS) to the back-end applications for
    ArcGIS for Server and Portal (over ports 6080/6443 and 7080/7443
    respectively). This allows the system to use a single hostname, SSL
    certificate and port to provide access to both Portal and ArcGIS
    Server.

-   Support authentication patterns leveraging web server-based
    authentication such as Integrated Windows authentication. This
    configuration is not used in the IMSMA Core project and is not
    relevant at this time.

The ArcGIS Web Adaptor is installed into an existing IIS installation,
and will install missing IIS components if required. It appears as a
dedicated .NET app inside of the Default Web Site of the IIS server.

Portal for ArcGIS
-----------------

Portal for ArcGIS is web-based application that allows users to organize
and share geospatial information and maps throughout their organization
with those who need access or are interested. It provides a framework to
easily manage and secure geographic assets within the organization,
enabling better decision making through maps, dashboards, data
collection, reporting and other tools while controlling access to
approved groups and responsible parties. In IMSMA Core, the Portal is
the primary interface for data consumers, for visualization and for
management or leadership. Portal includes a variety of map-centric
applications that can be used to view the geodata and tabular content
contained in the IMSMA Core system in different ways.

ArcGIS Pro and ArcGIS Desktop
-----------------------------

ArcGIS Pro is Esri's professional-grade desktop Geographic Information
System interface. Pro is an installable Windows application for
managing, viewing, analyzing and interacting with geospatial and tabular
data from filesystems, databases and web services. ArcGIS Pro allows
users of IMSMA Core to author new data, update existing data and delete
records as necessary. The Pro interface is configurable to reduce
complexity and include tasking and workflow management tools to guide
users through specific editing or data management projects.

ArcGIS Pro has been selected as the primary desktop GIS interface to the
IMSMA Core system as it represents Esri's latest developments and future
direction in Desktop GIS terms. ArcGIS Pro also provides a more modern
and less GIS-focused interface, with work and data access based on
project collections rather than requiring a deep understanding from the
user. ArcGIS Pro has support for 3D data visualization and editing,
advanced geoprocessing analysis and model building, tasking and workflow
management and many other functions that make it the best choice for
IMSMA Core.

Along with ArcGIS Pro, users will also be able to interact with the data
and services contained in IMSMA Core through Esri's ArcGIS for Desktop
suite of ArcMap, ArcCatalog and other apps. These applications are
supported and continue to be maintained by Esri, but are not intended to
be the primary data access, editing or management interface for IMSMA
Core. Experienced GIS teams, Information Management Officers or outer
staff with experience using ArcGIS for Desktop can make use of these
tools to access IMSMA Core.

ArcGIS Mobile Applications
--------------------------

**Survey123** is a form-centric data collection app that Esri created to
meet the needs of enumerators, data collectors and inspectors. Survey123
is built on the XLSForm standard, and includes three main components.
The **Field App** is used for data collection, consuming Survey123 Forms
and allowing for structured data entry, input validation, skip logic and
many other common survey tools. The Field App is supported on Android
and iOS devices along with Windows and Macintosh desktop operating
systems.

**Survey123 Connect** is a desktop app for Windows, Macintosh and Linux
desktop operating systems that is used to create the forms used by the
Field App. Survey123 Connect allows users to author forms using an Excel
spreadsheet (largely following the XLSform standard and specification)
and preview those forms before publishing the form as a new hosted
feature service to ArcGIS Enterprise or pointing to an existing editable
dataset on an ArcGIS Server host.

The **Survey123 Web Site** provides a straightforward data viewing and
basic analysis experience for Survey123 Forms, allowing the form author
and any other user with access to the data to access summary counts,
timelines of data and frequency statistics for question responses. This
webpage is available hosted by Esri or as a deployable part of the IMSMA
Core system

[Back to main menu](../index.md)  
