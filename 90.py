#modular nama terpajang

def terpanjang(listnama):
    jlnama = []
    for i in listnama:
        i = len(i) 
        jlnama.append(i)
        
    max_ang = 0
    
    for j in jlnama:
        if j >= max_ang:
            max_ang = j
            
    theindex = jlnama.index(max_ang)
            
    return listnama[theindex]

print(terpanjang(["akuhhh", "kamutuhyahile", "buiid"]))
