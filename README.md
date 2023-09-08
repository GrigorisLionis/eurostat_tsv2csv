# eurostat_tsv2csv
Small script for turning Eurostat tsv files to csv
## Eurostat tsv files
Eurostat publishes statistical data in a tsv.gz format. 
## Rationale
Many (most?) eurostat files contain data using distict columns for each time (date). This format is not a "nice" format for using the data in a database. To use the data in a database the data (should/might/could) be reshaped i an row format (transform them from a wide to a long format) .MySQL does not have a "melt" function, and the unpivoting is not straightforward. It is better to unpivot the data before entering them in the database. A simple pandas operation could have been used (i.e. melt) but the desigh choice was to use minimal requirements, as the goal is to load the data in an (My)SQL db and use them from there
## Usage
eurostat_tsv2svs filename.tsv > out.csv
## ToDo
* More checks for correctness  
* Increased scope of eurostat data recognised  
* Automate the download pipeline (download gz file, unpack, read the tsv)  
* Automatically produce database schema from the download data  


