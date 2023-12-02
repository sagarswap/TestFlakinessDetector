def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0182, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "constructorInitialization", "instances": 1773, "metric_value": 0.0056, "depth": 2}
		if obj[4]<=0:
			# {"feature": "sensitiveEquality", "instances": 1732, "metric_value": 0.005, "depth": 3}
			if obj[17]<=0:
				return -0.09044489681215609
			elif obj[17]>0:
				return 0.23003159277141094
			else: return 0.23003159277141094
		elif obj[4]>0:
			# {"feature": "duplicateAssert", "instances": 41, "metric_value": 0.1002, "depth": 3}
			if obj[6]>0:
				return 0.4289647936820984
			elif obj[6]<=0:
				return 0.14273486733436586
			else: return 0.14273486733436586
		else: return 0.35915261652411484
	elif obj[0]>20.533684606699286:
		# {"feature": "generalFixture", "instances": 884, "metric_value": 0.0099, "depth": 2}
		if obj[9]<=0:
			# {"feature": "eagerTest", "instances": 850, "metric_value": 0.0103, "depth": 3}
			if obj[7]<=0:
				return 0.24097032864713458
			elif obj[7]>0:
				return 0.13777977739921723
			else: return 0.13777977739921723
		elif obj[9]>0:
			# {"feature": "smellsCount", "instances": 34, "metric_value": 0.0364, "depth": 3}
			if obj[1]<=7:
				return -0.25474849063903093
			elif obj[1]>7:
				return 0.35981690883636475
			else: return 0.35981690883636475
		else: return -0.21859758478753707
	else: return 0.17706900811438106
