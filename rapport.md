# Rapport SAE Crypto

GRUSON--DELANNOY Jules

DOMINGUEZ Ugo

THOMAS Lucas

PERDIEUS Antony

## Sujet :

Au cours de cette SAE, nous avions au total 3 messages à déchiffrer. Chaque message déchiffré nous fournissait un indice nécessaire pour déchiffrer le suivant. Pour ce faire nous devions créer un programme Python.

Tous les programmes utilisés pour décrypter les messages sont retrouvables dans l’archive associée à ce rapport.

---

## Premier code :

*Le message était :*

<aside>

OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'
UZPUHGXSMNXQ EQODQF PQ OQFFQ
ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ
CGU FDAGHQDM XM OXQ?

</aside>

Étant donné le manque d’information concernant une quelconque clé, nous sommes partis du principe qu’il s’agissait du code césar. Il s’agit d’un code utilisé par Jules César pour crypter les messages qu’il transmettait, pour ce faire il décale chacune des lettres du mot d’une position n dans l’alphabet. Par exemple avec un décalage de n=3, le mot “informatique” devient "lqirupdwltxh”.

Suite au décryptage de ce premier message nous obtenons ce résultat :

<aside>

CE TEXTE D'APPARENCE ANODINE CONTIENT L'
INDIVULGABLE SECRET DE CETTE
NOUVELLE ENIGME. SEREZ-VOUS CELUI OU CELLE
QUI TROUVERA LA CLE?

</aside>

Le message est clair, la clé est contenue dans celui-ci, nous avons donc créé une fonction pour obtenir les premières lettres de chacune des lignes puisqu’elles semblaient agencées d’une manière particulière. Ce qui nous a retourné “CINQ”.

---

## Deuxième code :

*Le message était :*

<aside>

UCVLGH YUU BEQEMF TG ORETORI RIVDXQA
QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O
KEORBB

</aside>

Nous avions donc obtenu grâce au déchiffrement du premier message la clé “CINQ”, nous avions donc chercher parmi les systèmes de cryptage que nous avions vu un système fonctionnant avec un clé. Le chiffrement de Vernam était donc évident. Il s’agit d’un chiffrement qui utilise une clé unique car elle ne doit pas être réutilisée et doit être générée aléatoirement, seulement elle doit également être de même longueur que le message ce qui n’est pas le cas ici, nous avons donc répété cette clé en respectant les espaces puisqu’ils ne sont pas chiffré.

Après déchiffrement le résultat est le suivant :

<aside>

SUIVEZ LES TRACES DE GEORGES PAINVIN
AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M
CRYPTO

</aside>

On peut constater que le message est composé de trois lignes qui ont l’air de n’avoir rien à voir.

La première est plutôt claire, il s’agit d’un indice. Suite à une recherche Google, nous apprenons que Georges Painvin est un cryptanalyste qui a servi durant la Première Guerre Mondiale et qui a notamment réussi en 1918 à décrypter le code ADFGVX, un code de chiffrement allemand complexe. Il nous faut donc utiliser le code ADFGVX qui fonctionne avec une grille et une clé.

De ce fait la deuxième ligne prend tout son sens puisqu’elle nous permettra de compléter la grille de chiffrement qui sera utilisée.

Et la troisième ligne est donc la clé nécessaire au chiffrement/déchiffrement.

---

## Troisième code :

Pour ce dernier message nous avions des informations complémentaires qui nous étaient apportés:

<aside>

Vous avez sûrement compris que le code utilisé pour le 3eme message est le chiffre ADFGVX. Voici quelques informations complémentaires afin de vous aider dans votre déchiffrement.

Le message en clair contenait des caractères spéciaux (espace, retour à la ligne, chiffres etc) qui ont été conservé lors du chiffrement.

De plus, des espaces additionnels ont été rajouté à la fin après la substitution avec la matrice. Ce remplissage a pour but d'obtenir un message dont la taille est un multiple de la taille de la clé (en l'occurrence 6 pour la clé "CRYPTO").

</aside>

*Le message était :*

<aside>

AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX
VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG
F VGVXVGGD
VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V
X VVGGGGD
XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG

</aside>

Comme expliqué précédemment le chiffrement utilisé est le chiffrement ADFGVX.

Il est produit à partir d’une grille à double entrée sur laquelle est placés sur chacun des côtés ADFGVX. Il faut ensuite placer des caractères dans un ordre défini au sein de cette grille, ici nous utilisons la deuxième ligne du message décrypté précédemment. 

Ensuite, les lettres sont chiffrées en indiquant d’abord l'abscisse, puis l'ordonnée, par exemple, AV, VX et ainsi de suite.

Après avoir établi le programme python associé, nous obtenons comme résultat ce message :

<aside>

FELICITATIONS! VOUS ALLEZ BIENTOT RECEVOIR UN CODE QUI VOUS SERVIRA PAR LA
SUITE.
GARDEZ-LE PRECIEUSEMENT!
VOICI LE CODE A RENTRER SUR CELENE:
KU4VQMKESD

</aside>