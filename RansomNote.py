# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    mag_dict = {}
    for char in magazine:
        if char in mag_dict:
            mag_dict[char] += 1
        else:
            mag_dict[char] = 1
                
    for char in ransomNote:
        if char not in mag_dict or mag_dict[char] <= 0:
            return False
        else:
            mag_dict[char] -= 1
    return True
