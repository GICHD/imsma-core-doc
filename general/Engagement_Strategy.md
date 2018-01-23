Engagement Strategy
===================

This document serves to lay out a rough engagement strategy for an IMSMA
Core Deployment with either a Mine Action Organization ("Operator"), a
National Mine Action Centre ("NMAC") or a National Mine Action Authority
("NMAA"). This strategy will differ substantially between Programs or
Organizations that already use IMSMAng and those that use other systems
or other information collection methods which they aim to augment or
replace with IMSMA Core. For this reason these two different cases are
separated in the document. This document is intended to provide a
moderate level of detail which will be extended through available IMSMA
Core documentation, tutorials and examples, as well as through the
skills and background of GICHD IMSMA Advisors.

Engaging with Existing IMSMAng Programs
=======================================

Many NMAC/NMAAs are already using IMSMAng, the latest version of IMSMA
released prior to IMSMA Core. This system generally contains a large
amount of data that must be migrated into IMSMA Core, and also a series
of business processes that have been created through the use of forms
and custom-defined fields in IMSMAng.

Gathering Existing Information about the Program
------------------------------------------------

Once a program has been identified as a potential pilot user or as a
party interested in migrating from IMSMAng to IMSMA Core, the following
information should be gathered from the Program to help the GICHD IMSMA
Advisor assess the level of effort involved in migrating the Program as
well as which existing IMSMA Core workflows might provide good options
for the Program:

-   Full IMSMAng Database Export (backup)

-   IMSMAng Staging Area Database Export (if available)

-   Existing Information Management SOPs/Guidelines (if available)

-   Existing GIS Data availability (types of features, use and sources)

-   Overview of Program structure -- IM staff, GIS capabilities HQ and
    field offices, relationship with other primary
    operators/NMAC/government organizations as appropriate

    -   This data may be collected through a GICHD IM Assessment or
        other formal engagement, or may be available by request from the
        NMAC or Operator

-   Existing IT resources, mobile devices, network configuration and
    level of internet access for their primary users

    -   [[https://cloudharmony.com/speedtest-for-aws]{.underline}](https://cloudharmony.com/speedtest-for-aws)
        provides an excellent network speed test, which takes about 30
        minutes to run but provides guidance on which AWS regions
        provide the best access and Internet speeds from a user's
        location.

-   Overview of ongoing Mine Action activities: is the organization
    engaged in land release, MRE, Victim Assistance, EOD Spot Tasks,
    etc.?

Running IMSMAng database statistics
-----------------------------------

The GICHD IM team has created a series of PostgreSQL scripts that can be
run against the IMSMAng database to provide a summary of various
characteristics of the IMSMAng database such as:

-   Use of custom-defined fields (\# of fields and \# of fields used in
    system)

-   counts of features and rows in each data table in IMSMAng

-   frequency of use of existing ISMSMAng attributes or columns

-   types and counts of geographic features across object types

This script and report can be used to identify which types of features
are widely in use across the organization, and which activity types
might be piloted first during the Engagement process. The script also
will be used for the design of the program's Survey123 Forms, to
identify which CDFs are actively used so that some may be proposed for
deletion.

Identifying level of IMSMAng Customisation
------------------------------------------

The IMSMAng Database Statistics file will indicate the number of
custom-defined fields that were created in IMSMAng, as well as the level
of data completion for these fields (i.e. are the fields used and worth
retaining). This information will have a significant impact on how much
the IMSMA Core schema should deviate from the default structure during
configuration. When reviewing heavily-used custom-defined fields, it is
important to assess whether these values need to be added to the IMSMA
Core Schema or whether the recorded data could be inserted into a
different column in the default IMSMA Core schema. This case may be
useful for countries which created CDFs to store data which otherwise
could have been stored in the IMSMAng schema.

Obtaining copies of existing IMSMAng Forms
------------------------------------------

Existing IMSMA programs are likely using a series of well-reviewed and
approved Forms for entering Field Reports into the various record types
in IMSMAng. These forms can be saved as .ffml (Form Markup Files) and
should be requested from the program along with screenshots of the Form
interfaces so that the IMSMA Advisor can review existing data input
methods. IMSMA Core includes a processing tool that can be used in
conjunction with the country's IMSMA database to convert the FFML forms
to rough XLSForm representations that can be used as the starting point
for Survey123.

The IMSMAng Database Statistics file also provides a summary of Field
Reports and how they are actively used within a program for data entry
and updates -- this may help identify which FFML files should be
translated.

Identifying a project schedule and plan of action
-------------------------------------------------

IMSMA Core is a system of different tools, apps and components, deployed
in a base configuration but configured for each program's technical and
business requirements, while maintaining a core Esri software component.
Identifying the breadth of data collection activities undertaken by a
program will allow the IMSMA Advisor to tailor IMSMA Core to the
program's needs, omitting modules that are not used or not relevant and
focusing automation and customization efforts on the most relevant
modules.

The IMSMA advisor should identify a proposed schedule for IMSMA Core
trial, phased rollout and ongoing maintenance that can be presented to
and eventually agreed to by the NMAC or Operator. The default length of
schedule and content is still to be determined, but an example schedule
could follow this structure:

1.  Months 1-2

    -   Initial IMSMA Core scoping meeting (on-site with program) and
        production of materials related to existing IMSMAng current use
        cases

    -   Drafting and signature of IMSMA Core agreement -- documenting
        the Esri Licensing, GICHD support and other components of the
        Implementation.

    -   Obtain and convert FFML forms with IMSMA Core tools to provide a
        starting point for Survey123 Development.

2.  Months 3-6

    d.  IMSMA Advisor preparation of IMSMA Core pilot materials,
        migration process and scope of support based on mutual agreement
        with NMAC or Operator

3.  Months 6-8

    e.  Field visit to NMAC or Operator for rollout of IMSMA Core Trial
        (validation with a select set of field users with real data
        collection examples)

    f.  This activity should focus on the primary use cases for IMSMA
        Core (program-dependent)

4.  Months 9-16

    g.  Trial and final Data Migration to IMSMA Core, migration of
        existing attachments (photos and other) and related GIS and IM
        datasets

    h.  Rollout of IMSMA Core to production usage, with ongoing support,
        maintenance, upgrades and bug-fixed by GICHD as appropriate.

In general, IMSMA core trials have focused on a single data type or form
to begin, which supports the setup of the system and migration of one
data type, followed by the migration of other activity types and forms
as appropriate.

Identifying IMSMA Core Components to apply to the Program
---------------------------------------------------------

The IMSMA Core Module Library provides a navigable and searchable
database of IMSMA Core configurations, such as Survey123 forms, Web App
configuration patterns and other information, laying out the "default"
deployment of IMSMA Core as well as a series of workflows that the IMSMA
Advisor can follow to complete the following commonly-completed tasks:

-   Converting a program's existing data entry forms (likely
    spreadsheets or Word Documents) to Survey123 Forms using XLSForm
    templates. This process will include mapping data collected by the
    program to existing IMSMA Core fields in the database.

-   Adding custom fields from IMSMAng to the default IMSMA Core schema
    based on an identification of which CDFs are used in the IMSMAng
    deployment

-   Translating existing IMSMA users + privileges to IMSMA Core users
    and roles and identifying potential users of IMSMA Core workflows
    that may not have been able to make use of IMSMAng

-   Identifying existing hardware resources and advising on IMSMA Core
    system requirements

-   Migrating IMSMAng data into the new IMSMA Core data structure
    following the trial/testing period and with the organization's
    approval.

Initiating the IMSMA Core GitHub Repository and Content Folders
---------------------------------------------------------------

For each IMSMA Core project, the IM Advisor will create a new GitHub
repository under the GICHD organization. This repository will have a
standard Readme.md and will be set up with default folders for scripts,
tools, forms and documentation. This repository will also allow the
Organization IMSMA Core implementation lead to follow developments and
submit issues.

The IM Advisor should also create a folder within the IMSMA Core Box
folder hosted by GICHD, for storage of large files, IMSMA backups, etc.
This folder can be created based on the country name (for national
programs) or the operator name (for sub-national operations or
international NGO operations).

Engaging with Independent Mine Action Programs (Not Current IMSMA Users)
========================================================================

Gathering Existing Information about the Program or Operator
------------------------------------------------------------

[]{#_30j0zll .anchor}Once a program has been identified as a potential
pilot user or as a party interested in migrating from existing IM
processes to IMSMA Core, the following information should be gathered
from the Program to help the GICHD IMSMA Advisor and other involved
parties to assess the level of effort involved in migrating the
Program's existing processes as well as deciding which existing IMSMA
Core workflows might provide good options for the Program:

-   Review Program Structure

    -   How is the operator, program or organization structured in terms
        of reporting, responsibilities and staffing?

    -   Do they have staff in multiple locations and different
        office/field office locations?

    -   Do they employ their own field teams or work with local
        partners?

    -   How do they interact with the NMAC or NMAA (if they do)?

-   Review Existing Data Collection Process and IM Program

    -   Excel-based recording of results

    -   Existing use of mobile applications

    -   History of data collection patterns

    -   Necessary operational indicators and reporting details

    -   Paper Forms already in use?

    -   Type of Information Management tools in use at the country level
        or at the international level if appropriate

    -   Project Management tools -- project and donor tracking and
        project ID generation.

-   Review Reporting and Operational Requirements

    -   How are field teams tasked with specific operations or
        locations?

    -   When and how often is data submitted from field teams?

    -   How does existing data get used in operational decisions?

    -   What type of daily, weekly or monthly reporting is currently in
        place?

    -   How is Quality Management considered, tracked and implemented?

-   Explanation of existing partnerships with other data collection
    vendors or systems

    -   What other groups are working in the same area, and how do they
        interact?

-   Assess Existing resources

    -   Does the country program have a dedicated and long-term IM
        management team?

        -   Is there an international program that supports this task as
            well?

    -   Does the program have available IT resources, IM and GIS Staff?

    -   Is there good access to provisioning or personal mobile devices
        and mobile data in the country?

    -   Is there an existing network environment and internet
        connectivity to support IMSMA Core connections?

    -   Identify the available geospatial datasets that can support
        IMSMA Core deployment -- administrative boundaries, settlement
        and community locations, and other points of interest that will
        be used as part of the gazetteer for IMSMA Core

Identifying a project schedule and plan of action
-------------------------------------------------

IMSMA Core is a system of different tools, apps and components, which
can be deployed in a focused task-specific configuration, in a standard
base configuration tweaked to each program's needs, or in a highly
configured deployment with sufficient staff time investment. The three
factors that will control the schedule and scope of an IMSMA Core
deployment are as follows:

1.  Identifying the breadth of data collection activities undertaken by
    a program

2.  Identifying the complexity of existing data structures and data
    collection systems

3.  Assessing the willingness and ability of the organization's staff to
    learn and take ownership of IMSMA Core.

Identifying these considerations early in the project will allow the
IMSMA Advisor to tailor IMSMA Core to the program's needs quickly,
omitting modules that are not used or not relevant and focusing
automation and customization efforts on the most relevant modules. This
will also help the Advisor to identify key early Pilot presentations and
outputs which can show progress and continue to grow the interest and
involvement in the IMSMA Core system.

Early in the process, the IMSMA advisor should identify an initial
schedule for the IMSMA Core trial, rollout and ongoing maintenance that
can be presented to and eventually agreed to by the NMAC or Operator.
The default length of schedule and content is still to be determined,
but an example schedule could follow this structure:

1.  Months 1-2

    a.  Initial IMSMA Core scoping meeting (mission to visit the
        program) and preparation/sharing of materials related to
        existing IM systems and data collection processes

    b.  Identification of one or more areas for an IMSMA Core trial --
        specific Mine Action processes or data collection methods that
        are well-suited to prototyping with IMSMA Core

2.  Months 3-6

    c.  IMSMA Advisor preparation of IMSMA Core pilot materials,
        migration process and scope of support based on mutual agreement
        with NMAC or Operator

3.  Months 6-8

    d.  Field visit to NMAC or Operator for rollout of IMSMA Core Trial
        (validation with a select set of field users with real data
        collection examples)

4.  Months 9-16

    e.  Rollout of IMSMA Core to production usage, with ongoing support,
        maintenance, upgrades and bug fixed by GICHD as appropriate.

    f.  Expansion of IMSMA Core usage to cover other aspects of Mine
        Action workflows as the NMAC or Program expands into new
        programmatic areas or identifies additional areas for further
        work

Initiating the IMSMA Core GitHub Repository and Content Folders
---------------------------------------------------------------

For each IMSMA Core project, the IM Advisor will create a new GitHub
repository under the GICHD organization. This repository will have a
standard Readme.md and will be set up with default folders for scripts,
tools, forms and documentation. This repository will also allow the
Organization IMSMA Core implementation lead to follow developments and
submit issues.

The Advisor should also create a folder within the IMSMA Core Box folder
hosted by GICHD, for storage of large files, IMSMA backups, etc. This
folder can be created based on the country name (for national programs)
or the operator name (for sub-national operations or international NGO
operations).
