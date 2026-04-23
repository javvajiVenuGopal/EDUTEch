from app.notifications.models import Notification
from app.notifications.ws_manager import manager


def create_notification(db, user_id, title, message):

    notification = Notification(
        user_id=user_id,
        title=title,
        message=message
    )

    db.add(notification)
    db.commit()

    # realtime websocket push
    manager.send_to_user_sync(
        user_id,
        {
            "title": title,
            "message": message
        }
    )