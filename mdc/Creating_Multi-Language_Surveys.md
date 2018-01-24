Creating Multi-Language Surveys
===============================

The Survey123 field app will show a language switcher in the top-right
corner if your survey has been configured to support multiple languages.
In order to add multi language support into a survey, you will use
Survey123 Connect for ArcGIS to add columns translating questions,
hints, and choices.

Note that the language switcher defines the language to be used in the
survey, which is different from the language used by the app. The
language used by the app is defined by the locale of your device. 

The survey level language controls can change the following:

-   Question Labels

-   Hint Messages

-   Constraint Messages

-   Choice Labels

-   Images

-   Audio

Default Language Columns
------------------------

By default the advanced XLS form comes with two columns to change the
question label and the hint language.

### Label::language1

The label is equivalent to the alias of a feature class or service. It
is what will be seen by the user when the are filling out the form. This
column contains the label that is shown when the user switches to a
different language. The language1 in the column heading should be
switched to the appropriate name used to identify the language.

### Hint::language1

The values entered in this column will appear below the question label
and can provide the user with guidance about how to answer the question.
This column contains the hint that is shown when the user switches to a
different language. The language1 in the column heading should be
switched to the appropriate name used to identify the language.

If you want to have more than two languages or translate more than the
label and the hint you will need to add columns to the spreadsheet.

Translate survey questions
--------------------------

The process for including translations for your survey questions
in Survey123 for ArcGIS is as follows:

1.  Add a column to your survey worksheet and name it label:: followed
    by the name used to identify the language. While the name of the
    language will work, for example, label::Español, it\'s recommended
    that you instead use the two-character locale code, for
    example, label::es.

    a.  For information on a specific language\'s local codes, see
        Wikipedia\'s [List of ISO 639-1
        codes](https://en.wikipedia.org/wiki/list_of_iso_639-1_codes).
        However, keep in mind that not all of these languages are
        supported by Survey123.

2.  For each question to be translated, enter the translated text
    directly in this column.

3.  Repeat for each additional language.

![Create a label column for each
language](Creating_Multi-Language_Surveys/media/image1.png)


Translate hints and constraint messages
---------------------------------------

Hints are translated the same way as labels.

1.  Add a column to your survey worksheet and name it hint:: followed by
    the name or locale code used to identify the language, for
    example, hint::es.

2.  For each hint to be translated, enter the translated text directly
    in this column.

3.  Repeat for each additional language.

![Create a hint column for each
language](Creating_Multi-Language_Surveys/media/image2.png)


The constraint message that displays when a constraint is not adhered to
can also be translated, with a column such as constraint\_message::es.

Translate choice lists
----------------------

You can also provide translations for the options in your choice lists.

1.  Add a column to your choices worksheet and name it label:: followed
    by the name or locale code used to identify the language, for
    example, label::es.

2.  For each option to be translated, enter the translated text directly
    in this column.

3.  Repeat for each additional language.

![Create a label column for each
language](Creating_Multi-Language_Surveys/media/image3.png)


Translate images and media
--------------------------

Translated images can also be provided across languages.

1.  Add a column to your survey or choices worksheet and name
    it image:: followed by the name or locale code used to identify the
    language, for example, image::es.

2.  For each image to provide a translation for, place the translated
    image in the survey\'s media folder, and enter its file name in the
    new column.

3.  Repeat for each additional language.

![Create an image column for each
language](Creating_Multi-Language_Surveys/media/image4.png)


Audio files attached to a question or choice can be translated similarly
with an audio:: column, such as audio::es.

Default languages other than English
------------------------------------

If you intend to use a survey with non-English labels on a device with a
locale that is set to English, there is a subtle difference in behavior
depending on how the non-English language is identified. The default
column titled **label** can contain text in any language, and this
content will be displayed for the labels of your questions by default.
In most cases, this works as expected. In some cases, you may see RTL
text displayed as LTR, or dates, currency, and calendars displayed in
English.

To ensure the best translation experience it is recommended that you do
the following:

-   Use the locale code in the label column title, for
    example, label::he.

-   Define a **default\_language** on the **Settings** tab.

When you use the locale code, Survey123 will not only ensure that the
text you include in your spreadsheet is displayed as expected but also
use the locale preferences to display the expected numbers, currency
values, and calendar pickers.

Switch between languages in Survey123 field app
-----------------------------------------------

To switch between supported languages in your survey, open the menu in
the upper right corner and choose from the list of available languages.
If no translations have been supplied, there will be no languages
listed.

    ![image](Creating_Multi-Language_Surveys/media/image5.png)

