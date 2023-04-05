# Automasi Report Dashboard

Goal :
1. Data Sales Bulanan yang di output
2. Send ke Slack channel (platform kolaborasi team)
3. Goal : Team terkait bisa melihat report regular bulanan

Steps :
1. `pip install -r requirements.txt`
2. Buatlah `.env` file di dalam directory `plugins/send_to_slack`
3. Isilah `.env` dengan konten berikut SLACK_TOKEN='your-slack-token'
4. Jalankan `python report.py` untuk mengirim grafik ke Slack Channel

Problems :

MAC dan Linux user :
1. Jika devicemu MAC atau Linux dan menemui Python not found coba jalankan berintah berikut :
    `which python` atau `which python3`
2. Lalu check apakah path directory tersebut sudah ada di PATH environment variable dengan cara :
    `echo $PATH`
3. Jika belum ada maka tambahkan dengan cara `export PATH=$PATH:/path/to/python`

Windows :
1. https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows
