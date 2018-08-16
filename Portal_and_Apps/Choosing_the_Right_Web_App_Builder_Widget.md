[Back to main menu](../index.md)  

Choosing the Right Web App Builder Widget
=========================================

Web AppBuilder allows you to easily create applications by accessing
workflow tabs
including [Theme](http://server.arcgis.com/en/portal/latest/use/themes-tab.htm), [Map](http://server.arcgis.com/en/portal/latest/use/map-tab.htm), [Widget](http://server.arcgis.com/en/portal/latest/use/widgets-tab.htm),
and [Attribute](http://server.arcgis.com/en/portal/latest/use/attributes-tab.htm).

Here are some considerations to keep in mind as you consider which
widgets and theme to use:

-   Purpose---The most important consideration is the purpose of your
    app. Embedded within this goal is your intended audience: Who is
    going to use your app and what are the key points that you want them
    to take away from the experience?

-   Functionality---What is the critical functionality needed to support
    that goal?

-   Aesthetic---How does the app's layout and color scheme support your
    brand or message?

This document compares some of the widgets available through Web App
Builder that have similar functionality.

Editing
-------

The
[Edit](http://server.arcgis.com/en/portal/latest/use/widget-edit.htm)
widget allows you to do basic editing.

-   It has the following toolbar options: Merge, Cut, Reshape, and
    Enable Undo/Redo

-   It has the following tolerance options:

    -   **Set the snapping tolerance in pixels**---For geometry editing.

    -   **Set the tolerance of attribute editing popup in
        pixels**---Enables users to easily open the attribute editing
        pop-up by clicking on the feature.

    -   **Set the sticky move tolerance in pixels**---Prevents users
        from moving the features within a certain distance.

-   Editing can be enabled on only certain layers in the map and
    geometry updates can be disabled if desired.

-   Within the editable layers which fields are editable and which are
    displayed can be chosen.

-   An optional filter for the templates is available so you can quickly
    find the edit template.

The [Smart
Editor](http://server.arcgis.com/en/portal/latest/use/widget-smart-editor.htm)
widget extends the Edit widget with the following features:

-   Attribute editing is performed in the panel and not in the pop-up.

-   The ability to hide, require, or disable a field based on the values
    of other fields.

-   New features and changes to existing features are not pushed to the
    service until you click **Save**.

-   The ability to view pop-ups from other data on the map while
    editing.

-   The ability to preset field values across many fields on many layers
    and apply them to every new feature.

-   The ability to edit a series of features.

-   The option to move or modify existing geometry.

-   Only changed attributes are submitted to the service instead of the
    entire record.

-   Configurable descriptions are available on both the widget and for
    each layer.

The [Batch Attribute
Editor](http://server.arcgis.com/en/portal/latest/use/widget-batch-attribute-editor.htm)
widget is edits multiple features at once, while the Smart Editor and
Edit widgets focus on editing one feature at a time.

-   The following methods can be used to select features:

    -   **Select by Area**---Select a shape and sketch it on the map.

    -   **Select by Feature**---Select a polygon feature and update all
        within the area.

    -   **Select by Feature & Related Features**---Select a feature and
        update all related features.

-   One or multiple layers can be updated, if multiple layers only
    common fields can be updated.

Filtering
---------

The
[Filter](http://server.arcgis.com/en/portal/latest/use/widget-filter.htm)
widget allows you to limit the visibility of features in a layer. Only
the features that meet the expression criteria will be visible in the
map.

-   Option to remove preset layer filters from the map.

-   Ability to add one or multiple filters. Each filter points to one
    layer.

    -   Within a filter can add one or multiple filter expressions.

    -   Can give user a dropdown list to choose from when using the
        widget by creating an expression based unique values and
        clicking the box next to **Ask for values**.

The [Group
Filter](http://server.arcgis.com/en/portal/latest/use/widget-group-filter.htm)
widget allows you to apply a filter to multiple layers at once.

-   Option to append filter to existing web map filter using or or and.

-   Ability to add one or multiple filter groups. Each filter group
    points to one or multiple layers.

    -   Can enter a preset value so the filter automatically runs, have
        a blank box for the user to enter a value or have a dropdown of
        values for the user to choose from.

The
[Query](http://server.arcgis.com/en/portal/latest/use/widget-query.htm)
widget does not filter the source layer but instead creates a new layer
based on the filter criteria.

-   Can use spatial filters in addition to attribute filters like the
    Filter widget has.

-   Displays features that meet filter criteria in a list in the widget.

[Back to main menu](../index.md)  
