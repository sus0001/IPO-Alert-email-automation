from classes import MerolaganiScraper, EmailAutomation
import copy


merolagani = MerolaganiScraper()
posted_date = merolagani.ipo_announce_date()
latest_ipo_news = merolagani.ipo_news()
old_update = copy.deepcopy(latest_ipo_news)
email_receivers = ["rockin_sushil@hotmail.com", "gunz19able@gmail.com", 'sushil.bhandari002@gmail.com']


ipo_alert_email = EmailAutomation()


for receiver in email_receivers:
    ipo_alert_email.send_email(latest_ipo_news, receiver, posted_date)