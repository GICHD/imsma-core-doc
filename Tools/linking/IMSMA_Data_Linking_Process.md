[Back to main menu](../../index.md)  

Linked Data/Linking Design for IMSMA Core
=========================================

Implementation Details:
-----------------------

Each feature class in the IMSMA Core database will have a field added to
it called **imsma\_links**, which will be a string field with length of
20,000. This field will be used to store a comma-separated list of
linked features from other layers.

Each feature in IMSMA Core will have a dedicated IMSMA Identifier, which
incorporates the feature type and an integer ID which increases
sequentially. Examples: *hazard\_poly\_145*, *organization\_2*,
*accident\_34*, etc. This ID will be stored in a field called
**imsma\_id**, a 50-char text field.

Values for **imsma\_id** will be generated in one of several different
ways:

-   By concatenating the feature type ("hazard\_poly\_") with the
    feature's ObjectID during data loading from an IMSMAng Staging Area

-   When a feature is added/edited through an ArcGIS Pro task, the field
    can be calculated automatically after the feature is created

-   When linking features, if a feature is selected that has a Null
    **imsma\_id**, one can be generated automatically and updated during
    this process.

-   The program may choose to use an existing ID pattern, which can be
    imported for existing features

When a user wishes to link features together, they will use a
geoprocessing tool which will generate these links:

**Link through GP Tool**

1.  The user shall select all features which they wish to link. The user
    can select multiple features across different layers

2.  The user will open the tool, either by navigating to the toolbox or
    by launching it as part of a Pro Task Step.

3.  The tool will have two input parameters

    a.  Select Map

        i.  Select which Map in the Pro project to run the linking
            process on. The Linking Process will run against all layers
            with selections in the Map.

    b.  (Test Mode)

        i. This parameter, if checked, will simulate the linking and
            updating, rather than updating the feature in the database.

4.  The tool will also display descriptive text describing the number of
    features to be linked (using Tool Validation to show the number of
    selected features from each layer in the map)

    a.  To be developed

5.  They will execute the tool. The tool will then complete the
    following steps

    a.  Iterate through all selected features and collect a list of
        IMSMA IDs from each source layer which has a feature selection

        i. Ex. "hazard\_24, accident\_2, device\_4222"

    b.  If Linking Features

        i. If "test mode" is disabled, For each layer which has a
            feature selection, append all foreign imsma\_IDs (ids from
            any other selected features) to the imsma\_links field
            (including any other IDs for the current layer) as comma
            separated values, adding to any existing values.

    c.  If Unlinking Features

        i.  For each layer which has a feature selection, remove all
            foreign imsma\_IDs (ids from any other selected features)
            from the imsma\_links field (including any other IDs for the
            current layer), keeping the existing values as a comma
            separated list with that value removed.

    d.  Clear the current selection across all layers after completion
        of the tool, and provide a summary of actions taken.

6.  The GP tool should also have some validation to check if conditions
    are proper for execution:

    a.  If no features are selected, return an error (preferably in tool
        validation)

    b.  If any of the feature classes do not contain the proper fields,
        return a descriptive warning

    c.  Add new features to the links that already exist (do not
        overwrite existing linked features)

**Link through Pro Tasks**

As an optional Step that could be added to Pro Tasks would be to link to
other features. In this step, the user could select a set of additional
features from other layers that they wish to link their newly-created
feature or features to. The tool would then execute the geoprocessing
tool described above, which would append the linkage IDs into the
features. This differs because it would be based on features created
during that Pro task, not an ad-hoc selection of features.

Using imsma\_links Data
-----------------------

The Linking functionality described above serves several purposes:

1.  Users can view the attributes of a feature and see which other
    features are linked to it immediately and visually (no long GUIDs or
    identifiers.

2.  The Locate dialog in Pro can be configured to support this field
    with a "contains" query, so that a user can search for "hazard\_22"
    and find that hazard along with all other features that have that
    hazard in their Link field.

3.  Further analytical workflows can be run to compare linked features,
    assess linkages for potential errors, auto-link features based on
    spatial location, etc.
