def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0273, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 1773, "metric_value": 0.014, "depth": 2}
		if obj[2]<=0:
			# {"feature": "unknownTest", "instances": 1142, "metric_value": 0.0126, "depth": 3}
			if obj[19]<=0:
				return -0.24513890068827338
			elif obj[19]>0:
				return -0.04768732216623094
			else: return -0.04768732216623094
		elif obj[2]>0:
			# {"feature": "lazyTest", "instances": 631, "metric_value": 0.0164, "depth": 3}
			if obj[11]>0:
				return -0.000995339601286874
			elif obj[11]<=0:
				return 0.2789789832468274
			else: return 0.2789789832468274
		else: return 0.06910916596131544
	elif obj[0]>20.533684606699286:
		# {"feature": "resourceOptimism", "instances": 884, "metric_value": 0.0097, "depth": 2}
		if obj[16]<=0:
			# {"feature": "sleepyTest", "instances": 859, "metric_value": 0.0102, "depth": 3}
			if obj[18]<=0:
				return 0.2258374672912504
			elif obj[18]>0:
				return 0.35651405979605283
			else: return 0.35651405979605283
		elif obj[16]>0:
			# {"feature": "assertionRoulette", "instances": 25, "metric_value": 0.1096, "depth": 3}
			if obj[2]>0:
				return -0.0973767638206482
			elif obj[2]<=0:
				return -0.5084054602517022
			else: return -0.5084054602517022
		else: return -0.24534709453582765
	else: return 0.22507716900757535