# Automation Report using Slack

Slack is a popular communication and collaboration platform used by businesses and organizations of all sizes. 

Goal :
1. Create Sales visualization using bar chart
2. Send to Slack channel using API
3. All team member can see the result easier  

Steps :
1. `pip install -r requirements.txt`
2. Create ETL process on transformation folder
3. Extract all csv file to folder data and append into one file
4. Read append file and clean the not valid column, null date, and create a new column for sales(total price)
   Also group by product and month all data using pandas library
5. Import dotenv python library to hide your Slack Token on send to slack folder
6. Create `.env` file in directory `plugins/send_to_slack`
7. Write `.env` with your Slack Token (SLACK_TOKEN='your-slack-token')
8. Create bar chart using matlotlib for group by product and group by month and save them to output folder 
   Write send to slack to.execute to send graphs to slack channel

