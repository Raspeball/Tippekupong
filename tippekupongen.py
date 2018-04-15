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
	possible_res = ("H","U","B") #en kamp ender alltid hjemme, borte eller uavgjort
	pure_res = [] #for kun resultatene, for å kunne velge gardering
	present_res = [] #liste for å presentere resultatene
	#
	#
	def tippekupong():
		for k in range(kamper):
			res = random.choice(possible_res)
			pure_res.append(res)
			res_tekst = "Kamp nr. " + str((k+1)) + ": " + res
			present_res.append(res_tekst)
			#
		#
	#
	#def rekker(): #dersom man skal legge til en funksjon som plukker garderinger basert på antall rekker på tippekupongen
	#
	#
	def gardering():
		#gardering tar inn kupongen, og plukker ut to villkårlige kamper som skal halvgarderes
		#dette tilsvarer en kupong på 4 rekker
		bong_res = list(possible_res)
		gard_kamper = random.sample(range(0,len(present_res)),2)
		for g in range(len(gard_kamper)):
			bong_res.remove(pure_res[gard_kamper[g]])
			gard_choice = random.choice(bong_res)
			pure_res[gard_kamper[g]] += gard_choice
			present_res[gard_kamper[g]] += gard_choice
			bong_res = list(possible_res)
			#
		#
	#
	#
	tippekupong()
	gardering()
	#print(pure_res)
	for r in present_res:
		print(r,end="\n")
		#
	#
#
#
#
main()
