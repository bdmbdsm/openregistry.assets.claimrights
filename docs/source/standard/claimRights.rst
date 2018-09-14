.. . Kicking page rebuild 2014-10-30 17:00:08
.. include:: defs.hrst

.. index:: claim right, Parameter, Classification, Unit, Value, claimRights Workflow, Item

.. _claim right:

Claim Right
===========

Schema
------

:id:
    string, auto-generated, read-only
    
:assetID:
   string, auto-generated, read-only

   The claim right identifier to refer it to in the `paper` documentation. 

   |ocdsDescription|
   AssetID is included to make the flattened data structure more convenient.
   
:date:
    string, auto-generated, read-only
    
    The date of claim right creation/undoing.
    
:dateModified:    
    string, auto-generated, read-only
    
    |ocdsDescription|
    Date when claim right was last modified.
    
:mode:
    optional
    
    The additional parameter with a value ``test``.
    
:status:
    string, required, :ref:`claimRights Workflow`
    
    The claim right status within the Registry.
    
:value:
    :ref:`Value`, required 
    
    Estimated value of the claim right.
    
:relatedLot:
    string, required in `active` status
    
    ID of the related Lot.
    
:assetType:
    string, required

    The assetType to be used here is `claimRights`.

:title:
    string, multilingual
    
    * Ukrainian by default (required) - Ukrainian title
    
    * ``title_en`` (English) - English title
    
    * ``title_ru`` (Russian) - Russian title
    
    Oprionally can be mentioned in English/Russian.
    
:description:
    string, multilingual, optional
    
    |ocdsDescription|
    A description of the goods, services to be provided.
    
    * Ukrainian by default - Ukrainian decription
    
    * ``decription_en`` (English) - English decription
    
    * ``decription_ru`` (Russian) - Russian decription
    
:documents:
    
    |ocdsDescription|
    All related documents and attachments.
    
:assetCustodian:
   :ref:`Organization`, required

   The entity managing current claim right.
    
:classification:
    :ref:`Classification`, required

    The primary classification for claim right.

    It is required for `classification.scheme` to be `CAV`. The
    `classification.id` should be valid CAV code.

:additionalClassifications:
    List of :ref:`Classification` objects, optioanl

    |ocdsDescription|
    An array of additional classifications for the item. See the
    `itemClassificationScheme` codelist for common options to use in OCDS. 
    This may also be used to present codes from an internal classification
    scheme.

    The possible additional classifiers are CPVS and koatuu.

:unit:
    :ref:`Unit`, required

    |ocdsDescription| 
    Description of the unit which the good comes in e.g.  hours, kilograms. 
    Made up of a unit name, and the value of a single unit.

:quantity:
    integer, required

    |ocdsDescription|
    The number of units required.

:location:
    dictionary

    Geographical coordinates of the location. Element consists of the following items:

    :latitude:
        string, required
    :longitude:
        string, required
    :elevation:
        string, optional, usually not used

:items:
    :ref:`Item`
    
    List of assets specified within the claim right.


:debt:
    :ref:`Debt`, optional
        

.. _Classification:

Classification
==============

Schema
------

:scheme:
    string

    |ocdsDescription|
    A classification should be drawn from an existing scheme or list of
    codes.  This field is used to indicate the scheme/codelist from which
    the classification is drawn.  For line item classifications, this value
    should represent a known Item Classification Scheme wherever possible.

:id:
    string

    |ocdsDescription|
    The classification code drawn from the selected scheme.

:description:
    string

    |ocdsDescription|
    A textual description or title for the code.

:uri:
    uri

    |ocdsDescription|
    A URI to identify the code. In the event individual URIs are not
    available for items in the identifier scheme this value should be left
    blank.

.. _Unit:

Unit
====

Schema
------

:code:
    string, required

    UN/CEFACT Recommendation 20 unit code.

:name:
    string

    |ocdsDescription|
    Name of the unit
    
.. _value:

Value
===============

Schema
------

:amount:    
    float, required

    Should be positive.
    
:currency:
    string, required
    
    |ocdsDescription|
    The currency in 3-letter ISO 4217 format.
    
:valueAddedTaxIncluded:
    bool, required

