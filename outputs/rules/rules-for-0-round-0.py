def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0543, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 1773, "metric_value": 0.0169, "depth": 2}
		if obj[2]<=0:
			# {"feature": "unknownTest", "instances": 1142, "metric_value": 0.0119, "depth": 3}
			if obj[19]<=0:
				return 0.796242774566474
			elif obj[19]>0:
				return 0.6044444444444445
			else: return 0.6044444444444445
		elif obj[2]>0:
			# {"feature": "lazyTest", "instances": 631, "metric_value": 0.0176, "depth": 3}
			if obj[11]>0:
				return 0.5348837209302325
			elif obj[11]<=0:
				return 0.24050632911392406
			else: return 0.24050632911392406
		else: return 0.4611727416798732
	elif obj[0]>20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 884, "metric_value": 0.0164, "depth": 2}
		if obj[2]>0:
			# {"feature": "smellsCount", "instances": 709, "metric_value": 0.0263, "depth": 3}
			if obj[1]<=3:
				return 0.04668304668304668
			elif obj[1]>3:
				return 0.2119205298013245
			else: return 0.2119205298013245
		elif obj[2]<=0:
			# {"feature": "resourceOptimism", "instances": 175, "metric_value": 0.037, "depth": 3}
			if obj[16]<=0:
				return 0.3072289156626506
			elif obj[16]>0:
				return 1.0
			else: return 1.0
		else: return 0.34285714285714286
	else: return 0.16176470588235295
