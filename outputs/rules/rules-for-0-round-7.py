def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "assertionRoulette", "instances": 2657, "metric_value": 0.028, "depth": 1}
	if obj[2]>0:
		# {"feature": "loc", "instances": 1340, "metric_value": 0.0186, "depth": 2}
		if obj[0]<=28.105223880597016:
			# {"feature": "lazyTest", "instances": 874, "metric_value": 0.0172, "depth": 3}
			if obj[11]>0:
				return -0.04198742097949389
			elif obj[11]<=0:
				return -0.299312006779339
			else: return -0.299312006779339
		elif obj[0]>28.105223880597016:
			# {"feature": "smellsCount", "instances": 466, "metric_value": 0.0162, "depth": 3}
			if obj[1]<=3:
				return -0.3364430409091622
			elif obj[1]>3:
				return -0.24332423673735726
			else: return -0.24332423673735726
		else: return -0.2968775404241464
	elif obj[2]<=0:
		# {"feature": "loc", "instances": 1317, "metric_value": 0.0516, "depth": 2}
		if obj[0]<=12.829916476841307:
			# {"feature": "unknownTest", "instances": 867, "metric_value": 0.0143, "depth": 3}
			if obj[19]<=0:
				return 0.3493514577735145
			elif obj[19]>0:
				return 0.18977707376819689
			else: return 0.18977707376819689
		elif obj[0]>12.829916476841307:
			# {"feature": "resourceOptimism", "instances": 450, "metric_value": 0.0291, "depth": 3}
			if obj[16]<=0:
				return -0.17502043226430583
			elif obj[16]>0:
				return 0.5220538467168808
			else: return 0.5220538467168808
		else: return -0.1440393531984753
	else: return 0.139934272999644
