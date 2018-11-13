Upgrading ArcGIS Enterprise to 10.6.1
-------------------------------------

The main upgrade procedure is detailed in [this
page](http://enterprise.arcgis.com/en/portal/latest/administer/windows/upgrade-portal-for-arcgis.htm)
and the related steps are identified below.

## Before starting the procedure

 - Check the space available in your server -- Previous setup files can
be deleted from c:\\Users\\imsma-core\\Documents\\Arcgis10.X

 - Backup the config.js file located in \<Portal for ArcGIS installation
directory\>\\customizations\\\<version
number\>\\webapps\\arcgis\#home\\js\\arcgisonline\\ if some
customization was done.  

## Procedure

1.  Download Installers from GICHD-hosted Box Site or
    https://my.esri.com

    - Portal for ArcGIS for Windows

    - ArcGIS for Server for Windows

    - ArcGIS Web Adaptor for IIS

    - ArcGIS Data Store for Windows

    - Insights for ArcGIS for Windows

    - ArcGIS Desktop

    - ArcGIS Pro

    - ArcGIS License Manager

    **Note: when upgrading software, all versions must be kept in
        sync -- i.e. Portal and Server and Data Store must all be
        version 10.6.1 not a mix of versions. ArcGIS Desktop must also
        be kept in Sync, ArcGIS Pro versions are irrelevant.**

2.  Create an AMI on AWS or create a snapshot on Azure

3.  [Upgrade ArcGIS
    Desktop](http://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/existing-arcgis-desktop-users.htm)

4.  [Upgrade Portal for
    ArcGIS](http://server.arcgis.com/en/portal/latest/administer/windows/upgrade-portal-for-arcgis.htm)

    a.  Uninstall the /portal Web Adaptor -- **Step 3 in Upgrade page**

    b.  Run the Portal for ArcGIS Installer -- **Step 4 to 8 in Upgrade
        page**

    c.  Continue Portal Upgrade -- **Step 9 to 14 in Upgrade page**

    d.  Check that the upgrade finished properly by going to the Portal
        Admin page: https://<local ip>:7443/arcgis/portaladmin/

5.  [Upgrade Portal Web
    Adaptor](http://server.arcgis.com/en/web-adaptor/latest/install/iis/install-arcgis-web-adaptor-portal.htm#ESRI_SECTION1_707EA8289B024BCF94F754A59B7EBBE8)
    **Step 15 to 17 in Upgrade page**

    a.  Install new /portal Web Adaptor

        i. Run the Web Adaptor Installer

        ii. Name the web adaptor /portal

        iii. Select either Default Website (80 or 443)

        iv.  Install the Web Adaptor

        v. After install, a web browser will launch
        
If your web server hosts multiple sites, like dev.imsma-core.org also hosts GIS4Peace and the IMSMA Core storymap, then you will see **Error 2878** when trying to install the web adapter.  You can workaround this with some temporary re-configuration of the IIS bindings described in this [technical note](https://support.esri.com/en/technical-article/000012091)

    b.  Configure the /portal Web Adaptor

        i. Use the web browser launched by the installer or navigate to https://<local ip>/portal/webadaptor

        ii. Select "Portal for ArcGIS" and Next

        iii. For the Portal URL enter https://<local-ip>:7443 or https://<local-hotname>:7443

        iv. For the Admin User and Password, enter the username and password you created during the Initial Admin Account creation process in the Portal Install
        
        v.  If you receive the error "A Web Adaptor has already been configured with Portal for ArcGIS" then you need to first unregister the previous web adapter from Portal.  You can do this by visiting the web admin page https://<local-hostname>:7443/arcgis/portaladmin/system/webadaptors and selecting 'Unregister Web Adapter' against the previous web adapter.

        vi. After configuration, the Portal hostname and URL should appear at the bottom of the screen. Portal Install is complete.

6.  Upgrade Living Atlas -- **Step 18 in Upgrade page**

7.  Uninstall ArcGIS Server Web Adaptor -- **Step 19 in Upgrade page**

8.  [Upgrade ArcGIS
    Server](http://server.arcgis.com/en/server/latest/get-started/windows/upgrade-arcgis-server.htm)[]{#_Hlk525633611
    .anchor} - **Step 20 to 21 in Upgrade page**

    a.  Run the ArcGIS Server Installer

    b.  After extracting the software, run the Setup program

    c.  Select Finish to proceed with the Upgrade

    d.  After the upgrade completes, re-authorize the software with an ArcGIS Server license file if needed

    e.  After authorization finishes, a web browser will launch

    f.  Select Continue Upgrade to finish the Server Upgrade

    g.  If Continue Upgrade does not appear

        i. Check first that the file D:\\arcgisserver\\config-store\\version.json lists 10.6.0

        ii. Navigate to the file C:\\Program Files\\ArcGIS\\Server\\framework\\etc\\config-store-connection.xml

        iii. Stop ArcGIS Server

        iv. Copy this file then add \"-upgrade\" at the end to mimic config-store-connection-upgrade.xml

        v. Rename the original file so that it is not picked up by the system

        vi. Start ArcGIS Server

        vii.  Continue Upgrade should appear in Server manager now

        viii. The file D:\\arcgisserver\\config-store\\version.json is now set to 10.6.1

9.  Upgrade Server Web Adaptor - **Step 22 to 24 in Upgrade page**

    a.  Uninstall the /server Web Adaptor

    b.  Install a new /server Web Adaptor using the latest installer

        i. Follow the instructions from 5.b above except:

        ii. Configure the /server Web Adaptor using https://<local-ip>:6443

10. [Upgrade ArcGIS Data
    Store](http://server.arcgis.com/en/portal/latest/administer/windows/upgrade-data-store.htm) -
    **Step 25 in Upgrade page**

    **Note: ArcGIS Server must be upgraded before the ArcGIS Data
        Store**

    a.  Run the ArcGIS Data Store installer

    b.  Run the Setup program after the software extraction is completed

    c.  Complete the Installation, a web browser will launch

    d.  In the web browser, enter the ArcGIS Server site URL https://<local-ip>:6443

    e.  Select Next, the page should show the ArcGIS Data Store directory and be greyed out

    f.  Confirm that Relational and Tilecache are selected, then Select Next and complete the Upgrade

11. Upgrade License Manager - **Step 26 in Upgrade page**

12. Restore manual configuration (config.js) - **Step 27 in Upgrade page**

13. Upgrade ArcGIS Pro to latest version if needed

14. Upgrade Geodatabase(s)

    a.  Copy binaries from C:\\Program Files(x86)\\ArcGIS\\Desktop10.6\\DatabaseSupport\\PostgreSQL\\9.X\\Windows64
        to \<PostgreSQL Install Location\>\\lib (Stop the PosgreSQL service if needed)

    b.  From ArcGIS Pro, locate an .sde connection file with an ArcSDE Administrator for IMSMA Core

    c.  Run the [Upgrade Geodatabase](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/upgrade-geodatabase.htm)
        Tool from ArcGIS Pro

    d.  Repeat if there are more than 1 database

15. Delete previous setup files from
    c:\\Users\\imsma-core\\Documents\\Arcgis10.X

16. Get latest patches for ArcGIS Enterprise by running the "Check for
    ArcGIS Enterprise Updates" application

**Do not forget to update the Server Tracker file**
