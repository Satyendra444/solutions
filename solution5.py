class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        slow = self
        fast = self

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

first = Song("Hello")
second = Song("Eye of the tiger")
first.next_song(second)
second.next_song(first)
print(first.is_in_repeating_playlist()) 
print(second.is_in_repeating_playlist()) 
