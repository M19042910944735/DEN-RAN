======================
Quadratus Export ASCII
======================

This module allow to export account move lines in an ASCII format accepted by Quadratus application.
Note: The partner internal reference is used instead of account code for receivable/payable accounts

Usage
=====

- Go to to Accounting > Report > Quadra > Export ASCII
- Fill start and end date
- Click on "Generate" button
- A warning is displayed to alert if there is missing "Internal Reference" on partner associated to "Receivable"/"Payable" accounts
- Download your ASCII file and import it on Quadra

.. image:: static/description/export_wizard.png
   :width: 400
.. image:: static/description/result.png
   :width: 400
.. image:: static/description/exported_file.png
   :width: 800


Configuration
=============

In Accounting/Configuration/Settings you have an option "Quadra Export Group Lines", 
this allow to group the move lines by account/ journal entry / partner during the export.

.. image:: static/description/config.png
   :width: 800


Maintainer
----------

This module is maintained by Auneor Conseil.
