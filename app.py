from includes import functions
from includes import constants
from datetime import datetime

#Create an array of the texts and URLs as well so that they are looped through in the test.
text_url_array = {
    constants.ABOUT_TEXT: constants.ABOUT_URL,
    constants.PORTFOLIO_TEXT: constants.PORTFOLIO_URL,
    constants.SERVICES_TEXT: constants.SERVICES_URL,
    constants.CONTACT_TEXT: constants.CONTACT_URL,
    constants.HOME_TEXT: constants.HOME_URL 
}

#Try and loop through an array 
for test_index, (test_name, test_url) in enumerate(text_url_array.items(), start=1):
    #Call the function that it to perform the actual test
    test_results = functions.test_click_item(constants.TEST_URL,test_url, test_name)
    print(f"All tests have been completed. Please check the log file for details. {test_results['status']}")

    #Create a log file to hold the test results. The log file will be created in the logs directory with a timestamp in the filename.
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    lines_of_text = [
        f"TIMESTAMP: {now.strftime('%Y-%m-%d %H:%M:%S')}\n",
        f"LEVEL: {'INFO' if test_results['status'] == 'PASS' else 'ERROR'}\n",
        f"TEST ID: TC-{test_index:02d}\n",
        f"CLICKED LINK: \"{test_name}\" \n",
        f"EXPECTED RESULT: URL is {test_url}\n",
        f"ACTUAL RESULT: URL is {test_results['actual_url']}\n",
        f"STATUS: {test_results['status']}\n",
        f"DURATION: {test_results['duration']:.1f} s\n",
        f"\nRUN SUMMARY:\n",
        f"Page title: {test_results['page_title']}\n",
        f"URL: {test_results['actual_url']}\n",
        f"Browser and version: {test_results['browser']}\n",
        f"Error message: {test_results['error_message'] or 'None'}\n",
        f"----------------------------------------\n"
    ]

    #Write the lines of text to a log file
    with open(f"logs/LOG_FILE_{timestamp}.txt", "w", encoding="utf-8") as file:
        file.writelines(lines_of_text)

#Close the test activities after the test
print(f"End of test for all items. Closing the browser now...")
functions.close_browser()
