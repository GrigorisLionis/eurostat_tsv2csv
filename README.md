# eurostat
Set of scripts for loading  Eurostat tables in local MySQL.  
* Eurostat_get_tsv <table_name> downloads the table from Eurostat database
* Eurostat_tsv2csv reads tsv file and transforms it to csv file, while producing a file for reading the csv ibto a mysql table
* Eurostat calls both these files

## Eurostat tsv files
Eurostat publishes statistical data in a tsv.gz format, for the bulk download facility. 
## Rationale
Eurostat tsv files contain data using distict columns for each time (date). This format is not a "nice" format for using the data in a database. To use the data in a database the data (should/might/could) be reshaped i an row format (transform them from a wide to a long format) .MySQL does not have a "melt" function, and the unpivoting is not straightforward. It is better to unpivot the data before entering them in the database. A simple pandas operation could have been used (i.e. melt) but the desigh choice was to use minimal requirements, as the goal is to load the data in an (My)SQL db and use them from there
### Database Cloning
While Eurostat has published a number of veryu helpfull [tools for manipulating data](https://cros-legacy.ec.europa.eu/content/tools-and-software_en) , a db-> db facility is yet non existest. The rationale behind this script is to load the eurostat tables in a local SQL db, and to be able to perform all the data manipulation locally. 
## Usage
eurostat.sh table_name  
the script interbally calls 
eurostat_get_tsv table_nane
eurostat_tsv2csv table.name.tsv
The output  is  
* tablename.csv
* tablename.sql (sql commands to create table and load csv onto the database)   
The data can be fed into a MySQL database with
mysql  -e "source ./tablename.sql"
## ToDo
* Run test cases for verifying correctness of script
* More internall checks for verifying data is interpreted correctly
* ~~Increased scope of eurostat data recognised~~ Examine eurostat tsv file specification 
* ~~Automate the download pipeline (download gz file, unpack, read the tsv)~~
* ~~Automatically produce database schema from the download data~~  


