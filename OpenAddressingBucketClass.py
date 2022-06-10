# OpenAddressingBucket represents a bucket with a key and a value
class OpenAddressingBucket:
    def __init__(self, bucket_key=None, bucket_value=None):
        self.key = bucket_key
        self.value = bucket_value

    def isEmpty(self):
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


# Initialize two special bucket types: empty-since-start and empty-after-removal
OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()