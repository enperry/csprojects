# define the damn constituency
class constituency():
	def __init__(self, name, num, candidate):

		self.name = name
		self.num = num
		self.candidate = candidate
		self.elected = candidate[0]
		self.votesList = []
		for i in self.candidate:
			self.votesList.append(i.votes)

	def recalculate(votePercent):
		pass

	def __str__(self):
		return "Name: " + str(self.name) + "\nSeats to fill: " + str(self.num) + "\nCandidates: "
		
class candidate():
	def __init__(self, name, votes, party):

		self.name = name
		self.votes = votes
		self.party = party


def main():
	candidate1 = candidate("takisawa_motome", 239757, "jimin")
	candidate2 = candidate("odagiri_satoru", 206582, "rikken")
	candidate3 = candidate("koyama_hinako", 19310, "nkoku")

	candidatelist = [candidate1, candidate2, candidate3]

	constituency1 = constituency("aomori", 1, candidatelist)

	print(constituency1)

main()






	


