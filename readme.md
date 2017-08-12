# Mediasite API Example

This repository is intended to provide an example of using the Mediasite API with Python. When the example runs it will ask for a recorder name, search for that recorder using the Mediasite API, then return the serial number associated with the recorder name you provided.

## Prerequisites and Documentation

Before you get started, make sure to install or create the following prerequisites:

* Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Python Requests Library (non-native library used for HTTP requests): [http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)
* A Mediasite user with operations "API Access" and "Manage Auth Tickets" (configurable within the Mediasite Management Portal)
* A Mediasite API key: [https://&lt;your-hostname&gt;/mediasite/api/Docs/ApiKeyRegistration.aspx](https://&lt;your-hostname&gt;/mediasite/api/Docs/ApiKeyRegistration.aspx)

Mediasite API documentation can be found at the following URL (change the bracketed area to your site-specific base domain name): [http://&lt;your-hostname&gt;/mediasite/api/v1/$metadata](http://&lt;your-hostname&gt;/mediasite/api/v1/$metadata)

Also worth noting, as stated in the documentation, the Mediasite API makes heavy use of the ODATA standard for some requests (including the demo performed within this repo). For more docuemntation on this standard reference the following URL: [http://www.odata.org/documentation/odata-version-3-0/url-conventions/#requestingdata](http://www.odata.org/documentation/odata-version-3-0/url-conventions/#requestingdata)

## File Descriptions

- **mediasite_web_api_client.py**
A web api client used to connect to the system. This is Python class file used for making connections to the Mediasite system.

- **.mediasite_api_config_sample**
A file which uses JSON to store credentials used by the mediasite_web_api_client.py Python class for making web API connections to Mediasite. The file as it stands in this repository is a template and must be modified to be named ".mediasite_api_config" and filled in with your site-specific information.

- **mediasite_api_example.py**
A file which makes use of the  mediasite_web_api_client.py Python class for making web API connections to Mediasite. This example  gathers a recorder name, requests information from the Mediasite system on the gathered recorder name, and returns the recorder serial number associated with the gathered recorder name.

## Usage

1. Ensure prerequisites outlined above are completed.
2. Fill in necessary &lt;bracketed&gt; areas in .mediasite_api_config_sample specific to
2. Rename .mediasite_api_config_sample to  .mediasite_api_config (removing the text "_sample")
3. Run mediasite_api_example.py with Python 3.x

### Sample Usage

    C:\>python "C:\mediasite_api_example\mediasite_api_example.py"
    Enter recorder name: SAMPLE-RECORDER-NAME
    04/28/2017 - 11:04:01 AM - INFO - Finding ID of recorder
    04/28/2017 - 11:04:01 AM - INFO - Starting new HTTPS connection (1): <your-hostname>
    04/28/2017 - 11:04:01 AM - INFO - SAMPLE-RECORDER-NAME serial number: 002-XXXXXXX
    04/28/2017 - 11:04:01 AM - INFO - Example finished!

## License
MIT - See license.txt
