# ---+ Extensions
# ---++ TreePlugin
# **BOOLAN EXPERT LABEL="Disable cache"**
# Disable caching, usually enabled for developemnt purposes.
$Foswiki::cfg{Plugins}{TreePlugin}{NoCache} = 0;
# **NUMBER EXPERT LABEL="Debug level"**
# Set to 1 to enable debug logging, and 2 to enable verbose
# debugging.  The information is written to the Foswiki debug log.
# It is located in =working/logs/debug.log= or in an alternate location if 
# configured under the Logging tab.
$Foswiki::cfg{Plugins}{TreePlugin}{Debug} = 0;
1;
