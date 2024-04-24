from bs4 import BeautifulSoup
import requests

url ="https://www.amazon.fr/GIGABYTE-GeForce-EAGLE-Carte-graphique/dp/B0C5JWKK33/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2FYTAZRXWTC10&dib=eyJ2IjoiMSJ9.1AuVW11_zIWzrJccmHqwDLRzQ9yZrw5Q_fGWOecXKhe5bGNNpozukbBF2kjSc-ffYY6X7kWlUOd3ym_Pjr_O9E2BNMX67DIrNCDSMM3CWyAF3wMLSKL6qCN55DwCuR1cuhcQTr0NJciI0zGhJSWdpM21az5fMY83qtS4aPuYxRtI5YP2br3O2yVFBrzAiV5JOakgn9oCrUbYOYGJYdpL1Ba9gEbWshXQAb4rVCUCRZA2kuWsSrqDTzDAPgR_2qNKScENGT8WoB6-LyVuH6x6Jk7O5kNN3i5fT5uU5wW1SCk.FC55pOIm6BOSb9EZcSyEiPorX_BICnBoZAEmzCYf83Y&dib_tag=se&keywords=GIGABYTE+GeForce+RTX+4060+Ti+WINDFORCE+OC+8G+Graphics+Card%2C+2x+WINDFORCE+Fans%2C+8GB+128-bit+GDDR6%2C+GV-N406TWF2OC-8GD+Video+Card&qid=1713896486&s=computers&sprefix=gigabyte+geforce+rtx+4060+ti+windforce+oc+8g+graphics+card%2C+2x+windforce+fans%2C+8gb+128-bit+gddr6%2C+gv-n406twf2oc-8gd+video+card%2Ccomputers%2C85&sr=1-1"

result = requests.get(url)

soup = BeautifulSoup(result.text, "lxml")
print(soup)

