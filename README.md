# Stage_HIRACLES
Repo' contenant le code source utilisé pour le projet HIRACLES


<h3 align="left">Etat actuel du projet : </h3> 

Je vais tester le code présent sur le repo suivant : https://github.com/mrzhu-cool/pix2pix-pytorch qui semble être assez compréhensible et qui pourra potentiellement être réutilisé et adapté pour générer des images pléiades. 
Je vais donc tester cet algorithme avec le jeu de données fourni par l'auteur, tout en préparant le jeu de données avec les images satelites et les images Pléiades. Si le test est convaincant avec le jeu de données fournies par l'auteur du code, je pourrais essayer d'appliquer cet algorithme et d'observer le résultat sur les images satelites. Ce dernier test sera surement utilisé Jeudi et Vendredi 14 et 15 Avril grâce à l'ordinateur mis à disposition car cela apportera une très grande rapidité.

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
