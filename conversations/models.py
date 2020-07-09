from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Conversation Model Define"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for participant in self.participants.all():
            usernames.append(participant.username)
        return ", ".join(usernames)

    def count_message(self):
        return self.message_set.all().count()

    count_message.short_description = "Number Of Message"

    def count_participants(self):
        return self.participants.all().count()

    count_participants.short_description = "Number Of participants"


class Message(core_models.TimeStampedModel):
    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.message}"
