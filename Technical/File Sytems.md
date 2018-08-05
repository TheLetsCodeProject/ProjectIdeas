# File Systems
***
Every single interaction we have with computers occurs with a file interface. Without these systems, we would have no way of actually storing and retrieving data. Most new file systems are implemented in the form of a database such as SQL or MongoDB.

## Version control system (VCS)
Create a version control system such as git which is able to compare and track differences. This would be simpler than fully reimplementing a file system as you only have to introduce a new layer on top of your systems native file system.

Completing this project would invilve vast amounts of research and I could only begin to attempt to explain the steps involved.

## Full blown database/file system
This would involve a few layers of abstraction as, unless you intend to write a C class library or assembly language interface, you will probably need a better way to directly write to a hard drive. Instead you should probably interact with the native OS in order to write data to a disk. NOTE: this is not cheating because we should only use the OS to write a single packet to the drive. WE ARE NOT WRITING A WRAPPER CLASS FOR THE FILE UNIT.

To complete this project you'll need to understand the basics of data allocation and other fundamentals of file systems such as segmentation and volume labelling. 