def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0543, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 1773, "metric_value": 0.0169, "depth": 2}
		if obj[2]<=0:
			# {"feature": "unknownTest", "instances": 1142, "metric_value": 0.0119, "depth": 3}
			if obj[19]<=0:
				return 0.203757225433526
			elif obj[19]>0:
				return 0.39555555555555555
			else: return 0.39555555555555555
		elif obj[2]>0:
			# {"feature": "lazyTest", "instances": 631, "metric_value": 0.0176, "depth": 3}
			if obj[11]>0:
				return 0.46511627906976744
			elif obj[11]<=0:
				return 0.759493670886076
			else: return 0.759493670886076
		else: return 0.5388272583201268
	elif obj[0]>20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 884, "metric_value": 0.0164, "depth": 2}
		if obj[2]>0:
			# {"feature": "smellsCount", "instances": 709, "metric_value": 0.0263, "depth": 3}
			if obj[1]<=3:
				return 0.9533169533169533
			elif obj[1]>3:
				return 0.7880794701986755
			else: return 0.7880794701986755
		elif obj[2]<=0:
			# {"feature": "resourceOptimism", "instances": 175, "metric_value": 0.037, "depth": 3}
			if obj[16]<=0:
				return 0.6927710843373494
			elif obj[16]>0:
				return 0.0
			else: return 0.0
		else: return 0.6571428571428571
	else: return 0.8382352941176471
