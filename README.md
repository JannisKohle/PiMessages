# PiMessages

A messaging tool for the terminal; written in C, Python and Node.js

*Note: Please do only use this tool for fun, becasue it's made by a stupid 12 year old.*

## How PiMessages works:

First, you need to create an account with an unique username and secure password.
Then, you can write messages to other users, and if you don't want to get any more
messages from them, you can ignore them.
If you want to try PiMessages out yourself, continue reading in the ```Setup``` section.

## Usage of the CLI:

### Creating a new account:

You will automatically get logged in after creating a new account.

- ```pimessages signup```
- ```pimessages signup -un {username} -pw {password}```
- ```pimessages signup --username {username} --password {password}```

### Logging in with an existing account:

- ```pimessages login```
- ```pimessages login -un {username} -pw {password}```
- ```pimessages login --username {username} --password {password}```

### Writing and recieving messages:

1. Writing a single message:

- ```pimessages send {username}```
- ```pimessages send {username} -m {message}```
- ```pimessages send {username} --message {message}```

2. Interactive chat mode:

In ```interactive mode``` you can see the latest messages from you and the other
user, and it gets updated whenever you or the other user write a new message.

- ```pimessages chat {username}```

### Ignoring a user:

If somebody is getting on your nerves, you can ignore, and un-ignore him with these commands:

- ```pimessages ignore {username}```
- ```pimessages ignore {username} -y```
- ```pimessages ignore {username} --yes```

- ```pimessages unignore {username}```
- ```pimessages unignore {username} -y```
- ```pimessages unignore {username} --yes```

### Other useful commands:

- See all unread messages: ```pimessages inbox```
- Get info about account: ```pimessages account-info```
- Change your current password: ```pimessages pw```

## Usage of the Rest Api:

...

## Setup:

...
