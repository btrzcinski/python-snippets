EasyCocoaFileDialog
===================

============
Introduction
============

This module provides an easy abstraction of NSOpenPanel and NSSavePanel for
Python script writers that would like to prompt the user for input/output files
without the ugliness of using the command line. 

The module requires the Cocoa module, which is part of `PyObjC <https://pythonhosted.org/pyobjc/>`_.

.. tip:: PyObjC appears to be included with OS X, at least as of 10.10 Yosemite.

========
Examples
========

For example code, see the module's **main** method.

=========
Reference
=========

.. py:module:: EasyCocoaFileDialog
   :synopsis: Module that shows Cocoa file dialogs for selecting paths.

.. py:function:: chooseFileToOpen(prompt="Select the file to open")
   
   Show a Cocoa NSOpenPanel prompting the user for the path of a single file to open.

   :param str prompt: The message shown at the top of the NSOpenPanel
   :return: the path to the file chosen by the user, or :py:const:`None` if the user clicks Cancel.
   
.. py:function:: chooseFileToSave(prompt="Select the file to save")
   
   Show a Cocoa NSSavePanel prompting the user for a path of a file to save to.

   :param str prompt: The message shown at the top of the NSSavePanel
   :return: the path to the file chosen by the user, or :py:const:`None` if the user clicks Cancel.

