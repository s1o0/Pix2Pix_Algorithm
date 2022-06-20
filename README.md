# Pix2Pix_Algorithm
Implémentation de l'algorithme Pix2Pix permettant de réalisé le transfert de style. Cette implémentation repose sur le [dépôt suivant](https://github.com/mrzhu-cool/pix2pix-pytorch) réalisé par @mrzhu.

L'algorithme original de Pix2Pix se trouve sur [ce dépôt](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) ou alors vous pouvez également trouver d'autres implémentations sur [ce site](https://phillipi.github.io/pix2pix/)

# Exécution :

Pour exécuter l'entrainement de cet algorithme vous devez exécuter cette commande :
```bash
python3 train.py --dataset facades --cuda
```
Puis, pour exécuter les tests :
```bash
python3 test.py --dataset facades --cuda
```

# Documentation nécessaire :
Une documentation a été réalisé via le logiciel Notion, vous pouvez la trouver sur [ce document](https://resonant-tamarillo-324.notion.site/Github-Deep-Learning-43df5891e4994f9c8709aadc810f8307).
