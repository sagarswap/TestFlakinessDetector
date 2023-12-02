def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0275, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "constructorInitialization", "instances": 1773, "metric_value": 0.0058, "depth": 2}
		if obj[4]<=0:
			# {"feature": "sensitiveEquality", "instances": 1732, "metric_value": 0.0051, "depth": 3}
			if obj[17]<=0:
				return -0.11050770235119374
			elif obj[17]>0:
				return 0.21406832113862037
			else: return 0.21406832113862037
		elif obj[4]>0:
			# {"feature": "duplicateAssert", "instances": 41, "metric_value": 0.1038, "depth": 3}
			if obj[6]>0:
				return 0.41921350071507113
			elif obj[6]<=0:
				return 0.12685143947601318
			else: return 0.12685143947601318
		else: return 0.34790568090066676
	elif obj[0]>20.533684606699286:
		# {"feature": "generalFixture", "instances": 884, "metric_value": 0.0099, "depth": 2}
		if obj[9]<=0:
			# {"feature": "eagerTest", "instances": 850, "metric_value": 0.0106, "depth": 3}
			if obj[7]<=0:
				return 0.29069362692370815
			elif obj[7]>0:
				return 0.1837110578110724
			else: return 0.1837110578110724
		elif obj[9]>0:
			# {"feature": "smellsCount", "instances": 34, "metric_value": 0.036, "depth": 3}
			if obj[1]<=7:
				return -0.20752571895718575
			elif obj[1]>7:
				return 0.4026375412940979
			else: return 0.4026375412940979
		else: return -0.1716337624718161
	else: return 0.22498748596437376
