from welcome.models import Users, Notification
import random


def send_notification(notification, to):
    nid_id = random.randint(100, 999999)
    c = Notification(email_id=to, notification=notification, nid=nid_id)
    c.save()
