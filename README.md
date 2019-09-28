# Mikrotik Documentation
Pull data from Mikrotik and make it easy to read

# Synopsis
The goal of this project is an excerciese in working with the LibrouterOS Python API and pulling data from a Mikrotik Router.
Currently the script logins to a Router and formats the data and prints it to console.

# Required Packages
This usese the following Pakages/Modules
* getpass
* LibrouterOS

# How it works
The Script asks users in the following order
* FQDN or IP of Mikrotik
* Username
* Password

It then logs in and passes Commands to the Mikrotik and formats the data and prints it to console

# To Do
* Use token/SSL login instead of plain text login
* allow the ability to pass arguments and save to file
