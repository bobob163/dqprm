## Exercice 4 - Analyse des données enregistrées avec un oxymètre de pouls
-----------

L’oxymètre permet de mesurer la quantité d’oxygène dont le sang est saturé. Cette mesure permet de surveiller l’état des patients sujets à des troubles respiratoires ou souffrant d’affections de l’appareil respiratoire.

Le principe utilisé pour le fonctionnement des oxymètres de pouls est basé sur la capacité d’absorption du sang des lumières rouge et infrarouge, selon leur saturation en oxygène. Le calcul du taux de saturation sanguin en oxygène noté SpO2 est basé sur le rapport entre la CHbO2 sur la CHb, respectivement concentration sanguine en oxyhémoglobine et concentration totale d’hémoglobine dans le sang.

$$ SpO_2=\frac{CHbO_2}{Chb} $$

Lorsque l'hémoglobine capte l’oxygène au niveau des poumons, il se transforme en oxyhémoglobine et se colore en rouge vif et lorsque cet oxygène est libéré au niveau des tissus, il se transforme en désoxyhémoglobine. Ces deux types d’hémoglobines possèdent un taux d’absorption différent de la lumière rouge et de la lumière infrarouge. L’oxyhémoglobine absorbe mieux la lumière infrarouge et la désoxyhémoglobine absorbe mieux la lumière rouge.

Le principe d’absorbance va permettre de déterminer le taux de saturation en oxygène d’un milieu. En effet, la quantité de lumière absorbée par un milieu est proportionnelle à sa concentration en une espèce chimique donnée, selon la loi de Beer-lambert. Le capteur qui se place à l’extrémité du doigt est équipé d’un émetteur et d’un récepteur de lumière.

L’émetteur permet l’émission d’une lumière infrarouge et d’une lumière rouge grâce à deux Led. La lumière rouge a une longueur d’onde de 660 nm, la lumière infrarouge a une longueur d’onde de 950 nm. Ces deux lumières vont traverser la peau et vont être captées par un récepteur, constitué une photodiode, qui va les quantifier.

<center><figure>
<img src="./data/fonctionnement-oxymetre.jpg">
</figure></center>

Un calcul sur la quantité de lumière absorbée va permettre de déterminer la saturation sanguine en oxygène. La saturation du sang (SpO2), s’exprime en pourcentage et va permettre d’avoir une estimation de l’état d’un patient. La valeur normale est située entre 90 % et 100 %. L’oxymètre va en outre permettre de mesurer la fréquence cardiaque, par la mesure de la variation des différents flux de sang au niveau des extrémités.

Un oxymètre de pouls affiche 3 données : la **SpO2**, la **fréquence cardiaque** (fréquence de pulsation du pouls par minute) et la **courbe de l’onde du pouls**.

<center><figure>
<img src="./data/oxypleth.jpg">
</figure></center>

**Question 1.** Lire avec la bibliothèque Pandas le fichier `data_oxypleth.csv` contenu dans le dossier `data`. Déterminer le nombre de lignes et de colonnes ainsi que le nombre total d'éléments contenus dans ce fichier

**Question 2.**  Tracer côte à côte la courbe de l'onde du pouls correspondante et celle obtenue pour les 300 premières données du fichier uniquement

**Question 3.** Utiliser la fonction `print(*my_dataframe,sep=",")` pour lister les éléments contenus dans votre dataframe

Les données acquises par cet oxymètre de pouls ont été enregistrées de la façon suivante :

    * Les données (normalisées, valeurs comprises entre 0 et 100) se succèdent les unes à la suite des autres
    * A intervalle régulier, un élément de valeur 254 est stocké. Il s'agit d'un élément sans signification physiologique dont la valeur correspond en réalité à une étiquette (signal tag)
    * A ce signal tag + 1, la valeur de saturation calculée par l'oxymètre est enregistrée
    * A ce signal tag + 2, la valeur de fréquence cardiaque calculée par l'oxymètre est enregistrée

Exemple :

```python
...
29  : donnée  
254 : valeur signal tag t0, pas de signification physiologique donc de donnée correspondante
98  : t0+1 --> valeur de saturation (%)
84  : t0+2 --> valeur de la fréquence cardiaque (bpm)
21  : donnée  
15  : donnée  
12  : donnée    
26  : donnée  
...
```

**Question 4.** Nettoyer les données en retirant les éléments qui ne correspondent pas au signal de l'onde de pouls. Les valeurs de saturation et de fréquence cardiaque seront isolées et sauvegardées dans deux autres variables

**Question 5.** Tracer sur une même figure les 6 courbes suivantes :

* Données complètes de l'oxypleth (paramètres d'affichage par défaut)
* Données nettoyées (paramètres d'affichage par défaut)
* Données nettoyées réduites aux 300 premières valeurs (courbe de couleur verte)
* Valeurs de fréquence cardiaque seules (points de couleur bleu)
* Valeurs de saturation seules (points de couleur rouge)
* Valeurs de fréquence cardiaque et de saturation sur un même graphique (axe des ordonnées entre 0 et 120)
  