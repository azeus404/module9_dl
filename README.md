# Module 9 MCSE - Deep Learning in Cyber Security
Uitwerkingen van Module 9 Deep Learning practicum 13 maart 2020.

## Opdracht 1
Heb ik het meegeleverde weights.h5 bestand weggegooid. Vervolgens backprop_xor_train.py uitgevoerd. Het resultaat van de training is 100 accuracy
Vervolgens de classificatie backprop_xor_classify.py uitgevoerd eveneens 100% accuracy.

Accuracy: 100.00
correct estimated
[0.] [[0]]
[1.] [[1]]
[1.] [[1]]
[1.] [[1]]
[1.] [[1]]
[1.] [[1]]
[1.] [[1]]
[0.] [[0]]


## Opdracht 2
Ik heb het weights.h5 bestand verwijderd en de data aangepast naar AND functie en twee nieuwe scripts aangemaakt:
- backprop_and_train.py
- backprop_and_classify.py

Accuracy: 100.00
correct estimated
[0.] [[0]]
[1.] [[1]]
[1.] [[1]]
[0.] [[0]]
[1.] [[1]]
[0.] [[0]]
[0.] [[0]]
[1.] [[1]]


## Opdracht 3
Er is met deze opdracht van alles mis :(. Ik mis een uitleg van de gebruiken packages en welke folders er vooraf nodig zijn om de code goed te laten werken.
zoals: images_for_learning

Na wat knutselwerk heb ik de code werkend gekregen. Alleen het script om malware te classificeren mist volgens mij data? Alle data is nl. gebruikt bij trainen en valideren van het model.

Malware_Classify.py heeft maar 8 classes uit een ander voorbeeld. Ik heb deze aangepast naar 25: de verschillende families die zijn beschreven in de paper.

## Code
Ik heb de aangepaste code geupload in deze repo. Ik heb gebruik gemaakt van een lokale GPU. Om deze te benutten zijn er  aanpassingen gedaan in de scripts. 
