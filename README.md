# Sismondi NFT demo

Ce répertoire contient la démo pour la semaine des étudiants du gymnase Sismondi.
Pendant cette semaine, les étudiants vont passer une journée à l'EPFL pour apprendre
plus sur les blockchains et les NFTs.
Le programme de la journée est le suivant:

Matin:
- présentation de Mme Zürcher
- présentation de Linus Gasser sur les blockchains
- exercices pour se familiariser avec les outils nécessaires pour la suite

Après-midi:
- présentation de Linus Gasser sur les NFTs
- exercices sur les NFTs en utilisant ce répertoire

# 1.1 - Préliminaires

On va commencer par s'installer sur l'ordinateur.
Puis, on va faire un portefeuille pour vos jetons, et commencer
à remplir le portefeuille.
Vu que cette opération va prendre pas mal de temps, on y va avant
d'avoir vu ce que ça fait vraiment.

## 1.1.1 - Exercices

Chaque exercice va se poursuivre de la manière suivante:

1. Vous mettez la carte "A l'écoute" sur vos écrans
2. Linus va vous montrer comment faire la procédure
3. Vous mettez la carte "Au travail" et exécutez le travail.
Si vous avez des questions, n'hésitez pas à demander aux assistants.
4. Une fois que vous avez terminé, mettez la carte "Terminé"
5. Assurez-vous que tout le monde dans le groupe a bien compris
6. Si vous voulez aider les autres, mettez la carte "Au partage"

## 1.1.2 - Se connecter à votre compte

Sur la feuille que vous avez reçue, il y a un nom et un mot de passe.
Utilisez-les pour vous connecter à votre compte.
Puis cliquez sur "IC-Gymnases".

## 1.1.3 - Fichiers de la journée

Pour retrouver tous les fichiers, ouvrez Firefox et entrez l'adresse
suivante:

1. Cliquez la grille en bas à gauche, sélectionnez  "Firefox"
2. Entrez l'adresse go.epfl.ch/sismondi dans la barre de navigation
3. Scrollez en bas jusqu'au 1.1.4

## 1.1.4 - Questions et discussions

On va utiliser un chat commun entre les étudiants et l'enseignant.
Pour ceci, connectez-vous au chat en indiquant un pseudonyme et le
mot de passe que vous trouvez sur le tableau.
Normalement, vous devriez déjà lire ceci sur github, donc il suffit
de cliquer sur le lien suivant:

https://www.chatzy.com/78734252296038

## 1.1.5 - Créer un portefeuille (wallet)

On verra que les jetons sur la blockchain sont protégés par une "clé privée".
Cette clé privée est stockée dans un portefeuille, ou "Wallet" en Anglais.
Ces clés privées sont comme un mot de passe, mais beaucoup plus long, et avec des
propriétés mathématiques intéressantes pour les blockchains.
Si quelqu'un réussi à copier vos clés privées, cette personne a le même accès que vous
à votre portefeuille.
Donc ne donnez votre clé privée à personne!
Le portefeuille Metamask demande un mot de passe qui protègera vos clés privées.
Pour sécuriser, il est conseillé d'écrire le "recovery phrase" quelque part.

On utilisera ici le portefeuille le plus connu: Metamask.

### ATTENTION! SCAMS! VOLS!

Il faut être très prudent dans le monde des blockchains sur les scams (tricheries)
et vols.
Vu que la clé privée est la seule chose qui protège vos jetons, du moment que quelqu'un
la possède, cette personne peut faire ce qu'elle veut avec vos jetons.
Donc, il est impératif de:
- ne jamais partager sa clé privée
- ne pas installer des logiciels d'une source douteuse

## 1.1.6 - Installer Metamask

Aller sur le site de Metamask et suivre les instructions d'installation:

[Installer Metamask](https://metamask.io/download/)

1. On va faire confiance à Firefox pour stocker le mot de passe
2. Sécurisez l'installation
3. Copiez TOUS LES 12 mots de récupération dans un éditeur de texte
4. Pour confirmer, remplissez les espaces vides - ceci est pour vérifier que vous avez bien
noté votre phrase de récupération
5. Suivez les instructions pour `pin` Metamask
6. Choisissez le réseau "Sepolia": cliquez en haut à gauche dans 
 `Ethereum Mainnet`, puis cochez `Show test networks`, ensuite choisissez "Sepolia".

## 1.1.7 - Charger votre portefeuille avec quelques jetons depuis un "robinet"

Pour la prochaine étape, vous avez besoin de quelques jetons.
Les réseaux blockchains de test vous permettent de recevoir des jetons gratuits.
Bien sûr que vous ne pouvez pas revendre ces jetons, ils ne valent rien.

Afin de recevoir quelques jetons, vous pouvez copier votre adresse depuis Metamask
dans le robinet suivant:

[Faucet](https://sepolia-faucet.pk910.de)

L'adresse PUBLIQUE commence avec un `0x` et contient des chiffres et des lettres a-f.

Une fois le robinet ouvert, on va continuer la présentation.
Assurez-vous que le "minage" continue en arrière-plan, parce qu'il vous faudra
1 SepoliaETH pour le reste de la journée.

# 1.2 - Utiliser des jetons

Assurez-vous que vous avez au moins 1 SepoliaETH jusqu'à maintenant.
Puis continuez sur l'étape suivante.

## 1.2.1 - Empocher la récompense

Quand le montant est atteint, cliquez sur `Stop Mining`, puis `Claim Rewards` et attendez que vos jetons
se trouvent sur votre compte.

## 1.2.2 - Vérifier la réception des jetons

Maintenant, on va utiliser `Etherscan` pour voir ce qui s'est passé.
Entrez votre adresse publique sur le site suivant, afin de
suivre les transactions sur votre compte et depuis votre compte:

[Etherscan](https://sepolia.etherscan.io)

Si vous ne voyez pas votre transaction, assurez-vous que vous êtes connecté au réseau 
"Sepolia".

## 1.2.3 - Transférer des jetons

Pour finir cette partie, vous allez transférer quelques jetons à vos voisins.
Ne mettez pas trop de jetons, quelque chose comme 0.001 est très bien.

1. Demandez à vos voisins leur adresse publique de leur portefeuille
  - Assurez-vous qu'ils ne vous la donnent pas! Sinon, vous pouvez créer un
  nouveau portefeuille et transférer tous leurs jetons chez vous!
2. Demandez à vos voisins leur adresse publique de leur portefeuille.
Vous pouvez utiliser [Chatzy](https://www.chatzy.com/78734252296038)
3. Ouvrez "Metamask" dans Firefox
4. Cliquez sur "Send"
5. Entrez l'adresse que vous avez reçu de vos voisins
6. Entrez 0.001 SepETH et confirmez

## 1.2.4 - Visualiser le transfert

Utilisez de nouveau [Etherscan](https://sepolia.etherscan.io) pour visualiser
votre compte.
Cherchez quel lien il faut cliquer pour voir le compte de vos voisins.

# 1.3 - Préparer la configuration de `Brownie`

[Brownie](https://eth-brownie.readthedocs.io/en/stable/) est un outil de développement et
de teste pour écrire des smart contracts pour Ethereum.
Brownie réunit tous les outils nécessaires pour intéragir avec Ethereum:

- un compilateur pour traduire un smart contract dans un format convenable pour Ethereum
- une blockchain de test locale pour faire les premiers pas
- les outils nécessaires pour envoyer et intéragir avec un smart contract

Ici, on va configurer cet outil avec la clé privée et un accès supplémentaire nécessaire
pour le bon fonctionnement.

## 1.3.1 - Télécharger le répertoire

Pour commencer, il faut télécharger le répertoire github sur votre ordinateur.
Suivez ces étapes:

1. Cliquez la grille en bas à gauche, sélectionnez "terminal"
2. Copiez la commande suivante dans votre terminal - attention, tous les caractères doivent
être copiés/collés tel quel! Vous pouvez faire un copier/coller depuis Firefox:

```bash
git clone https://github.com/c4dt/sismondi_nft_2024
```

Une fois que c'est téléchargé, vous pouvez changer dans ce répertoire avec la commande
suivante:

```bash
cd sismondi_nft_2024
ls
```

Ceci devrait vous montrer les fichiers dans le répertoire.
Garder le terminal ouvert, on en aura encore besoin!

## 1.3.2 - Ouvrir Thonny

Pour ouvrir le logiciel Thonny, suivez ces étapes:
1. Cliquez sur la grille en bas à gauche, cherchez "Thonny"
2. Sélectionnez `all files` en bas à droite du dialogue de fichiers pour voir aussi les fichiers
qui se terminent en `.md`.
3. Ouvrez le fichier `NOTES.md` qui se trouve dans le répertoire
`sismondi_nft_2024`

## 1.3.3 - Remplir le fichier `NOTES.md`

Pour vous faciliter la vie, utilisez le fichier `NOTES.md`:
1. Copiez la phrase de récupération depuis votre éditeur de texte dans ce fichier
2. Recopiez votre adresse PUBLIQUE depuis Metamask dans le fichier `NOTES.md`
3. Faites de même pour la clé privée. Elle est protégée par Metamask:
  - Cliquez sur les trois petits points à droite du nom de votre compte
  - Choisissez "Account details", puis "Show private key"
  - Confirmez avec votre mot de passe
  - Appuyez longuement sur le bouton
  - Copiez/collez la clé privée depuis la fenêtre dans le fichier `NOTES.md`

## 1.3.4 - Créer le fichier `.env`

Afin de pouvoir envoyer des commandes à la chaîne de teste "Sepolia", il faut configurer
le fichier `.env`.
Le plus simple est de copier le fichier `env.example` dans le fichier `.env`.

1. Ouvrez le fichier `env.example` avec Thonny (n'oubliez pas d'utiliser `all files`)
2. `Fichier` -> `Enregistrer sous`
3. Changer le nom en `.env`
4. Sélectionnez `all files` en bas à droite 
5. Enregistrez avec `OK`

## 1.3.5 - Copier la clé privée

Maintenant, vous pouvez copier la clé privée dans votre fichier `.env`.
Vous la trouvez dans votre fichier `NOTES.md`.
Copiez/collez la clé privée dans le fichier `.env`

## 1.3.6 - Enregistrer sur Infura

Pour communiquer avec la blockchain, il vous faut un intermédiaire.
Ici, on va choisir Infura, et il faut créer un compte.
Allez sur

[Register Infura](https://app.infura.io/register)

et entrez votre nom (vous pouvez mettre n'importe quoi) et votre email.
Il est important que l'email soit correcte, parce qu'ils vous envoient
un lien qu'il faut pour confirmer.

## 1.3.7 - Copier la clé d'accès dans ´.env`

Une fois la régistration confirmée, vous pouvez activer la clé d'accès.
Cette clé vous permet de vous identifier auprès d'Infura pour créer votre
contrat.

1. Cliquez sur `API Keys` en haut
2. Choisissez la clé existante `My First Key`.
3. Dans la page qui s'ouvre, cochez la case `Sepolia` sous `Ethereum`
et appuyez sur `Save Changes`.
4. En haut, vous trouvez la clé d'accès que vous pouvez Copier/coller dans votre 
`.env`.

## 1.3.8 - Le `.env`

Votre `.env` doit maintenant contenir quelque chose comme ça.
Bien sûr que la clé privée et la clé d'accès auront des valeurs différentes!

```
PRIVATE_KEY = 0x41ede96cc603bf0d7a0e0bd67819ebaf5802ae8ea1060a4f6f3d8b9d723a24ea
WEB3_INFURA_PROJECT_ID = a691dd6311fb41eb6f3d8b9d723a24ea
```

## 1.3.9 - Vérifier le `.env`

Faites le test suivant pour voir si tout a bien fonctionné.
Lancez la commande suivante:

```bash
./brownie.sh run test_env.py
```

Ceci coûte à peu près 0.007 SepoliaETH.
Le test devrait prendre autour de 30 seconds et il va vous côuter quelques jetons.

# 2.1 - Configurer le contrat Sismondi_NFT avec vos images

Avant d'installer le contrat Sismondi_NFT sur la blockchain, il faut le configurer avec
vos images.
Il faut commencer par copier vos images sur l'ordinateur de l'EPFL.
Puis, il faut transformer les images pour qu'elles soient compatibles avec le smart contract.
A la fin, il faut copier les images dans le smart contract.

## 2.1.1 - Préparer les images

1. Copier les images dans les sous-répertoires de `./images` en remplaçant les images
qui y sont déjà présentes
2. Ouvrez le fichier `./scripts/images.py`
3. Modifiez le nom des fichiers - faites attention au chemin d'accès
4. Lancez le script dans le terminal:

```bash
./mk_images.sh
```

5. Il y a deux parties qu'il faut copier/coller dans le contrat `./contracts/SismondiNFT.sol`:
  - La partie `Prefix` doit suivre la déclaration d'`images_prefix`. 
  Ne pas oublier le `;` à la fin!
  - Les valeurs après le `Images are:` doivent remplacer ceux actuellement dans le
  tableau de `images`
6. Vous pouvez aussi modifier la liste des mots qui est utilisé pour nommer vos NFTs.
Essayez de montrer de la maturité dans le choix de vos mots...

Chaque NFT se verra attribuer aléatoirement une des images et aussi aléatoirement un des
mots de la liste.

## 2.1.2 - Tester le contrat localement

Avant d'installer le contrat sur la blockchain Sepolia, on va d'abord le tester
localement.
Ceci peut assurer que vous n'avez pas fait d'erreur dans le copier/coller des images
dans le contrat.
Lancez la commande suivante:

```bash
./brownie.sh run sismondi.py deploy_mint --network development
```

Si tout va bien, vous devriez voir un total de 3 blocs:
- block 0: installation du contrat
- block 1: mint d'un premier NFT
- block 2: mint d'un deuxième NFT

## 2.1.3 - Installer le contrat sur le réseau de test Sepolia

Maintenant que vous avez mis à jour le contrat `SismondiNFT.sol`, et que vous
avez créé le fichier `.env`, vous êtes prêt·e·s!
Pour installer votre contrat `SismondiNFT.sol` sur la chaîne, vous pouvez
lancer la commande suivante:

```bash
./brownie.sh run sismondi.py deploy
```

Si tout se passe bien, vous devrez voir un commentaire qui se termine avec quelque
chose comme ceci:

```
Running 'scripts/sismondi.py::deploy'...
Transaction sent: 0x84096187a70ccfbdbb16546bbc250e72db949af3e726a5d0156222b7f7dc6f6d
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  SismondiNFT.constructor confirmed   Block: 1   Gas used: 2816575 (23.47%)
  SismondiNFT deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

contract has been deployed successfully to : 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87
Terminating local RPC client...
```

Ce qui est le plus important, c'est le dernier long numéro, dans notre cas le
`0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87`.
C'est l'adresse de votre contrat sur la blockchain.
Copiez cette adresse dans le fichier NOTES.md.

Vous trouvez tous les messages d'exécution dans le fichier `operations.log`.
Donc si vous avez oublié l'adresse de votre contrat, vous pouvez y jeter un coup
d'œil.

## 2.1.4 - Vérifier l'installation du contrat

Avec l'aide de l'outil [Etherscan](https://sepolia.etherscan.io), vous pouvez maintenant
vérifier que votre contrat est bel et bien installé sur la chaîne.
Entrez l'adresse du contrat que vous avez reçu en 2.1.3, et regardez ce que
Etherscan sait de votre contrat.
On verra qu'une fois que vous faites un "mint" sur ce contrat, Etherscan va ajouter
plus d'information.

# 2.2 - Utilisation du contrat

## 2.2.1 - Minter un NFT

Maintenant, vous êtes prêt·e·s pour faire un mint de votre premier NFT!
Parce que le contrat lui-même n'a encore rien minté, il n'y a pas encore de
NFT stocké dans le contrat!

Lancez la commande:

```bash
./brownie.sh run sismondi.py mint 0xADRESSE_CONTRAT
```

Vous devez remplacer `0xADRESSE_CONTRAT` par l'adresse que vous avez trouvé dans l'étape
`Création d'un contrat NFT`.
Si tout va bien, vous devez voir quelque chose comme ça:

```
Transaction sent: 0xb267bdc54994fe92746c21ca45853ae0d0f6d5d36461f92040462fae3558c407
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
  SismondiNFT.makeSismondiNFT confirmed   Block: 2   Gas used: 1493155 (12.44%)

A new NFT with id 0 has been successfully created in block 2 with transaction 0xb267bdc54994fe92746c21ca45853ae0d0f6d5d36461f92040462fae3558c407
```

Les numéros sont sûrement différents des vôtres.
Ce qu'il faut noter ici, c'est le `id 0`, qui signifie que c'est le premier NFT
créé par ce contrat. 

## 2.2.2 - Vérifier sur Etherscan

Allez regarder de nouveau sur Etherscan l'adresse de votre smart contract et vérifiez
qu'il y a bien une deuxième transaction.
Vous pouvez aussi cliquer sur le `Token Tracker` pour voir combien de NFTs ont
été émis.

## 2.2.3 - Minter un NFT d'un autre groupe

Prenez l'adresse d'un contrat d'un autre groupe, afin de faire
du mint sur leur contrat à eux.
Quand ils vous donnent leur adresse, il faut d'abord vérifier que c'est bien
un contrat de mintage, à l'aide de [Etherscan](https://sepolia.etherscan.io).
Dans la partie `More Info`, il faudrait une mention de `Token Tracker`.
Si ce n'est pas le cas, ça peut être à cause de:
- une erreur dans la transmission de l'adresse
- que l'autre groupe n'a pas encore fait un premier mint

## 2.2.4 - Visualiser dans OpenSea

La visualisation avec le site OpenSea est possible même sans inscription.
Allez sur le site ici:

[OpenSea](https://testnets.opensea.io)

et entrez l'adresse de votre contrat NFT en haut dans la barre de recherche.
Si vous avez déjà minté un NFT, il devrait s'afficher ici.

## 2.2.5 - Ajouter au portefeuille Metamask

Afin de transmettre le NFT, on peut utiliser Metamask:
1. Dans votre page de Metamask, cliquez sur `NFTs`, puis sur `Import NFT`
2. Ajoutez l'adresse de votre contrat, ainsi que le `id` de votre NFT

Vous ne pouvez pas ajouter un NFT que vous n'avez pas minté!

## 2.2.6 - Envoyer vers d'autres utilisateurs

Pour envoyer votre NFT vers un autre utilisateur, vous devez d'abord
ajouter le NFT comme dans la section précédente.
Maintenant, vous pouvez cliquer sur le NFT, et choisir `Send`.
On vous demande l'adresse du destinataire.

ATTENTION: une fois envoyé, il n'est pas possible de récupérer le NFT!
Donc si vous envoyez à une mauvaise adresse, le NFT est perdu!

# Documentation

- Transparents de la journée: [Blockchains et NFTs](https://docs.google.com/presentation/d/1x2FqWLHjh-F-auDqM0_eJ4Nv5r-jLTy-K3gfAH9umH8/edit?usp=sharing)
- Howto qui a été utilisé pour préparer la journée: [Deploy Your First NFT With Python](https://www.codeforests.com/2022/01/14/deploy-your-first-nft-with-python/) - 
    [Github with contract](https://github.com/codeforests/brownie_legendnft) 
- Contract utilisé pour le NFT: [openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master) 
[Definition of ERC 721](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721) 
- Réseaux de test Ethereum: https://ethereum.org/en/developers/docs/networks/
