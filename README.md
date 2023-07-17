# CCI_Namespace_Injector
Injects (or removes) the namespace placeholder needed for CumulusCI into files within your project

## Problem
When you have a CumulusCI Project, you want to be able to inject the namespace placeholder "%%%NAMESPACED_ORG%%%" into the files within your project which don't automatically inject the namespace, wherever there is a custom reference like My_Custom_Field__c or a custom relationship like Custom_Relationship_r. 

## Solution/Install
Add the python file located within the scripts folder to the root of your CumulusCI project and then run the file. Ensure that you have python 3+ installed.

The script will update the required files by finding and updating all the references.

## Terms

Use this script at your own risk. Check and ensure that all files are updated correctly in a test environment first.
