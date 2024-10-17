
def creation_matrice_ADFGVX(alphabet):
    matrice_ADFGVX = []
    for i in range(6):
        matrice_ADFGVX.append([])
        for j in range(6):
            matrice_ADFGVX[i].append(alphabet[j+i*6])
    return matrice_ADFGVX


def traitement_message(message):
    res=""
    for el in message:
        if el =="\n":
            res+="n"

        else:
            res+=el

    return res


def decryptage_painvin(message, alphabet, key):
    lettres = traitement_message(message)
    matrice_ADFGVX = creation_matrice_ADFGVX(alphabet)

    matrice_key = []
    nb_ligne = len(lettres)//len(key)
    for i in range(nb_ligne):
        matrice_key.append([])
        for j in range(len(key)):
            matrice_key[i].append(lettres[j+i*(len(key))])
    print(matrice_key)

m = '''AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX
VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG
F VGVXVGGD
VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD
XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG'''

decryptage_painvin(m, "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M", "CRYPTO")
