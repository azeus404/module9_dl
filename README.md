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
Ik heb het weights.h5 bestand  dat na het uitvoeren van het vorige script gemaakt is verwijderd en de data aangepast door het toepassen van een AND functie. Vervolgens zijn er twee nieuwe scripts aangemaakt:
- backprop_and_train.py
- backprop_and_classify.py
Training:


Classify:
Accuracy: 50.00
Accuracy: 88.89
correct estimated
[0.] [[0]]
[1.] [[0]]
[1.] [[1]]
[1.] [[1]]
[0.] [[0]]
[1.] [[1]]
[0.] [[0]]
[0.] [[0]]

## Opdracht 3
Er is met deze opdracht van alles mis :(. Ik mis een uitleg van de gebruiken packages en welke folders er vooraf nodig zijn om de code goed te laten werken.
Zoals: images_for_learning en models

Na wat knutselwerk heb ik de code werkend gekregen. Alleen het script om onbekende malware te classificeren mist volgens mij data(?). Alle data is nl. gebruikt bij trainen en valideren van het model.

Daarnaast heeft Malware_Classify.py maar 8 classes om de malware in te kunnen verdelen. Ik heb deze aangepast naar 25: de verschillende families die aanwezig zijn in de dataset.

## Code
Ik heb de aangepaste code geupload in deze repo. Ik heb gebruik gemaakt van een lokale NVIDIA GPU met 8GB geheugen. Om deze te benutten zijn er  aanpassingen gedaan in de scripts. 
