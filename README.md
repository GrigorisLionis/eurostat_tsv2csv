# eurostat
Pyhton app for downloading  Eurostat tables and prepare them for loading in local MySQL using csv.  

## Eurostat tsv files
Eurostat publishes statistical data in a tsv.gz format, for the bulk download facility. 

## Rationale
Eurostat tsv files contain data using distict columns for each time (date). This format is not a "nice" format for using the data in a database. To use the data in a database the data (should/might/could) be reshaped i an row format (transform them from a wide to a long format) .MySQL does not have a "melt" function, and the unpivoting is not completely straightforward. 
A easier apporach is to unpivot the data before entering them in the database. A simple pandas operation could have been used (i.e. melt) but the desigh choice was to use minimal requirements, as the goal is to load the data in an (My)SQL db and use them from there

### Database Cloning
While Eurostat has published a number of veryu helpfull [tools for manipulating data](https://cros-legacy.ec.europa.eu/content/tools-and-software_en) , a db-> db facility is yet non existest. The rationale behind this script is to load the eurostat tables in a local SQL db, and to be able to perform all the data manipulation locally. Moreover, more often than not, It is necessary to use subset of data from multiple tables. A SQL approach seems a better fit. 

## Usage

### Building 
The pyhton package has to be built & installed. 
* Building the package : python3 -m build
* Installing the package :  python3 -m pip ./dist/eurostat2csv-0.5.0-py3-none-any.whl 

The package is bundled as a small python app

### Using
eurostat2csv table_name  
(the script will be installed out of the path, so care has to by taken)

The output  is  
* tablename.csv
* tablename.sql (sql commands to create table and load csv onto the database)   
The data can be fed into a MySQL database with
mysql  -e "source ./tablename.sql"


## ToDo
* Run test cases for verifying correctness of script
* More internall checks for verifying data is interpreted correctly
* Clean the code
* add key


