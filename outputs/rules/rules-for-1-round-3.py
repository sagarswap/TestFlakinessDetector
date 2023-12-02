def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0329, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 1773, "metric_value": 0.0139, "depth": 2}
		if obj[2]<=0:
			# {"feature": "unknownTest", "instances": 1142, "metric_value": 0.0126, "depth": 3}
			if obj[19]<=0:
				return -0.25719121068371514
			elif obj[19]>0:
				return -0.05934491780069139
			else: return -0.05934491780069139
		elif obj[2]>0:
			# {"feature": "lazyTest", "instances": 631, "metric_value": 0.0165, "depth": 3}
			if obj[11]>0:
				return -0.0137331760458916
			elif obj[11]<=0:
				return 0.266844776046427
			else: return 0.266844776046427
		else: return 0.05652247598356377
	elif obj[0]>20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 884, "metric_value": 0.0156, "depth": 2}
		if obj[2]>0:
			# {"feature": "smellsCount", "instances": 709, "metric_value": 0.021, "depth": 3}
			if obj[1]<=3:
				return 0.3529642022212542
			elif obj[1]>3:
				return 0.21559012439471997
			else: return 0.21559012439471997
		elif obj[2]<=0:
			# {"feature": "resourceOptimism", "instances": 175, "metric_value": 0.0325, "depth": 3}
			if obj[16]<=0:
				return 0.10920613537351768
			elif obj[16]>0:
				return -0.5580518477492862
			else: return -0.5580518477492862
		else: return 0.07489001052720207
	else: return 0.2509846150605387
