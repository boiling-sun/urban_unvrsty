"""
Task

In this kata you have to create a function that given an array of words returns another array 
with all the words that have been stored in the magic music box in the correct order.

A word can be stored in the magic music box when it contains the musical note that the box 
is playing at each moment. When a word is stored, the music box starts to play the next note, and so on.

The function must try to store every word from the input if possible, 
even if it means to retry some words that didn't fitted previuosly.

If there are no more words in the input that can be stored in the box, the function should stop 
and return the array with the stored words in the order they have been stored.

Rules

The same word cannot be stored more than once.
The magic music box plays the musical notes over and over, in a cyclic infinite loop.
If a word cannot be stored, it does not mean it could not be stored in the future with the appropiate note.
You don't have to verify the word, you only have to check that it contains the musical note with all its letters together 
(i.e. SOLAR would be a valid word but SOCIAL wouldn't).
The musical notes are represented in the european solfège format (DO, RE, MI, FA, SOL, LA, SI).
The method must return an empty array if there are no words present inside the array.

Example

Given the input array ["DOWN","PLANE","AMIDST","REPTILE","SOFA","SOLAR","SILENCE","DOWN","MARKDOWN"]

The function flow should be:

As the first musical note is DO, the word DOWN fits, and is stored inside the box.

The next note is RE, and iterating the array, the next word that fits is REPTILE.

The next note is MI, but if we continue in the array, we don't find any word that fits, 
so we should try again from the begining. This time, we find AMIDST, which fits.

The flow continues like this for the next musical notes (FA, SOL, LA, SI). At this point, 
our temporal resulted array looks like this: ["DOWN", "REPTILE", "AMIDST", "SOFA", "SOLAR", "PLANE", "SILENCE"]

The next note is DO again, because the music box never stops playing notes. Following the array, 
we find the word DOWN. The word itself fits with the note, but as long as it is forbidden to repeat words, 
we have to omit it. The next word that fits is MARKDOWN, we store it and continue.

The next note is RE, but this time, searching a fitting word, we end doing a complete iteration over 
the array with finding any, so the function ends and return the definitive array solution: 
["DOWN","REPTILE","AMIDST","SOFA","SOLAR","PLANE","SILENCE","MARKDOWN"]
"""


from itertools import cycle, islice


def main():
    input_array = ["DOWN","PLANE","AMIDST","REPTILE","SOFA","SOLAR","SILENCE","DOWN","MARKDOWN"]
    print(magic_music_box(input_array))
    print(magic_music_box(['DOWN', 'AMIDST', 'SOFA', 'FACTION'])) 

def magic_music_box(words):
    sorted_words = []
    flag = True
    notes = infinite_generator(['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'])
    for note in notes:
        if not len(words) or not flag:
            return sorted_words
        flag = False
        for i, word in enumerate(words):
            if note in word:
                sorted_words.append(word)
                words = words[i:] + words[:i]
                words = remove_same_word(words, word)
                flag = True
                break
         
def infinite_generator(array):
    while True:
        for item in array:
            yield item

def remove_same_word(array, word):
    for _ in range(array.count(word)):
        array.remove(word)
    return array


if __name__ == '__main__':
    main()