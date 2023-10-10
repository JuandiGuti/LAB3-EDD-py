class LZWCompression:

    def __init__(self, dictionary_size=256):
        self.dictionary = dict()
        self.reverse_dictionary = dict()
        for i in range(dictionary_size):
            self.dictionary[chr(i)] = i
            self.reverse_dictionary[i] = chr(i)
        self.max_dictionary_size = dictionary_size

    def compress(self, string):
        compressed = []
        current_string = ""
        for c in string:
            if current_string + c not in self.dictionary:
                compressed.append(self.dictionary[current_string])
                if len(self.dictionary) < self.max_dictionary_size:
                    self.dictionary[current_string + c] = len(self.dictionary)
                current_string = c
            else:
                current_string += c
        if current_string:
            compressed.append(self.dictionary[current_string])
        return compressed

    def decompress(self, compressed):
        decoded = self.reverse_dictionary[compressed[0]]
        previous_string = decoded
        for code in compressed[1:]:
            if code in self.reverse_dictionary:
                current_string = self.reverse_dictionary[code]
            else:  # Handle special case where current string is previous string + previous string[0]
                current_string = previous_string + previous_string[0]
            decoded += current_string
            # Add to dictionary
            if len(self.reverse_dictionary) < self.max_dictionary_size:
                self.reverse_dictionary[len(self.reverse_dictionary)] = previous_string + current_string[0]
            previous_string = current_string
        return decoded
