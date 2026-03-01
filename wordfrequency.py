from pathlib import Path
import sys



def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:     # with slik at filn lukkes automatisk, "r" read mode, as f: variabelnavn, la til utf-8 elller fikk jeg feil
        lines = f.read().splitlines()   # lines = variabelnavn, leser hele filen, deler teksten opp en streng pr linje
    
    return lines


def lines_to_words(lines):
    symbol = ".,:;?!"                           # Variabel med symboler som skal fjernes
    words = []                                  # En tom liste 
    
    for line in lines:                          # Går gjennom hver linje i listen lines
        parts = line.split()                    # Splitter opp strengen ved "whitespace"
        
        for elementer in parts:                 # Går gjennom hvert ord i parts
            removed = elementer.strip(symbol)   # Fjerner "ikke ord" som definert over
            removed = removed.lower()           # Gjor ord om til små bokstaver
            
            if removed != "":                   # Hopper over evt tomme ord etter fjerning av tegn
                words.append(removed)           
    
    return words



def compute_frequency(words):
    frequency = {}                                          # tom ordbok
    
    for element in words:
        frequency[element] = frequency.get(element, 0) + 1  # Nåværende telling for ordet(0 om første gang),
                                                            # legg til 1, lagre tilbake i frequency
    return frequency



FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    filtered = {}
    
    for word, count in frequency_table.items():         #henter ord og hvor mange gnager det forekommer (ett og ett ord)
        if word not in FILL_WORDS:                      #sjekekr at ordet ikke er i filler listen
            filtered[word] = count                      #legger til ord og antall i ny ordbok
    
    return filtered


def largest_pair(par_1, par_2):
    nummer_1 = par_1[1]                  # henter antall fra første tuple
    nummer_2 = par_2[1]                  # andre tuple
    
    if nummer_1 >= nummer_2:             # om første er større ller lik
        return par_1
    else:
        return par_2
    


def find_most_frequent(frequency_table):
    if not frequency_table:
        return None
    
    most_used = ("", -1)                                    # Startverdi
    
    for word, count in frequency_table.items():             # går gjennom alle (ord, antall) par
        most_used = largest_pair(most_used, (word, count))  # sammenliger nåværende høyeste med nytt (ord, antall)
    
    return most_used[0]                                     # Returnere selve ordet (index 0, (1 = tall))


############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()