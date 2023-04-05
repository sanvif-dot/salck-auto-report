import requests


def execute(message, channel, file_bytes, file=None, file_type=None, title=None):
    token = 'xoxb-4586634390964-5065863001124-rKLXJYxaW0Ckboo9brgC5zm8'

    slack_token = token
    slack_channel = channel
    slack_icon_emoji = ':bar_chart:'
    slack_user_name = 'Automated Reporting'

    with open(file_bytes, "rb") as image:
        send = requests.post(
            'https://slack.com/api/files.upload',
            {
                'token': slack_token,
                'icon_emoji': slack_icon_emoji,
                'username': slack_user_name,
                'filename': file,
                'channels': slack_channel,
                'filetype': file_type,
                'initial_comment': message,
                'title': title
            },
            files={'file': image.read()})

    if not send.json()['ok']:
        raise Exception(
            f"Error send report to channel {channel} with error messages : \n{send.json()['error']}")
    else:
        print(f"Message send success to channel : {channel}")

if __name__ == '__main__':
    execute('test', '#auto_report', '/Users/sanvi/Documents/project-1/automate_reports/output/sales_per_month.png', file=None, file_type=None, title=None)
