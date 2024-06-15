import pika
import sys
import json

def create_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='34.131.86.186',  # changes everytime so replace it with external ip after starting vm
            credentials=pika.PlainCredentials('ElderDragon', 'chirag') 
        )
    )
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    return connection, connection.channel()

def update_subscription(username, action, youtuber):
    connection, channel = create_channel()
    subscribe_action = action == 's'
    message = {
        'user': username,
        'youtuber': youtuber,
        'subscribe': subscribe_action
    }
    channel.queue_declare(queue='user_requests')
    channel.basic_publish(exchange='', routing_key='user_requests', body=json.dumps(message))
    print("Subscription request sent: SUCCESS")
    channel.close()
    connection.close()

def listen_for_notifications(username):
    connection, channel = create_channel()
    notification_queue = f'{username}_notifications'
    channel.queue_declare(queue=notification_queue)

    def callback(ch, method, properties, body):
        print(f"{body.decode()}")

    channel.basic_consume(queue=notification_queue, on_message_callback=callback, auto_ack=True)
    print(f"Listening for notifications for {username}...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("logging out...")
    finally:
        channel.stop_consuming()
        channel.close()
        connection.close()

if __name__ == "__main__":
    username = sys.argv[1]
    if len(sys.argv)>3:
        action= sys.argv[2]
        youtuber=sys.argv[3]
    else:
        action=youtuber=None
    if action and youtuber:
        update_subscription(username, action, youtuber)

    listen_for_notifications(username)
