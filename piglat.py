vowels = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U')


def translate_word(word):
    end = 0
    if word[0] in vowels:  
        return word + "hay"     
    else:
	for i in len(word):
	    if word[i] in vowels:
		break
	    else:
		end=i
        return word[end+1:] + word[0:end] + "ay"    

def translate(sentence):
    words = sentence.split(' ')
    pig = ""   
    for word in words:
        pig = pig + translate_word(word) + " "  

    return pig


sentence = input( "Enter sentence")

print(translate(sentence))