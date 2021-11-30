# Android Study Jams Badge Scraper
A script that scrapes badges and displays completion details of participant for android study jams using selenium and beautiful soup.

It takes participant details from Participant_Details.csv file and outputs data into Participant_Completion.csv file. 


# Screenshots of CSV Files

*-> Contents of Participant_Details.csv file*

![details](https://user-images.githubusercontent.com/62807226/144016029-e8b03c4b-af31-4196-a8a7-1cdf391e8710.png)


*-> Contents of Participant_Completion.csv file*

![completion](https://user-images.githubusercontent.com/62807226/144016313-a072fa86-c8b2-4372-994a-1f742dd98750.png)

# Installation Instructions

1. Make sure Python 3 and pip is installed
2. Download the chromedriver according to your chrome version and OS (Windows or Linux)
3. Install the required libraries in your terminal using the following commands:
 
`pip install selenium`

`pip install beautifulsoup4`

`pip install pandas`

4. Execute the script using the following command:

`python3 badge_scraper.py`

 

