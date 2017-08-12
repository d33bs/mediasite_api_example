#Mediasite API Example
#Intended to provide demonstration of mediasite API utilization using pre-built
#client to communicate with system. Example takes recorder name, searches for
#information, then returns serial number.
#Pre-reqs: Python 3.x and requests library
#License: MIT - see license.txt

import os
import logging
import json
import sys
import datetime
import urllib.request
import mediasite_web_api_client as mediasite_web_api_client

if __name__ == "__main__":

    #gather our runpath
    run_path = os.path.dirname(os.path.realpath(__file__))

    #log file datetime
    current_datetime_string = '{dt.month}-{dt.day}-{dt.year}_{dt.hour}-{dt.minute}-{dt.second}'.format(dt = datetime.datetime.now())
    logfile_path = run_path+'/logs/mediasite_api_example_'+current_datetime_string+'.log'

    #logger for log file
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging_datefmt = '%m/%d/%Y - %I:%M:%S %p'
    logging.basicConfig(filename=logfile_path,
        filemode='w',
        format=logging_format,
        datefmt=logging_datefmt,
        level=logging.INFO
        )

    #logger for console
    console = logging.StreamHandler()
    formatter = logging.Formatter(logging_format,
    datefmt=logging_datefmt)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    #open config file with api key/secret information
    api_config_file = open(run_path+"/"+".mediasite_api_config")
    api_data = json.load(api_config_file)

    #create mediasite api client
    client = mediasite_web_api_client.client(
        api_data["base_url"],
        api_data["api_secret"],
        api_data["api_user"],
        api_data["api_pass"]
        )

    #gather a recorder name
    input_recorder_name = input("Enter recorder name: ")

    #reference the following url for mediasite documentation:
    #http://<your-hostname>/mediasite/api/v1/$metadata

    #reference odata standards for more information on additional attributes
    #http://www.odata.org/documentation/odata-version-3-0/odata-version-3-0-core-protocol/

    #perform request for single recorder information
    logging.info("Finding ID of recorder")
    report_result = client.do_request("get", "Recorders", "$top=1&$filter=Name eq '"+input_recorder_name+"'", "")

    #check that we find results from the given name (will return count > 1 with results)
    if json.loads(report_result)["odata.count"] != "0":
        #find the serial number from the json results
        input_recorder_serial = json.loads(report_result)["value"][0]["SerialNumber"]

        #display and log our serial number associated with the recorder name
        logging.info(input_recorder_name+" serial number: "+input_recorder_serial)

    #return an error message when the return count is 0
    else:
        logging.error("Unable to find recorder information.")

    logging.info("Example finished!")
