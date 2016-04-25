print "Welcome to Brogrammer"

wo = ""

while not wo.lower().startswith("chill" or "Chill"):
	
	print "Where's the focus, bro?"
	print "Enter Arms, Legs, Back, or Cardio:"

	ezR = 10
	medR = 15
	crayR = 20

	ezS = 3
	medS = 4
	crayS = 5

	wo = raw_input("> ")

	if wo == "Arms" or wo == "arms":
		print "Sun's out guns out, amirite?"
		print "OK, how hard are we going here, easy, medium, or CRAY?"

		effort = raw_input("> ")

		if effort == "easy" or effort == "Easy":
			print "Do %d sets of %d curls, %d sets of %d dips." % (ezS, ezR, ezS, ezR)
		elif effort == "medium" or effort == "Medium":
			print "Do %d sets of %d curls, %d sets of %d dips." % (medS, medR, medS, medR)
		elif effort == "CRAY" or effort == "cray":
			print "Get wild on %d sets of %d curls, %d sets of %d dips, and 50 pushups." % (crayS, crayR, crayS, crayR)
		else:
			print "%s sounds like a gnary typo, bro." % effort

		print "Hit return for another dose, or 'Chill' to quit"
		wo = raw_input("> ")		
	
			
	if wo == "Legs" or wo == "legs":
		print "Nice, urryday's a leg day."
		print "OK, how hard are we going here, easy, medium, or CRAY?"

		effort = raw_input("> ")

		if effort == "easy" or effort == "Easy":
			print "Do %d sets of %d leglifts, %d sets of %d hamstrings." % (ezS, ezR, ezS, ezR)
		elif effort == "medium" or effort == "Medium":
			print "Do %d sets of %d leglifts, %d sets of %d hamstrings." % (medS, medR, medS, medR)
		elif effort == "CRAY" or effort == "cray":
			print "Push through %d sets of %d leglifts, %d sets of %d hamstrings, and 50 lunges." % (crayS, crayR, crayS, crayR)
		else:
			print "%s sounds like a gnary typo, bro." % effort
			
		print "Hit return for another dose, or 'Chill' to quit"
		wo = raw_input("> ")
	

	if wo == "Back" or wo == "back":
		print "What's that they say about the straw and the camel?"
		print "How hard are we going here, easy, medium, or CRAY?"

		effort = raw_input("> ")

		if effort == "easy" or effort == "Easy":
			print "Do %d sets of %d rows, %d sets of %d pullups." % (ezS, ezR, ezS, ezR)
		elif effort == "medium" or effort == "Medium":
			print "Do %d sets of %d rows, %d sets of %d pullups." % (medS, medR, medS, medR)
		elif effort == "CRAY" or effort == "cray":
			print "Push through %d sets of %d rows, %d sets of %d pullups, and 100 reverse flys." % (crayS, crayR, crayS, crayR)
		else:
			print "%s sounds like a gnary typo, bro." % effort
			
		print "Hit return for another dose, or 'Chill' to quit"
		wo = raw_input("> ")	
	
	
	if wo == "Cardio" or wo == "cardio":
		print "Run Forrest!"
		print "Are you looking for something easy, medium, or CRAY?"

		effort = raw_input("> ")

		if effort == "easy" or effort == "Easy":
			print "Do 20 minutes on the treadmill at a 2% incline."
		elif effort == "medium" or effort == "Medium":
			print "Do 30 minutes on the treadmill at a 3% incline." 
		elif effort == "CRAY" or effort == "cray":
			print "Try out a 5 mile run alternating between 3% and 5% incline every quarter mile."
		else:
			print "%s sounds like a gnary typo, bro." % effort
		
		print "Hit return for another dose, or 'Chill' to quit"
		wo = raw_input("> ")
	
	else:
		print "%s sounds like a gnary typo, try again." % wo

print "OK good effort bro, get a shake."
