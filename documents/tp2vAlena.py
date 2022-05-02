# Nom: Jade Adonis et Mario Sekpona
# Matricule: 20226410 et 20179552 respectivement
#
# Ce travail pratique permet de créer une application web afin de jouer au jeu 
# de paires avec une interface graphique en HTML. Le compte à rebours est 
# affiché dans une boîte sous le score et à  chaque seconde, le nombre de 
# secondes restantes est mis à jour dans la boîte.


#Ce texte correspond au style élémentaire du design du jeu
style ="""<style>
table#jeu {
    border-spacing: 10px;
    border-collapse: separate;
    display: inline-block;
}
table#jeu td {
    background-color: #d0d0d0;
    border:1px solid #008CBA;
    width: 100px;
    height: 120px;
    background-position: center;
    background-size: cover;
}

.menu-element {
  margin: 10px;
  border:1px solid #008CBA;
  width: 100%;
}

.level-button {
  padding: 15px 30px;
  background-color: #008CBA;
  opacity: 0.7;
  border: none;
  color: white;
  text-align: center;
  font-size: 16px;
}

.active-level-button {
  opacity: 1 !important;
}

#score-box {
  padding: 5px 5px;
  text-align: center;
}

#score-text {
  font-family: OCR A Std, monospace;
}

.score-title {
  font-weight: bold;
}

.texte-meilleur {
  font-size: small;
}

.menu {
  display: inline-block;
  width: 150px;
}
</style>
"""


#Le texte suivant correspond à la table html
jeuFormat = """
<div>
  <table id="jeu">
    <tr>
      <td id="carte0"></td>
      <td id="carte1"></td>
      <td id="carte2"></td>
      <td id="carte3"></td>
    </tr>
    <tr>
      <td id="carte4"></td>
      <td id="carte5"></td>
      <td id="carte6"></td>
      <td id="carte7"></td>
    </tr>
    <tr>
      <td id="carte8"></td>
      <td id="carte9"></td>
      <td id="carte10"></td>
      <td id="carte11"></td>
      
    </tr>
  </table>
"""

#La variable représente la partie menu du jeu
menu ="""
  <div class="menu">
    <div id="score-box" class="menu-element">
      <div class="score-title">SCORE</div>
      <div id="score-text">100</div>
    </div>
    <button id="niveauFacile" class="level-button menu-element active-level-button">
      <b>Facile</b><br>
      <div class="texte-meilleur">Meilleur: -</div>
    </button>
    <br>
    <button id="niveauMoyen" class="level-button menu-element">
      <b>Moyen</b>
      <br>
      <div class="texte-meilleur">Meilleur: -</div>
    </button>
    <br>
    <button id="niveauDifficile" class="level-button menu-element">
      <b>Difficile</b>
      <br>
      <div class="texte-meilleur">Meilleur: -</div>
    </button>
  </div>
</div>  """









#Cette fonction prend le lien et retourne la balise link avec comme attribut
#href le lien en paramètre
def imgPreload(lien):
    return '<link rel="preload" as="image" href="' + lien+'">'




# Cette fonction prend un texte HTML en parametre et retourne le 
#dans une balise table 

def tableHTML(contenu): return '<table>' + contenu + '</table>'

# Cette fonction  prend  en parametre un texte et retourne
# un  texte HTML équivalent à une balise tr avec le texte comme contenu

def trHTML(contenu): return '<tr>' + contenu + '</tr>'

# Cette fonction  prend  en parametre trois textes et retourne le
# texte  de deux balises, soient img et div 
#def entree(img, valeur, nom): 
    #return img + '<div class = "centered" class="' + nom + '">'+valeur+'</div>'
    
#cette fonction retourne le contenu d'un attribut style avec le lien en 
#paramètre

def styleImage(adresseImg):
    
    return  "background-image: url("+adresseImg+"); background-position:\
     center; background-size: cover;"

#Cette fonction retorune un texte correpondant a un attribut style  
def styleColor():
    
    return ' style="background-color: #d0d0d0; background-position:\
     center; background-size: cover;"'

#Cette fonction retourne un textecorrspondant à un attribut id avec son 
#contenu

def attrId(chiffreLettre): 
    return  ' id="carte'+chiffreLettre+'"'


#Cette fonction retourne l'attribut onclick avec son contenu qui est 
#la procédure clicTd.

def attrCliqueTd(chiffreLettre):
    
    return ' onclick="clicTd(' + str(chiffreLettre) + ')"'

# Cette fonction  prend  en parametre deux textes et retourne une balise td     
def tdHTML(attr1, attr2, attr3): 
    return '<td' + attr1 + attr2+ attr3+'></td>'

# Cette fonction  prend un tableau de textes en parametre et
# retourne la concaténation  dutableau en paramètre. Ce retour correspond
#à une balise tr.
def trHTMLJoin(tab): return trHTML(''.join(tab))



# Cette fonction  prend un tableau de textes en parametre et
# retourne la concaténation  des textes du  tableau en paramètre. Ce
#retour coorepond à une balise table avec son contenu

def tableHTMLJoin(tab): return tableHTML(''.join(tab))

#Cette fonction permet de grouper par nombre de taille, 
#les éléments du tableau tab par groupe dans un tableau qui est retourné
def grouper(tab, taille):
    groupes = []
    accum = []
    for elem in tab:
        accum.append(elem)
        if len(accum) == taille:
            groupes.append(accum)
            accum = []
    if len(accum) > 0:
        groupes.append(accum)
    return groupes
#Cette fonction correspond à la table HTML. elle prend un tableau et un nombre
# et retourne une grille de taille élément.
def tableauATableHTML(tab, taille):
    return tableHTMLJoin(list(map(trHTMLJoin, grouper(tab, taille))))

# Cetteb Corrspond aux cases du jeu. elle retourn les balises td avec
# ces attributs
def caseHTML(index):
   
    return tdHTML(attrId(str(index)), styleColor(), attrCliqueTd(str(index)))

largeur = 4
hauteur1 = 3
hauteur2 = 4
hauteur3 = 5


#Cette fonction détermine le format du jeu. Exemple une grille
#de largeur par hauteur est retournée
def formatDuJeu(largeur, hauteur):
    
    return tableauATableHTML(list(map(caseHTML, list(range(largeur*hauteur)))), largeur)

##############################################################################
largeur = 4
hauteur = 3
#Tableau des liens des images
tabImages=['https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/320px-Kittyply_edit1.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Felis_silvestris_catus_lying_on_rice_straw.jpg/320px-Felis_silvestris_catus_lying_on_rice_straw.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Domestic_Cat_Face_Shot.jpg/320px-Domestic_Cat_Face_Shot.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Gato_enervado_pola_presencia_dun_can.jpg/308px-Gato_enervado_pola_presencia_dun_can.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on_snow.jpg/320px-Felis_catus-cat_on_snow.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Feral_cat_Virginia_crop.jpg/206px-Feral_cat_Virginia_crop.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Black_Cat_%287983739954%29.jpg/320px-Black_Cat_%287983739954%29.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Roo_Female_Somali_in_Cat_Caf%C3%A9_Tokyo.jpg/160px-Roo_Female_Somali_in_Cat_Caf%C3%A9_Tokyo.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/6/6e/Longhairedmunchkin.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Niobe050905-Siamese_Cat.jpeg/179px-Niobe050905-Siamese_Cat.jpeg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Charcoal_Bengal.jpg/320px-Charcoal_Bengal.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Paintedcats_Red_Star_standing.jpg/187px-Paintedcats_Red_Star_standing.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/ChausieBGT.jpg/221px-ChausieBGT.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Savannah_Cat_portrait.jpg/160px-Savannah_Cat_portrait.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Plume_the_Cat.JPG/320px-Plume_the_Cat.JPG',
  'https://upload.wikimedia.org/wikipedia/commons/e/e9/Persian_sand_CAT.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Detalhe_nariz_Osk.jpg/180px-Detalhe_nariz_Osk.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Siam_blue_point.jpg/263px-Siam_blue_point.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Felis_silvestris_silvestris.jpg/208px-Felis_silvestris_silvestris.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/f/f7/Prionailurus_viverrinus_01.jpg']



#Cette partie du code traite la partie de sélection des liens des images
#qui se trouve dans tabImages. La sélection est fait de manière aléatoire.
# n/2  d'images sont d'abord sélectionner,où n correspond au nombre de case
#dans le jeu. Ensuite les n/2 sont distribué aléatoirementde sorte à avoir
#une paire par n/2 élément. Ainsi, les n éléments sont assurés.
###############################################################################
def formerMat(x): 
    
    global largeur
    resultat =[]
    
    for _ in range(largeur):
        
        resultat.append(None)
        
    return resultat


#Cette fonction prend un nombre et uun tableau. elle selectionne aléatoirement
#les indices des éléments du tableau, les mets dans un tableau et les retourne. 
def tabIndImgChoisie(n,tab):
    a=0
    resultat=[]
    
  
    while len(resultat)!=n:
        
        a=math.floor(len(tab)*random())
        
        while a in resultat:
            a=math.floor(len(tab)*random())
        
        resultat.append(a)
            
    return resultat


tabNImg =[]


#Cette fonction permet d'aller chercher aléatoirement deux éléments d'un
#tableau pour chaque élément en paramètre.

def paireAleatoire(x):
    
    
    resultat = []
    global tabNImg  
    for _ in range(2):
        
        
        indTab = tabIndImgChoisie(1,tabNImg)
        
        resultat.append(tabNImg[indTab[0]])
        tabNImg.pop(indTab[0])
       
    return resultat  

#tabPairesAlea = list(map(paireAleatoire,tabIndImgChoisie(n,tab)))

#Cette fonction prend trois paramètres, dont deux tableaux et un chiffre
# indiquant la taille du tableau a retourné. La fonction permet de prendre 
#chaque élément du deux tableau et d'aller le mettre dans un nouveau à un 
#certain indice. les informations des indices se trouvent dans le premier 
#tableau. 
def formerTab(tabIndSel, tabIndImg, n):
    resultat = list(range(n))
    
    for i in range(n//2):
        resultat[tabIndSel[i][0]] = tabIndImg[i]
        resultat[tabIndSel[i][1]] = tabIndImg[i]
        
    return resultat
    
    
   
    
    
#Cette fonction a trois paramètres une largeur, une hauteur, 
#et un  tableau, elle retourne un tableau d'indice choisi aléatoirement du
# le tableau de lien d'images en défini plus haut.
def tabNFormatSel(largeur, hauteur, tab):
    
    resultat =[]
    
    #Ne pas oublier d'appeler les variables globales 
    n = largeur*hauteur
    
    global tabNImg
    tabNImg = list(range(largeur*hauteur))
    tImg = tabIndImgChoisie(n//2,tab)
    
    
    tabPairesAlea = list(map(paireAleatoire,list(range(n//2))))
    
    resultat = formerTab(tabPairesAlea, tImg, n)
    
    return resultat

  
###############################################################################
#Cette partie du code permet de changer de niveau du jeu. Aussi la fonction
#qui initialise le jeu s'y trouve.

niveauActuel = "niveauFacile"

#Cette fonction prend un nom d'attribut et va le selectionner dans le dom 
#et le retourne
def element(nomAttr):  return document.querySelector(nomAttr)


#Cette procédure permet de permuter des  classes du DOM
def permuterClass(nomSelect, niveauActuel):
    classSelect =element('#'+nomSelect).getAttribute('class')
    classActuelle = element('#'+niveauActuel).getAttribute('class')
    
    
    temp = classSelect
    classSelect = classActuelle
    
    element('#'+nomSelect).setAttribute('class',classSelect)
    
    classActuelle = temp
    
    element('#'+ niveauActuel).setAttribute('class', classActuelle)
    
#la fonction prend deux paramètres textes et retourne un texte correspondant 
#à une balise  div avec un  attribut et un contenu.
def divHTML(attr,contenu):  return '<div '+attr+'>'+contenu+'</div>'


#Cette procédure permet de faire des changement dans le dom dans le but de 
#changer de niveau de difficulté en applicant les conditions de format.
def changerNiveau(largeur,hauteur):

    
    menuContenu = element('.menu').innerHTML
    menu = divHTML('class="menu"',menuContenu)
    forme =formatDuJeu(largeur,hauteur)
    divJeu = forme+'\n\n'+ menu
    mainContenu = style+imagePreload+'\n\n'+ divHTML('',divJeu)
    element('#main').innerHTML = mainContenu
    element('table').setAttribute('id','jeu')
    
    
#Cette variable texte corrrespond à la balise style responsable de l'animation
#du compte à rebours
css="""
<style>
#time-box{
  background-color: #dbd400;
  animation: temps 1s infinite
}
 @keyframes temps {}
</style> 
"""    
#Cette procédure créer la boite, la balise du compte à rebours ainsi que
#le css responsable de l'animation.
def boiteDuTemps():  
    
    global css
    
    a = '<div id="time-box" ></div>'
    
    element('#score-box').innerHTML += a 
    
    element("#time-box").innerHTML = " compte à rebours"
    
    element('#main').innerHTML +='<br>'+ css
    
tabImgNiveau = []

#Cette procédure prend en paramètre un nom(texte) et en fonction du niveau de 
# difficulté sélectionné, une modification est opérée dans le DOM. Aussi un 
#tableau contenant les indices d'images choisies aléatoirement dans le tableau 
#d'images, selon les contraintes aléatoires fournis est généré.
#Une réinitialisation du temps est faite si necessaire ou voulue.

def clicMenu(nomSelect):
    
    global niveauActuel, menu, style, largeur, hauteur1, hauteur2, hauteur3
    global tabImages, tabImgNiveau, cpt, tabId, perdu
    global eltReussi, sec
    
    
    #on réinitialise le compteur et le tableau identificateur
    cpt = 0 
    tabId = []    
    tabInfoImg = []
    perdu = True
    sec = 60
    if nomSelect =='niveauFacile':
        
        vefReInitTemps()
        
        permuterClass(nomSelect, niveauActuel)
    
        changerNiveau(largeur,hauteur1)
        
        niveauActuel = nomSelect
        
        tabImgNiveau = tabNFormatSel(largeur, hauteur1, tabImages)
        boiteDuTemps()
        perdu = False
       
        
    elif nomSelect =='niveauMoyen':
        
        vefReInitTemps()
        
        permuterClass(nomSelect, niveauActuel)
        
        changerNiveau(largeur,hauteur2)
        
        niveauActuel = nomSelect
        
        tabImgNiveau = tabNFormatSel(largeur, hauteur2, tabImages)
        boiteDuTemps()
        perdu = False
        
        
    elif nomSelect =='niveauDifficile': 
        
        vefReInitTemps()
        
        permuterClass(nomSelect, niveauActuel)
        
        changerNiveau(largeur,hauteur3)
        
        niveauActuel = nomSelect 
        
        tabImgNiveau = tabNFormatSel(largeur, hauteur3, tabImages)
        boiteDuTemps()
        perdu = False
     
      
      

# la liste des images préchargées    
imagePreload = '\n'.join(list(map(imgPreload, tabImages)))

# Cette fonction prend un nom d'id et un attribut et modifie ou créer
# l'attribut indiqué
def setAttr(attr, nom):
    r = '\'' +nom+'\''
    return element('#'+nom).setAttribute(attr,'clicMenu('+r+')')


#Cette procédure permet d'initialiser pour la première fois le jeu
def init(largeur,hauteur):
   
    global tabImgNiveau
    divContenu =  style+imagePreload+formatDuJeu(largeur,hauteur)+menu
    
    element('#main').innerHTML = divHTML('',divContenu)
    
   
    
    element('table').setAttribute('id','jeu')
    element('#niveauFacile').setAttribute('onclick','clicMenu("niveauFacile")')
    element('#niveauMoyen').setAttribute('onclick','clicMenu("niveauMoyen")')
    element('#niveauDifficile').setAttribute('onclick','clicMenu("niveauDifficile")')
    
    boiteDuTemps()
    
  
    tabImgNiveau = tabNFormatSel(largeur, hauteur, tabImages)
    
    
cpt= 0
tabId = []
tabInfoImg = []     
color = "background-color: #d0d0d0; background-position: center; \
background-size: cover;"
eltReussi=[]
eltPasReussi = []


#Cette procédure s'occupe de retourner les éléments selectionnés et 
#dépendamment de la situation, les spécifications sont appliquées
def validerPaire(index):

    global cpt, tabId,  tabImgNiveau, color, pointsAEnlever
    global eltReussi, eltPasReussi, tabInfoImg
    cpt+=1
    
    
    
    if cpt==1 :
        
        idNom = "#carte"+str(index)
        
        adresseImg = tabImages[tabImgNiveau[index]]
     
        image = styleImage(adresseImg)
        
        #element(idNom).removeAttribute('style')
        
        element(idNom).setAttribute('style',image)
        
        tabInfoImg.append(tabImgNiveau[index])
        
        tabId.append(index)
        
        
        
   
    
    elif cpt == 2 and  tabImgNiveau[index] != tabInfoImg[-1]:
        
       
        
        idNom = "#carte"+str(index)
        
        adresseImg = tabImages[tabImgNiveau[index]]
        
        image = styleImage(adresseImg)
        
        
        element(idNom).setAttribute('style',image)
        
        sleep(0.5)            #On fait une paus de 0,5 seconde
        
        score(pointsAEnlever)      #on va enlever n points du score
        
        #On recache les images, et les informations sur ces images sont
        #retournées dans des tableaux
        
        element(idNom).setAttribute('style',color)
        
        nom = "#carte"+str(tabId[-1])
         
        element(nom).setAttribute('style',color)
        eltPasReussi.append(tabId[-1])
        tabId.append(index)
        tabInfoImg.append(tabImgNiveau[index])
        
        eltPasReussi.append(index)
        
        
        cpt= 0
      
    elif cpt==2 and tabImgNiveau[index]==tabInfoImg[-1] and index !=tabId[-1]:
        
        idNom = "#carte"+str(index)
        adresseImg = tabImages[tabImgNiveau[index]]
        
     
        image = styleImage(adresseImg)
        
        
        #element(idNom).removeAttribute('style')
        
        element(idNom).setAttribute('style',image)
        
        cpt=0
        tabInfoImg.append(tabImgNiveau[index])
        eltReussi.append(tabId[-1])
        eltReussi.append(index)
        
        
        
        element(idNom).setAttribute('id', 'tournee')
        nom = "#carte"+str(tabId[-1])
        tabId.append(index)
        
        element(nom).setAttribute('id', 'tournee')
        
    elif  index ==tabId[-1]:
        cpt -= 1
        
        
        
pointsAEnlever = 0        
scoreActuel=100

#Cette fonction permet de décrémenter une valeur initialement déclarée et
#appelé par variable globale.la valeur en paramètre correspond de combien veut
#on diminuer le score actuelle. On fait également clignoter en rouge quand 
#la valeur est mis à jour
def score(n):
    
    global scoreActuel
    scoreActuel-=n
    
    if scoreActuel < 0:   
        scoreActuel=0
    
    element("#score-text").innerHTML = str(scoreActuel)
    
    #on definit la couleur rouge pour 0.5 seconde, après on enlève la couleur 
    #ce qui parait comme un clignotement
    if pointsAEnlever==0:
        
        sleep(0.5)
        
    elif  pointsAEnlever==5:

        element("#score-box").setAttribute('style','background-color:red;')
        sleep(0.5)
        element("#score-box").removeAttribute('style')
    
    
    
#Dépendamment si l'un des paires a été déjà selectionné ou non, cette procédure
#va faire l'opération appropriée en tenant compte de l'élément cliqué et des 
#données du jeu. Elle fait aussi la vérification du temps et du score
def clicTd(index):
    
    global cpt, eltReussi, tabInfoImg, tabImgNiveau , color 
    global pointsAEnlever, perdu, partieStart
   
       
        
    if index in tabId:
        
        idNom = "#carte"+str(index)
            
        if  index in eltPasReussi and not(index in eltReussi):
            pointsAEnlever = 5
            validerPaire(index)
                
        elif index in eltReussi:
            cpt = 0
    else:
        pointsAEnlever = 0
        validerPaire(index)
        
    if len(tabId)==1:
        
        partieStart=True
        initTemps() 
    
    if scoreActuel == 0 or len(eltReussi) == len(tabImgNiveau) or perdu :
        
        decision()
    else:
        
        return 'rien'
        
#la fonction permet de déterminer l'élément maximum dans tableau      
def maximum(tab):
    maxi = tab[0]
    for i in range(len(tab)):
        if tab[i]> maxi:
            maxi = tab[i]
    return maxi  


tabScoreFacile = []
tabScoreMoyen = []
tabScoreDifficile = []
maxScoreF = '-'
maxScoreM = '-'
maxScoreD = '-'

#Cette procédure permet de déterminer le meilleur score après victoire ou 
#défaite depuis que la partie a commencé. Les variables globales du niveau et
# du score actuel, ainsi que les tableaux adéquats sont appelés pour faire la 
#mise dans le DOM.

def replacerScore():
    global tabScoreFacile, tabScoreMoyen, tabScoreDifficile
    global maxScoreF, maxScoreM,maxScoreD
    global niveauActuel, scoreActuel
    if niveauActuel =='niveauFacile':
        
        tabScoreFacile.append(scoreActuel)
       
        maxScoreF = maximum(tabScoreFacile)
      
        
        element('#'+niveauActuel+' div').innerHTML = 'Meilleur: '+str(maxScoreF)
        
        element('#niveauMoyen div').innerHTML = 'Meilleur: '+str(maxScoreM)
        
        element('#niveauDifficile div').innerHTML = 'Meilleur: '+str(maxScoreD)
       
        
    elif niveauActuel =='niveauMoyen':
        
        
        tabScoreMoyen.append(scoreActuel)
        maxScoreM = maximum(tabScoreMoyen)
        
        element('#niveauFacile div').innerHTML = 'Meilleur: '+str(maxScoreF)
        element('#'+niveauActuel+' div').innerHTML = 'Meilleur: '+str(maxScoreM)
        element('#niveauDifficile div').innerHTML = 'Meilleur: '+str(maxScoreD)
    elif niveauActuel =='niveauDifficile':   
        
        tabScoreDifficile.append(scoreActuel)
        maxScoreD = maximum(tabScoreDifficile)
        
        element('#niveauFacile div').innerHTML = 'Meilleur: '+str(maxScoreF)
        element('#niveauMoyen div').innerHTML = 'Meilleur: '+str(maxScoreM)
        element('#'+niveauActuel+ ' div').innerHTML = 'Meilleur: '+str(maxScoreD)
    
    
#Cette procédure utilise meilleurScoree et fonctionne comme ce dernière
#Elle tient compte d'une défaite par manque de temps    
def meilleurScore():
    global tabScoreFacile, tabScoreMoyen, tabScoreDifficile
    global maxScoreF, maxScoreM,maxScoreD
    global niveauActuel, scoreActuel, perdu
    
    
    if perdu ==True:   #Si on aperdu par temps
        
        if niveauActuel =='niveauFacile':
            
            scoreActuel = 0
            replacerScore()
            
        elif niveauActuel =='niveauMoyen':
            
            scoreActuel = 0
            replacerScore()
            
        elif niveauActuel =='niveauDifficile': 
            
            scoreActuel = 0
            replacerScore()
    else:
        
        replacerScore()
   
        
        
#Cette procédure permet d'initialiser les variables qui ont gardé en mémoire
#les données importantes d'une partie du jeu paire
def varInit():
    
    global tabId, eltReussi, eltPasreussi, tabInfoImg, scoreActuel, cpt
    global tabImgNiveau, sec
    
    tabId =[]
    elt =[]
    eltReussi=[]
    eltPasReussi=[]
    tabInfoImg=[]
    scoreActuel=100
    cpt=0
    perdu = False
    element("#score-text").innerHTML = str(scoreActuel)#on remet le score à 100
    reInitTemps() 
    element("#time-box").innerHTML = " compte à rebours"
    sec = 60
    
    
 # Cette procédure annonce la décision de la partie et réinitialise le texte 
#HTML pour une autre partie. Les données en mémoire de la dernière partie sont
#effacer.
def decision():
    
    global scoreActuel, eltReussi, tabImgNiveau
    global tabScoreFacile, tabScoreMoyen, tabScoreDifficile
    global maxScoreF, maxScoreM,maxScoreD
    global niveauActuel, perdu
    #on vérifie d'abord si c'est la fin d'une partie, si oui on peut sortir de 
    # la fonction, sinon on continue dans la fonction
    
    if scoreActuel==0 or perdu: 
        
        
        meilleurScore()
        
        clicMenu(niveauActuel)
        
        alert("Vous avez perdu...")
        
        
    elif   len(eltReussi) == len(tabImgNiveau):
        
        meilleurScore()
        
        clicMenu(niveauActuel)
        
        alert("Vous avez gagnez!!!")
     
        
    varInit()    
      
        
        

###############################################################################
#Cette partie traite l'implémentation d,un compte à rebours de 60s




partieStart=False 

#Cette procédure initialise la boite de temps
def initTemps():
    
    global partieStart
    
    if partieStart ==True:

        element("#time-box").setAttribute("onanimationiteration","temps()")
        
        
   
   

perdu = False   
gagne = False

#Cette procédure réinitialise la boite de temps
def reInitTemps():
    
    element("#time-box").removeAttribute("onanimationiteration")
    
    element("#time-box").innerHTML = ""
    
# Cette procédure permet de vérifier avant de réinitialiser la boite de temps   
def vefReInitTemps():
    
    global perdu, eltReussi,tabImgNiveau, scoreActuel
    
    if perdu == True or len(eltReussi) == len(tabImgNiveau) or scoreActuel==0:
        
        reInitTemps()

        
sec=60
perdu = False
#Cette procédure est appelée à chaque fois que l'événement animationiteration
# est activé. Elle permet recalculer le nombre de secondes restants et le 
#remet dans la balise appropriée.
def temps():
    
    global sec, perdu, eltReussi,tabImgNiveau
    
    sec-=1
    
    element("#time-box").innerHTML = 'Temps restant: ' + str(sec)+'s'
    
    if sec ==0:
        
        perdu = True
        
        decision()
            
        
# Cette procédure permet d'exécuter un élément a en paramètre une fois    
def excecuterUneFois(a):
   
    n = 0 
    while n<1:
        
        n+=1
        #init(4,3)
        a
        
        initTemps()

    
excecuterUneFois(init(4,3))       #initialisation de la partie


#version2

























