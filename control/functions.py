from django.shortcuts import render

from web3 import Web3
from coordonator.models import Alegere
from control.models import Candidat
import json

# Ma conectez la ganache.
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
if web3.isConnected():
    print('Web3 s-a conectat...')

# Variable initilize

# List of Candidates
lista_Candidati = []
for candidat in Candidat.objects.all():
    lista_Candidati.append(candidat.nume)

data = json.load(open("build/contracts/eVOT_Contract.json", "r"))

abi = data['abi']
deployedBytecode = data["deployedBytecode"]
print("==================>>>: ", data['networks']['5777']['address'])
adresa = web3.toChecksumAddress(data['networks']['5777']['address'])

# Instanțiez contract-ul
MyContract = web3.eth.contract(abi=abi,
                               bytecode=deployedBytecode,
                               address=adresa)

# iau conturile curente de la ganache
conturi = web3.eth.accounts

tx = {'from': conturi[7]}
tx_for_vote = {'from': conturi[3]}

def adauga_Candidat(candidati):
    alegere = Alegere.objects.get(id=1)
    if (alegere.status):
        print("Candidatul a fost deja adăugat pe blockchain!")
    else:
        for candidat in candidati:
            print('Candidatul a fost adăugat.', candidat.name)
            MyContract.functions.adaugaCandidat(candidat.name).transact(tx)
        alegere.status = True
        alegere.save()


def conturi_noi():
    return conturi[0]


def Transactions(nume_alegator, alegator_token):
    print("Transactions is up")
    for i in range(len(lista_Candidati)):
        print(lista_Candidati[i])
        if str(lista_Candidati[i]) == str(nume_alegator):
            tx_vote = {'from': alegator_token}
            print(tx_vote)
            MyContract.functions.vote(i + 1).transact(tx_vote)
            print("Voted for :", i + 1, lista_Candidati[i])


def rezultate_finale():
    rezultate = {}
    rezultat_candidat = []
    for x in range(1, len(lista_Candidati) + 1):
        rezultat_candidat.append(MyContract.functions.getResult(x).call(tx))
    rezultate['candidati'] = lista_Candidati
    rezultate['nr_voturi'] = rezultate
    print("Rezultate: ", rezultate)
    return (rezultate)
