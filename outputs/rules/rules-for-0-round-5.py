def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2657, "metric_value": 0.0287, "depth": 1}
	if obj[0]<=20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 1773, "metric_value": 0.0139, "depth": 2}
		if obj[2]<=0:
			# {"feature": "unknownTest", "instances": 1142, "metric_value": 0.0127, "depth": 3}
			if obj[19]<=0:
				return 0.24922856740179777
			elif obj[19]>0:
				return 0.05129516151216295
			else: return 0.05129516151216295
		elif obj[2]>0:
			# {"feature": "lazyTest", "instances": 631, "metric_value": 0.0165, "depth": 3}
			if obj[11]>0:
				return 0.006080388140728811
			elif obj[11]<=0:
				return -0.27412534722044496
			else: return -0.27412534722044496
		else: return -0.06408206223496922
	elif obj[0]>20.533684606699286:
		# {"feature": "assertionRoulette", "instances": 884, "metric_value": 0.0156, "depth": 2}
		if obj[2]>0:
			# {"feature": "smellsCount", "instances": 709, "metric_value": 0.0209, "depth": 3}
			if obj[1]<=3:
				return -0.33406547297716727
			elif obj[1]>3:
				return -0.19724363404393985
			else: return -0.19724363404393985
		elif obj[2]<=0:
			# {"feature": "resourceOptimism", "instances": 175, "metric_value": 0.0325, "depth": 3}
			if obj[16]<=0:
				return -0.09044504004070558
			elif obj[16]>0:
				return 0.576436267958747
			else: return 0.576436267958747
		else: return -0.056148287057876584
	else: return -0.23230562807477978
