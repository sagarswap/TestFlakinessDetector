def findDecision(obj): #obj[0]: index, obj[1]: loc, obj[2]: smellsCount, obj[3]: assertionRoulette, obj[4]: conditionalTestLogic, obj[5]: constructorInitialization, obj[6]: defaultTest, obj[7]: duplicateAssert, obj[8]: eagerTest, obj[9]: emptyTest, obj[10]: generalFixture, obj[11]: ignoredTest, obj[12]: lazyTest, obj[13]: magicNumberTest, obj[14]: mysteryGuest, obj[15]: printStatement, obj[16]: redundantAssertion, obj[17]: resourceOptimism, obj[18]: sensitiveEquality, obj[19]: sleepyTest, obj[20]: unknownTest, obj[21]: verboseTest
	# {"feature": "index", "instances": 2953, "metric_value": 0.2358, "depth": 1}
	if obj[0]<=1476.0:
		# {"feature": "loc", "instances": 1477, "metric_value": 0.0234, "depth": 2}
		if obj[1]<=28.857142857142858:
			# {"feature": "assertionRoulette", "instances": 946, "metric_value": 0.0124, "depth": 3}
			if obj[3]>0:
				# {"feature": "generalFixture", "instances": 542, "metric_value": 0.0144, "depth": 4}
				if obj[10]<=0:
					# {"feature": "sensitiveEquality", "instances": 522, "metric_value": 0.0091, "depth": 5}
					if obj[18]<=0:
						# {"feature": "eagerTest", "instances": 470, "metric_value": 0.0067, "depth": 6}
						if obj[8]<=0:
							# {"feature": "smellsCount", "instances": 268, "metric_value": 0.013, "depth": 7}
							if obj[2]<=3:
								# {"feature": "conditionalTestLogic", "instances": 220, "metric_value": 0.0067, "depth": 8}
								if obj[4]<=0:
									# {"feature": "lazyTest", "instances": 201, "metric_value": 0.0037, "depth": 9}
									if obj[12]<=0:
										# {"feature": "duplicateAssert", "instances": 123, "metric_value": 0.015, "depth": 10}
										if obj[7]<=0:
											# {"feature": "printStatement", "instances": 96, "metric_value": 0.0054, "depth": 11}
											if obj[15]<=0:
												# {"feature": "magicNumberTest", "instances": 89, "metric_value": 0.0049, "depth": 12}
												if obj[13]<=0:
													# {"feature": "sleepyTest", "instances": 66, "metric_value": 0.0038, "depth": 13}
													if obj[19]<=0:
														# {"feature": "constructorInitialization", "instances": 62, "metric_value": 0.0, "depth": 14}
														if obj[5]<=0:
															# {"feature": "defaultTest", "instances": 62, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 62, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 62, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "mysteryGuest", "instances": 62, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 62, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 62, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 62, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 62, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9838709677419355
																					else: return 0.9838709677419355
																				else: return 0.9838709677419355
																			else: return 0.9838709677419355
																		else: return 0.9838709677419355
																	else: return 0.9838709677419355
																else: return 0.9838709677419355
															else: return 0.9838709677419355
														else: return 0.9838709677419355
													elif obj[19]>0:
														return 1
													else: return 1.0
												elif obj[13]>0:
													# {"feature": "constructorInitialization", "instances": 23, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "defaultTest", "instances": 23, "metric_value": 0.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "emptyTest", "instances": 23, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "ignoredTest", "instances": 23, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "mysteryGuest", "instances": 23, "metric_value": 0.0, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 23, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 23, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 23, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 23, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 23, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9565217391304348
																					else: return 0.9565217391304348
																				else: return 0.9565217391304348
																			else: return 0.9565217391304348
																		else: return 0.9565217391304348
																	else: return 0.9565217391304348
																else: return 0.9565217391304348
															else: return 0.9565217391304348
														else: return 0.9565217391304348
													else: return 0.9565217391304348
												else: return 0.9565217391304348
											elif obj[15]>0:
												return 1
											else: return 1.0
										elif obj[7]>0:
											return 1
										else: return 1.0
									elif obj[12]>0:
										# {"feature": "magicNumberTest", "instances": 78, "metric_value": 0.0217, "depth": 10}
										if obj[13]<=0:
											# {"feature": "constructorInitialization", "instances": 62, "metric_value": 0.0112, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 56, "metric_value": 0.0003, "depth": 12}
												if obj[7]<=0:
													# {"feature": "defaultTest", "instances": 40, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 40, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 40, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "mysteryGuest", "instances": 40, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 40, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 40, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 40, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 40, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 40, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 40, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.95
																					else: return 0.95
																				else: return 0.95
																			else: return 0.95
																		else: return 0.95
																	else: return 0.95
																else: return 0.95
															else: return 0.95
														else: return 0.95
													else: return 0.95
												elif obj[7]>0:
													# {"feature": "defaultTest", "instances": 16, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 16, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 16, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "mysteryGuest", "instances": 16, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 16, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 16, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 16, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 16, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 16, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 16, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9375
																					else: return 0.9375
																				else: return 0.9375
																			else: return 0.9375
																		else: return 0.9375
																	else: return 0.9375
																else: return 0.9375
															else: return 0.9375
														else: return 0.9375
													else: return 0.9375
												else: return 0.9375
											elif obj[5]>0:
												return 1
											else: return 1.0
										elif obj[13]>0:
											return 1
										else: return 1.0
									else: return 0.9615384615384616
								elif obj[4]>0:
									return 1
								else: return 1.0
							elif obj[2]>3:
								return 1
							else: return 1.0
						elif obj[8]>0:
							# {"feature": "duplicateAssert", "instances": 202, "metric_value": 0.0083, "depth": 7}
							if obj[7]<=0:
								# {"feature": "smellsCount", "instances": 144, "metric_value": 0.0107, "depth": 8}
								if obj[2]>2:
									# {"feature": "lazyTest", "instances": 133, "metric_value": 0.0135, "depth": 9}
									if obj[12]>0:
										# {"feature": "constructorInitialization", "instances": 132, "metric_value": 0.0078, "depth": 10}
										if obj[5]<=0:
											# {"feature": "conditionalTestLogic", "instances": 130, "metric_value": 0.007, "depth": 11}
											if obj[4]<=0:
												# {"feature": "magicNumberTest", "instances": 123, "metric_value": 0.0033, "depth": 12}
												if obj[13]<=0:
													# {"feature": "mysteryGuest", "instances": 93, "metric_value": 0.0001, "depth": 13}
													if obj[14]<=0:
														# {"feature": "resourceOptimism", "instances": 68, "metric_value": 0.0127, "depth": 14}
														if obj[17]<=0:
															# {"feature": "defaultTest", "instances": 62, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 62, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 62, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "printStatement", "instances": 62, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 62, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 62, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 62, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 62, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9193548387096774
																					else: return 0.9193548387096774
																				else: return 0.9193548387096774
																			else: return 0.9193548387096774
																		else: return 0.9193548387096774
																	else: return 0.9193548387096774
																else: return 0.9193548387096774
															else: return 0.9193548387096774
														elif obj[17]>0:
															return 1
														else: return 1.0
													elif obj[14]>0:
														# {"feature": "resourceOptimism", "instances": 25, "metric_value": 0.0084, "depth": 14}
														if obj[17]<=0:
															# {"feature": "defaultTest", "instances": 18, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 18, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 18, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "printStatement", "instances": 18, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 18, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 18, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 18, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 18, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9444444444444444
																					else: return 0.9444444444444444
																				else: return 0.9444444444444444
																			else: return 0.9444444444444444
																		else: return 0.9444444444444444
																	else: return 0.9444444444444444
																else: return 0.9444444444444444
															else: return 0.9444444444444444
														elif obj[17]>0:
															# {"feature": "defaultTest", "instances": 7, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 7, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 7, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "printStatement", "instances": 7, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 7, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 7, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 7, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 7, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.8571428571428571
																					else: return 0.8571428571428571
																				else: return 0.8571428571428571
																			else: return 0.8571428571428571
																		else: return 0.8571428571428571
																	else: return 0.8571428571428571
																else: return 0.8571428571428571
															else: return 0.8571428571428571
														else: return 0.8571428571428571
													else: return 0.92
												elif obj[13]>0:
													# {"feature": "defaultTest", "instances": 30, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 30, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 30, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "mysteryGuest", "instances": 30, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 30, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 30, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 30, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 30, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 30, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 30, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9666666666666667
																					else: return 0.9666666666666667
																				else: return 0.9666666666666667
																			else: return 0.9666666666666667
																		else: return 0.9666666666666667
																	else: return 0.9666666666666667
																else: return 0.9666666666666667
															else: return 0.9666666666666667
														else: return 0.9666666666666667
													else: return 0.9666666666666667
												else: return 0.9666666666666667
											elif obj[4]>0:
												return 1
											else: return 1.0
										elif obj[5]>0:
											return 0.5
										else: return 0.5
									elif obj[12]<=0:
										return 0
									else: return 0.0
								elif obj[2]<=2:
									return 1
								else: return 1.0
							elif obj[7]>0:
								# {"feature": "smellsCount", "instances": 58, "metric_value": 0.0225, "depth": 8}
								if obj[2]<=4:
									# {"feature": "lazyTest", "instances": 40, "metric_value": 0.002, "depth": 9}
									if obj[12]>0:
										# {"feature": "conditionalTestLogic", "instances": 39, "metric_value": 0.0, "depth": 10}
										if obj[4]<=0:
											# {"feature": "constructorInitialization", "instances": 39, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "defaultTest", "instances": 39, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 39, "metric_value": 0.0, "depth": 13}
													if obj[9]<=0:
														# {"feature": "ignoredTest", "instances": 39, "metric_value": 0.0, "depth": 14}
														if obj[11]<=0.0:
															# {"feature": "magicNumberTest", "instances": 39, "metric_value": 0.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "mysteryGuest", "instances": 39, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 39, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 39, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 39, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 39, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 39, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 39, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9743589743589743
																					else: return 0.9743589743589743
																				else: return 0.9743589743589743
																			else: return 0.9743589743589743
																		else: return 0.9743589743589743
																	else: return 0.9743589743589743
																else: return 0.9743589743589743
															else: return 0.9743589743589743
														else: return 0.9743589743589743
													else: return 0.9743589743589743
												else: return 0.9743589743589743
											else: return 0.9743589743589743
										else: return 0.9743589743589743
									elif obj[12]<=0:
										return 1
									else: return 1.0
								elif obj[2]>4:
									return 1
								else: return 1.0
							else: return 0.9827586206896551
						else: return 0.9455445544554455
					elif obj[18]>0:
						return 1
					else: return 1.0
				elif obj[10]>0:
					# {"feature": "lazyTest", "instances": 20, "metric_value": 0.1583, "depth": 5}
					if obj[12]>0:
						# {"feature": "magicNumberTest", "instances": 12, "metric_value": 0.0918, "depth": 6}
						if obj[13]<=0:
							# {"feature": "smellsCount", "instances": 10, "metric_value": 0.0427, "depth": 7}
							if obj[2]<=5:
								# {"feature": "eagerTest", "instances": 9, "metric_value": 0.0323, "depth": 8}
								if obj[8]>0:
									# {"feature": "duplicateAssert", "instances": 5, "metric_value": 0.0071, "depth": 9}
									if obj[7]<=0:
										return 0.3333333333333333
									elif obj[7]>0:
										return 0.5
									else: return 0.5
								elif obj[8]<=0:
									return 0.75
								else: return 0.75
							elif obj[2]>5:
								return 1
							else: return 1.0
						elif obj[13]>0:
							return 0
						else: return 0.0
					elif obj[12]<=0:
						return 1
					else: return 1.0
				else: return 0.7
			elif obj[3]<=0:
				# {"feature": "unknownTest", "instances": 404, "metric_value": 0.0252, "depth": 4}
				if obj[20]>0:
					# {"feature": "mysteryGuest", "instances": 216, "metric_value": 0.0102, "depth": 5}
					if obj[14]<=0:
						# {"feature": "lazyTest", "instances": 215, "metric_value": 0.0137, "depth": 6}
						if obj[12]<=0:
							# {"feature": "conditionalTestLogic", "instances": 132, "metric_value": 0.0078, "depth": 7}
							if obj[4]<=0:
								# {"feature": "generalFixture", "instances": 130, "metric_value": 0.0038, "depth": 8}
								if obj[10]<=0:
									# {"feature": "smellsCount", "instances": 114, "metric_value": 0.001, "depth": 9}
									if obj[2]<=1:
										# {"feature": "constructorInitialization", "instances": 113, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "defaultTest", "instances": 113, "metric_value": 0.0, "depth": 11}
											if obj[6]<=0:
												# {"feature": "duplicateAssert", "instances": 113, "metric_value": 0.0, "depth": 12}
												if obj[7]<=0:
													# {"feature": "eagerTest", "instances": 113, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "emptyTest", "instances": 113, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 113, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "magicNumberTest", "instances": 113, "metric_value": 0.0, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 113, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 113, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 113, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sensitiveEquality", "instances": 113, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "sleepyTest", "instances": 113, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 113, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9469026548672567
																					else: return 0.9469026548672567
																				else: return 0.9469026548672567
																			else: return 0.9469026548672567
																		else: return 0.9469026548672567
																	else: return 0.9469026548672567
																else: return 0.9469026548672567
															else: return 0.9469026548672567
														else: return 0.9469026548672567
													else: return 0.9469026548672567
												else: return 0.9469026548672567
											else: return 0.9469026548672567
										else: return 0.9469026548672567
									elif obj[2]>1:
										return 1
									else: return 1.0
								elif obj[10]>0:
									# {"feature": "smellsCount", "instances": 16, "metric_value": 0.0, "depth": 9}
									if obj[2]<=2:
										# {"feature": "constructorInitialization", "instances": 16, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "defaultTest", "instances": 16, "metric_value": 0.0, "depth": 11}
											if obj[6]<=0:
												# {"feature": "duplicateAssert", "instances": 16, "metric_value": 0.0, "depth": 12}
												if obj[7]<=0:
													# {"feature": "eagerTest", "instances": 16, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "emptyTest", "instances": 16, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 16, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "magicNumberTest", "instances": 16, "metric_value": 0.0, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 16, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 16, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 16, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sensitiveEquality", "instances": 16, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "sleepyTest", "instances": 16, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 16, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.875
																					else: return 0.875
																				else: return 0.875
																			else: return 0.875
																		else: return 0.875
																	else: return 0.875
																else: return 0.875
															else: return 0.875
														else: return 0.875
													else: return 0.875
												else: return 0.875
											else: return 0.875
										else: return 0.875
									else: return 0.875
								else: return 0.875
							elif obj[4]>0:
								return 0.5
							else: return 0.5
						elif obj[12]>0:
							# {"feature": "smellsCount", "instances": 83, "metric_value": 0.0076, "depth": 7}
							if obj[2]<=2:
								# {"feature": "conditionalTestLogic", "instances": 72, "metric_value": 0.0, "depth": 8}
								if obj[4]<=0:
									# {"feature": "constructorInitialization", "instances": 72, "metric_value": 0.0, "depth": 9}
									if obj[5]<=0:
										# {"feature": "defaultTest", "instances": 72, "metric_value": 0.0, "depth": 10}
										if obj[6]<=0:
											# {"feature": "duplicateAssert", "instances": 72, "metric_value": 0.0, "depth": 11}
											if obj[7]<=0:
												# {"feature": "eagerTest", "instances": 72, "metric_value": 0.0, "depth": 12}
												if obj[8]<=0:
													# {"feature": "emptyTest", "instances": 72, "metric_value": 0.0, "depth": 13}
													if obj[9]<=0:
														# {"feature": "generalFixture", "instances": 72, "metric_value": 0.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "ignoredTest", "instances": 72, "metric_value": 0.0, "depth": 15}
															if obj[11]<=0.0:
																# {"feature": "magicNumberTest", "instances": 72, "metric_value": 0.0, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 72, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 72, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 72, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sensitiveEquality", "instances": 72, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "sleepyTest", "instances": 72, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 72, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9861111111111112
																					else: return 0.9861111111111112
																				else: return 0.9861111111111112
																			else: return 0.9861111111111112
																		else: return 0.9861111111111112
																	else: return 0.9861111111111112
																else: return 0.9861111111111112
															else: return 0.9861111111111112
														else: return 0.9861111111111112
													else: return 0.9861111111111112
												else: return 0.9861111111111112
											else: return 0.9861111111111112
										else: return 0.9861111111111112
									else: return 0.9861111111111112
								else: return 0.9861111111111112
							elif obj[2]>2:
								return 1
							else: return 1.0
						else: return 0.9879518072289156
					elif obj[14]>0:
						return 0
					else: return 0.0
				elif obj[20]<=0:
					# {"feature": "conditionalTestLogic", "instances": 188, "metric_value": 0.0106, "depth": 5}
					if obj[4]<=0:
						# {"feature": "eagerTest", "instances": 178, "metric_value": 0.0082, "depth": 6}
						if obj[8]<=0:
							# {"feature": "duplicateAssert", "instances": 142, "metric_value": 0.0081, "depth": 7}
							if obj[7]<=0:
								# {"feature": "sleepyTest", "instances": 141, "metric_value": 0.0077, "depth": 8}
								if obj[19]<=0:
									# {"feature": "printStatement", "instances": 136, "metric_value": 0.0049, "depth": 9}
									if obj[15]<=0:
										# {"feature": "mysteryGuest", "instances": 133, "metric_value": 0.0034, "depth": 10}
										if obj[14]<=0:
											# {"feature": "smellsCount", "instances": 131, "metric_value": 0.0023, "depth": 11}
											if obj[2]>0:
												# {"feature": "generalFixture", "instances": 100, "metric_value": 0.0001, "depth": 12}
												if obj[10]<=0:
													# {"feature": "lazyTest", "instances": 75, "metric_value": 0.0058, "depth": 13}
													if obj[12]>0:
														# {"feature": "magicNumberTest", "instances": 73, "metric_value": 0.0083, "depth": 14}
														if obj[13]<=0:
															# {"feature": "sensitiveEquality", "instances": 70, "metric_value": 0.0001, "depth": 15}
															if obj[18]<=0:
																# {"feature": "constructorInitialization", "instances": 64, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 64, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 64, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 64, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 64, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "resourceOptimism", "instances": 64, "metric_value": 0.0, "depth": 21}
																					if obj[17]<=0:
																						# {"feature": "verboseTest", "instances": 64, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.859375
																					else: return 0.859375
																				else: return 0.859375
																			else: return 0.859375
																		else: return 0.859375
																	else: return 0.859375
																else: return 0.859375
															elif obj[18]>0:
																# {"feature": "constructorInitialization", "instances": 6, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 6, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 6, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 6, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 6, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "resourceOptimism", "instances": 6, "metric_value": 0.0, "depth": 21}
																					if obj[17]<=0:
																						# {"feature": "verboseTest", "instances": 6, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.8333333333333334
																					else: return 0.8333333333333334
																				else: return 0.8333333333333334
																			else: return 0.8333333333333334
																		else: return 0.8333333333333334
																	else: return 0.8333333333333334
																else: return 0.8333333333333334
															else: return 0.8333333333333334
														elif obj[13]>0:
															return 1
														else: return 1.0
													elif obj[12]<=0:
														return 0.5
													else: return 0.5
												elif obj[10]>0:
													# {"feature": "lazyTest", "instances": 25, "metric_value": 0.0466, "depth": 13}
													if obj[12]>0:
														# {"feature": "constructorInitialization", "instances": 20, "metric_value": 0.0, "depth": 14}
														if obj[5]<=0:
															# {"feature": "defaultTest", "instances": 20, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 20, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 20, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "magicNumberTest", "instances": 20, "metric_value": 0.0, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 20, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 20, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "sensitiveEquality", "instances": 20, "metric_value": 0.0, "depth": 21}
																					if obj[18]<=0:
																						# {"feature": "verboseTest", "instances": 20, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.8
																					else: return 0.8
																				else: return 0.8
																			else: return 0.8
																		else: return 0.8
																	else: return 0.8
																else: return 0.8
															else: return 0.8
														else: return 0.8
													elif obj[12]<=0:
														return 1
													else: return 1.0
												else: return 0.84
											elif obj[2]<=0:
												# {"feature": "constructorInitialization", "instances": 31, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "defaultTest", "instances": 31, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 31, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "generalFixture", "instances": 31, "metric_value": 0.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "ignoredTest", "instances": 31, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "lazyTest", "instances": 31, "metric_value": 0.0, "depth": 17}
																	if obj[12]<=0:
																		# {"feature": "magicNumberTest", "instances": 31, "metric_value": 0.0, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 31, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 31, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "sensitiveEquality", "instances": 31, "metric_value": 0.0, "depth": 21}
																					if obj[18]<=0:
																						# {"feature": "verboseTest", "instances": 31, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.7741935483870968
																					else: return 0.7741935483870968
																				else: return 0.7741935483870968
																			else: return 0.7741935483870968
																		else: return 0.7741935483870968
																	else: return 0.7741935483870968
																else: return 0.7741935483870968
															else: return 0.7741935483870968
														else: return 0.7741935483870968
													else: return 0.7741935483870968
												else: return 0.7741935483870968
											else: return 0.7741935483870968
										elif obj[14]>0:
											return 1
										else: return 1.0
									elif obj[15]>0:
										return 1
									else: return 1.0
								elif obj[19]>0:
									return 1
								else: return 1.0
							elif obj[7]>0:
								return 0
							else: return 0.0
						elif obj[8]>0:
							# {"feature": "lazyTest", "instances": 36, "metric_value": 0.0632, "depth": 7}
							if obj[12]>0:
								# {"feature": "smellsCount", "instances": 30, "metric_value": 0.0253, "depth": 8}
								if obj[2]<=2:
									# {"feature": "constructorInitialization", "instances": 23, "metric_value": 0.0, "depth": 9}
									if obj[5]<=0:
										# {"feature": "defaultTest", "instances": 23, "metric_value": 0.0, "depth": 10}
										if obj[6]<=0:
											# {"feature": "duplicateAssert", "instances": 23, "metric_value": 0.0, "depth": 11}
											if obj[7]<=0:
												# {"feature": "emptyTest", "instances": 23, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													# {"feature": "generalFixture", "instances": 23, "metric_value": 0.0, "depth": 13}
													if obj[10]<=0:
														# {"feature": "ignoredTest", "instances": 23, "metric_value": 0.0, "depth": 14}
														if obj[11]<=0.0:
															# {"feature": "magicNumberTest", "instances": 23, "metric_value": 0.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "mysteryGuest", "instances": 23, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 23, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 23, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 23, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sensitiveEquality", "instances": 23, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "sleepyTest", "instances": 23, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 23, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.5217391304347826
																					else: return 0.5217391304347826
																				else: return 0.5217391304347826
																			else: return 0.5217391304347826
																		else: return 0.5217391304347826
																	else: return 0.5217391304347826
																else: return 0.5217391304347826
															else: return 0.5217391304347826
														else: return 0.5217391304347826
													else: return 0.5217391304347826
												else: return 0.5217391304347826
											else: return 0.5217391304347826
										else: return 0.5217391304347826
									else: return 0.5217391304347826
								elif obj[2]>2:
									# {"feature": "generalFixture", "instances": 7, "metric_value": 0.0305, "depth": 9}
									if obj[10]>0:
										# {"feature": "constructorInitialization", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "defaultTest", "instances": 6, "metric_value": 0.0, "depth": 11}
											if obj[6]<=0:
												# {"feature": "duplicateAssert", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[7]<=0:
													# {"feature": "emptyTest", "instances": 6, "metric_value": 0.0, "depth": 13}
													if obj[9]<=0:
														# {"feature": "ignoredTest", "instances": 6, "metric_value": 0.0, "depth": 14}
														if obj[11]<=0.0:
															# {"feature": "magicNumberTest", "instances": 6, "metric_value": 0.0, "depth": 15}
															if obj[13]<=1:
																# {"feature": "mysteryGuest", "instances": 6, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "printStatement", "instances": 6, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "redundantAssertion", "instances": 6, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 6, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sensitiveEquality", "instances": 6, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "sleepyTest", "instances": 6, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 6, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.8333333333333334
																					else: return 0.8333333333333334
																				else: return 0.8333333333333334
																			else: return 0.8333333333333334
																		else: return 0.8333333333333334
																	else: return 0.8333333333333334
																else: return 0.8333333333333334
															else: return 0.8333333333333334
														else: return 0.8333333333333334
													else: return 0.8333333333333334
												else: return 0.8333333333333334
											else: return 0.8333333333333334
										else: return 0.8333333333333334
									elif obj[10]<=0:
										return 1
									else: return 1.0
								else: return 0.8571428571428571
							elif obj[12]<=0:
								return 1
							else: return 1.0
						else: return 0.6666666666666666
					elif obj[4]>0:
						# {"feature": "mysteryGuest", "instances": 10, "metric_value": 0.2449, "depth": 6}
						if obj[14]<=0:
							# {"feature": "printStatement", "instances": 7, "metric_value": 0.3499, "depth": 7}
							if obj[15]<=0:
								return 0
							elif obj[15]>0:
								return 1
							else: return 1.0
						elif obj[14]>0:
							return 1
						else: return 1.0
					else: return 0.4
				else: return 0.7819148936170213
			else: return 0.8712871287128713
		elif obj[1]>28.857142857142858:
			# {"feature": "smellsCount", "instances": 531, "metric_value": 0.0141, "depth": 3}
			if obj[2]>2:
				# {"feature": "resourceOptimism", "instances": 351, "metric_value": 0.0116, "depth": 4}
				if obj[17]<=0:
					# {"feature": "printStatement", "instances": 346, "metric_value": 0.0042, "depth": 5}
					if obj[15]<=0:
						# {"feature": "sleepyTest", "instances": 309, "metric_value": 0.0047, "depth": 6}
						if obj[19]<=0:
							# {"feature": "magicNumberTest", "instances": 252, "metric_value": 0.0306, "depth": 7}
							if obj[13]<=0:
								return 1
							elif obj[13]>0:
								# {"feature": "duplicateAssert", "instances": 67, "metric_value": 0.0342, "depth": 8}
								if obj[7]>0:
									# {"feature": "lazyTest", "instances": 35, "metric_value": 0.0636, "depth": 9}
									if obj[12]<=0:
										return 1
									elif obj[12]>0:
										# {"feature": "conditionalTestLogic", "instances": 14, "metric_value": 0.0978, "depth": 10}
										if obj[4]>0:
											return 1
										elif obj[4]<=0:
											# {"feature": "eagerTest", "instances": 6, "metric_value": 0.0393, "depth": 11}
											if obj[8]>0:
												# {"feature": "assertionRoulette", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[3]<=1:
													# {"feature": "constructorInitialization", "instances": 5, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "defaultTest", "instances": 5, "metric_value": 0.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "emptyTest", "instances": 5, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "generalFixture", "instances": 5, "metric_value": 0.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "mysteryGuest", "instances": 5, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sensitiveEquality", "instances": 5, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "unknownTest", "instances": 5, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 5, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.8
																					else: return 0.8
																				else: return 0.8
																			else: return 0.8
																		else: return 0.8
																	else: return 0.8
																else: return 0.8
															else: return 0.8
														else: return 0.8
													else: return 0.8
												else: return 0.8
											elif obj[8]<=0:
												return 1
											else: return 1.0
										else: return 0.8333333333333334
									else: return 0.9285714285714286
								elif obj[7]<=0:
									return 1
								else: return 1.0
							else: return 0.9850746268656716
						elif obj[19]>0:
							# {"feature": "lazyTest", "instances": 57, "metric_value": 0.0246, "depth": 7}
							if obj[12]<=0:
								# {"feature": "conditionalTestLogic", "instances": 38, "metric_value": 0.0044, "depth": 8}
								if obj[4]>0:
									# {"feature": "assertionRoulette", "instances": 36, "metric_value": 0.0, "depth": 9}
									if obj[3]<=1:
										# {"feature": "constructorInitialization", "instances": 36, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "defaultTest", "instances": 36, "metric_value": 0.0, "depth": 11}
											if obj[6]<=0:
												# {"feature": "duplicateAssert", "instances": 36, "metric_value": 0.0, "depth": 12}
												if obj[7]<=0:
													# {"feature": "eagerTest", "instances": 36, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "emptyTest", "instances": 36, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "generalFixture", "instances": 36, "metric_value": 0.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "ignoredTest", "instances": 36, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "magicNumberTest", "instances": 36, "metric_value": 0.0, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "mysteryGuest", "instances": 36, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 36, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sensitiveEquality", "instances": 36, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "unknownTest", "instances": 36, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 36, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.9722222222222222
																					else: return 0.9722222222222222
																				else: return 0.9722222222222222
																			else: return 0.9722222222222222
																		else: return 0.9722222222222222
																	else: return 0.9722222222222222
																else: return 0.9722222222222222
															else: return 0.9722222222222222
														else: return 0.9722222222222222
													else: return 0.9722222222222222
												else: return 0.9722222222222222
											else: return 0.9722222222222222
										else: return 0.9722222222222222
									else: return 0.9722222222222222
								elif obj[4]<=0:
									return 1
								else: return 1.0
							elif obj[12]>0:
								return 1
							else: return 1.0
						else: return 0.9824561403508771
					elif obj[15]>0:
						return 1
					else: return 1.0
				elif obj[17]>0:
					# {"feature": "conditionalTestLogic", "instances": 5, "metric_value": 0.4, "depth": 5}
					if obj[4]<=0:
						return 1
					elif obj[4]>0:
						return 0
					else: return 0.0
				else: return 0.8
			elif obj[2]<=2:
				return 1
			else: return 1.0
		else: return 0.9943502824858758
	elif obj[0]>1476.0:
		# {"feature": "loc", "instances": 1476, "metric_value": 0.0217, "depth": 2}
		if obj[1]<=12.392953929539296:
			# {"feature": "resourceOptimism", "instances": 1010, "metric_value": 0.0032, "depth": 3}
			if obj[17]<=0:
				# {"feature": "magicNumberTest", "instances": 983, "metric_value": 0.0022, "depth": 4}
				if obj[13]<=0:
					# {"feature": "printStatement", "instances": 888, "metric_value": 0.0025, "depth": 5}
					if obj[15]<=0:
						# {"feature": "assertionRoulette", "instances": 887, "metric_value": 0.0012, "depth": 6}
						if obj[3]<=0:
							# {"feature": "duplicateAssert", "instances": 734, "metric_value": 0.0009, "depth": 7}
							if obj[7]<=0:
								# {"feature": "smellsCount", "instances": 728, "metric_value": 0.0007, "depth": 8}
								if obj[2]<=3:
									# {"feature": "conditionalTestLogic", "instances": 721, "metric_value": 0.0009, "depth": 9}
									if obj[4]<=0:
										# {"feature": "eagerTest", "instances": 701, "metric_value": 0.0015, "depth": 10}
										if obj[8]<=0:
											# {"feature": "mysteryGuest", "instances": 602, "metric_value": 0.0005, "depth": 11}
											if obj[14]<=0:
												# {"feature": "sensitiveEquality", "instances": 599, "metric_value": 0.0005, "depth": 12}
												if obj[18]<=0:
													# {"feature": "generalFixture", "instances": 596, "metric_value": 0.0003, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 507, "metric_value": 0.0008, "depth": 14}
														if obj[12]<=0:
															# {"feature": "unknownTest", "instances": 273, "metric_value": 0.0038, "depth": 15}
															if obj[20]>0:
																# {"feature": "constructorInitialization", "instances": 188, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 188, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 188, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 188, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 188, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 188, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 188, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.026595744680851064
																					else: return 0.026595744680851064
																				else: return 0.026595744680851064
																			else: return 0.026595744680851064
																		else: return 0.026595744680851064
																	else: return 0.026595744680851064
																else: return 0.026595744680851064
															elif obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 85, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 85, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 85, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 85, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 85, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 85, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 85, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.058823529411764705
																					else: return 0.058823529411764705
																				else: return 0.058823529411764705
																			else: return 0.058823529411764705
																		else: return 0.058823529411764705
																	else: return 0.058823529411764705
																else: return 0.058823529411764705
															else: return 0.058823529411764705
														elif obj[12]>0:
															# {"feature": "unknownTest", "instances": 234, "metric_value": 0.0034, "depth": 15}
															if obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 190, "metric_value": 0.0006, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 189, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 189, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 189, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 189, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 189, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 189, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.042328042328042326
																					else: return 0.042328042328042326
																				else: return 0.042328042328042326
																			else: return 0.042328042328042326
																		else: return 0.042328042328042326
																	else: return 0.042328042328042326
																elif obj[5]>0:
																	return 0
																else: return 0.0
															elif obj[20]>0:
																# {"feature": "constructorInitialization", "instances": 44, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 44, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 44, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 44, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 44, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 44, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 44, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.09090909090909091
																					else: return 0.09090909090909091
																				else: return 0.09090909090909091
																			else: return 0.09090909090909091
																		else: return 0.09090909090909091
																	else: return 0.09090909090909091
																else: return 0.09090909090909091
															else: return 0.09090909090909091
														else: return 0.05128205128205128
													elif obj[10]>0:
														# {"feature": "lazyTest", "instances": 89, "metric_value": 0.009, "depth": 14}
														if obj[12]>0:
															# {"feature": "unknownTest", "instances": 74, "metric_value": 0.0129, "depth": 15}
															if obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 65, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 65, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 65, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 65, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 65, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 65, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 65, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.046153846153846156
																					else: return 0.046153846153846156
																				else: return 0.046153846153846156
																			else: return 0.046153846153846156
																		else: return 0.046153846153846156
																	else: return 0.046153846153846156
																else: return 0.046153846153846156
															elif obj[20]>0:
																return 0
															else: return 0.0
														elif obj[12]<=0:
															# {"feature": "unknownTest", "instances": 15, "metric_value": 0.0136, "depth": 15}
															if obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 11, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 11, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 11, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 11, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 11, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 11, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 11, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.09090909090909091
																					else: return 0.09090909090909091
																				else: return 0.09090909090909091
																			else: return 0.09090909090909091
																		else: return 0.09090909090909091
																	else: return 0.09090909090909091
																else: return 0.09090909090909091
															elif obj[20]>0:
																return 0.25
															else: return 0.25
														else: return 0.13333333333333333
													else: return 0.056179775280898875
												elif obj[18]>0:
													return 0
												else: return 0.0
											elif obj[14]>0:
												return 0
											else: return 0.0
										elif obj[8]>0:
											# {"feature": "sensitiveEquality", "instances": 99, "metric_value": 0.0212, "depth": 11}
											if obj[18]<=0:
												# {"feature": "unknownTest", "instances": 93, "metric_value": 0.01, "depth": 12}
												if obj[20]<=0:
													# {"feature": "generalFixture", "instances": 76, "metric_value": 0.0095, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 64, "metric_value": 0.005, "depth": 14}
														if obj[12]>0:
															# {"feature": "constructorInitialization", "instances": 59, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 59, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 59, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 59, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "mysteryGuest", "instances": 59, "metric_value": 0.0, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 59, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 59, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 59, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.01694915254237288
																					else: return 0.01694915254237288
																				else: return 0.01694915254237288
																			else: return 0.01694915254237288
																		else: return 0.01694915254237288
																	else: return 0.01694915254237288
																else: return 0.01694915254237288
															else: return 0.01694915254237288
														elif obj[12]<=0:
															return 0
														else: return 0.0
													elif obj[10]>0:
														return 0
													else: return 0.0
												elif obj[20]>0:
													return 0
												else: return 0.0
											elif obj[18]>0:
												# {"feature": "constructorInitialization", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "defaultTest", "instances": 6, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 6, "metric_value": 0.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "generalFixture", "instances": 6, "metric_value": 0.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "ignoredTest", "instances": 6, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "lazyTest", "instances": 6, "metric_value": 0.0, "depth": 17}
																	if obj[12]<=1:
																		# {"feature": "mysteryGuest", "instances": 6, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 6, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 6, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 6, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 6, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.16666666666666666
																					else: return 0.16666666666666666
																				else: return 0.16666666666666666
																			else: return 0.16666666666666666
																		else: return 0.16666666666666666
																	else: return 0.16666666666666666
																else: return 0.16666666666666666
															else: return 0.16666666666666666
														else: return 0.16666666666666666
													else: return 0.16666666666666666
												else: return 0.16666666666666666
											else: return 0.16666666666666666
										else: return 0.020202020202020204
									elif obj[4]>0:
										# {"feature": "eagerTest", "instances": 20, "metric_value": 0.2293, "depth": 10}
										if obj[8]<=0:
											return 0
										elif obj[8]>0:
											return 0.6666666666666666
										else: return 0.6666666666666666
									else: return 0.1
								elif obj[2]>3:
									# {"feature": "conditionalTestLogic", "instances": 7, "metric_value": 0.2071, "depth": 9}
									if obj[4]>0:
										return 0
									elif obj[4]<=0:
										return 0.5
									else: return 0.5
								else: return 0.14285714285714285
							elif obj[7]>0:
								return 0
							else: return 0.0
						elif obj[3]>0:
							# {"feature": "conditionalTestLogic", "instances": 153, "metric_value": 0.0093, "depth": 7}
							if obj[4]<=0:
								# {"feature": "smellsCount", "instances": 143, "metric_value": 0.0044, "depth": 8}
								if obj[2]<=4:
									# {"feature": "duplicateAssert", "instances": 140, "metric_value": 0.0081, "depth": 9}
									if obj[7]<=0:
										# {"feature": "sensitiveEquality", "instances": 132, "metric_value": 0.0044, "depth": 10}
										if obj[18]<=0:
											# {"feature": "mysteryGuest", "instances": 128, "metric_value": 0.0023, "depth": 11}
											if obj[14]<=0:
												# {"feature": "redundantAssertion", "instances": 126, "metric_value": 0.0023, "depth": 12}
												if obj[16]<=0:
													# {"feature": "lazyTest", "instances": 124, "metric_value": 0.0015, "depth": 13}
													if obj[12]>0:
														# {"feature": "generalFixture", "instances": 108, "metric_value": 0.0247, "depth": 14}
														if obj[10]<=0:
															# {"feature": "eagerTest", "instances": 90, "metric_value": 0.0027, "depth": 15}
															if obj[8]>0:
																# {"feature": "constructorInitialization", "instances": 57, "metric_value": 0.003, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 56, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 56, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 56, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "sleepyTest", "instances": 56, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 56, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 56, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.10714285714285714
																					else: return 0.10714285714285714
																				else: return 0.10714285714285714
																			else: return 0.10714285714285714
																		else: return 0.10714285714285714
																	else: return 0.10714285714285714
																elif obj[5]>0:
																	return 0
																else: return 0.0
															elif obj[8]<=0:
																# {"feature": "constructorInitialization", "instances": 33, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 33, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 33, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 33, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "sleepyTest", "instances": 33, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 33, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 33, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.06060606060606061
																					else: return 0.06060606060606061
																				else: return 0.06060606060606061
																			else: return 0.06060606060606061
																		else: return 0.06060606060606061
																	else: return 0.06060606060606061
																else: return 0.06060606060606061
															else: return 0.06060606060606061
														elif obj[10]>0:
															return 0
														else: return 0.0
													elif obj[12]<=0:
														# {"feature": "generalFixture", "instances": 16, "metric_value": 0.0969, "depth": 14}
														if obj[10]<=0:
															# {"feature": "eagerTest", "instances": 15, "metric_value": 0.0494, "depth": 15}
															if obj[8]<=0:
																# {"feature": "constructorInitialization", "instances": 10, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 10, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 10, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 10, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "sleepyTest", "instances": 10, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 10, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 10, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.1
																					else: return 0.1
																				else: return 0.1
																			else: return 0.1
																		else: return 0.1
																	else: return 0.1
																else: return 0.1
															elif obj[8]>0:
																return 0
															else: return 0.0
														elif obj[10]>0:
															return 1
														else: return 1.0
													else: return 0.125
												elif obj[16]>0:
													return 0
												else: return 0.0
											elif obj[14]>0:
												return 0
											else: return 0.0
										elif obj[18]>0:
											return 0
										else: return 0.0
									elif obj[7]>0:
										return 0
									else: return 0.0
								elif obj[2]>4:
									return 0.3333333333333333
								else: return 0.3333333333333333
							elif obj[4]>0:
								return 0
							else: return 0.0
						else: return 0.0718954248366013
					elif obj[15]>0:
						return 1
					else: return 1.0
				elif obj[13]>0:
					# {"feature": "lazyTest", "instances": 95, "metric_value": 0.0353, "depth": 5}
					if obj[12]>0:
						# {"feature": "smellsCount", "instances": 76, "metric_value": 0.0212, "depth": 6}
						if obj[2]>2:
							# {"feature": "assertionRoulette", "instances": 63, "metric_value": 0.0371, "depth": 7}
							if obj[3]>0:
								# {"feature": "sensitiveEquality", "instances": 47, "metric_value": 0.123, "depth": 8}
								if obj[18]<=0:
									return 0
								elif obj[18]>0:
									return 0.5
								else: return 0.5
							elif obj[3]<=0:
								# {"feature": "conditionalTestLogic", "instances": 16, "metric_value": 0.0716, "depth": 8}
								if obj[4]<=0:
									# {"feature": "duplicateAssert", "instances": 15, "metric_value": 0.0418, "depth": 9}
									if obj[7]<=0:
										# {"feature": "eagerTest", "instances": 12, "metric_value": 0.0393, "depth": 10}
										if obj[8]>0:
											# {"feature": "generalFixture", "instances": 10, "metric_value": 0.0258, "depth": 11}
											if obj[10]<=0:
												# {"feature": "sensitiveEquality", "instances": 9, "metric_value": 0.0308, "depth": 12}
												if obj[18]<=0:
													# {"feature": "constructorInitialization", "instances": 8, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "defaultTest", "instances": 8, "metric_value": 0.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "emptyTest", "instances": 8, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "ignoredTest", "instances": 8, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "mysteryGuest", "instances": 8, "metric_value": 0.0, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "printStatement", "instances": 8, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 8, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 8, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 8, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 8, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.25
																					else: return 0.25
																				else: return 0.25
																			else: return 0.25
																		else: return 0.25
																	else: return 0.25
																else: return 0.25
															else: return 0.25
														else: return 0.25
													else: return 0.25
												elif obj[18]>0:
													return 0
												else: return 0.0
											elif obj[10]>0:
												return 0
											else: return 0.0
										elif obj[8]<=0:
											return 0
										else: return 0.0
									elif obj[7]>0:
										return 0
									else: return 0.0
								elif obj[4]>0:
									return 1
								else: return 1.0
							else: return 0.1875
						elif obj[2]<=2:
							return 0
						else: return 0.0
					elif obj[12]<=0:
						# {"feature": "generalFixture", "instances": 19, "metric_value": 0.0571, "depth": 6}
						if obj[10]<=0:
							# {"feature": "sensitiveEquality", "instances": 16, "metric_value": 0.0422, "depth": 7}
							if obj[18]<=0:
								# {"feature": "smellsCount", "instances": 15, "metric_value": 0.0242, "depth": 8}
								if obj[2]<=2:
									# {"feature": "assertionRoulette", "instances": 14, "metric_value": 0.0369, "depth": 9}
									if obj[3]<=0:
										# {"feature": "conditionalTestLogic", "instances": 9, "metric_value": 0.0, "depth": 10}
										if obj[4]<=0:
											# {"feature": "constructorInitialization", "instances": 9, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "defaultTest", "instances": 9, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "duplicateAssert", "instances": 9, "metric_value": 0.0, "depth": 13}
													if obj[7]<=0:
														# {"feature": "eagerTest", "instances": 9, "metric_value": 0.0, "depth": 14}
														if obj[8]<=0:
															# {"feature": "emptyTest", "instances": 9, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "ignoredTest", "instances": 9, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "mysteryGuest", "instances": 9, "metric_value": 0.0, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "printStatement", "instances": 9, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 9, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 9, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 9, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 9, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.2222222222222222
																					else: return 0.2222222222222222
																				else: return 0.2222222222222222
																			else: return 0.2222222222222222
																		else: return 0.2222222222222222
																	else: return 0.2222222222222222
																else: return 0.2222222222222222
															else: return 0.2222222222222222
														else: return 0.2222222222222222
													else: return 0.2222222222222222
												else: return 0.2222222222222222
											else: return 0.2222222222222222
										else: return 0.2222222222222222
									elif obj[3]>0:
										# {"feature": "conditionalTestLogic", "instances": 5, "metric_value": 0.0, "depth": 10}
										if obj[4]<=0:
											# {"feature": "constructorInitialization", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "defaultTest", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "duplicateAssert", "instances": 5, "metric_value": 0.0, "depth": 13}
													if obj[7]<=0:
														# {"feature": "eagerTest", "instances": 5, "metric_value": 0.0, "depth": 14}
														if obj[8]<=0:
															# {"feature": "emptyTest", "instances": 5, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "mysteryGuest", "instances": 5, "metric_value": 0.0, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "printStatement", "instances": 5, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 5, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 5, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 5, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.6
																					else: return 0.6
																				else: return 0.6
																			else: return 0.6
																		else: return 0.6
																	else: return 0.6
																else: return 0.6
															else: return 0.6
														else: return 0.6
													else: return 0.6
												else: return 0.6
											else: return 0.6
										else: return 0.6
									else: return 0.6
								elif obj[2]>2:
									return 0
								else: return 0.0
							elif obj[18]>0:
								return 1
							else: return 1.0
						elif obj[10]>0:
							return 0
						else: return 0.0
					else: return 0.3157894736842105
				else: return 0.10526315789473684
			elif obj[17]>0:
				return 0
			else: return 0.0
		elif obj[1]>12.392953929539296:
			# {"feature": "mysteryGuest", "instances": 466, "metric_value": 0.0182, "depth": 3}
			if obj[14]<=0:
				# {"feature": "sensitiveEquality", "instances": 434, "metric_value": 0.0153, "depth": 4}
				if obj[18]<=0:
					# {"feature": "printStatement", "instances": 404, "metric_value": 0.0117, "depth": 5}
					if obj[15]<=0:
						# {"feature": "assertionRoulette", "instances": 394, "metric_value": 0.0079, "depth": 6}
						if obj[3]>0:
							# {"feature": "smellsCount", "instances": 228, "metric_value": 0.0194, "depth": 7}
							if obj[2]<=3:
								# {"feature": "magicNumberTest", "instances": 121, "metric_value": 0.0213, "depth": 8}
								if obj[13]<=0:
									# {"feature": "duplicateAssert", "instances": 104, "metric_value": 0.0117, "depth": 9}
									if obj[7]<=0:
										# {"feature": "sleepyTest", "instances": 94, "metric_value": 0.0065, "depth": 10}
										if obj[19]<=0:
											# {"feature": "eagerTest", "instances": 93, "metric_value": 0.0068, "depth": 11}
											if obj[8]>0:
												# {"feature": "lazyTest", "instances": 59, "metric_value": 0.0009, "depth": 12}
												if obj[12]>0:
													# {"feature": "conditionalTestLogic", "instances": 56, "metric_value": 0.0, "depth": 13}
													if obj[4]<=0:
														# {"feature": "constructorInitialization", "instances": 56, "metric_value": 0.0, "depth": 14}
														if obj[5]<=0:
															# {"feature": "defaultTest", "instances": 56, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 56, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "generalFixture", "instances": 56, "metric_value": 0.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "ignoredTest", "instances": 56, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 56, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 56, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 56, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 56, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.4642857142857143
																					else: return 0.4642857142857143
																				else: return 0.4642857142857143
																			else: return 0.4642857142857143
																		else: return 0.4642857142857143
																	else: return 0.4642857142857143
																else: return 0.4642857142857143
															else: return 0.4642857142857143
														else: return 0.4642857142857143
													else: return 0.4642857142857143
												elif obj[12]<=0:
													return 0.3333333333333333
												else: return 0.3333333333333333
											elif obj[8]<=0:
												# {"feature": "lazyTest", "instances": 34, "metric_value": 0.0166, "depth": 12}
												if obj[12]>0:
													# {"feature": "conditionalTestLogic", "instances": 20, "metric_value": 0.0354, "depth": 13}
													if obj[4]<=0:
														# {"feature": "generalFixture", "instances": 16, "metric_value": 0.0081, "depth": 14}
														if obj[10]<=0:
															# {"feature": "constructorInitialization", "instances": 11, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 11, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 11, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 11, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 11, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 11, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 11, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 11, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.09090909090909091
																					else: return 0.09090909090909091
																				else: return 0.09090909090909091
																			else: return 0.09090909090909091
																		else: return 0.09090909090909091
																	else: return 0.09090909090909091
																else: return 0.09090909090909091
															else: return 0.09090909090909091
														elif obj[10]>0:
															# {"feature": "constructorInitialization", "instances": 5, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 5, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 5, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 5, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 5, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 5, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.2
																					else: return 0.2
																				else: return 0.2
																			else: return 0.2
																		else: return 0.2
																	else: return 0.2
																else: return 0.2
															else: return 0.2
														else: return 0.2
													elif obj[4]>0:
														return 0.5
													else: return 0.5
												elif obj[12]<=0:
													# {"feature": "conditionalTestLogic", "instances": 14, "metric_value": 0.1449, "depth": 13}
													if obj[4]<=0:
														# {"feature": "generalFixture", "instances": 10, "metric_value": 0.0026, "depth": 14}
														if obj[10]<=0:
															# {"feature": "constructorInitialization", "instances": 8, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 8, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 8, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 8, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 8, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 8, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 8, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 8, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 1
																						else: return 0.625
																					else: return 0.625
																				else: return 0.625
																			else: return 0.625
																		else: return 0.625
																	else: return 0.625
																else: return 0.625
															else: return 0.625
														elif obj[10]>0:
															return 0.5
														else: return 0.5
													elif obj[4]>0:
														return 0
													else: return 0.0
												else: return 0.42857142857142855
											else: return 0.29411764705882354
										elif obj[19]>0:
											return 1
										else: return 1.0
									elif obj[7]>0:
										# {"feature": "conditionalTestLogic", "instances": 10, "metric_value": 0.1586, "depth": 10}
										if obj[4]<=0:
											return 0
										elif obj[4]>0:
											return 0.3333333333333333
										else: return 0.3333333333333333
									else: return 0.1
								elif obj[13]>0:
									# {"feature": "lazyTest", "instances": 17, "metric_value": 0.0797, "depth": 9}
									if obj[12]>0:
										return 0
									elif obj[12]<=0:
										# {"feature": "conditionalTestLogic", "instances": 8, "metric_value": 0.0807, "depth": 10}
										if obj[4]<=0:
											# {"feature": "eagerTest", "instances": 5, "metric_value": 0.1172, "depth": 11}
											if obj[8]<=0:
												return 0.3333333333333333
											elif obj[8]>0:
												return 0
											else: return 0.0
										elif obj[4]>0:
											return 0
										else: return 0.0
									else: return 0.125
								else: return 0.058823529411764705
							elif obj[2]>3:
								# {"feature": "magicNumberTest", "instances": 107, "metric_value": 0.0112, "depth": 8}
								if obj[13]>0:
									# {"feature": "generalFixture", "instances": 59, "metric_value": 0.0197, "depth": 9}
									if obj[10]<=0:
										# {"feature": "duplicateAssert", "instances": 54, "metric_value": 0.0101, "depth": 10}
										if obj[7]>0:
											# {"feature": "eagerTest", "instances": 28, "metric_value": 0.0434, "depth": 11}
											if obj[8]>0:
												# {"feature": "sleepyTest", "instances": 24, "metric_value": 0.0337, "depth": 12}
												if obj[19]<=0:
													# {"feature": "conditionalTestLogic", "instances": 23, "metric_value": 0.0067, "depth": 13}
													if obj[4]<=0:
														# {"feature": "constructorInitialization", "instances": 21, "metric_value": 0.0, "depth": 14}
														if obj[5]<=0:
															# {"feature": "defaultTest", "instances": 21, "metric_value": 0.0, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 21, "metric_value": 0.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "ignoredTest", "instances": 21, "metric_value": 0.0, "depth": 17}
																	if obj[11]<=0.0:
																		# {"feature": "lazyTest", "instances": 21, "metric_value": 0.0, "depth": 18}
																		if obj[12]<=1:
																			# {"feature": "redundantAssertion", "instances": 21, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 21, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "unknownTest", "instances": 21, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 21, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.23809523809523808
																					else: return 0.23809523809523808
																				else: return 0.23809523809523808
																			else: return 0.23809523809523808
																		else: return 0.23809523809523808
																	else: return 0.23809523809523808
																else: return 0.23809523809523808
															else: return 0.23809523809523808
														else: return 0.23809523809523808
													elif obj[4]>0:
														return 0.5
													else: return 0.5
												elif obj[19]>0:
													return 1
												else: return 1.0
											elif obj[8]<=0:
												return 0
											else: return 0.0
										elif obj[7]<=0:
											# {"feature": "eagerTest", "instances": 26, "metric_value": 0.0158, "depth": 11}
											if obj[8]>0:
												# {"feature": "conditionalTestLogic", "instances": 23, "metric_value": 0.0283, "depth": 12}
												if obj[4]<=0:
													# {"feature": "constructorInitialization", "instances": 19, "metric_value": 0.0092, "depth": 13}
													if obj[5]<=0:
														# {"feature": "defaultTest", "instances": 18, "metric_value": 0.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "emptyTest", "instances": 18, "metric_value": 0.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "ignoredTest", "instances": 18, "metric_value": 0.0, "depth": 16}
																if obj[11]<=0.0:
																	# {"feature": "lazyTest", "instances": 18, "metric_value": 0.0, "depth": 17}
																	if obj[12]<=1:
																		# {"feature": "redundantAssertion", "instances": 18, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "resourceOptimism", "instances": 18, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 18, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 18, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 18, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.1111111111111111
																					else: return 0.1111111111111111
																				else: return 0.1111111111111111
																			else: return 0.1111111111111111
																		else: return 0.1111111111111111
																	else: return 0.1111111111111111
																else: return 0.1111111111111111
															else: return 0.1111111111111111
														else: return 0.1111111111111111
													elif obj[5]>0:
														return 0
													else: return 0.0
												elif obj[4]>0:
													return 0
												else: return 0.0
											elif obj[8]<=0:
												return 0.3333333333333333
											else: return 0.3333333333333333
										else: return 0.11538461538461539
									elif obj[10]>0:
										return 0
									else: return 0.0
								elif obj[13]<=0:
									# {"feature": "conditionalTestLogic", "instances": 48, "metric_value": 0.089, "depth": 9}
									if obj[4]>0:
										return 0
									elif obj[4]<=0:
										# {"feature": "eagerTest", "instances": 21, "metric_value": 0.0642, "depth": 10}
										if obj[8]>0:
											# {"feature": "generalFixture", "instances": 20, "metric_value": 0.1775, "depth": 11}
											if obj[10]<=0:
												return 0
											elif obj[10]>0:
												# {"feature": "duplicateAssert", "instances": 5, "metric_value": 0.0071, "depth": 12}
												if obj[7]<=0:
													return 0.3333333333333333
												elif obj[7]>0:
													return 0.5
												else: return 0.5
											else: return 0.4
										elif obj[8]<=0:
											return 1
										else: return 1.0
									else: return 0.14285714285714285
								else: return 0.0625
							else: return 0.12149532710280374
						elif obj[3]<=0:
							# {"feature": "duplicateAssert", "instances": 166, "metric_value": 0.0201, "depth": 7}
							if obj[7]<=0:
								# {"feature": "magicNumberTest", "instances": 148, "metric_value": 0.0105, "depth": 8}
								if obj[13]<=0:
									# {"feature": "smellsCount", "instances": 140, "metric_value": 0.0063, "depth": 9}
									if obj[2]>1:
										# {"feature": "resourceOptimism", "instances": 73, "metric_value": 0.0097, "depth": 10}
										if obj[17]<=0:
											# {"feature": "eagerTest", "instances": 70, "metric_value": 0.0057, "depth": 11}
											if obj[8]>0:
												# {"feature": "generalFixture", "instances": 42, "metric_value": 0.0099, "depth": 12}
												if obj[10]<=0:
													# {"feature": "lazyTest", "instances": 40, "metric_value": 0.0107, "depth": 13}
													if obj[12]>0:
														# {"feature": "conditionalTestLogic", "instances": 38, "metric_value": 0.0008, "depth": 14}
														if obj[4]<=0:
															# {"feature": "unknownTest", "instances": 30, "metric_value": 0.0004, "depth": 15}
															if obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 23, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 23, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 23, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 23, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 23, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 23, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 23, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.17391304347826086
																					else: return 0.17391304347826086
																				else: return 0.17391304347826086
																			else: return 0.17391304347826086
																		else: return 0.17391304347826086
																	else: return 0.17391304347826086
																else: return 0.17391304347826086
															elif obj[20]>0:
																# {"feature": "constructorInitialization", "instances": 7, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 7, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 7, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 7, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 7, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 7, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 7, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.14285714285714285
																					else: return 0.14285714285714285
																				else: return 0.14285714285714285
																			else: return 0.14285714285714285
																		else: return 0.14285714285714285
																	else: return 0.14285714285714285
																else: return 0.14285714285714285
															else: return 0.14285714285714285
														elif obj[4]>0:
															# {"feature": "unknownTest", "instances": 8, "metric_value": 0.0245, "depth": 15}
															if obj[20]<=0:
																# {"feature": "constructorInitialization", "instances": 7, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 7, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 7, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 7, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 7, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 7, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 7, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.14285714285714285
																					else: return 0.14285714285714285
																				else: return 0.14285714285714285
																			else: return 0.14285714285714285
																		else: return 0.14285714285714285
																	else: return 0.14285714285714285
																else: return 0.14285714285714285
															elif obj[20]>0:
																return 0
															else: return 0.0
														else: return 0.125
													elif obj[12]<=0:
														return 0
													else: return 0.0
												elif obj[10]>0:
													return 0
												else: return 0.0
											elif obj[8]<=0:
												# {"feature": "conditionalTestLogic", "instances": 28, "metric_value": 0.0185, "depth": 12}
												if obj[4]>0:
													# {"feature": "generalFixture", "instances": 14, "metric_value": 0.1025, "depth": 13}
													if obj[10]<=0:
														# {"feature": "unknownTest", "instances": 8, "metric_value": 0.0285, "depth": 14}
														if obj[20]<=0:
															# {"feature": "constructorInitialization", "instances": 6, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 6, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 6, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 6, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "lazyTest", "instances": 6, "metric_value": 0.0, "depth": 19}
																			if obj[12]<=1:
																				# {"feature": "redundantAssertion", "instances": 6, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 6, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 6, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.16666666666666666
																					else: return 0.16666666666666666
																				else: return 0.16666666666666666
																			else: return 0.16666666666666666
																		else: return 0.16666666666666666
																	else: return 0.16666666666666666
																else: return 0.16666666666666666
															else: return 0.16666666666666666
														elif obj[20]>0:
															return 0.5
														else: return 0.5
													elif obj[10]>0:
														return 0
													else: return 0.0
												elif obj[4]<=0:
													# {"feature": "generalFixture", "instances": 14, "metric_value": 0.122, "depth": 13}
													if obj[10]>0:
														# {"feature": "lazyTest", "instances": 10, "metric_value": 0.0122, "depth": 14}
														if obj[12]>0:
															# {"feature": "constructorInitialization", "instances": 7, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 7, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 7, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 7, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 7, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sleepyTest", "instances": 7, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "unknownTest", "instances": 7, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						# {"feature": "verboseTest", "instances": 7, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.42857142857142855
																					else: return 0.42857142857142855
																				else: return 0.42857142857142855
																			else: return 0.42857142857142855
																		else: return 0.42857142857142855
																	else: return 0.42857142857142855
																else: return 0.42857142857142855
															else: return 0.42857142857142855
														elif obj[12]<=0:
															return 0.6666666666666666
														else: return 0.6666666666666666
													elif obj[10]<=0:
														return 0
													else: return 0.0
												else: return 0.35714285714285715
											else: return 0.25
										elif obj[17]>0:
											return 0
										else: return 0.0
									elif obj[2]<=1:
										# {"feature": "lazyTest", "instances": 67, "metric_value": 0.0572, "depth": 10}
										if obj[12]<=0:
											# {"feature": "eagerTest", "instances": 45, "metric_value": 0.0624, "depth": 11}
											if obj[8]<=0:
												# {"feature": "generalFixture", "instances": 43, "metric_value": 0.0153, "depth": 12}
												if obj[10]<=0:
													# {"feature": "unknownTest", "instances": 39, "metric_value": 0.0072, "depth": 13}
													if obj[20]<=0:
														# {"feature": "resourceOptimism", "instances": 22, "metric_value": 0.0092, "depth": 14}
														if obj[17]<=0:
															# {"feature": "conditionalTestLogic", "instances": 21, "metric_value": 0.0027, "depth": 15}
															if obj[4]<=0:
																# {"feature": "constructorInitialization", "instances": 16, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 16, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 16, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 16, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 16, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 16, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 16, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.125
																					else: return 0.125
																				else: return 0.125
																			else: return 0.125
																		else: return 0.125
																	else: return 0.125
																else: return 0.125
															elif obj[4]>0:
																# {"feature": "constructorInitialization", "instances": 5, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "defaultTest", "instances": 5, "metric_value": 0.0, "depth": 17}
																	if obj[6]<=0:
																		# {"feature": "emptyTest", "instances": 5, "metric_value": 0.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.0, "depth": 19}
																			if obj[11]<=0.0:
																				# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "sleepyTest", "instances": 5, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 5, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.2
																					else: return 0.2
																				else: return 0.2
																			else: return 0.2
																		else: return 0.2
																	else: return 0.2
																else: return 0.2
															else: return 0.2
														elif obj[17]>0:
															return 0
														else: return 0.0
													elif obj[20]>0:
														# {"feature": "conditionalTestLogic", "instances": 17, "metric_value": 0.0, "depth": 14}
														if obj[4]<=0:
															# {"feature": "constructorInitialization", "instances": 17, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "defaultTest", "instances": 17, "metric_value": 0.0, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "emptyTest", "instances": 17, "metric_value": 0.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "ignoredTest", "instances": 17, "metric_value": 0.0, "depth": 18}
																		if obj[11]<=0.0:
																			# {"feature": "redundantAssertion", "instances": 17, "metric_value": 0.0, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "resourceOptimism", "instances": 17, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "sleepyTest", "instances": 17, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						# {"feature": "verboseTest", "instances": 17, "metric_value": 0.0, "depth": 22}
																						if obj[21]<=0:
																							return 0
																						else: return 0.058823529411764705
																					else: return 0.058823529411764705
																				else: return 0.058823529411764705
																			else: return 0.058823529411764705
																		else: return 0.058823529411764705
																	else: return 0.058823529411764705
																else: return 0.058823529411764705
															else: return 0.058823529411764705
														else: return 0.058823529411764705
													else: return 0.058823529411764705
												elif obj[10]>0:
													return 0
												else: return 0.0
											elif obj[8]>0:
												return 1
											else: return 1.0
										elif obj[12]>0:
											return 0
										else: return 0.0
									else: return 0.08955223880597014
								elif obj[13]>0:
									return 0
								else: return 0.0
							elif obj[7]>0:
								return 0
							else: return 0.0
						else: return 0.1144578313253012
					elif obj[15]>0:
						# {"feature": "smellsCount", "instances": 10, "metric_value": 0.1172, "depth": 6}
						if obj[2]>3:
							# {"feature": "assertionRoulette", "instances": 6, "metric_value": 0.1381, "depth": 7}
							if obj[3]>0:
								# {"feature": "eagerTest", "instances": 5, "metric_value": 0.4, "depth": 8}
								if obj[8]>0:
									return 1
								elif obj[8]<=0:
									return 0
								else: return 0.0
							elif obj[3]<=0:
								return 0
							else: return 0.0
						elif obj[2]<=3:
							return 1
						else: return 1.0
					else: return 0.8
				elif obj[18]>0:
					# {"feature": "lazyTest", "instances": 30, "metric_value": 0.3713, "depth": 5}
					if obj[12]<=0:
						return 1
					elif obj[12]>0:
						# {"feature": "printStatement", "instances": 12, "metric_value": 0.2764, "depth": 6}
						if obj[15]<=0:
							return 0
						elif obj[15]>0:
							return 1
						else: return 1.0
					else: return 0.08333333333333333
				else: return 0.6333333333333333
			elif obj[14]>0:
				return 0
			else: return 0.0
		else: return 0.21244635193133046
	else: return 0.10365853658536585
