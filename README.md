# USCIS Monitors

Every now and then I use these scripts to monitor something online and
alert me when changes happen.  Since these are related to information
available on the USCIS website, they might be useful to other people
as well.


## Usage

### All Scripts

There's a convenience script that runs all monitors and outputs either
the results or "No chages." that I currently use along with
[shellwrangler][].  It loads all tasks from the `tasks` file. See
`tasks.sample` for an example of how to write new tasks.


### Individual Scripts

    ./uscis_case_status.py <case-number> "<last-known-status>"
    # Displays new status every time it changes
    # e.g. ./uscis_case_status.py CSR1234123412 "Was Received"

    ./uscis_processing_time.py <service-center-code> "<classification>" "<last-known-date>"
    # Detects when processing date for Employment-base applications changes
    # e.g. ./uscis_processing_time.py TSC "Employment-based adjustment applications" "December 10, 2016"


## Tooling

These scripts depend on python 3.  If you're on a mac, you might find an
app called [shellwrangler][] useful to display the information on the
taskbar.


[shellwrangler]: www.shellwrangler.com
