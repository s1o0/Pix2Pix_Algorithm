# Stage_HIRACLES
Repo' contenant le code source utilisé pour le projet HIRACLES


<h3 align="left">Etat actuel du projet : </h3> 

Après avoir testé l'algorithme de Deep Learning sur le calculateur de l'IUEM, je m'attaque à la préparation du jeu de données. J'ai créer une méthode permettant de pouvoir couper une image pléiade en prennant une image IGN en entrée, pour ainsi obtenir une image pleiade qui possèdera les mêmes 4 coordonées dans chaque coin que l'image IGN. Maintenant, il faut automatiser ce programme pour qu'il puisse réaliser ce travail sur toutes les images IGN à notre disposition.

--------------------------------------------
-------------------------------------------
<h3 align="left">Entrainer le model : </h3>
python train.py --dataset facades --cuda

<h3 align="left">Tester le model : </h3>
python test.py --dataset facades --cuda

<h3 align="left">Installation nécessaire (Dans l'ordre) :</h3>
- Python <br>
- pip <br>
- torch (pip) <br>
- torchvision (pip) <br>
- pillow (pip) <br>
- torch.utils (pip) <br>
- numpy (pip) <br>


<h3 align="left">Crédit : </h3>

https://github.com/mrzhu-cool/pix2pix-pytorch par @mrzhu 

https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix par @junyanz
