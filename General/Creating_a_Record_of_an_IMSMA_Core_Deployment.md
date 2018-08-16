[Back to main menu](../index.md)  

Creating IMSMA Core Deployment Records
--------------------------------------

#### Purpose

During and following an IMSMA Core deployment, the IMSMA Advisor will
need to document a variety of configurations related to the Solution.
This will assist GICHD with supporting the country or operator and will
also provide reference documentation for the country or operator to
refer to. A Deployment Record also assists with upgrading the IMSMA Core
deployment and troubleshooting issues reported by the Operator or
Organization.

An IMSMA Core deployment involves configuration of ArcGIS Enterprise,
PostgreSQL, Survey123, ArcGIS Pro and other software components. The
intent of this document is to lay out what configurations should be
recorded for each program, and provide sample documents to begin filling
in this information.

### Storage of IMSMA Core Deployment Records

Deployment records are stored using a combination of GitHub and Box.com,
depending on the preference of the IMSMA Advisor, the complexity of the
data and the wishes of the Mine Action Programme. GitHub is well-suited
to storage of code, scripts or files where a record of changes is
beneficial. Box is suited to storage of larger files, folder structures
and simpler file-system access using Box Sync.

### ArcGIS Enterprise Configuration 

#### Portal for ArcGIS

The Portal's configuration can be easily changed by administrators or
publishers, to include the creation of new apps and web maps or changes
to existing settings. This means that the exact state of a Portal is
likely to change frequently over the life of an IMSMA Core deployment,
so not all details are required for a deployment record. The relevant
details to record about an IMSMA Core deployment from the Portal
perspective include:

-   Portal external URL: such as <https://drc.imsma-core.org/portal>

-   Federated Server External URLs, ex.
    <https://drc.imsma-core.org/server>

-   Hosting environment, local and external IP addresses

    -   Ex: AWS VPC instance, local IP 172.16.31.226, external IP
        55.23.44.61

-   Full User List -- identify the users of the Portal, their
    affiliation, role and contact information.

-   Full Groups Listing -- identify the Groups that have been created to
    support the IMSMA Core deployment, which are often used to
    specifically assign access to certain users for certain content

-   List of Key Services -- ItemIDs for key map and feature services
    that are used by the system, these URLs will be helpful when
    configuring or resetting Survey123 logic.

#### ArcGIS Server Services

The best method for recording the map and feature services used in an
IMSMA Core deployment is to keep a copy of the Map documents (.mxds) or
ArcGIS Pro Project(s) (.aprx) used to publish these services. These
files can record symbology, filters or definition queries, and other
settings that will help in the re-creation of these services or may be
usable by future deployments.

### Survey123 Forms

Survey123 Forms are best recorded as a .xlsx file that contains the
Survey123 XLSform and configurations. This file may be accompanied by a
readme.txt or similar file that describes the use of the form,
considerations for publishing, the overall data structure and
information about the source of certain information like community
locations, pcodes, administrative boundaries and other data included in
the choice lists.

In this format, new Survey123 forms can easily be created from the
template and then adjusted to fit a program's needs.

### Data Structure for Survey Forms

Ideally, the Deployment Record should include a zipped file geodatabase
representation of the data schema used by the Survey123 forms. This
provides an easy way to republish the survey data to an enterprise
geodatabase and review the structure of the data. This file geodatabase
can be created by copying feature classes from the PostgreSQL IMSMA Core
database to a file geodatabase using the copy and paste commands in
ArcCatalog or ArcGIS Pro. This data can then be cleaned using the
Truncate Table geoprocessing tool, if desired, to provide a blank
"template" database for a deployment.

### Documentation

Information Management Processes and Standards should be kept in the
Deployment Record as well. These documents are often created by IM staff
during the IMSMA Core development process and are excellent records of
the workflows, data sharing and background on the program's
requirements.

HI-Syria Example
----------------

-   Survey123

    -   XLSforms

    -   Single External Choices list

    -   Maybe some doc about the naming convention and other settings
        that were set in Connect

-   Pro

    -   One "final" project -- fully configured

    -   Export the tasks as .esriTask files

-   Tools

    -   Folder of project-specific Python (if necessary)

-   Data

    -   Copy of the blank data structure (Survey123 schema without any
        rows)

    -   (if possible) include example records for each data type

-   Documentation

    -   High Level IM Process/SOP Description (from Mission)

    -   IM Process from the IMSMA Expert Perspective

    -   Portal Configuration

        -   Users

            -   How were users created, how were roles defined, and how
                were logins provided to users, naming conventions?

        -   Groups

            -   Group structure and/or hierarchy

            -   Group membership

        -   Information Products

            -   WAB app \#1

        -   Apps and Web Maps

            -   "Schematic" documentation of the web maps and apps

                -   RA Tasking Map 1

                    -   Includes RA layer, symbolized by X, filtered by
                        Y

                -   Collector Map for RA Activities 1

                    -   Includes RA Layer, symbology X

                -   Survey123 Form on Device 1
