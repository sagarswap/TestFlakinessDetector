def findDecision(obj): #obj[0]: loc, obj[1]: smellsCount, obj[2]: assertionRoulette, obj[3]: conditionalTestLogic, obj[4]: constructorInitialization, obj[5]: defaultTest, obj[6]: duplicateAssert, obj[7]: eagerTest, obj[8]: emptyTest, obj[9]: generalFixture, obj[10]: ignoredTest, obj[11]: lazyTest, obj[12]: magicNumberTest, obj[13]: mysteryGuest, obj[14]: printStatement, obj[15]: redundantAssertion, obj[16]: resourceOptimism, obj[17]: sensitiveEquality, obj[18]: sleepyTest, obj[19]: unknownTest, obj[20]: verboseTest
	# {"feature": "loc", "instances": 2221, "metric_value": 43.599, "depth": 1}
	if obj[0]<=20.831157136425034:
		# {"feature": "smellsCount", "instances": 1479, "metric_value": 26.8038, "depth": 2}
		if obj[1]>0:
			# {"feature": "constructorInitialization", "instances": 1398, "metric_value": 24.2159, "depth": 3}
			if obj[4]<=0:
				# {"feature": "generalFixture", "instances": 1360, "metric_value": 25.2726, "depth": 4}
				if obj[9]<=0:
					# {"feature": "eagerTest", "instances": 1174, "metric_value": 20.2395, "depth": 5}
					if obj[7]<=0:
						# {"feature": "resourceOptimism", "instances": 788, "metric_value": 16.091, "depth": 6}
						if obj[16]<=0:
							# {"feature": "sleepyTest", "instances": 770, "metric_value": 15.0573, "depth": 7}
							if obj[18]<=0:
								# {"feature": "unknownTest", "instances": 757, "metric_value": 14.8731, "depth": 8}
								if obj[19]<=0:
									# {"feature": "lazyTest", "instances": 428, "metric_value": 17.7071, "depth": 9}
									if obj[11]>0:
										# {"feature": "assertionRoulette", "instances": 336, "metric_value": 17.4458, "depth": 10}
										if obj[2]<=0:
											# {"feature": "conditionalTestLogic", "instances": 240, "metric_value": 17.5272, "depth": 11}
											if obj[3]<=0:
												# {"feature": "magicNumberTest", "instances": 230, "metric_value": 16.1065, "depth": 12}
												if obj[12]<=0:
													# {"feature": "sensitiveEquality", "instances": 217, "metric_value": 15.4528, "depth": 13}
													if obj[17]<=0:
														# {"feature": "duplicateAssert", "instances": 211, "metric_value": 15.0105, "depth": 14}
														if obj[6]<=0:
															# {"feature": "mysteryGuest", "instances": 209, "metric_value": 14.8766, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 207, "metric_value": 14.4206, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "defaultTest", "instances": 206, "metric_value": 13.0063, "depth": 17}
																	if obj[5]<=0:
																		# {"feature": "emptyTest", "instances": 206, "metric_value": 13.0063, "depth": 18}
																		if obj[8]<=0:
																			# {"feature": "ignoredTest", "instances": 206, "metric_value": 13.0063, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "redundantAssertion", "instances": 206, "metric_value": 13.0063, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 206, "metric_value": 13.0063, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																elif obj[14]>0:
																	return '1'
																else: return '1'
															elif obj[13]>0:
																return '0'
															else: return '0'
														elif obj[6]>0:
															return '0'
														else: return '0'
													elif obj[17]>0:
														# {"feature": "defaultTest", "instances": 6, "metric_value": 2.3094, "depth": 14}
														if obj[5]<=0:
															# {"feature": "duplicateAssert", "instances": 6, "metric_value": 2.3094, "depth": 15}
															if obj[6]<=0:
																# {"feature": "emptyTest", "instances": 6, "metric_value": 2.3094, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 6, "metric_value": 2.3094, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "mysteryGuest", "instances": 6, "metric_value": 2.3094, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "printStatement", "instances": 6, "metric_value": 2.3094, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 6, "metric_value": 2.3094, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 6, "metric_value": 2.3094, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[12]>0:
													# {"feature": "duplicateAssert", "instances": 13, "metric_value": 4.6802, "depth": 13}
													if obj[6]<=0:
														# {"feature": "defaultTest", "instances": 12, "metric_value": 3.266, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 12, "metric_value": 3.266, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 12, "metric_value": 3.266, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "mysteryGuest", "instances": 12, "metric_value": 3.266, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 12, "metric_value": 3.266, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 12, "metric_value": 3.266, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 12, "metric_value": 3.266, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 12, "metric_value": 3.266, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													elif obj[6]>0:
														return '0'
													else: return '0'
												else: return '0'
											elif obj[3]>0:
												return '0'
											else: return '0'
										elif obj[2]>0:
											# {"feature": "duplicateAssert", "instances": 96, "metric_value": 6.3638, "depth": 11}
											if obj[6]<=0:
												# {"feature": "mysteryGuest", "instances": 86, "metric_value": 6.6407, "depth": 12}
												if obj[13]<=0:
													# {"feature": "magicNumberTest", "instances": 83, "metric_value": 5.5846, "depth": 13}
													if obj[12]<=0:
														# {"feature": "conditionalTestLogic", "instances": 52, "metric_value": 6.159, "depth": 14}
														if obj[3]<=0:
															# {"feature": "sensitiveEquality", "instances": 46, "metric_value": 5.1168, "depth": 15}
															if obj[17]<=0:
																# {"feature": "defaultTest", "instances": 44, "metric_value": 5.1168, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 44, "metric_value": 5.1168, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 44, "metric_value": 5.1168, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "printStatement", "instances": 44, "metric_value": 5.1168, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 44, "metric_value": 5.1168, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 44, "metric_value": 5.1168, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															elif obj[17]>0:
																# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "printStatement", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														elif obj[3]>0:
															# {"feature": "sensitiveEquality", "instances": 6, "metric_value": 3.3116, "depth": 15}
															if obj[17]<=0:
																# {"feature": "defaultTest", "instances": 5, "metric_value": 1.8974, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 5, "metric_value": 1.8974, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 5, "metric_value": 1.8974, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "printStatement", "instances": 5, "metric_value": 1.8974, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 5, "metric_value": 1.8974, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 1.8974, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															elif obj[17]>0:
																return '0'
															else: return '0'
														else: return '1'
													elif obj[12]>0:
														# {"feature": "conditionalTestLogic", "instances": 31, "metric_value": 2.7878, "depth": 14}
														if obj[3]<=0:
															# {"feature": "sensitiveEquality", "instances": 29, "metric_value": 1.9487, "depth": 15}
															if obj[17]<=0:
																# {"feature": "defaultTest", "instances": 28, "metric_value": 0.5345, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 28, "metric_value": 0.5345, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 28, "metric_value": 0.5345, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "printStatement", "instances": 28, "metric_value": 0.5345, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 28, "metric_value": 0.5345, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 28, "metric_value": 0.5345, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															elif obj[17]>0:
																return '0'
															else: return '0'
														elif obj[3]>0:
															return '0'
														else: return '0'
													else: return '0'
												elif obj[13]>0:
													return '0'
												else: return '0'
											elif obj[6]>0:
												# {"feature": "conditionalTestLogic", "instances": 10, "metric_value": 3.7712, "depth": 12}
												if obj[3]<=0:
													# {"feature": "magicNumberTest", "instances": 9, "metric_value": 4.4142, "depth": 13}
													if obj[12]<=0:
														# {"feature": "defaultTest", "instances": 8, "metric_value": 3.0, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 8, "metric_value": 3.0, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 8, "metric_value": 3.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "mysteryGuest", "instances": 8, "metric_value": 3.0, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 8, "metric_value": 3.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 8, "metric_value": 3.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 8, "metric_value": 3.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 3.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[12]>0:
														return '0'
													else: return '0'
												elif obj[3]>0:
													return '0'
												else: return '0'
											else: return '1'
										else: return '0'
									elif obj[11]<=0:
										# {"feature": "assertionRoulette", "instances": 92, "metric_value": 7.564, "depth": 10}
										if obj[2]>0:
											# {"feature": "magicNumberTest", "instances": 72, "metric_value": 8.3152, "depth": 11}
											if obj[12]<=0:
												# {"feature": "conditionalTestLogic", "instances": 47, "metric_value": 6.7135, "depth": 12}
												if obj[3]<=0:
													# {"feature": "duplicateAssert", "instances": 44, "metric_value": 6.4074, "depth": 13}
													if obj[6]<=0:
														# {"feature": "sensitiveEquality", "instances": 35, "metric_value": 4.3246, "depth": 14}
														if obj[17]<=0:
															# {"feature": "defaultTest", "instances": 34, "metric_value": 2.9104, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 34, "metric_value": 2.9104, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 34, "metric_value": 2.9104, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "mysteryGuest", "instances": 34, "metric_value": 2.9104, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "printStatement", "instances": 34, "metric_value": 2.9104, "depth": 19}
																			if obj[14]<=0:
																				# {"feature": "redundantAssertion", "instances": 34, "metric_value": 2.9104, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "verboseTest", "instances": 34, "metric_value": 2.9104, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														elif obj[17]>0:
															return '1'
														else: return '1'
													elif obj[6]>0:
														# {"feature": "defaultTest", "instances": 9, "metric_value": 3.2998, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 9, "metric_value": 3.2998, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 9, "metric_value": 3.2998, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "mysteryGuest", "instances": 9, "metric_value": 3.2998, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 9, "metric_value": 3.2998, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 9, "metric_value": 3.2998, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 9, "metric_value": 3.2998, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 9, "metric_value": 3.2998, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[3]>0:
													return '0'
												else: return '0'
											elif obj[12]>0:
												# {"feature": "conditionalTestLogic", "instances": 25, "metric_value": 6.4233, "depth": 12}
												if obj[3]<=0:
													# {"feature": "duplicateAssert", "instances": 23, "metric_value": 5.6354, "depth": 13}
													if obj[6]<=0:
														# {"feature": "defaultTest", "instances": 22, "metric_value": 4.2212, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 22, "metric_value": 4.2212, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 22, "metric_value": 4.2212, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "mysteryGuest", "instances": 22, "metric_value": 4.2212, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 22, "metric_value": 4.2212, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 22, "metric_value": 4.2212, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 22, "metric_value": 4.2212, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 22, "metric_value": 4.2212, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[6]>0:
														return '1'
													else: return '1'
												elif obj[3]>0:
													return '1'
												else: return '1'
											else: return '1'
										elif obj[2]<=0:
											# {"feature": "mysteryGuest", "instances": 20, "metric_value": 7.1789, "depth": 11}
											if obj[13]<=0:
												# {"feature": "printStatement", "instances": 15, "metric_value": 7.099, "depth": 12}
												if obj[14]<=0:
													return '0'
												elif obj[14]>0:
													return '1'
												else: return '1'
											elif obj[13]>0:
												return '1'
											else: return '1'
										else: return '0'
									else: return '1'
								elif obj[19]>0:
									# {"feature": "lazyTest", "instances": 329, "metric_value": 9.1864, "depth": 9}
									if obj[11]<=0:
										# {"feature": "conditionalTestLogic", "instances": 240, "metric_value": 6.9669, "depth": 10}
										if obj[3]<=0:
											# {"feature": "assertionRoulette", "instances": 238, "metric_value": 6.9669, "depth": 11}
											if obj[2]<=0:
												# {"feature": "defaultTest", "instances": 238, "metric_value": 6.9669, "depth": 12}
												if obj[5]<=0:
													# {"feature": "duplicateAssert", "instances": 238, "metric_value": 6.9669, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 238, "metric_value": 6.9669, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 238, "metric_value": 6.9669, "depth": 15}
															if obj[10]<=0:
																# {"feature": "magicNumberTest", "instances": 238, "metric_value": 6.9669, "depth": 16}
																if obj[12]<=0:
																	# {"feature": "mysteryGuest", "instances": 238, "metric_value": 6.9669, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 238, "metric_value": 6.9669, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 238, "metric_value": 6.9669, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 238, "metric_value": 6.9669, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 238, "metric_value": 6.9669, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										elif obj[3]>0:
											# {"feature": "assertionRoulette", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[2]<=0:
												# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "duplicateAssert", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "magicNumberTest", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[12]<=0:
																	# {"feature": "mysteryGuest", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[11]>0:
										# {"feature": "conditionalTestLogic", "instances": 89, "metric_value": 4.4142, "depth": 10}
										if obj[3]<=0:
											# {"feature": "assertionRoulette", "instances": 81, "metric_value": 1.4142, "depth": 11}
											if obj[2]<=0:
												# {"feature": "defaultTest", "instances": 81, "metric_value": 1.4142, "depth": 12}
												if obj[5]<=0:
													# {"feature": "duplicateAssert", "instances": 81, "metric_value": 1.4142, "depth": 13}
													if obj[6]<=0:
														# {"feature": "emptyTest", "instances": 81, "metric_value": 1.4142, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 81, "metric_value": 1.4142, "depth": 15}
															if obj[10]<=0:
																# {"feature": "magicNumberTest", "instances": 81, "metric_value": 1.4142, "depth": 16}
																if obj[12]<=0:
																	# {"feature": "mysteryGuest", "instances": 81, "metric_value": 1.4142, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 81, "metric_value": 1.4142, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 81, "metric_value": 1.4142, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 81, "metric_value": 1.4142, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 81, "metric_value": 1.4142, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[3]>0:
											# {"feature": "printStatement", "instances": 8, "metric_value": 4.3094, "depth": 11}
											if obj[14]<=0:
												# {"feature": "assertionRoulette", "instances": 6, "metric_value": 2.3094, "depth": 12}
												if obj[2]<=0:
													# {"feature": "defaultTest", "instances": 6, "metric_value": 2.3094, "depth": 13}
													if obj[5]<=0:
														# {"feature": "duplicateAssert", "instances": 6, "metric_value": 2.3094, "depth": 14}
														if obj[6]<=0:
															# {"feature": "emptyTest", "instances": 6, "metric_value": 2.3094, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 6, "metric_value": 2.3094, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "magicNumberTest", "instances": 6, "metric_value": 2.3094, "depth": 17}
																	if obj[12]<=0:
																		# {"feature": "mysteryGuest", "instances": 6, "metric_value": 2.3094, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 6, "metric_value": 2.3094, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sensitiveEquality", "instances": 6, "metric_value": 2.3094, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 6, "metric_value": 2.3094, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											elif obj[14]>0:
												return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '0'
							elif obj[18]>0:
								# {"feature": "assertionRoulette", "instances": 13, "metric_value": 6.1283, "depth": 8}
								if obj[2]>0:
									# {"feature": "conditionalTestLogic", "instances": 9, "metric_value": 3.2998, "depth": 9}
									if obj[3]<=1:
										# {"feature": "defaultTest", "instances": 9, "metric_value": 3.2998, "depth": 10}
										if obj[5]<=0:
											# {"feature": "duplicateAssert", "instances": 9, "metric_value": 3.2998, "depth": 11}
											if obj[6]<=0:
												# {"feature": "emptyTest", "instances": 9, "metric_value": 3.2998, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 9, "metric_value": 3.2998, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 9, "metric_value": 3.2998, "depth": 14}
														if obj[11]<=1:
															# {"feature": "magicNumberTest", "instances": 9, "metric_value": 3.2998, "depth": 15}
															if obj[12]<=0:
																# {"feature": "mysteryGuest", "instances": 9, "metric_value": 3.2998, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 9, "metric_value": 3.2998, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 9, "metric_value": 3.2998, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sensitiveEquality", "instances": 9, "metric_value": 3.2998, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 9, "metric_value": 3.2998, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 9, "metric_value": 3.2998, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								elif obj[2]<=0:
									return '1'
								else: return '1'
							else: return '1'
						elif obj[16]>0:
							return '0'
						else: return '0'
					elif obj[7]>0:
						# {"feature": "assertionRoulette", "instances": 386, "metric_value": 14.8791, "depth": 6}
						if obj[2]>0:
							# {"feature": "sensitiveEquality", "instances": 245, "metric_value": 9.2492, "depth": 7}
							if obj[17]<=0:
								# {"feature": "duplicateAssert", "instances": 212, "metric_value": 7.1959, "depth": 8}
								if obj[6]<=0:
									# {"feature": "resourceOptimism", "instances": 174, "metric_value": 8.4123, "depth": 9}
									if obj[16]<=0:
										# {"feature": "magicNumberTest", "instances": 165, "metric_value": 8.8166, "depth": 10}
										if obj[12]<=0:
											# {"feature": "mysteryGuest", "instances": 120, "metric_value": 7.078, "depth": 11}
											if obj[13]<=0:
												# {"feature": "conditionalTestLogic", "instances": 112, "metric_value": 7.3471, "depth": 12}
												if obj[3]<=0:
													# {"feature": "redundantAssertion", "instances": 101, "metric_value": 6.4495, "depth": 13}
													if obj[15]<=0:
														# {"feature": "lazyTest", "instances": 98, "metric_value": 5.9319, "depth": 14}
														if obj[11]>0:
															# {"feature": "defaultTest", "instances": 85, "metric_value": 4.7552, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 85, "metric_value": 4.7552, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 85, "metric_value": 4.7552, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "printStatement", "instances": 85, "metric_value": 4.7552, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "sleepyTest", "instances": 85, "metric_value": 4.7552, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 85, "metric_value": 4.7552, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 85, "metric_value": 4.7552, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														elif obj[11]<=0:
															# {"feature": "defaultTest", "instances": 13, "metric_value": 1.1767, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 13, "metric_value": 1.1767, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 13, "metric_value": 1.1767, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "printStatement", "instances": 13, "metric_value": 1.1767, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "sleepyTest", "instances": 13, "metric_value": 1.1767, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 13, "metric_value": 1.1767, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 13, "metric_value": 1.1767, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[15]>0:
														return '0'
													else: return '0'
												elif obj[3]>0:
													# {"feature": "lazyTest", "instances": 11, "metric_value": 4.0975, "depth": 13}
													if obj[11]>0:
														# {"feature": "defaultTest", "instances": 10, "metric_value": 2.6833, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 10, "metric_value": 2.6833, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 10, "metric_value": 2.6833, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "printStatement", "instances": 10, "metric_value": 2.6833, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 10, "metric_value": 2.6833, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 10, "metric_value": 2.6833, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 10, "metric_value": 2.6833, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 10, "metric_value": 2.6833, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													elif obj[11]<=0:
														return '0'
													else: return '0'
												else: return '0'
											elif obj[13]>0:
												# {"feature": "conditionalTestLogic", "instances": 8, "metric_value": 2.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "defaultTest", "instances": 8, "metric_value": 2.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "emptyTest", "instances": 8, "metric_value": 2.0, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 8, "metric_value": 2.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "lazyTest", "instances": 8, "metric_value": 2.0, "depth": 16}
																if obj[11]<=1:
																	# {"feature": "printStatement", "instances": 8, "metric_value": 2.0, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 8, "metric_value": 2.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 8, "metric_value": 2.0, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 8, "metric_value": 2.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 2.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[12]>0:
											# {"feature": "lazyTest", "instances": 45, "metric_value": 6.3774, "depth": 11}
											if obj[11]>0:
												# {"feature": "conditionalTestLogic", "instances": 42, "metric_value": 5.5777, "depth": 12}
												if obj[3]<=0:
													# {"feature": "defaultTest", "instances": 40, "metric_value": 3.5777, "depth": 13}
													if obj[5]<=0:
														# {"feature": "emptyTest", "instances": 40, "metric_value": 3.5777, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 40, "metric_value": 3.5777, "depth": 15}
															if obj[10]<=0:
																# {"feature": "mysteryGuest", "instances": 40, "metric_value": 3.5777, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 40, "metric_value": 3.5777, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 40, "metric_value": 3.5777, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 40, "metric_value": 3.5777, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 40, "metric_value": 3.5777, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 40, "metric_value": 3.5777, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												elif obj[3]>0:
													return '0'
												else: return '0'
											elif obj[11]<=0:
												return '0'
											else: return '0'
										else: return '0'
									elif obj[16]>0:
										# {"feature": "magicNumberTest", "instances": 9, "metric_value": 4.4142, "depth": 10}
										if obj[12]<=0:
											# {"feature": "mysteryGuest", "instances": 8, "metric_value": 3.9788, "depth": 11}
											if obj[13]<=0:
												return '1'
											elif obj[13]>0:
												# {"feature": "conditionalTestLogic", "instances": 3, "metric_value": 0.8165, "depth": 12}
												if obj[3]<=0:
													# {"feature": "defaultTest", "instances": 3, "metric_value": 0.8165, "depth": 13}
													if obj[5]<=0:
														# {"feature": "emptyTest", "instances": 3, "metric_value": 0.8165, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 3, "metric_value": 0.8165, "depth": 15}
															if obj[10]<=0:
																# {"feature": "lazyTest", "instances": 3, "metric_value": 0.8165, "depth": 16}
																if obj[11]<=1:
																	# {"feature": "printStatement", "instances": 3, "metric_value": 0.8165, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 3, "metric_value": 0.8165, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 3, "metric_value": 0.8165, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 3, "metric_value": 0.8165, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 3, "metric_value": 0.8165, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[12]>0:
											return '0'
										else: return '0'
									else: return '1'
								elif obj[6]>0:
									# {"feature": "conditionalTestLogic", "instances": 38, "metric_value": 3.5067, "depth": 9}
									if obj[3]<=0:
										# {"feature": "magicNumberTest", "instances": 37, "metric_value": 3.1325, "depth": 10}
										if obj[12]<=0:
											# {"feature": "lazyTest", "instances": 32, "metric_value": 2.582, "depth": 11}
											if obj[11]>0:
												# {"feature": "defaultTest", "instances": 30, "metric_value": 2.582, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 30, "metric_value": 2.582, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 30, "metric_value": 2.582, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 30, "metric_value": 2.582, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 30, "metric_value": 2.582, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 30, "metric_value": 2.582, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 30, "metric_value": 2.582, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 30, "metric_value": 2.582, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 30, "metric_value": 2.582, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 30, "metric_value": 2.582, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											elif obj[11]<=0:
												# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 2, "metric_value": 0.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[12]>0:
											# {"feature": "defaultTest", "instances": 5, "metric_value": 0.6325, "depth": 11}
											if obj[5]<=0:
												# {"feature": "emptyTest", "instances": 5, "metric_value": 0.6325, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.6325, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 5, "metric_value": 0.6325, "depth": 14}
														if obj[11]<=1:
															# {"feature": "mysteryGuest", "instances": 5, "metric_value": 0.6325, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 5, "metric_value": 0.6325, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.6325, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 5, "metric_value": 0.6325, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 5, "metric_value": 0.6325, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 5, "metric_value": 0.6325, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 0.6325, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									elif obj[3]>0:
										return '0'
									else: return '0'
								else: return '1'
							elif obj[17]>0:
								# {"feature": "magicNumberTest", "instances": 33, "metric_value": 5.334, "depth": 8}
								if obj[12]<=0:
									# {"feature": "conditionalTestLogic", "instances": 31, "metric_value": 5.334, "depth": 9}
									if obj[3]<=0:
										# {"feature": "defaultTest", "instances": 31, "metric_value": 5.334, "depth": 10}
										if obj[5]<=0:
											# {"feature": "duplicateAssert", "instances": 31, "metric_value": 5.334, "depth": 11}
											if obj[6]<=0:
												# {"feature": "emptyTest", "instances": 31, "metric_value": 5.334, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 31, "metric_value": 5.334, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 31, "metric_value": 5.334, "depth": 14}
														if obj[11]<=1:
															# {"feature": "mysteryGuest", "instances": 31, "metric_value": 5.334, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 31, "metric_value": 5.334, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 31, "metric_value": 5.334, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 31, "metric_value": 5.334, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 31, "metric_value": 5.334, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 31, "metric_value": 5.334, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 31, "metric_value": 5.334, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								elif obj[12]>0:
									# {"feature": "conditionalTestLogic", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "duplicateAssert", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[6]<=0:
												# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 2, "metric_value": 0.0, "depth": 14}
														if obj[11]<=1:
															# {"feature": "mysteryGuest", "instances": 2, "metric_value": 0.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							else: return '1'
						elif obj[2]<=0:
							# {"feature": "unknownTest", "instances": 141, "metric_value": 17.1916, "depth": 7}
							if obj[19]<=0:
								# {"feature": "duplicateAssert", "instances": 116, "metric_value": 15.5935, "depth": 8}
								if obj[6]<=0:
									# {"feature": "conditionalTestLogic", "instances": 105, "metric_value": 14.0274, "depth": 9}
									if obj[3]<=0:
										# {"feature": "sensitiveEquality", "instances": 98, "metric_value": 13.1953, "depth": 10}
										if obj[17]<=0:
											# {"feature": "resourceOptimism", "instances": 92, "metric_value": 12.4111, "depth": 11}
											if obj[16]<=0:
												# {"feature": "magicNumberTest", "instances": 87, "metric_value": 10.9554, "depth": 12}
												if obj[12]<=0:
													# {"feature": "mysteryGuest", "instances": 82, "metric_value": 10.3709, "depth": 13}
													if obj[13]<=0:
														# {"feature": "lazyTest", "instances": 81, "metric_value": 9.4347, "depth": 14}
														if obj[11]>0:
															# {"feature": "defaultTest", "instances": 73, "metric_value": 9.4347, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 73, "metric_value": 9.4347, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 73, "metric_value": 9.4347, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "printStatement", "instances": 73, "metric_value": 9.4347, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 73, "metric_value": 9.4347, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sleepyTest", "instances": 73, "metric_value": 9.4347, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 73, "metric_value": 9.4347, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														elif obj[11]<=0:
															# {"feature": "defaultTest", "instances": 8, "metric_value": 0.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 8, "metric_value": 0.0, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 8, "metric_value": 0.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "printStatement", "instances": 8, "metric_value": 0.0, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 8, "metric_value": 0.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sleepyTest", "instances": 8, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													elif obj[13]>0:
														return '0'
													else: return '0'
												elif obj[12]>0:
													# {"feature": "defaultTest", "instances": 5, "metric_value": 1.8974, "depth": 13}
													if obj[5]<=0:
														# {"feature": "emptyTest", "instances": 5, "metric_value": 1.8974, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 5, "metric_value": 1.8974, "depth": 15}
															if obj[10]<=0:
																# {"feature": "lazyTest", "instances": 5, "metric_value": 1.8974, "depth": 16}
																if obj[11]<=1:
																	# {"feature": "mysteryGuest", "instances": 5, "metric_value": 1.8974, "depth": 17}
																	if obj[13]<=0:
																		# {"feature": "printStatement", "instances": 5, "metric_value": 1.8974, "depth": 18}
																		if obj[14]<=0:
																			# {"feature": "redundantAssertion", "instances": 5, "metric_value": 1.8974, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "sleepyTest", "instances": 5, "metric_value": 1.8974, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 1.8974, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											elif obj[16]>0:
												return '0'
											else: return '0'
										elif obj[17]>0:
											return '0'
										else: return '0'
									elif obj[3]>0:
										return '0'
									else: return '0'
								elif obj[6]>0:
									return '0'
								else: return '0'
							elif obj[19]>0:
								# {"feature": "mysteryGuest", "instances": 25, "metric_value": 7.4575, "depth": 8}
								if obj[13]<=0:
									# {"feature": "conditionalTestLogic", "instances": 21, "metric_value": 5.5822, "depth": 9}
									if obj[3]<=0:
										# {"feature": "lazyTest", "instances": 16, "metric_value": 5.2915, "depth": 10}
										if obj[11]>0:
											return '0'
										elif obj[11]<=0:
											# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "magicNumberTest", "instances": 2, "metric_value": 0.0, "depth": 15}
															if obj[12]<=0:
																# {"feature": "printStatement", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[3]>0:
										# {"feature": "defaultTest", "instances": 5, "metric_value": 0.6325, "depth": 10}
										if obj[5]<=0:
											# {"feature": "duplicateAssert", "instances": 5, "metric_value": 0.6325, "depth": 11}
											if obj[6]<=0:
												# {"feature": "emptyTest", "instances": 5, "metric_value": 0.6325, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.6325, "depth": 13}
													if obj[10]<=0:
														# {"feature": "lazyTest", "instances": 5, "metric_value": 0.6325, "depth": 14}
														if obj[11]<=1:
															# {"feature": "magicNumberTest", "instances": 5, "metric_value": 0.6325, "depth": 15}
															if obj[12]<=0:
																# {"feature": "printStatement", "instances": 5, "metric_value": 0.6325, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.6325, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 5, "metric_value": 0.6325, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 5, "metric_value": 0.6325, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 5, "metric_value": 0.6325, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 0.6325, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									else: return '0'
								elif obj[13]>0:
									return '0'
								else: return '0'
							else: return '0'
						else: return '0'
					else: return '0'
				elif obj[9]>0:
					# {"feature": "assertionRoulette", "instances": 186, "metric_value": 15.7255, "depth": 5}
					if obj[2]<=0:
						# {"feature": "conditionalTestLogic", "instances": 135, "metric_value": 11.8019, "depth": 6}
						if obj[3]<=0:
							# {"feature": "eagerTest", "instances": 126, "metric_value": 9.8401, "depth": 7}
							if obj[7]<=0:
								# {"feature": "magicNumberTest", "instances": 110, "metric_value": 8.8041, "depth": 8}
								if obj[12]<=0:
									# {"feature": "unknownTest", "instances": 108, "metric_value": 8.0412, "depth": 9}
									if obj[19]<=0:
										# {"feature": "lazyTest", "instances": 87, "metric_value": 9.798, "depth": 10}
										if obj[11]>0:
											# {"feature": "defaultTest", "instances": 75, "metric_value": 7.3485, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 75, "metric_value": 7.3485, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 75, "metric_value": 7.3485, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 75, "metric_value": 7.3485, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 75, "metric_value": 7.3485, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 75, "metric_value": 7.3485, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 75, "metric_value": 7.3485, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 75, "metric_value": 7.3485, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 75, "metric_value": 7.3485, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 75, "metric_value": 7.3485, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 75, "metric_value": 7.3485, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										elif obj[11]<=0:
											# {"feature": "defaultTest", "instances": 12, "metric_value": 2.4495, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 12, "metric_value": 2.4495, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 12, "metric_value": 2.4495, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 12, "metric_value": 2.4495, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 12, "metric_value": 2.4495, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 12, "metric_value": 2.4495, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 12, "metric_value": 2.4495, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 12, "metric_value": 2.4495, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 12, "metric_value": 2.4495, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 12, "metric_value": 2.4495, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 12, "metric_value": 2.4495, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									elif obj[19]>0:
										# {"feature": "lazyTest", "instances": 21, "metric_value": 5.2836, "depth": 10}
										if obj[11]<=0:
											# {"feature": "defaultTest", "instances": 16, "metric_value": 2.1213, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 16, "metric_value": 2.1213, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 16, "metric_value": 2.1213, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 16, "metric_value": 2.1213, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 16, "metric_value": 2.1213, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 16, "metric_value": 2.1213, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 16, "metric_value": 2.1213, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 16, "metric_value": 2.1213, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 16, "metric_value": 2.1213, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 16, "metric_value": 2.1213, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 16, "metric_value": 2.1213, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[11]>0:
											return '0'
										else: return '0'
									else: return '1'
								elif obj[12]>0:
									return '0'
								else: return '0'
							elif obj[7]>0:
								# {"feature": "magicNumberTest", "instances": 16, "metric_value": 5.6268, "depth": 8}
								if obj[12]<=0:
									return '0'
								elif obj[12]>0:
									# {"feature": "defaultTest", "instances": 6, "metric_value": 1.1547, "depth": 9}
									if obj[5]<=0:
										# {"feature": "duplicateAssert", "instances": 6, "metric_value": 1.1547, "depth": 10}
										if obj[6]<=0:
											# {"feature": "emptyTest", "instances": 6, "metric_value": 1.1547, "depth": 11}
											if obj[8]<=0:
												# {"feature": "ignoredTest", "instances": 6, "metric_value": 1.1547, "depth": 12}
												if obj[10]<=0:
													# {"feature": "lazyTest", "instances": 6, "metric_value": 1.1547, "depth": 13}
													if obj[11]<=1:
														# {"feature": "mysteryGuest", "instances": 6, "metric_value": 1.1547, "depth": 14}
														if obj[13]<=0:
															# {"feature": "printStatement", "instances": 6, "metric_value": 1.1547, "depth": 15}
															if obj[14]<=0:
																# {"feature": "redundantAssertion", "instances": 6, "metric_value": 1.1547, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 6, "metric_value": 1.1547, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 6, "metric_value": 1.1547, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 6, "metric_value": 1.1547, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 6, "metric_value": 1.1547, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 6, "metric_value": 1.1547, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '0'
						elif obj[3]>0:
							return '0'
						else: return '0'
					elif obj[2]>0:
						# {"feature": "eagerTest", "instances": 51, "metric_value": 10.4003, "depth": 6}
						if obj[7]<=0:
							# {"feature": "duplicateAssert", "instances": 27, "metric_value": 6.6619, "depth": 7}
							if obj[6]<=0:
								# {"feature": "magicNumberTest", "instances": 23, "metric_value": 5.3964, "depth": 8}
								if obj[12]<=0:
									# {"feature": "lazyTest", "instances": 17, "metric_value": 6.0166, "depth": 9}
									if obj[11]>0:
										# {"feature": "printStatement", "instances": 15, "metric_value": 5.1939, "depth": 10}
										if obj[14]<=0:
											# {"feature": "conditionalTestLogic", "instances": 14, "metric_value": 3.7796, "depth": 11}
											if obj[3]<=0:
												# {"feature": "defaultTest", "instances": 14, "metric_value": 3.7796, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 14, "metric_value": 3.7796, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 14, "metric_value": 3.7796, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 14, "metric_value": 3.7796, "depth": 15}
															if obj[13]<=0:
																# {"feature": "redundantAssertion", "instances": 14, "metric_value": 3.7796, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 14, "metric_value": 3.7796, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 14, "metric_value": 3.7796, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 14, "metric_value": 3.7796, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 14, "metric_value": 3.7796, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 14, "metric_value": 3.7796, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										elif obj[14]>0:
											return '0'
										else: return '0'
									elif obj[11]<=0:
										return '1'
									else: return '1'
								elif obj[12]>0:
									# {"feature": "lazyTest", "instances": 6, "metric_value": 3.266, "depth": 9}
									if obj[11]>0:
										return '0'
									elif obj[11]<=0:
										# {"feature": "conditionalTestLogic", "instances": 3, "metric_value": 0.8165, "depth": 10}
										if obj[3]<=0:
											# {"feature": "defaultTest", "instances": 3, "metric_value": 0.8165, "depth": 11}
											if obj[5]<=0:
												# {"feature": "emptyTest", "instances": 3, "metric_value": 0.8165, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 3, "metric_value": 0.8165, "depth": 13}
													if obj[10]<=0:
														# {"feature": "mysteryGuest", "instances": 3, "metric_value": 0.8165, "depth": 14}
														if obj[13]<=0:
															# {"feature": "printStatement", "instances": 3, "metric_value": 0.8165, "depth": 15}
															if obj[14]<=0:
																# {"feature": "redundantAssertion", "instances": 3, "metric_value": 0.8165, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 3, "metric_value": 0.8165, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 3, "metric_value": 0.8165, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 3, "metric_value": 0.8165, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 3, "metric_value": 0.8165, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 3, "metric_value": 0.8165, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[6]>0:
								return '0'
							else: return '0'
						elif obj[7]>0:
							# {"feature": "magicNumberTest", "instances": 24, "metric_value": 8.1308, "depth": 7}
							if obj[12]<=0:
								# {"feature": "resourceOptimism", "instances": 18, "metric_value": 6.5592, "depth": 8}
								if obj[16]<=0:
									# {"feature": "conditionalTestLogic", "instances": 17, "metric_value": 6.7469, "depth": 9}
									if obj[3]<=0:
										# {"feature": "duplicateAssert", "instances": 15, "metric_value": 6.1046, "depth": 10}
										if obj[6]<=0:
											return '0'
										elif obj[6]>0:
											# {"feature": "mysteryGuest", "instances": 4, "metric_value": 2.2307, "depth": 11}
											if obj[13]<=0:
												# {"feature": "defaultTest", "instances": 3, "metric_value": 0.8165, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 3, "metric_value": 0.8165, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 3, "metric_value": 0.8165, "depth": 14}
														if obj[10]<=0:
															# {"feature": "lazyTest", "instances": 3, "metric_value": 0.8165, "depth": 15}
															if obj[11]<=1:
																# {"feature": "printStatement", "instances": 3, "metric_value": 0.8165, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 3, "metric_value": 0.8165, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "sensitiveEquality", "instances": 3, "metric_value": 0.8165, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 3, "metric_value": 0.8165, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 3, "metric_value": 0.8165, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 3, "metric_value": 0.8165, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											elif obj[13]>0:
												return '0'
											else: return '0'
										else: return '0'
									elif obj[3]>0:
										return '0'
									else: return '0'
								elif obj[16]>0:
									return '1'
								else: return '1'
							elif obj[12]>0:
								return '0'
							else: return '0'
						else: return '0'
					else: return '0'
				else: return '0'
			elif obj[4]>0:
				# {"feature": "lazyTest", "instances": 38, "metric_value": 9.7947, "depth": 4}
				if obj[11]>0:
					# {"feature": "assertionRoulette", "instances": 20, "metric_value": 6.6667, "depth": 5}
					if obj[2]>0:
						# {"feature": "eagerTest", "instances": 18, "metric_value": 6.7301, "depth": 6}
						if obj[7]>0:
							# {"feature": "duplicateAssert", "instances": 12, "metric_value": 6.4721, "depth": 7}
							if obj[6]>0:
								return '1'
							elif obj[6]<=0:
								return '0'
							else: return '0'
						elif obj[7]<=0:
							return '1'
						else: return '1'
					elif obj[2]<=0:
						return '0'
					else: return '0'
				elif obj[11]<=0:
					return '1'
				else: return '1'
			else: return '1'
		elif obj[1]<=0:
			# {"feature": "assertionRoulette", "instances": 81, "metric_value": 10.8423, "depth": 3}
			if obj[2]<=0:
				# {"feature": "conditionalTestLogic", "instances": 81, "metric_value": 10.8423, "depth": 4}
				if obj[3]<=0:
					# {"feature": "constructorInitialization", "instances": 81, "metric_value": 10.8423, "depth": 5}
					if obj[4]<=0:
						# {"feature": "defaultTest", "instances": 81, "metric_value": 10.8423, "depth": 6}
						if obj[5]<=0:
							# {"feature": "duplicateAssert", "instances": 81, "metric_value": 10.8423, "depth": 7}
							if obj[6]<=0:
								# {"feature": "eagerTest", "instances": 81, "metric_value": 10.8423, "depth": 8}
								if obj[7]<=0:
									# {"feature": "emptyTest", "instances": 81, "metric_value": 10.8423, "depth": 9}
									if obj[8]<=0:
										# {"feature": "generalFixture", "instances": 81, "metric_value": 10.8423, "depth": 10}
										if obj[9]<=0:
											# {"feature": "ignoredTest", "instances": 81, "metric_value": 10.8423, "depth": 11}
											if obj[10]<=0:
												# {"feature": "lazyTest", "instances": 81, "metric_value": 10.8423, "depth": 12}
												if obj[11]<=0:
													# {"feature": "magicNumberTest", "instances": 81, "metric_value": 10.8423, "depth": 13}
													if obj[12]<=0:
														# {"feature": "mysteryGuest", "instances": 81, "metric_value": 10.8423, "depth": 14}
														if obj[13]<=0:
															# {"feature": "printStatement", "instances": 81, "metric_value": 10.8423, "depth": 15}
															if obj[14]<=0:
																# {"feature": "redundantAssertion", "instances": 81, "metric_value": 10.8423, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 81, "metric_value": 10.8423, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 81, "metric_value": 10.8423, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 81, "metric_value": 10.8423, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 81, "metric_value": 10.8423, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 81, "metric_value": 10.8423, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							else: return '0'
						else: return '0'
					else: return '0'
				else: return '0'
			else: return '0'
		else: return '0'
	elif obj[0]>20.831157136425034:
		# {"feature": "lazyTest", "instances": 742, "metric_value": 36.5722, "depth": 2}
		if obj[11]>0:
			# {"feature": "smellsCount", "instances": 460, "metric_value": 24.8912, "depth": 3}
			if obj[1]>3:
				# {"feature": "printStatement", "instances": 240, "metric_value": 15.3017, "depth": 4}
				if obj[14]<=0:
					# {"feature": "generalFixture", "instances": 222, "metric_value": 14.255, "depth": 5}
					if obj[9]<=0:
						# {"feature": "duplicateAssert", "instances": 211, "metric_value": 14.6852, "depth": 6}
						if obj[6]<=0:
							# {"feature": "conditionalTestLogic", "instances": 117, "metric_value": 11.1888, "depth": 7}
							if obj[3]<=0:
								# {"feature": "assertionRoulette", "instances": 62, "metric_value": 10.999, "depth": 8}
								if obj[2]>0:
									# {"feature": "magicNumberTest", "instances": 58, "metric_value": 11.5286, "depth": 9}
									if obj[12]>0:
										# {"feature": "mysteryGuest", "instances": 33, "metric_value": 7.9142, "depth": 10}
										if obj[13]<=0:
											# {"feature": "constructorInitialization", "instances": 32, "metric_value": 6.5, "depth": 11}
											if obj[4]<=0:
												# {"feature": "defaultTest", "instances": 32, "metric_value": 6.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "eagerTest", "instances": 32, "metric_value": 6.5, "depth": 13}
													if obj[7]<=1:
														# {"feature": "emptyTest", "instances": 32, "metric_value": 6.5, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 32, "metric_value": 6.5, "depth": 15}
															if obj[10]<=0:
																# {"feature": "redundantAssertion", "instances": 32, "metric_value": 6.5, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 32, "metric_value": 6.5, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 32, "metric_value": 6.5, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 32, "metric_value": 6.5, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 32, "metric_value": 6.5, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 32, "metric_value": 6.5, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[13]>0:
											return '0'
										else: return '0'
									elif obj[12]<=0:
										# {"feature": "sensitiveEquality", "instances": 25, "metric_value": 7.6819, "depth": 10}
										if obj[17]<=0:
											# {"feature": "resourceOptimism", "instances": 19, "metric_value": 5.677, "depth": 11}
											if obj[16]<=0:
												# {"feature": "mysteryGuest", "instances": 14, "metric_value": 4.9443, "depth": 12}
												if obj[13]>0:
													# {"feature": "constructorInitialization", "instances": 13, "metric_value": 3.5301, "depth": 13}
													if obj[4]<=0:
														# {"feature": "defaultTest", "instances": 13, "metric_value": 3.5301, "depth": 14}
														if obj[5]<=0:
															# {"feature": "eagerTest", "instances": 13, "metric_value": 3.5301, "depth": 15}
															if obj[7]<=1:
																# {"feature": "emptyTest", "instances": 13, "metric_value": 3.5301, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 13, "metric_value": 3.5301, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "redundantAssertion", "instances": 13, "metric_value": 3.5301, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 13, "metric_value": 3.5301, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 13, "metric_value": 3.5301, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 13, "metric_value": 3.5301, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[13]<=0:
													return '1'
												else: return '1'
											elif obj[16]>0:
												# {"feature": "constructorInitialization", "instances": 5, "metric_value": 1.8974, "depth": 12}
												if obj[4]<=0:
													# {"feature": "defaultTest", "instances": 5, "metric_value": 1.8974, "depth": 13}
													if obj[5]<=0:
														# {"feature": "eagerTest", "instances": 5, "metric_value": 1.8974, "depth": 14}
														if obj[7]<=1:
															# {"feature": "emptyTest", "instances": 5, "metric_value": 1.8974, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 5, "metric_value": 1.8974, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "mysteryGuest", "instances": 5, "metric_value": 1.8974, "depth": 17}
																	if obj[13]<=1:
																		# {"feature": "redundantAssertion", "instances": 5, "metric_value": 1.8974, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 5, "metric_value": 1.8974, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 5, "metric_value": 1.8974, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 1.8974, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[17]>0:
											return '1'
										else: return '1'
									else: return '1'
								elif obj[2]<=0:
									return '0'
								else: return '0'
							elif obj[3]>0:
								# {"feature": "magicNumberTest", "instances": 55, "metric_value": 7.1571, "depth": 8}
								if obj[12]<=0:
									# {"feature": "eagerTest", "instances": 47, "metric_value": 7.8497, "depth": 9}
									if obj[7]>0:
										# {"feature": "assertionRoulette", "instances": 39, "metric_value": 6.0727, "depth": 10}
										if obj[2]>0:
											# {"feature": "sensitiveEquality", "instances": 34, "metric_value": 4.6146, "depth": 11}
											if obj[17]<=0:
												# {"feature": "mysteryGuest", "instances": 33, "metric_value": 5.1919, "depth": 12}
												if obj[13]<=0:
													# {"feature": "constructorInitialization", "instances": 29, "metric_value": 3.5523, "depth": 13}
													if obj[4]<=0:
														# {"feature": "defaultTest", "instances": 28, "metric_value": 2.1381, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 28, "metric_value": 2.1381, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 28, "metric_value": 2.1381, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "redundantAssertion", "instances": 28, "metric_value": 2.1381, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 28, "metric_value": 2.1381, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sleepyTest", "instances": 28, "metric_value": 2.1381, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 28, "metric_value": 2.1381, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 28, "metric_value": 2.1381, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[4]>0:
														return '1'
													else: return '1'
												elif obj[13]>0:
													return '1'
												else: return '1'
											elif obj[17]>0:
												return '0'
											else: return '0'
										elif obj[2]<=0:
											return '1'
										else: return '1'
									elif obj[7]<=0:
										return '1'
									else: return '1'
								elif obj[12]>0:
									# {"feature": "mysteryGuest", "instances": 8, "metric_value": 3.1547, "depth": 9}
									if obj[13]<=0:
										# {"feature": "assertionRoulette", "instances": 6, "metric_value": 2.0467, "depth": 10}
										if obj[2]>0:
											# {"feature": "eagerTest", "instances": 5, "metric_value": 1.4142, "depth": 11}
											if obj[7]>0:
												# {"feature": "sleepyTest", "instances": 4, "metric_value": 2.2307, "depth": 12}
												if obj[18]<=0:
													# {"feature": "constructorInitialization", "instances": 3, "metric_value": 0.8165, "depth": 13}
													if obj[4]<=0:
														# {"feature": "defaultTest", "instances": 3, "metric_value": 0.8165, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 3, "metric_value": 0.8165, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 3, "metric_value": 0.8165, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "redundantAssertion", "instances": 3, "metric_value": 0.8165, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 3, "metric_value": 0.8165, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 3, "metric_value": 0.8165, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 3, "metric_value": 0.8165, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 3, "metric_value": 0.8165, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[18]>0:
													return '0'
												else: return '0'
											elif obj[7]<=0:
												return '0'
											else: return '0'
										elif obj[2]<=0:
											return '0'
										else: return '0'
									elif obj[13]>0:
										return '0'
									else: return '0'
								else: return '0'
							else: return '1'
						elif obj[6]>0:
							# {"feature": "mysteryGuest", "instances": 94, "metric_value": 10.0738, "depth": 7}
							if obj[13]<=0:
								# {"feature": "constructorInitialization", "instances": 78, "metric_value": 7.6313, "depth": 8}
								if obj[4]<=0:
									# {"feature": "sleepyTest", "instances": 73, "metric_value": 6.9352, "depth": 9}
									if obj[18]<=0:
										# {"feature": "assertionRoulette", "instances": 68, "metric_value": 6.1779, "depth": 10}
										if obj[2]>0:
											# {"feature": "magicNumberTest", "instances": 66, "metric_value": 6.1462, "depth": 11}
											if obj[12]<=0:
												# {"feature": "eagerTest", "instances": 44, "metric_value": 7.9178, "depth": 12}
												if obj[7]>0:
													# {"feature": "conditionalTestLogic", "instances": 39, "metric_value": 7.3474, "depth": 13}
													if obj[3]<=0:
														# {"feature": "verboseTest", "instances": 37, "metric_value": 6.5997, "depth": 14}
														if obj[20]<=0:
															# {"feature": "sensitiveEquality", "instances": 36, "metric_value": 5.5, "depth": 15}
															if obj[17]<=0:
																# {"feature": "defaultTest", "instances": 32, "metric_value": 5.5, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 32, "metric_value": 5.5, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 32, "metric_value": 5.5, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "redundantAssertion", "instances": 32, "metric_value": 5.5, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "resourceOptimism", "instances": 32, "metric_value": 5.5, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "unknownTest", "instances": 32, "metric_value": 5.5, "depth": 21}
																					if obj[19]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															elif obj[17]>0:
																# {"feature": "defaultTest", "instances": 4, "metric_value": 0.0, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 4, "metric_value": 0.0, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 4, "metric_value": 0.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "redundantAssertion", "instances": 4, "metric_value": 0.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "resourceOptimism", "instances": 4, "metric_value": 0.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "unknownTest", "instances": 4, "metric_value": 0.0, "depth": 21}
																					if obj[19]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														elif obj[20]>0:
															return '1'
														else: return '1'
													elif obj[3]>0:
														return '0'
													else: return '0'
												elif obj[7]<=0:
													return '1'
												else: return '1'
											elif obj[12]>0:
												# {"feature": "conditionalTestLogic", "instances": 22, "metric_value": 4.2678, "depth": 12}
												if obj[3]<=0:
													# {"feature": "eagerTest", "instances": 14, "metric_value": 2.9485, "depth": 13}
													if obj[7]>0:
														# {"feature": "defaultTest", "instances": 11, "metric_value": 2.132, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 11, "metric_value": 2.132, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 11, "metric_value": 2.132, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "redundantAssertion", "instances": 11, "metric_value": 2.132, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 11, "metric_value": 2.132, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 11, "metric_value": 2.132, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 11, "metric_value": 2.132, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 11, "metric_value": 2.132, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													elif obj[7]<=0:
														# {"feature": "defaultTest", "instances": 3, "metric_value": 0.8165, "depth": 14}
														if obj[5]<=0:
															# {"feature": "emptyTest", "instances": 3, "metric_value": 0.8165, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 3, "metric_value": 0.8165, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "redundantAssertion", "instances": 3, "metric_value": 0.8165, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 3, "metric_value": 0.8165, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 3, "metric_value": 0.8165, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 3, "metric_value": 0.8165, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 3, "metric_value": 0.8165, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												elif obj[3]>0:
													# {"feature": "sensitiveEquality", "instances": 8, "metric_value": 4.0868, "depth": 13}
													if obj[17]<=0:
														# {"feature": "defaultTest", "instances": 7, "metric_value": 2.6726, "depth": 14}
														if obj[5]<=0:
															# {"feature": "eagerTest", "instances": 7, "metric_value": 2.6726, "depth": 15}
															if obj[7]<=1:
																# {"feature": "emptyTest", "instances": 7, "metric_value": 2.6726, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 7, "metric_value": 2.6726, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "redundantAssertion", "instances": 7, "metric_value": 2.6726, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "resourceOptimism", "instances": 7, "metric_value": 2.6726, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "unknownTest", "instances": 7, "metric_value": 2.6726, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 7, "metric_value": 2.6726, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[17]>0:
														return '0'
													else: return '0'
												else: return '1'
											else: return '0'
										elif obj[2]<=0:
											return '0'
										else: return '0'
									elif obj[18]>0:
										return '1'
									else: return '1'
								elif obj[4]>0:
									return '1'
								else: return '1'
							elif obj[13]>0:
								# {"feature": "sensitiveEquality", "instances": 16, "metric_value": 6.7815, "depth": 8}
								if obj[17]>0:
									return '1'
								elif obj[17]<=0:
									# {"feature": "resourceOptimism", "instances": 6, "metric_value": 2.8284, "depth": 9}
									if obj[16]<=0:
										return '1'
									elif obj[16]>0:
										# {"feature": "assertionRoulette", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[2]<=1:
											# {"feature": "conditionalTestLogic", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "constructorInitialization", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[4]<=0:
													# {"feature": "defaultTest", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "eagerTest", "instances": 2, "metric_value": 0.0, "depth": 14}
														if obj[7]<=1:
															# {"feature": "emptyTest", "instances": 2, "metric_value": 0.0, "depth": 15}
															if obj[8]<=0:
																# {"feature": "ignoredTest", "instances": 2, "metric_value": 0.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "magicNumberTest", "instances": 2, "metric_value": 0.0, "depth": 17}
																	if obj[12]<=0:
																		# {"feature": "redundantAssertion", "instances": 2, "metric_value": 0.0, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "sleepyTest", "instances": 2, "metric_value": 0.0, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 2, "metric_value": 0.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 2, "metric_value": 0.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '1'
						else: return '1'
					elif obj[9]>0:
						# {"feature": "eagerTest", "instances": 11, "metric_value": 5.3615, "depth": 6}
						if obj[7]>0:
							return '0'
						elif obj[7]<=0:
							# {"feature": "conditionalTestLogic", "instances": 5, "metric_value": 4.2426, "depth": 7}
							if obj[3]>0:
								return '0'
							elif obj[3]<=0:
								return '1'
							else: return '1'
						else: return '0'
					else: return '0'
				elif obj[14]>0:
					return '1'
				else: return '1'
			elif obj[1]<=3:
				# {"feature": "eagerTest", "instances": 220, "metric_value": 20.2834, "depth": 4}
				if obj[7]<=0:
					# {"feature": "generalFixture", "instances": 127, "metric_value": 14.6492, "depth": 5}
					if obj[9]<=0:
						# {"feature": "unknownTest", "instances": 121, "metric_value": 15.6211, "depth": 6}
						if obj[19]<=0:
							# {"feature": "conditionalTestLogic", "instances": 98, "metric_value": 13.0147, "depth": 7}
							if obj[3]<=0:
								# {"feature": "duplicateAssert", "instances": 75, "metric_value": 10.0164, "depth": 8}
								if obj[6]<=0:
									# {"feature": "assertionRoulette", "instances": 66, "metric_value": 9.3122, "depth": 9}
									if obj[2]>0:
										# {"feature": "magicNumberTest", "instances": 49, "metric_value": 10.1677, "depth": 10}
										if obj[12]<=0:
											# {"feature": "constructorInitialization", "instances": 39, "metric_value": 8.3789, "depth": 11}
											if obj[4]<=0:
												# {"feature": "defaultTest", "instances": 39, "metric_value": 8.3789, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 39, "metric_value": 8.3789, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 39, "metric_value": 8.3789, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 39, "metric_value": 8.3789, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 39, "metric_value": 8.3789, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 39, "metric_value": 8.3789, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 39, "metric_value": 8.3789, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 39, "metric_value": 8.3789, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 39, "metric_value": 8.3789, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 39, "metric_value": 8.3789, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										elif obj[12]>0:
											# {"feature": "constructorInitialization", "instances": 10, "metric_value": 1.7889, "depth": 11}
											if obj[4]<=0:
												# {"feature": "defaultTest", "instances": 10, "metric_value": 1.7889, "depth": 12}
												if obj[5]<=0:
													# {"feature": "emptyTest", "instances": 10, "metric_value": 1.7889, "depth": 13}
													if obj[8]<=0:
														# {"feature": "ignoredTest", "instances": 10, "metric_value": 1.7889, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 10, "metric_value": 1.7889, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 10, "metric_value": 1.7889, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 10, "metric_value": 1.7889, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 10, "metric_value": 1.7889, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 10, "metric_value": 1.7889, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 10, "metric_value": 1.7889, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 10, "metric_value": 1.7889, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[2]<=0:
										# {"feature": "magicNumberTest", "instances": 17, "metric_value": 2.8284, "depth": 10}
										if obj[12]<=0:
											# {"feature": "mysteryGuest", "instances": 16, "metric_value": 3.24, "depth": 11}
											if obj[13]<=0:
												# {"feature": "constructorInitialization", "instances": 15, "metric_value": 1.8257, "depth": 12}
												if obj[4]<=0:
													# {"feature": "defaultTest", "instances": 15, "metric_value": 1.8257, "depth": 13}
													if obj[5]<=0:
														# {"feature": "emptyTest", "instances": 15, "metric_value": 1.8257, "depth": 14}
														if obj[8]<=0:
															# {"feature": "ignoredTest", "instances": 15, "metric_value": 1.8257, "depth": 15}
															if obj[10]<=0:
																# {"feature": "printStatement", "instances": 15, "metric_value": 1.8257, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 15, "metric_value": 1.8257, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 15, "metric_value": 1.8257, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 15, "metric_value": 1.8257, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 15, "metric_value": 1.8257, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 15, "metric_value": 1.8257, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											elif obj[13]>0:
												return '0'
											else: return '0'
										elif obj[12]>0:
											return '0'
										else: return '0'
									else: return '1'
								elif obj[6]>0:
									# {"feature": "assertionRoulette", "instances": 9, "metric_value": 4.4142, "depth": 9}
									if obj[2]>0:
										# {"feature": "constructorInitialization", "instances": 8, "metric_value": 3.0, "depth": 10}
										if obj[4]<=0:
											# {"feature": "defaultTest", "instances": 8, "metric_value": 3.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "emptyTest", "instances": 8, "metric_value": 3.0, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 8, "metric_value": 3.0, "depth": 13}
													if obj[10]<=0:
														# {"feature": "magicNumberTest", "instances": 8, "metric_value": 3.0, "depth": 14}
														if obj[12]<=0:
															# {"feature": "mysteryGuest", "instances": 8, "metric_value": 3.0, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 8, "metric_value": 3.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 8, "metric_value": 3.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 8, "metric_value": 3.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 8, "metric_value": 3.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 8, "metric_value": 3.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 3.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[2]<=0:
										return '0'
									else: return '0'
								else: return '1'
							elif obj[3]>0:
								# {"feature": "duplicateAssert", "instances": 23, "metric_value": 6.8414, "depth": 8}
								if obj[6]<=0:
									# {"feature": "assertionRoulette", "instances": 22, "metric_value": 6.7475, "depth": 9}
									if obj[2]>0:
										# {"feature": "constructorInitialization", "instances": 18, "metric_value": 5.3333, "depth": 10}
										if obj[4]<=0:
											# {"feature": "defaultTest", "instances": 18, "metric_value": 5.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "emptyTest", "instances": 18, "metric_value": 5.3333, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 18, "metric_value": 5.3333, "depth": 13}
													if obj[10]<=0:
														# {"feature": "magicNumberTest", "instances": 18, "metric_value": 5.3333, "depth": 14}
														if obj[12]<=0:
															# {"feature": "mysteryGuest", "instances": 18, "metric_value": 5.3333, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 18, "metric_value": 5.3333, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 18, "metric_value": 5.3333, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 18, "metric_value": 5.3333, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 18, "metric_value": 5.3333, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 18, "metric_value": 5.3333, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 18, "metric_value": 5.3333, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[2]<=0:
										# {"feature": "constructorInitialization", "instances": 4, "metric_value": 1.4142, "depth": 10}
										if obj[4]<=0:
											# {"feature": "defaultTest", "instances": 4, "metric_value": 1.4142, "depth": 11}
											if obj[5]<=0:
												# {"feature": "emptyTest", "instances": 4, "metric_value": 1.4142, "depth": 12}
												if obj[8]<=0:
													# {"feature": "ignoredTest", "instances": 4, "metric_value": 1.4142, "depth": 13}
													if obj[10]<=0:
														# {"feature": "magicNumberTest", "instances": 4, "metric_value": 1.4142, "depth": 14}
														if obj[12]<=0:
															# {"feature": "mysteryGuest", "instances": 4, "metric_value": 1.4142, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 4, "metric_value": 1.4142, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 4, "metric_value": 1.4142, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 4, "metric_value": 1.4142, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 4, "metric_value": 1.4142, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 4, "metric_value": 1.4142, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 4, "metric_value": 1.4142, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								elif obj[6]>0:
									return '0'
								else: return '0'
							else: return '1'
						elif obj[19]>0:
							# {"feature": "conditionalTestLogic", "instances": 23, "metric_value": 8.0475, "depth": 7}
							if obj[3]<=0:
								return '1'
							elif obj[3]>0:
								return '0'
							else: return '0'
						else: return '1'
					elif obj[9]>0:
						return '0'
					else: return '0'
				elif obj[7]>0:
					# {"feature": "assertionRoulette", "instances": 93, "metric_value": 13.0219, "depth": 5}
					if obj[2]>0:
						# {"feature": "conditionalTestLogic", "instances": 65, "metric_value": 10.3493, "depth": 6}
						if obj[3]<=0:
							# {"feature": "constructorInitialization", "instances": 65, "metric_value": 10.3493, "depth": 7}
							if obj[4]<=0:
								# {"feature": "defaultTest", "instances": 65, "metric_value": 10.3493, "depth": 8}
								if obj[5]<=0:
									# {"feature": "duplicateAssert", "instances": 65, "metric_value": 10.3493, "depth": 9}
									if obj[6]<=0:
										# {"feature": "emptyTest", "instances": 65, "metric_value": 10.3493, "depth": 10}
										if obj[8]<=0:
											# {"feature": "generalFixture", "instances": 65, "metric_value": 10.3493, "depth": 11}
											if obj[9]<=0:
												# {"feature": "ignoredTest", "instances": 65, "metric_value": 10.3493, "depth": 12}
												if obj[10]<=0:
													# {"feature": "magicNumberTest", "instances": 65, "metric_value": 10.3493, "depth": 13}
													if obj[12]<=0:
														# {"feature": "mysteryGuest", "instances": 65, "metric_value": 10.3493, "depth": 14}
														if obj[13]<=0:
															# {"feature": "printStatement", "instances": 65, "metric_value": 10.3493, "depth": 15}
															if obj[14]<=0:
																# {"feature": "redundantAssertion", "instances": 65, "metric_value": 10.3493, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 65, "metric_value": 10.3493, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 65, "metric_value": 10.3493, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 65, "metric_value": 10.3493, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 65, "metric_value": 10.3493, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 65, "metric_value": 10.3493, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '1'
						else: return '1'
					elif obj[2]<=0:
						# {"feature": "magicNumberTest", "instances": 28, "metric_value": 4.408, "depth": 6}
						if obj[12]<=0:
							# {"feature": "conditionalTestLogic", "instances": 27, "metric_value": 4.2575, "depth": 7}
							if obj[3]<=0:
								# {"feature": "unknownTest", "instances": 14, "metric_value": 2.9895, "depth": 8}
								if obj[19]<=0:
									# {"feature": "mysteryGuest", "instances": 9, "metric_value": 3.4142, "depth": 9}
									if obj[13]<=0:
										# {"feature": "constructorInitialization", "instances": 8, "metric_value": 2.0, "depth": 10}
										if obj[4]<=0:
											# {"feature": "defaultTest", "instances": 8, "metric_value": 2.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "duplicateAssert", "instances": 8, "metric_value": 2.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "emptyTest", "instances": 8, "metric_value": 2.0, "depth": 13}
													if obj[8]<=0:
														# {"feature": "generalFixture", "instances": 8, "metric_value": 2.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "ignoredTest", "instances": 8, "metric_value": 2.0, "depth": 15}
															if obj[10]<=0:
																# {"feature": "printStatement", "instances": 8, "metric_value": 2.0, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 8, "metric_value": 2.0, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 8, "metric_value": 2.0, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 8, "metric_value": 2.0, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 8, "metric_value": 2.0, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 2.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									elif obj[13]>0:
										return '1'
									else: return '1'
								elif obj[19]>0:
									# {"feature": "constructorInitialization", "instances": 5, "metric_value": 0.6325, "depth": 9}
									if obj[4]<=0:
										# {"feature": "defaultTest", "instances": 5, "metric_value": 0.6325, "depth": 10}
										if obj[5]<=0:
											# {"feature": "duplicateAssert", "instances": 5, "metric_value": 0.6325, "depth": 11}
											if obj[6]<=0:
												# {"feature": "emptyTest", "instances": 5, "metric_value": 0.6325, "depth": 12}
												if obj[8]<=0:
													# {"feature": "generalFixture", "instances": 5, "metric_value": 0.6325, "depth": 13}
													if obj[9]<=0:
														# {"feature": "ignoredTest", "instances": 5, "metric_value": 0.6325, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 5, "metric_value": 0.6325, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 5, "metric_value": 0.6325, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 5, "metric_value": 0.6325, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 5, "metric_value": 0.6325, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 5, "metric_value": 0.6325, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "sleepyTest", "instances": 5, "metric_value": 0.6325, "depth": 20}
																				if obj[18]<=0:
																					# {"feature": "verboseTest", "instances": 5, "metric_value": 0.6325, "depth": 21}
																					if obj[20]<=0:
																						return '0'
																					else: return '0'
																				else: return '0'
																			else: return '0'
																		else: return '0'
																	else: return '0'
																else: return '0'
															else: return '0'
														else: return '0'
													else: return '0'
												else: return '0'
											else: return '0'
										else: return '0'
									else: return '0'
								else: return '0'
							elif obj[3]>0:
								# {"feature": "constructorInitialization", "instances": 13, "metric_value": 2.7456, "depth": 8}
								if obj[4]<=0:
									# {"feature": "defaultTest", "instances": 13, "metric_value": 2.7456, "depth": 9}
									if obj[5]<=0:
										# {"feature": "duplicateAssert", "instances": 13, "metric_value": 2.7456, "depth": 10}
										if obj[6]<=0:
											# {"feature": "emptyTest", "instances": 13, "metric_value": 2.7456, "depth": 11}
											if obj[8]<=0:
												# {"feature": "generalFixture", "instances": 13, "metric_value": 2.7456, "depth": 12}
												if obj[9]<=0:
													# {"feature": "ignoredTest", "instances": 13, "metric_value": 2.7456, "depth": 13}
													if obj[10]<=0:
														# {"feature": "mysteryGuest", "instances": 13, "metric_value": 2.7456, "depth": 14}
														if obj[13]<=0:
															# {"feature": "printStatement", "instances": 13, "metric_value": 2.7456, "depth": 15}
															if obj[14]<=0:
																# {"feature": "redundantAssertion", "instances": 13, "metric_value": 2.7456, "depth": 16}
																if obj[15]<=0:
																	# {"feature": "resourceOptimism", "instances": 13, "metric_value": 2.7456, "depth": 17}
																	if obj[16]<=0:
																		# {"feature": "sensitiveEquality", "instances": 13, "metric_value": 2.7456, "depth": 18}
																		if obj[17]<=0:
																			# {"feature": "sleepyTest", "instances": 13, "metric_value": 2.7456, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "unknownTest", "instances": 13, "metric_value": 2.7456, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 13, "metric_value": 2.7456, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '1'
						elif obj[12]>0:
							return '0'
						else: return '0'
					else: return '1'
				else: return '1'
			else: return '1'
		elif obj[11]<=0:
			# {"feature": "smellsCount", "instances": 282, "metric_value": 26.929, "depth": 3}
			if obj[1]<=2:
				# {"feature": "sleepyTest", "instances": 170, "metric_value": 18.175, "depth": 4}
				if obj[18]<=0:
					# {"feature": "duplicateAssert", "instances": 158, "metric_value": 17.2217, "depth": 5}
					if obj[6]<=0:
						# {"feature": "unknownTest", "instances": 139, "metric_value": 15.9055, "depth": 6}
						if obj[19]<=0:
							# {"feature": "sensitiveEquality", "instances": 126, "metric_value": 14.7611, "depth": 7}
							if obj[17]<=0:
								# {"feature": "magicNumberTest", "instances": 119, "metric_value": 13.5104, "depth": 8}
								if obj[12]<=0:
									# {"feature": "generalFixture", "instances": 115, "metric_value": 13.0422, "depth": 9}
									if obj[9]<=0:
										# {"feature": "printStatement", "instances": 113, "metric_value": 12.8727, "depth": 10}
										if obj[14]<=0:
											# {"feature": "eagerTest", "instances": 111, "metric_value": 12.5773, "depth": 11}
											if obj[7]<=0:
												# {"feature": "assertionRoulette", "instances": 99, "metric_value": 12.7753, "depth": 12}
												if obj[2]>0:
													# {"feature": "conditionalTestLogic", "instances": 78, "metric_value": 14.4941, "depth": 13}
													if obj[3]<=0:
														# {"feature": "verboseTest", "instances": 70, "metric_value": 12.8211, "depth": 14}
														if obj[20]<=0:
															# {"feature": "constructorInitialization", "instances": 69, "metric_value": 11.4068, "depth": 15}
															if obj[4]<=0:
																# {"feature": "defaultTest", "instances": 69, "metric_value": 11.4068, "depth": 16}
																if obj[5]<=0:
																	# {"feature": "emptyTest", "instances": 69, "metric_value": 11.4068, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "ignoredTest", "instances": 69, "metric_value": 11.4068, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "mysteryGuest", "instances": 69, "metric_value": 11.4068, "depth": 19}
																			if obj[13]<=0:
																				# {"feature": "redundantAssertion", "instances": 69, "metric_value": 11.4068, "depth": 20}
																				if obj[15]<=0:
																					# {"feature": "resourceOptimism", "instances": 69, "metric_value": 11.4068, "depth": 21}
																					if obj[16]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														elif obj[20]>0:
															return '1'
														else: return '1'
													elif obj[3]>0:
														# {"feature": "constructorInitialization", "instances": 8, "metric_value": 3.0, "depth": 14}
														if obj[4]<=0:
															# {"feature": "defaultTest", "instances": 8, "metric_value": 3.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 8, "metric_value": 3.0, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 8, "metric_value": 3.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "mysteryGuest", "instances": 8, "metric_value": 3.0, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 8, "metric_value": 3.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "resourceOptimism", "instances": 8, "metric_value": 3.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "verboseTest", "instances": 8, "metric_value": 3.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[2]<=0:
													# {"feature": "conditionalTestLogic", "instances": 21, "metric_value": 4.4495, "depth": 13}
													if obj[3]<=0:
														# {"feature": "constructorInitialization", "instances": 18, "metric_value": 2.0, "depth": 14}
														if obj[4]<=0:
															# {"feature": "defaultTest", "instances": 18, "metric_value": 2.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 18, "metric_value": 2.0, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 18, "metric_value": 2.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "mysteryGuest", "instances": 18, "metric_value": 2.0, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 18, "metric_value": 2.0, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "resourceOptimism", "instances": 18, "metric_value": 2.0, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "verboseTest", "instances": 18, "metric_value": 2.0, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													elif obj[3]>0:
														return '0'
													else: return '0'
												else: return '1'
											elif obj[7]>0:
												# {"feature": "assertionRoulette", "instances": 12, "metric_value": 4.6833, "depth": 12}
												if obj[2]>0:
													# {"feature": "conditionalTestLogic", "instances": 10, "metric_value": 2.6833, "depth": 13}
													if obj[3]<=0:
														# {"feature": "constructorInitialization", "instances": 10, "metric_value": 2.6833, "depth": 14}
														if obj[4]<=0:
															# {"feature": "defaultTest", "instances": 10, "metric_value": 2.6833, "depth": 15}
															if obj[5]<=0:
																# {"feature": "emptyTest", "instances": 10, "metric_value": 2.6833, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "ignoredTest", "instances": 10, "metric_value": 2.6833, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "mysteryGuest", "instances": 10, "metric_value": 2.6833, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "redundantAssertion", "instances": 10, "metric_value": 2.6833, "depth": 19}
																			if obj[15]<=0:
																				# {"feature": "resourceOptimism", "instances": 10, "metric_value": 2.6833, "depth": 20}
																				if obj[16]<=0:
																					# {"feature": "verboseTest", "instances": 10, "metric_value": 2.6833, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												elif obj[2]<=0:
													return '0'
												else: return '0'
											else: return '1'
										elif obj[14]>0:
											return '1'
										else: return '1'
									elif obj[9]>0:
										return '0'
									else: return '0'
								elif obj[12]>0:
									return '1'
								else: return '1'
							elif obj[17]>0:
								return '1'
							else: return '1'
						elif obj[19]>0:
							# {"feature": "assertionRoulette", "instances": 13, "metric_value": 4.3146, "depth": 7}
							if obj[2]<=0:
								# {"feature": "conditionalTestLogic", "instances": 13, "metric_value": 4.3146, "depth": 8}
								if obj[3]<=0:
									# {"feature": "constructorInitialization", "instances": 13, "metric_value": 4.3146, "depth": 9}
									if obj[4]<=0:
										# {"feature": "defaultTest", "instances": 13, "metric_value": 4.3146, "depth": 10}
										if obj[5]<=0:
											# {"feature": "eagerTest", "instances": 13, "metric_value": 4.3146, "depth": 11}
											if obj[7]<=0:
												# {"feature": "emptyTest", "instances": 13, "metric_value": 4.3146, "depth": 12}
												if obj[8]<=0:
													# {"feature": "generalFixture", "instances": 13, "metric_value": 4.3146, "depth": 13}
													if obj[9]<=0:
														# {"feature": "ignoredTest", "instances": 13, "metric_value": 4.3146, "depth": 14}
														if obj[10]<=0:
															# {"feature": "magicNumberTest", "instances": 13, "metric_value": 4.3146, "depth": 15}
															if obj[12]<=0:
																# {"feature": "mysteryGuest", "instances": 13, "metric_value": 4.3146, "depth": 16}
																if obj[13]<=0:
																	# {"feature": "printStatement", "instances": 13, "metric_value": 4.3146, "depth": 17}
																	if obj[14]<=0:
																		# {"feature": "redundantAssertion", "instances": 13, "metric_value": 4.3146, "depth": 18}
																		if obj[15]<=0:
																			# {"feature": "resourceOptimism", "instances": 13, "metric_value": 4.3146, "depth": 19}
																			if obj[16]<=0:
																				# {"feature": "sensitiveEquality", "instances": 13, "metric_value": 4.3146, "depth": 20}
																				if obj[17]<=0:
																					# {"feature": "verboseTest", "instances": 13, "metric_value": 4.3146, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '1'
						else: return '1'
					elif obj[6]>0:
						# {"feature": "conditionalTestLogic", "instances": 19, "metric_value": 6.6921, "depth": 6}
						if obj[3]<=0:
							# {"feature": "assertionRoulette", "instances": 16, "metric_value": 6.1611, "depth": 7}
							if obj[2]>0:
								# {"feature": "constructorInitialization", "instances": 15, "metric_value": 4.7469, "depth": 8}
								if obj[4]<=0:
									# {"feature": "defaultTest", "instances": 15, "metric_value": 4.7469, "depth": 9}
									if obj[5]<=0:
										# {"feature": "eagerTest", "instances": 15, "metric_value": 4.7469, "depth": 10}
										if obj[7]<=0:
											# {"feature": "emptyTest", "instances": 15, "metric_value": 4.7469, "depth": 11}
											if obj[8]<=0:
												# {"feature": "generalFixture", "instances": 15, "metric_value": 4.7469, "depth": 12}
												if obj[9]<=0:
													# {"feature": "ignoredTest", "instances": 15, "metric_value": 4.7469, "depth": 13}
													if obj[10]<=0:
														# {"feature": "magicNumberTest", "instances": 15, "metric_value": 4.7469, "depth": 14}
														if obj[12]<=0:
															# {"feature": "mysteryGuest", "instances": 15, "metric_value": 4.7469, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 15, "metric_value": 4.7469, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 15, "metric_value": 4.7469, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 15, "metric_value": 4.7469, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 15, "metric_value": 4.7469, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 15, "metric_value": 4.7469, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 15, "metric_value": 4.7469, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							elif obj[2]<=0:
								return '0'
							else: return '0'
						elif obj[3]>0:
							return '1'
						else: return '1'
					else: return '1'
				elif obj[18]>0:
					return '1'
				else: return '1'
			elif obj[1]>2:
				# {"feature": "magicNumberTest", "instances": 112, "metric_value": 18.151, "depth": 4}
				if obj[12]<=0:
					# {"feature": "conditionalTestLogic", "instances": 58, "metric_value": 12.3667, "depth": 5}
					if obj[3]>0:
						# {"feature": "sleepyTest", "instances": 36, "metric_value": 9.9488, "depth": 6}
						if obj[18]>0:
							# {"feature": "assertionRoulette", "instances": 28, "metric_value": 6.9488, "depth": 7}
							if obj[2]<=1:
								# {"feature": "constructorInitialization", "instances": 28, "metric_value": 6.9488, "depth": 8}
								if obj[4]<=0:
									# {"feature": "defaultTest", "instances": 28, "metric_value": 6.9488, "depth": 9}
									if obj[5]<=0:
										# {"feature": "duplicateAssert", "instances": 28, "metric_value": 6.9488, "depth": 10}
										if obj[6]<=0:
											# {"feature": "eagerTest", "instances": 28, "metric_value": 6.9488, "depth": 11}
											if obj[7]<=0:
												# {"feature": "emptyTest", "instances": 28, "metric_value": 6.9488, "depth": 12}
												if obj[8]<=0:
													# {"feature": "generalFixture", "instances": 28, "metric_value": 6.9488, "depth": 13}
													if obj[9]<=0:
														# {"feature": "ignoredTest", "instances": 28, "metric_value": 6.9488, "depth": 14}
														if obj[10]<=0:
															# {"feature": "mysteryGuest", "instances": 28, "metric_value": 6.9488, "depth": 15}
															if obj[13]<=0:
																# {"feature": "printStatement", "instances": 28, "metric_value": 6.9488, "depth": 16}
																if obj[14]<=0:
																	# {"feature": "redundantAssertion", "instances": 28, "metric_value": 6.9488, "depth": 17}
																	if obj[15]<=0:
																		# {"feature": "resourceOptimism", "instances": 28, "metric_value": 6.9488, "depth": 18}
																		if obj[16]<=0:
																			# {"feature": "sensitiveEquality", "instances": 28, "metric_value": 6.9488, "depth": 19}
																			if obj[17]<=0:
																				# {"feature": "unknownTest", "instances": 28, "metric_value": 6.9488, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "verboseTest", "instances": 28, "metric_value": 6.9488, "depth": 21}
																					if obj[20]<=0:
																						return '1'
																					else: return '1'
																				else: return '1'
																			else: return '1'
																		else: return '1'
																	else: return '1'
																else: return '1'
															else: return '1'
														else: return '1'
													else: return '1'
												else: return '1'
											else: return '1'
										else: return '1'
									else: return '1'
								else: return '1'
							else: return '1'
						elif obj[18]<=0:
							# {"feature": "generalFixture", "instances": 8, "metric_value": 4.3469, "depth": 7}
							if obj[9]<=0:
								# {"feature": "assertionRoulette", "instances": 5, "metric_value": 2.8284, "depth": 8}
								if obj[2]>0:
									# {"feature": "duplicateAssert", "instances": 4, "metric_value": 3.8637, "depth": 9}
									if obj[6]<=0:
										return '1'
									elif obj[6]>0:
										return '0'
									else: return '0'
								elif obj[2]<=0:
									return '1'
								else: return '1'
							elif obj[9]>0:
								return '1'
							else: return '1'
						else: return '1'
					elif obj[3]<=0:
						# {"feature": "assertionRoulette", "instances": 22, "metric_value": 7.6921, "depth": 6}
						if obj[2]>0:
							# {"feature": "printStatement", "instances": 20, "metric_value": 8.0498, "depth": 7}
							if obj[14]<=0:
								# {"feature": "generalFixture", "instances": 10, "metric_value": 5.6569, "depth": 8}
								if obj[9]<=0:
									return '1'
								elif obj[9]>0:
									return '0'
								else: return '0'
							elif obj[14]>0:
								return '1'
							else: return '1'
						elif obj[2]<=0:
							return '0'
						else: return '0'
					else: return '1'
				elif obj[12]>0:
					# {"feature": "constructorInitialization", "instances": 54, "metric_value": 13.0711, "depth": 5}
					if obj[4]<=0:
						# {"feature": "duplicateAssert", "instances": 36, "metric_value": 10.112, "depth": 6}
						if obj[6]<=0:
							# {"feature": "sensitiveEquality", "instances": 23, "metric_value": 7.0462, "depth": 7}
							if obj[17]<=0:
								# {"feature": "conditionalTestLogic", "instances": 19, "metric_value": 8.1063, "depth": 8}
								if obj[3]<=0:
									return '1'
								elif obj[3]>0:
									return '0'
								else: return '0'
							elif obj[17]>0:
								return '1'
							else: return '1'
						elif obj[6]>0:
							return '1'
						else: return '1'
					elif obj[4]>0:
						return '1'
					else: return '1'
				else: return '1'
			else: return '1'
		else: return '1'
	else: return '1'
