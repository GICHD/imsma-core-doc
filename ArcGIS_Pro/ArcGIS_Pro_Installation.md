[Back to main menu](../index.md)  

ArcGIS Pro Installation, Licensing and Configuration
====================================================

ArcGIS Pro is a key component of most IMSMA Core deployments. Pro
provides an enterprise-grade Desktop GIS product for geospatial data
management, editing, geoprocessing and cartographic layouts. Pro is a
professional tool that can be configured to be fully featured or more
carefully focused. IMSMA Core uses ArcGIS Pro Configurations
(.proConfigX) files, ArcGIS Pro **Tasks**, and other settings to
streamline the Pro interface and user experience for IMSMA's potential
User Community.

This document covers topics surrounding the installation, licensing and
configuration of ArcGIS Pro.

Installation
------------

ArcGIS Pro is installed from a single .exe file, delivered via HTTP link
at <https://esri.box.com/s/obv3v9c14vgwfd8t5v38xflq59rh9dx7> (Current
version, ArcGIS Pro 2.0). ArcGIS Pro can also be downloaded from My
Esri, Esri's software download, licensing and distribution site, or
hosted on an internal file share, external hard drive or FTP site.
Follow these steps to install ArcGIS Pro (see documentation for
additional references:
<http://pro.arcgis.com/en/pro-app/get-started/install-and-sign-in-to-arcgis-pro.htm>)

1.  Confirm System Requirements for ArcGIS Pro

2.  Download the Installation File

3.  Run the Installer, installing ArcGIS Pro to the default location
    [C:\\Program Files\\ArcGIS\\Pro]{.underline}

After installing the software, you will be prompted to authorize ArcGIS
Pro with a License.

Authorizing and Licensing ArcGIS Pro
------------------------------------

ArcGIS Pro can be authorized in three separate ways, each with their own
benefits and drawbacks. See the [ArcGIS Pro License
Types](http://pro.arcgis.com/en/pro-app/get-started/licensing-arcgis-pro.htm)
documentation page for more details, along with a short description
below:

1.  [Named User
    License](http://pro.arcgis.com/en/pro-app/get-started/named-user-licenses.htm)

    a.  This license is tied to a user's login, and can be used across
        multiple ArcGIS Pro installations or on multiple machines at a
        single time (when logged in as that user). The benefit of this
        license is flexibility, while the difficulty of the license is
        attaching the Named User to a single ArcGIS Online or Portal for
        ArcGIS deployment.

    b.  Each IMSMA Core licensee can allocate ArcGIS Pro Named User
        Licenses to either ArcGIS Online or Portal, but not both. This
        may impact the decision to use this license type

    c.  Named User licensing requires access to your licensing Portal or
        ArcGIS Online unless the license is taken offline, which allows
        you to continue to use the license on a single server for as
        long as is necessary. Offline Single Use licenses can be
        returned at any time.

2.  [Concurrent Use
    License](http://pro.arcgis.com/en/pro-app/get-started/concurrent-use-licenses.htm)

    a.  A Concurrent Use license is a shared license -- a pool of
        licenses which is used up when a user accesses a license and
        then is returned when the user shuts down Pro. This license
        model has some significant advantages in that many different
        occasional users can be licensed for Pro if only a selected set
        of users are actively using the program at one time. One
        limitation of this license model is reliance on a combination of
        Portal for ArcGIS and the ArcGIS License Manager to provision
        licenses -- they must be upgraded in concert and kept current to
        provide the latest ArcGIS Pro licenses.

    b.  Concurrent Use Licensing relies on having internet or intranet
        access to your Portal and License Manager

    c.  The ArcGIS License Manager also requires direct access via
        non-standard network ports, which are generally locked to Ports
        27000 and 27001 and may require specific firewall exemptions
        between the user's computer and the License Manager host.

    d.  Concurrent Use Licenses can be taken offline in the same fashion
        as Single Use licenses

3.  [Single Use
    License](http://pro.arcgis.com/en/pro-app/get-started/single-use-licenses.htm)

    a.  The Single Use License for ArcGIS Pro is the most versatile
        license deployment for a single user's needs. It locks the
        license to a single machine, which means that that license is
        unavailable to any other users until the license is
        deauthorized. This license is available to the user whether
        offline or online, regardless of connectivity to any other
        ArcGIS or IMSMA Core components.

    b.  With a Single Use license there is no need for offline
        authorization as the license is tied to the user's machine
        whether online or offline.

Configuring ArcGIS Pro for IMSMA Core
-------------------------------------

After installing and licensing ArcGIS Pro, connect it to your Portal
using the Manage Portal Connections dialog documented
[here](http://pro.arcgis.com/en/pro-app/help/projects/manage-portal-connections-from-arcgis-pro.htm).
This allows the user to authenticate to any web services hosted in IMSMA
Core and use the same login to access all content. This also connects
ArcGIS Pro to the user's Groups and Content -- accessible through the
[Catalog
Pane](http://pro.arcgis.com/en/pro-app/help/projects/the-project-pane.htm)
in Pro.

When opening ArcGIS Pro projects from Portal, use the Project -\> Open
-\> Portal dialog and select the proper group to find the available
Project Files.
