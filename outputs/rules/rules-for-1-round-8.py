def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0291, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "constructorInitialization", "instances": 1773, "metric_value": 0.0057, "depth": 2}
		if obj[4]<=0:
			# {"feature": "sensitiveEquality", "instances": 1732, "metric_value": 0.0045, "depth": 3}
			if obj[17]<=0:
				return -0.11400555626243425
			elif obj[17]>0:
				return 0.1830856878310442
			else: return 0.1830856878310442
		elif obj[4]>0:
			# {"feature": "duplicateAssert", "instances": 41, "metric_value": 0.1033, "depth": 3}
			if obj[6]>0:
				return 0.40279793162499705
			elif obj[6]<=0:
				return 0.1167949378490448
			else: return 0.1167949378490448
		else: return 0.33304110387476477
	elif obj[0]>20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 884, "metric_value": 0.0122, "depth": 2}
		if obj[2]>0:
			# {"feature": "smellsCount", "instances": 709, "metric_value": 0.0211, "depth": 3}
			if obj[1]<=3:
				return 0.321352317380085
			elif obj[1]>3:
				return 0.19727342334014691
			else: return 0.19727342334014691
		elif obj[2]<=0:
			# {"feature": "unknownTest", "instances": 175, "metric_value": 0.032, "depth": 3}
			if obj[19]<=0:
				return -0.017309922438401442
			elif obj[19]>0:
				return 0.29830819471129055
			else: return 0.29830819471129055
		else: return 0.08729493924549647
	else: return 0.23262848573572495
