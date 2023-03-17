class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title ,message_body, urgent=False):  # added message_title for
        # more info
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_title (str): The title of the message.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N):
        """Read a user's inbox.

        Args:
            username (str): The user username.
            N (int): The number of messages to read.

        Returns:
            list: A list of the last N messages in the user inbox.

        Raises:
            KeyError: If the user does not exist.

        Examples:
            After creating a PO box and sending 2 letters,
            the recipient should have 2 messages in the inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> po_box.send_message('a', 'b', 'Hello!', 'Hello!')
            1
            >>> po_box.send_message('a', 'b', 'Hello again!', 'Hello again!')
            2
            >>> len(po_box.boxes['b'])
            2
            >>> po_box.read_inbox('b', 1)
            [{'id': 2,'title': 'Hello again!','body': 'Hello again!', 'sender': 'a'}]
        """
        if  username not in self.boxes:
            raise KeyError("User does not exist")
        user_box = self.boxes[username]
        if N == 0:
            return user_box

        if N > len(user_box):
            N = len(user_box)
        return user_box[:N]

    def search_inbox(self, username, keywords):
        """Search a user's inbox.

        Args:
            username (str): The user username.
            keywords (str): The keywords to search for.

        Returns:
            list: A list of the messages that contain the keywords.

        Raises:
            KeyError: If the user does not exist.

        Examples:
            After creating a PO box and sending 2 letters that contain the keyword 'Hello',
            the recipient should have 2 messages that contain the keyword 'Hello' in the inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> po_box.send_message('a', 'b', 'Hello!', 'Hello!')
            1
            >>> po_box.send_message('a', 'b', 'Hello again!', "How's it going?")
            2
            >>> len(po_box.boxes['b'])
            2
            >>> po_box.search_inbox('b', 'Hello')
            [{'id': 1, 'title': 'Hello!','body': 'Hello!', 'sender': 'a'},
             {'id': 2, 'title': 'Hello again!','body': "How's it going?", 'sender': 'a'}]

        """
        if username not in self.boxes:
            raise KeyError("User does not exist")

        user_box = self.boxes[username]
        return [message for message in user_box if keywords in message['body'] or keywords in message['title']]
