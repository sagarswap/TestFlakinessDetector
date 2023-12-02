def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0256, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "constructorInitialization", "instances": 1773, "metric_value": 0.0058, "depth": 2}
		if obj[4]<=0:
			# {"feature": "sensitiveEquality", "instances": 1732, "metric_value": 0.0051, "depth": 3}
			if obj[17]<=0:
				return 0.10670172751454984
			elif obj[17]>0:
				return -0.21782242357730866
			else: return -0.21782242357730866
		elif obj[4]>0:
			# {"feature": "duplicateAssert", "instances": 41, "metric_value": 0.1036, "depth": 3}
			if obj[6]>0:
				return -0.4227700819892268
			elif obj[6]<=0:
				return -0.13065956830978392
			else: return -0.13065956830978392
		else: return -0.3515236152381432
	elif obj[0]>20.533684606699286:
		# {"feature": "generalFixture", "instances": 884, "metric_value": 0.0099, "depth": 2}
		if obj[9]<=0:
			# {"feature": "eagerTest", "instances": 850, "metric_value": 0.0106, "depth": 3}
			if obj[7]<=0:
				return -0.2820461329384522
			elif obj[7]>0:
				return -0.17497930916571858
			else: return -0.17497930916571858
		elif obj[9]>0:
			# {"feature": "smellsCount", "instances": 34, "metric_value": 0.036, "depth": 3}
			if obj[1]<=7:
				return 0.21634674817323685
			elif obj[1]>7:
				return -0.3938445448875427
			else: return -0.3938445448875427
		else: return 0.18045314269907334
	else: return -0.21629563793202872
