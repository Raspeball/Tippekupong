## Import ##
import easygui as egui
import math
import random
## --- --- ##
#
#
#
def main():
	#
	#
	## Global variables ##
	kamper = 12 #alltid 12 kamper på tippekupongen
	pure_res = [] #for kun resultatene, for å kunne velge gardering
	present_res = [] #liste for å presentere resultatene
	possible_res = {0:"H",1:"U",2:"B"}
	#
	#
	def tippekupong():
		for k in range(kamper):
			res = random.choice(list(possible_res.keys()))
			pure_res.append([res])#liste av lister, der resultatet av en kamp er en liste
			#resultatet av en gardert kamp er en liste med lengde > 1
			#
		#
	#
	#
	#
	def gardering():
		#gardering tar inn kupongen, og plukker ut to villkårlige kamper som skal halvgarderes
		#dette tilsvarer en kupong på 4 rekker jfr. Norsk Tipping
		gard_res = list(possible_res.keys())
		gard_kamper = random.sample(range(0,len(pure_res)),2)
		for g in range(len(gard_kamper)):
			gard_res.remove(pure_res[gard_kamper[g]][0])#pure_res liste av liste
			gard_choice = random.choice(gard_res)
			pure_res[gard_kamper[g]].append(gard_choice)
			pure_res[gard_kamper[g]].sort()#sorterer resultatene slik at de kommer "HUB"
			gard_res = list(possible_res.keys())
			#
		#
	#
	#
	#
	def tippetekst(): #skriver resultatene i tekstform
		for r in range(len(pure_res)):
			res_tekst = "Kamp nr. " + str((r+1)) + ": "
			for s in pure_res[r]:
				res_tekst += possible_res[s]
				#
			present_res.append(res_tekst)
			#
		#
	#
	#
	#
	## Call functions ##
	tippekupong()
	gardering()
	tippetekst()
	## Print results to screen ##
	#print(pure_res)
	for r in present_res:
		print(r,end="\n")
		#
	#
#
#
## Run program ##
main()
#
