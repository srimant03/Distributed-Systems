# YouTube Server

This part of assignment consists of three processes:

1. `YoutubeServer.py`: Sets up and runs the YouTube server, capable of handling login, subscription/unsubscription requests from users, and new video uploads from YouTubers.

2. `Youtuber.py`: Represents the YouTuber service, allowing YouTubers to publish videos.

3. `User.py`: Represents the User service, enabling users to log in, subscribe/unsubscribe to YouTubers, and receive notifications for new videos.

## Running the code

This README file containing all necessary steps to run the program.

### a. YoutubeServer.py

This file sets up and runs the YouTube server. It is now ready to consume the following two messages:

- Login and Subscription/Unsubscription Requests from Users.
- New video upload from users.

Note that the server should be able to simultaneously consume messages from YouTubers and Users.

#### Methods:

- `consume_user_requests()`: Starts consuming Login and Subscription/Unsubscription Requests from Users.
    - Prints "<username> logged in" whenever a user logs in.
    - Prints "<username> <subscribed/unsubscribed> to <youtuberName>" whenever a user updates their subscriptions.

- `consume_youtuber_requests()`: Starts consuming video upload requests from YouTubers.
    - Prints "<YouTuberName> uploaded <videoName>" whenever a YouTuber uploads a new video.

- `notify_users()`: Sends notifications to all users whenever a YouTuber they subscribe to uploads a new video.

#### Example:

To run the server:
```
$ python YoutubeServer.py
```


### b. Youtuber.py

This file represents the Youtuber service. It takes two command line arguments: the YouTuber's name and the video it wants to publish.

#### Methods:

- `publishVideo(youtuber, videoName)`: Sends the video to the YouTube server.
    - The YouTube server adds a new YouTuber if the name appears for the first time else; it adds the video to the existing YouTuber.
    - Prints "SUCCESS" message when the video is received by the YouTube server.

#### Example:

To run the Youtuber service to publish a video:
```
$ python Youtuber.py TomScott After ten years its time to stop weekly videos.
```


(The Youtuber name should not contain spaces, but the name of the video can contain spaces)

### c. User.py

This file represents the User service. It contains either 1 or 3 command line arguments. The first argument is the name of the user. If the user wants to subscribe or unsubscribe, the second argument is 's' or 'u', respectively, and the third argument is the name of the YouTuber. (Second and third arguments are optional)

#### Methods:

- `updateSubscription`: Sends the subscription/unsubscription request to the YouTube Server.
    - Prints "SUCCESS" message after completing the request.

- `receiveNotifications`: Receives any notifications already in the queue for the users' subscriptions and starts receiving real-time notifications for videos uploaded while the user is logged in.
    - Prints "New Notification: <YouTuberName> uploaded <videoName>"

#### Examples:

To log in, subscribe to a YouTuber, and receive notifications:
```
$ python User.py username s TomScott
```

To log in, unsubscribe to a YouTuber, and receive notifications:
```
$ python User.py username u TomScott
```
To log in and receive notifications:
```
$ python User.py username
```

--- 
